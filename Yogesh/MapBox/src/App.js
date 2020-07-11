import React, { useState, useEffect } from "react";
import ReactMapGL, { Marker, Popup } from "react-map-gl";
import * as data from "./stadiumdata";



export default function App() {
    const [viewport, setViewport] = useState({
        latitude: 11.1271,
        longitude: 78.6569,
        width: "100vw",
        height: "100vh",
        zoom: 6
    });
    const [selectedStadium, setSelectedStadium] = useState(null);
    useEffect(() => {
        const listener = e => {
            if (e.key === "Escape") {
                setSelectedStadium(null);
            }
        };
        window.addEventListener("keydown", listener);
        return () => {
            window.removeEventListener("keydown", listener);
        };
    }, []);
    return ( <
        div >
        <
        ReactMapGL {...viewport }
        mapboxApiAccessToken = 'pk.eyJ1IjoieW9nZXNodGhpcnUwMSIsImEiOiJja2M0ZnljNWwwN2VuMnpvMHN0aXQ2b3YwIn0.siIjmOXC_agaoPPDciyjuA'
        mapStyle = "mapbox://styles/mapbox/streets-v10"
        onViewportChange = { viewport => { setViewport(viewport); } } > {
            data.features.map(stadium => ( <
                Marker key = { stadium.properties.ID }
                latitude = { stadium.geometry.coordinates[0] }
                longitude = { stadium.geometry.coordinates[1] } >
                <
                button className = "marker"
                onClick = {
                    e => {
                        e.preventDefault();
                        setSelectedStadium(stadium);
                    }
                } >
                <
                img src = '/marker.svg'
                alt = "icon" / >
                <
                /button> < /
                Marker >
            ))
        } {
            selectedStadium ? ( <
                Popup latitude = { selectedStadium.geometry.coordinates[0] }
                longitude = { selectedStadium.geometry.coordinates[1] }
                onClose = {
                    () => { setSelectedStadium(null); }
                } >
                <
                div className = "popupmenu" >
                <
                h2 > { selectedStadium.properties.NAME } < /h2> <
                p > { selectedStadium.properties.DESCRIPTION } < /p> <
                p > < b > Address: < /b> {selectedStadium.properties.ADDRESS}</p >
                <
                p > < b > Ph.no: < /b> {selectedStadium.properties.PHONENO}</p >
                <
                p > < b > Establishment.: < /b> {selectedStadium.properties.ESTABLISHMENT}</p >
                <
                p > < b > Ratings: < /b> {selectedStadium.properties.RATING}</p >
                <
                p > < b > Capacity: < /b> {selectedStadium.properties.SEATING_CAPACITY}</p >
                <
                p > < b > Review: < /b> {selectedStadium.properties.REVIEWS}</p >
                <
                p > < b > Website: < /b> {selectedStadium.properties.WEBSITE}< /p > < /
                div > < /
                Popup >
            ) : null
        } <
        /ReactMapGL> < /
        div >
    );
}