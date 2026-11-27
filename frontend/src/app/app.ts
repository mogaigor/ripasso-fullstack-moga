import { Component, signal, inject } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { GiocatoreService } from './services/giocatore-service';
import { ListaGiocatori } from './pages/lista-giocatori/lista-giocatori';

@Component({
  imports: [RouterOutlet, ListaGiocatori],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('frontend');

}