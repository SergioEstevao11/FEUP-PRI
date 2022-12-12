import './App.css';
// import Alert from 'react-bootstrap/Alert';




function App() {
  return (
    <>
      <div class="d-flex align-items-center justify-content-center" style={{height: 100 + 'vh'}}>
      <div class="w-50">
        <div class="py-5">
          <h1 class="text-center">SciHub Light</h1>
        </div>
      
      <div class="container">
        <div class="input-group py-auto">
          <input type="search" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="search-addon" />
          <button type="button" class="btn btn-primary">Filters</button>     
          <button type="button" class="btn btn-outline-primary">Search</button>
        </div>
        <div class="form-check mt-5">
        <div class="container">

          <div class="row">
            <div class="col-4">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault"/>
              <label class="form-check-label" for="flexCheckDefault">
                Artificial Intelligence
              </label>
            </div>
            <div class="col-4">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault8"/>
              <label class="form-check-label" for="flexCheckDefault8">
                Artificial Intelligence
              </label>
            </div>
            <div class="col-4">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault9"/>
              <label class="form-check-label" for="flexCheckDefault9">
                Artificial Intelligence
              </label>
            </div>
          </div>
          <div class="">
          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault1"/>
          <label class="form-check-label" for="flexCheckDefault1">
            Statistics
          </label>
          </div>
          <div class="">
          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault2"/>
          <label class="form-check-label" for="flexCheckDefault2">
            Machine Learning
          </label>
          </div>
          <div class="">

          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault3"/>
          <label class="form-check-label" for="flexCheckDefault3">
            Mathematics
          </label>
          </div>
          <div class="">

          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault4"/>
          <label class="form-check-label" for="flexCheckDefault4">
            Physics
          </label>
          </div>
          <div class="">

          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault5"/>
          <label class="form-check-label" for="flexCheckDefault5">
            Chemistry
          </label>
          </div>
          </div>
        </div>
      </div>
      </div>
      </div>
    </>
  );
}

export default App;
