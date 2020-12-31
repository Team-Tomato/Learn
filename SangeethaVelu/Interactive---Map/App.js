import React, {useState,useEffect} from "react";
import ReactMapGl,{Marker,Popup} from "react-map-gl";
import * as Cricketdata from "./data/Cricket.json";
export default function App(){
  const [viewport,setViewport] = useState(
    {
      latitude: 11.1271,
    longitude: 78.6569,
    width: "100vw",
    height: "100vh",
    zoom: 10,
    }
  );
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
    <ReactMapGl 
    {...viewport}
mapboxApiAccessToken="pk.
eyJ1Ijoic2FuZ2VldGhhdmVsdSIsImEiOiJja2ZqZ3hxOXIwaDdkMzBxaHFpcW5iNGF5In0.dL09uNJTuQHOADYlIHK10g"
mapStyle="mapbox://styles/sangeethavelu/ckfjln7j4594k19mrvn537zf7"
onViewportChange={viewport => {
  setViewport(viewport);
}}
>
{Cricketdata.features.map((cricket) => (
          <Marker
            key={cricket.properties.CRICKET_ID}
            latitude={cricket.geometry.coordinates[0]}
            longitude={cricket.geometry.coordinates[1]}
          >
            <button class="marker-btn " onClick={(e) => {
                e.preventDefault();
                setSelectedGround(cricket);
              }}>
              <img src=".\image\criketimg.png" alt="Cricket Icon"/>
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
      </ReactMapGl>
    </div>
  );
}