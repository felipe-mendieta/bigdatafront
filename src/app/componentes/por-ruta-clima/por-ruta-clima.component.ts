import { Component, OnInit } from '@angular/core';
import { RetrasoPorRutaClima } from 'src/app/modelos/retraso-ruta-clima';
import { VuelosRutasClimaService } from 'src/app/servicios/vuelos-rutas-clima.service';

@Component({
  selector: 'app-por-ruta-clima',
  templateUrl: './por-ruta-clima.component.html',
  styleUrls: ['./por-ruta-clima.component.css']
})
export class PorRutaClimaComponent implements OnInit {

  vuelos: RetrasoPorRutaClima[]= [];
  public page = 1; // página actual
  public pageSize = 150; // número de páginas
  public maxSize = 10;

  constructor(private vuelosRutaClimaService: VuelosRutasClimaService) { }

  ngOnInit(): void {
    this.vuelosRutaClimaService.getVuelos().subscribe(respuesta=>{
      console.log(respuesta);
      this.vuelos=respuesta;
    });
  }

}
