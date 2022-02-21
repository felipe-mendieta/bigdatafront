import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatPaginatorModule } from '@angular/material/paginator';
import { NgbModule, NgbPaginationModule } from '@ng-bootstrap/ng-bootstrap';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PrincipalComponent } from './principal/principal.component';
import { PorAerolineaComponent } from './componentes/por-aerolinea/por-aerolinea.component';
import { PorRutaClimaComponent } from './componentes/por-ruta-clima/por-ruta-clima.component';
import { PorRutaComponent } from './componentes/por-ruta/por-ruta.component';

@NgModule({
  declarations: [
    AppComponent,
    PrincipalComponent,
    PorAerolineaComponent,
    PorRutaClimaComponent,
    PorRutaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatButtonModule,
    MatTableModule,
    MatToolbarModule,
    MatPaginatorModule,
    NgbModule,
    NgbPaginationModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
