import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VuelosAerolineasService {

  public baseUrl = "http://localhost:3000/data2/";
  constructor(private httpClient: HttpClient) { }

  public getVuelos(): Observable<any> {
    return this.httpClient.get(`${this.baseUrl}`);
  }
}
