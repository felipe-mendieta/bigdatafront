import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PorAerolineaComponent } from './componentes/por-aerolinea/por-aerolinea.component';
import { PorRutaClimaComponent } from './componentes/por-ruta-clima/por-ruta-clima.component';
import { PorRutaComponent } from './componentes/por-ruta/por-ruta.component';
import { PrincipalComponent } from './principal/principal.component';

const routes: Routes = [
  { path: 'principal', component: PrincipalComponent },
  { path: '', redirectTo: 'principal', pathMatch: 'full' },
  { path: 'vuelos-ruta', component: PorRutaComponent},
  { path: 'vuelos-aerolinea', component: PorAerolineaComponent},
  { path: 'vuelos-ruta-clima', component: PorRutaClimaComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
