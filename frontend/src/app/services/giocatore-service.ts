import { Service, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Giocatore } from '../models/giocatore.model';


@Service()
export class GiocatoreService {
    private http = inject(HttpClient);
    private url = '/api/giocatori';

    getGiocatori(): Observable<Giocatore[]> {
    return this.http.get<Giocatore[]>(this.url);
    }
}