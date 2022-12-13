import '../App.css';
// import Alert from 'react-bootstrap/Alert';
import React from "react";
import SearchBar from '../components/SearchBar';
import ArticleCard from '../components/ArticleCard';
import arxiv_logo from '../assets/arxiv_logo.png';


export default function SearchResult() {

    const results = {
        "link": "http://arxiv.org/abs/1508.03329v1",
        "summary": "When faced with learning a set of inter-related tasks from a limited amount\nof usable data, learning each task independently may lead to poor\ngeneralization performance. Multi-Task Learning (MTL) exploits the latent\nrelations between tasks and overcomes data scarcity limitations by co-learning\nall these tasks simultaneously to offer improved performance. We propose a\nnovel Multi-Task Multiple Kernel Learning framework based on Support Vector\nMachines for binary classification tasks. By considering pair-wise task\naffinity in terms of similarity between a pair's respective feature spaces, the\nnew framework, compared to other similar MTL approaches, offers a high degree\nof flexibility in determining how similar feature spaces should be, as well as\nwhich pairs of tasks should share a common feature space in order to benefit\noverall performance. The associated optimization problem is solved via a block\ncoordinate descent, which employs a consensus-form Alternating Direction Method\nof Multipliers algorithm to optimize the Multiple Kernel Learning weights and,\nhence, to determine task affinities. Empirical evaluation on seven data sets\nexhibits a statistically significant improvement of our framework's results\ncompared to the ones of several other Clustered Multi-Task Learning methods.",
        "title": "Multi-Task Learning with Group-Specific Feature Space Sharing",
        "authors": [
         "Niloofar Yousefi",
         "Michael Georgiopoulos",
         "Georgios C. Anagnostopoulos"
        ],
        "date": "2015-8-13",
        "areas": [
         "Computer Science"
        ],
        "fields": [
         "Computer Science"
        ],
        "subjects": [
         "Machine Learning"
        ],
        "id": 32823
    }

    function moreLikeThis(){
        console.log("moreLikeThis")
    }

  return (
    <>
        <div>
            <img src={arxiv_logo} alt="arxiv_logo" style={{position:"absolute", width: "100px", margin:"15px"}}/>        
        </div>
      
        <div class="row">
            <div class="d-flex align-items-center justify-content-center" >
                <div class="w-50 my-3">
                <SearchBar />
                </div>
            </div>
        </div>
        
        <div class="d-flex align-items-center justify-content-end">
            <div class="mb-2" style={{marginRight: "11%"}}>
            <button type="button" class="btn btn-warning" onClick={moreLikeThis}>MoreLikeThis!</button>
            </div>
        </div>
      
        <div class="row justify-content-around">
            {/* { data.results.map(paper => <div class="col-10"> <ArticleCard data={paper} /> </div>) } */}
            
            <div class="col-10">
                <ArticleCard data={results}/>
            </div>
            <div class="col-10">
                <ArticleCard data={results}/>
            </div>
            <div class="col-10">
                <ArticleCard data={results}/>
            </div>  
        </div>
     
    </>
  );
}
