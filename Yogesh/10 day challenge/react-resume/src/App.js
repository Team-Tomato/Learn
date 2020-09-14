import React from 'react';
//import logo from './logo.svg';
import './App.css';
import Main from './Components/main.js';
import Education from './Components/education.js';
import resumeData from './resumeData';

function App() {
  return (
    <div>
      <Main resumeData={resumeData}/>
     

    </div>
  );
}

export default App;
