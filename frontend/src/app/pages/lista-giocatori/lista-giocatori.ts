import { Component, OnInit, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { GiocatoreService } from '../../services/giocatore-service';
import { Giocatore } from '../../models/giocatore.model';

@Component({
  selector: 'app-lista-giocatori',
  imports: [RouterLink],
  templateUrl: './lista-giocatori.html'
})
export class ListaGiocatori implements OnInit {
  private service = inject(GiocatoreService);
  giocatori = signal<Giocatore[]>([]);
  loading = signal(true);
  errore = signal('');

  ngOnInit() {
    this.service.getGiocatori().subscribe({
      next: dati => { this.giocatori.set(dati); this.loading.set(false); },
      error: err => { this.errore.set('Errore ' + err.status);
                      this.loading.set(false); }
    });
  }
}