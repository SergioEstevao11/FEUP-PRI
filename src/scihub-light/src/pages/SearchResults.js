import '../App.css';
// import Alert from 'react-bootstrap/Alert';
import React from "react";
import SearchBar from '../components/SearchBar';
import ArticleCard from '../components/ArticleCard';
import arxiv_logo from '../assets/arxiv_logo.png';
import Axios  from 'axios';


export default function SearchResult() {

    const [results, setResults] = React.useState({papers: {}});

    function moreLikeThis(){
        console.log("moreLikeThis")
        Axios.get("http://localhost:3001/moreLikeThis/34768").then((response) => {
            console.log(response);
            }).catch((error) => {
            console.log(error);
            });
    }

  return (
    <>
        <div>
            <img src={arxiv_logo} alt="arxiv_logo" style={{position:"absolute", width: "100px", margin:"15px"}}/>        
        </div>
      
        <div class="row">
            <div class="d-flex align-items-center justify-content-center" >
                <div class="w-50 my-3">
                <SearchBar setResults={setResults}/>
                </div>
            </div>
        </div>
        
        <div class="d-flex align-items-center justify-content-end">
            <div class="mb-2" style={{marginRight: "11%"}}>
            <button type="button" class="btn btn-warning" onClick={moreLikeThis}>MoreLikeThis!</button>
            </div>
        </div>
      
        <div class="row justify-content-around">
            {/* { results.data.papers.map(paper => <div class="col-10"> <ArticleCard data={paper} /> </div>) } */}
            {Object.entries(results.papers).map(([key, value]) =>  <div class="col-10"> <ArticleCard data={value}/> </div>)}
        </div>
     
    </>
  );
}
