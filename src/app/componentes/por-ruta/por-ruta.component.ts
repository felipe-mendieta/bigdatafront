import { Component, OnInit } from '@angular/core';
import { RetrasoPorRuta } from 'src/app/modelos/retraso-ruta';
import { VuelosRutasService } from 'src/app/servicios/vuelos-rutas.service';

@Component({
  selector: 'app-por-ruta',
  templateUrl: './por-ruta.component.html',
  styleUrls: ['./por-ruta.component.css']
})
export class PorRutaComponent implements OnInit {

  vuelos: RetrasoPorRuta[]= [];
  public page = 1; // página actual
  public pageSize = 150; // número de páginas
  public maxSize = 10;

  constructor(private vuelosRutaService: VuelosRutasService) { }

  async ngOnInit(): Promise<void> {
    function delay(ms: number) {
      return new Promise( resolve => setTimeout(resolve, ms) );
    }
    let speedView=[2006,2007,2008];
    for (let year of speedView) {
      this.vuelosRutaService.getVuelos(year).subscribe(respuesta=>{
        console.log(respuesta);
        this.vuelos=respuesta;
      });
      await delay(3000);
    }
    
  }

  

}
