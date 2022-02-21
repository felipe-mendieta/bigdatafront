import { Component, OnInit } from '@angular/core';
import { RetrasoPorAerolinea } from 'src/app/modelos/retraso-aero';
import { VuelosAerolineasService } from 'src/app/servicios/vuelos-aerolineas.service';

@Component({
  selector: 'app-por-aerolinea',
  templateUrl: './por-aerolinea.component.html',
  styleUrls: ['./por-aerolinea.component.css']
})
export class PorAerolineaComponent implements OnInit {

  vuelos: RetrasoPorAerolinea[]= [];
  public page = 1; // página actual
  public pageSize = 150; // número de páginas
  public maxSize = 10;

  constructor(private vuelosAeroService: VuelosAerolineasService) { }

  async ngOnInit(): Promise<void> {
    function delay(ms: number) {
      return new Promise( resolve => setTimeout(resolve, ms) );
    }
    let speedView=[2007,2008,2007,2008];
    for (let year of speedView) {
      this.vuelosAeroService.getVuelos(year).subscribe(respuesta=>{
        console.log(respuesta);
        this.vuelos=respuesta;
      });
      await delay(3000);
    }
    
  }
}
