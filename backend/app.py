from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_conn():
    # il MySQL nel container Docker (sezione 1)
    return mysql.connector.connect(
        host="127.0.0.1", user="root",
        password="root", database="fantabasket")

def riga_to_dict(r):
    return {"id": r[0], "nome": r[1],
            "media": float(r[2]),
            "valutazione_fanta": float(r[3])}

@app.get("/api/giocatori")
def lista_giocatori():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, media, "
                "media * 1.5 AS valutazione_fanta "
                "FROM giocatori")
    righe = cur.fetchall()
    cur.close(); conn.close()
    giocatori = [riga_to_dict(r) for r in righe]
    return jsonify(giocatori), 200

# dettaglio: parametro nell'URL
@app.get("/api/giocatori/<int:id>")
def dettaglio(id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, nome, media, "
                "media * 1.5 AS valutazione_fanta "
                "FROM giocatori WHERE id = %s", (id,))
    r = cur.fetchone()
    cur.close(); conn.close()
    if r is None:
        return jsonify({"errore": "non trovato"}), 404
    return jsonify(riga_to_dict(r)), 200

# nuova iscrizione: i dati arrivano nel BODY
# {"utente": "Rossi", "totale": 42.3, "giocatori": [1, 4]}
@app.post("/api/iscrizioni")
def crea_iscrizione():
    dati = request.get_json()        # JSON → dizionario
    conn = get_conn(); cur = conn.cursor()
    cur.execute("INSERT INTO iscrizioni (utente, totale) "
                "VALUES (%s, %s)",
                (dati["utente"], dati["totale"]))
    nuovo_id = cur.lastrowid         # id appena creato
    for gid in dati["giocatori"]:    # una riga per giocatore
        cur.execute("INSERT INTO righe_iscrizione "
                    "(iscrizione_id, giocatore_id) VALUES (%s, %s)",
                    (nuovo_id, gid))
    conn.commit()                    # salva tutto insieme
    cur.close(); conn.close()
    return jsonify({"id": nuovo_id}), 201