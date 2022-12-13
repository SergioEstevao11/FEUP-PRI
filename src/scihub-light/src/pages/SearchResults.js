import '../App.css';
// import Alert from 'react-bootstrap/Alert';
import React, { useEffect } from "react";
import SearchBar from '../components/SearchBar';
import ArticleCard from '../components/ArticleCard';
import arxiv_logo from '../assets/arxiv_logo.png';
import Axios  from 'axios';


export default function SearchResult() {

    const [results, setResults] = React.useState({papers: {}});
    const [orderChanged, setOrderChanged] = React.useState(false);

    useEffect(() => {}, [results, orderChanged]);

    async function moreLikeThis(){
        console.log("moreLikeThis")
        const collection = document.getElementsByClassName("result_checkbox");
        var mlt_results = {};
        let first = true;
        if(collection.length === 0)
            return;
        for (let i=0; i < collection.length; i++){
            if (collection[i].checked){
                document.getElementById(collection[i].id).checked = false;
            
                await Axios.get("http://localhost:3001/moreLikeThis/"+collection[i].id ).then((response) => {
                    console.log(response);
                    if (first){
                        mlt_results = response.data;
                        first = false;
                    }
                    else{
                        mlt_results.papers = mlt_results.papers.concat(response.data.papers);
                    }
                }).catch((error) => {
                console.log(error);
                });
            }
        }
        
        console.log("mlt_results: ", mlt_results)
        setResults(mlt_results);
        
    }

  return (
    <>
        <div>
            <img src={arxiv_logo} alt="arxiv_logo" style={{position:"absolute", width: "100px", margin:"15px"}}/>        
        </div>
      
        <div class="row">
            <div class="d-flex align-items-center justify-content-center" >
                <div class="w-50 my-3">
                <SearchBar setResults={setResults} orderChanged={orderChanged} setOrderChanged={setOrderChanged}/>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-6">

            <div class="d-flex align-items-center justify-content-start">
                <div class="mb-2" style={{marginLeft: "17.2%"}}>
                <select class="form-select" aria-label="Default select example" id="orderBySelect" style={{visibility:"hidden"}} onChange={setOrderChanged(true)}>
                    <option selected value="Relevance">Relevance</option>
                    <option value="date asc">Date Ascending</option>
                    <option value="date desc">Date Descending</option>
                </select>
                </div>
            </div>
            </div>
            <div class="col-6">
                <div class="d-flex align-items-center justify-content-end">
                    <div class="mb-2" style={{marginRight: "25.5%"}}>
                    <button type="button" id="moreLikeThisBtn" class="btn btn-warning" onClick={moreLikeThis} style={{visibility:"hidden"}}>MoreLike...</button>
                    </div>
                </div>
            </div>
        </div>
      
        <div class="row justify-content-around">
            {Object.entries(results.papers).map(([key, value]) =>  <div class="col-10"> <ArticleCard data={value}/> </div>)}
        </div>
     
    </>
  );
}
