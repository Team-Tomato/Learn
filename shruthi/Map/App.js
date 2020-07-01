import React, { useState, useEffect } from "react";
import ReactMapGL, { Marker, Popup } from "react-map-gl";
import * as cricketData from "./data/cricket-grounds.json";
export default function App() {
  const [viewport, setViewport] = useState({
    latitude: 11.1271,
    longitude: 78.6569,
    width: "100vw",
    height: "100vh",
    zoom: 10,
  });
  const [selectedGround, setSelectedGround] = useState(null);
  useEffect(() => {
    const listener = (e) => {
      if (e.key == "Escape") {
        setSelectedGround(null);
      }
    };
    window.addEventListener("keydown", listener);
    return () => {
      window.removeEventListener("keydown", listener);
    };
  }, []);
  return (
    <div>
      <ReactMapGL
        {...viewport}
        mapboxApiAccessToken="pk.eyJ1Ijoic2hydXRoaTEyMCIsImEiOiJja2J3ZDg2emUwZXZ2MnNucTNsZ3Vpejl0In0.NHPq95OFCnucqIdRv8ZNAg"
        mapStyle="mapbox://styles/shruthi120/ckbxtetqv1uti1iqqa7oo8bs0"
        onViewportChange={(viewport) => {
          setViewport(viewport);
        }}
      >
        {cricketData.features.map((cricket) => (
          <Marker
            key={cricket.properties.PARK_ID}
            latitude={cricket.geometry.coordinates[0]}
            longitude={cricket.geometry.coordinates[1]}
          >
            <button
              className="marker-btn"
              onClick={(e) => {
                e.preventDefault();
                setSelectedGround(cricket);
              }}
            >
              <img src="/cri.png" alt="Cricet Icon" />
            </button>
          </Marker>
        ))}
        {selectedGround ? (
          <Popup
            latitude={selectedGround.geometry.coordinates[0]}
            longitude={selectedGround.geometry.coordinates[1]}
            onClose={() => {
              setSelectedGround(null);
            }}
          >
            <div>
              <p>
                <h4>
                  {selectedGround.properties.NAME} (
                  {selectedGround.properties.RATING})
                </h4>
              </p>
              <h7> {selectedGround.properties.WEBSITE}</h7>
              <p>{selectedGround.properties.DESCRIPTION}</p>
              <p>
                <h4>
                  {selectedGround.properties.ADDRESS}
                  {selectedGround.properties.CODE} , ({" "}
                  {selectedGround.properties.PHONENO} ) ,
                  {selectedGround.properties.ESTABLISHMENT}
                </h4>
              </p>
            </div>
          </Popup>
        ) : null}
      </ReactMapGL>
    </div>
  );
}
