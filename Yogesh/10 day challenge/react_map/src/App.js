import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
//import logo from './logo.svg';
//import './App.css';

//lat 13.011164
//lon 80.235437

const AnyReactComponent = ({ text }) => <div>
                                          {text}
                                        </div>;


class SimpleMap extends Component {

  static defaultProps={
    center:{
      lat:13.01,
      lng:80.23
    },zoom:15
  };

  render(){
    return(

      <div style={{height:'100vh',width:'100%'}}>
        <GoogleMapReact
          bootstrapURLKeys={{key:"AIzaSyBTMsi_y15FeYl2Pqh7hyy9Q1fZykA3MWY"}}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
          >
          <AnyReactComponent
            lat={13.011164}
            lng={80.235437}
            text="Anna University, CEG Campus"
            />
        </GoogleMapReact>
      </div>

    );
  }

}

export default SimpleMap;
