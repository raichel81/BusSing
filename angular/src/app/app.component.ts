import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/toPromise';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  heading = 'Bus Sing';
  todayDate;
  url;
  title;
  code;
  language;
  style;
  owner;
  highlight;
  data;
  
  constructor(private http: HttpClient){}
  ngOnInit(): void {
    this.http.get<BusResponse>('http://localhost:4200/buses').subscribe(data => {
      this.data = data;
      this.url = data.url;
      this.title = data.title;
      this.code = data.code;
      this.language = data.language;
      this.style = data.style;
      this.owner = data.owner;
      this.highlight = data.highlight;
      this.todayDate = new Date();

    },
    (err: HttpErrorResponse) => {
      if (err.error instanceof Error) {
        // A client-side or network error occurred. Handle it accordingly.
        console.log('An error occurred:', err.error.message);
      } else {
        // The backend returned an unsuccessful response code.
        // The response body may contain clues as to what went wrong,
        console.log(`Backend returned code ${err.status}, body was: ${err.error}`);
      }
    });
  }
}


interface BusResponse {
  url: string;
  title: string;
  code: string;
  language: string;
  style: string;
  owner: string;
  highlight: string;
}