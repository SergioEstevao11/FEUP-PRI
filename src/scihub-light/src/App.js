import './App.css';
// import Alert from 'react-bootstrap/Alert';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import React from "react";
import HomePage from './pages/HomePage';
import SearchResult from './pages/SearchResults'; 


function App() {


  return (
    <>
     <Router>
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="/searchresults/" element={<SearchResult/>} />
      </Routes>
    </Router>
    </>
  );
}

export default App;
