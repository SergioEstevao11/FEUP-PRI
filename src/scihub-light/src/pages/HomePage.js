import '../App.css';
// import Alert from 'react-bootstrap/Alert';
import React from "react";
import SearchBar from '../components/SearchBar';



export default function HomePage() {


  return (
    <>
      <div class="d-flex align-items-center justify-content-center" style={{height: 100 + 'vh'}}>
      <div class="w-50">
        <div class="py-5">
          <h1 class="text-center">Arxiv Light</h1>
        </div>
        
          <SearchBar />
          </div>
        </div>
     
    </>
  );
}
