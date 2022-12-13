import '../App.css';
// import Alert from 'react-bootstrap/Alert';
import React from "react";
import SearchBar from '../components/SearchBar';



export default function HomePage() {


  return (
    <>
      <div className="d-flex align-items-center justify-content-center" style={{height: 100 + 'vh'}}>
      <div className="w-50">
        <div className="py-5">
          <h1 className="text-center">Arxiv Light</h1>
        </div>
        
          <SearchBar />
          </div>
        </div>
     
    </>
  );
}
