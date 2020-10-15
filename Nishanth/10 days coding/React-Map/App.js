import React, { Component } from 'react';
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
import logo from './logo.svg';
import './App.css';

class  App extends Component{
  render(){
  return (
    <div className="App">
      <Map google={this.props.google} zoom={14}>
 
 <Marker onClick={this.onMarkerClick}
         name={'Current location'} />

 <InfoWindow onClose={this.onInfoWindowClose}>

 </InfoWindow>
</Map>
    </div>
  );
}
    
}

export default GoogleApiWrapper({
  apiKey: ("AIzaSyA06SsEj24MzvrExLayQH6cVRkInCL2s94")
})(App)