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