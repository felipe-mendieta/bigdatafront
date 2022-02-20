import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VuelosRutasClimaService {

  public baseUrl = "http://localhost:3000/data3/";
  constructor(private httpClient: HttpClient) { }

  public getVuelos(): Observable<any> {
    return this.httpClient.get(`${this.baseUrl}`);
  }
}
