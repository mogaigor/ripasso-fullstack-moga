import { Component, signal, inject } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { GiocatoreService } from './services/giocatore-service';

@Component({
  imports: [RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('frontend');

}