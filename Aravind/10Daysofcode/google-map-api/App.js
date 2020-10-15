import React, { Component } from "react";
import "./App.css";
import { Map, Marker, GoogleApiWrapper } from "google-maps-react";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Map google={this.props.google} zoom={14}>
          <Marker onClick={this.onMarkerClick} name={"Current location"} />
        </Map>
      </div>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: ("AIzaSyAUCG8BaljTl8c4M67o3bKDRofCh6eZdfY")
})(App);
