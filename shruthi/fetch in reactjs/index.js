import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import "./Fetapi.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import Fetapi from "./component/Fetapi";
ReactDOM.render(
  <React.StrictMode>
    <Fetapi />
  </React.StrictMode>,
  document.getElementById("root")
);
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
