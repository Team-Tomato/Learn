import React, { Component } from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';
import './App.css';
class App extends Component{
  render(){
    return (
      <Map
        google={this.props.google}
        zoom={7}
        initialCenter={{
         lat: 11.1271,
         lng: 78.6569}}>
           <Marker onClick={this.onMarkerClick} name={"My Marker"}/>
      </Map>
    );
  }
}
export default GoogleApiWrapper({
  apiKey:'AIzaSyCBzCx2TGwPUjxqGaRpLu-7c5tPYNIdYlI'
})(App);