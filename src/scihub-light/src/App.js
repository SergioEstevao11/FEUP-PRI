import './App.css';
// import Alert from 'react-bootstrap/Alert';
import React, { useState } from "react";
import Select from "react-select";
import TextField from '@mui/material/TextField';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';


function App() {
  const [selectedAreas, setSelectedAreas] = useState();
  const [selectedFields, setSelectedFields] = useState();
  const [selectedSubjects, setSelectedSubjects] = useState();
  const [value, setValue] = React.useState(Date.now());


  // Array of all options
  const AreasList = [
    { value: "red", label: "Red" },
    { value: "green", label: "Green" },
    { value: "yellow", label: "Yellow" },
    { value: "blue", label: "Blue" },
    { value: "white", label: "White" },
    { value: "black", label: "Black" },
    { value: "orange", label: "Orange" },
    { value: "purple", label: "Purple" },
    { value: "brown", label: "Brown" },
    { value: "grey", label: "Grey" },
    { value: "pink", label: "Pink" },
    { value: "silver", label: "Silver" },
    { value: "gold", label: "Gold" },
    { value: "beige", label: "Beige" },
    { value: "maroon", label: "Maroon" },
    { value: "navy", label: "Navy" },
    { value: "olive", label: "Olive" },
    { value: "teal", label: "Teal" }

  ];

  const FieldsList = [
    { value: "red", label: "Red" },
    { value: "green", label: "Green" },
    { value: "yellow", label: "Yellow" },
    { value: "blue", label: "Blue" },
    { value: "white", label: "White" },
    { value: "black", label: "Black" },
    { value: "orange", label: "Orange" },
    { value: "purple", label: "Purple" },
    { value: "brown", label: "Brown" },
    { value: "grey", label: "Grey" },
    { value: "pink", label: "Pink" },
    { value: "silver", label: "Silver" },
    { value: "gold", label: "Gold" },
    { value: "beige", label: "Beige" },
    { value: "maroon", label: "Maroon" },
    { value: "navy", label: "Navy" },
    { value: "olive", label: "Olive" },
    { value: "teal", label: "Teal" }

  ];

  const SubjectsList = [
    { value: "red", label: "Red" },
    { value: "green", label: "Green" },
    { value: "yellow", label: "Yellow" },
    { value: "blue", label: "Blue" },
    { value: "white", label: "White" },
    { value: "black", label: "Black" },
    { value: "orange", label: "Orange" },
    { value: "purple", label: "Purple" },
    { value: "brown", label: "Brown" },
    { value: "grey", label: "Grey" },
    { value: "pink", label: "Pink" },
    { value: "silver", label: "Silver" },
    { value: "gold", label: "Gold" },
    { value: "beige", label: "Beige" },
    { value: "maroon", label: "Maroon" },
    { value: "navy", label: "Navy" },
    { value: "olive", label: "Olive" },
    { value: "teal", label: "Teal" }

  ];

  // Function triggered on selection
  function handleSelectArea(data) {
    setSelectedAreas(data);
  }

  function handleSelectField(data) {
    setSelectedFields(data);
  }

  function handleSelectSubject(data) {
    setSelectedSubjects(data);
  }

  function showFilters() {
    if (document.getElementById("filters").style.display === "none")
      document.getElementById("filters").style.display = "block";
    else
      document.getElementById("filters").style.display = "none";
    
    console.log("here")
  }


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
            <button type="button" class="btn btn-primary" onClick={showFilters}>Filters</button>     
            <button type="button" class="btn btn-outline-primary">Search</button>
          </div>
          <div class="form mt-3" id="filters">

            <div class="row">
              <div class="col-6" style={{paddingLeft: 15 + '%'}}>
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <DatePicker
                      label="Basic example"
                      value={value}
                      onChange={(newValue) => {
                        setValue(newValue);
                      }}
                      renderInput={(params) => <TextField {...params} />}
                    />
                  </LocalizationProvider>
              </div>
              <div class="col-6">
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <DatePicker
                      label="Basic example"
                      value={value}
                      onChange={(newValue) => {
                        setValue(newValue);
                      }}
                      renderInput={(params) => <TextField {...params} />}
                    />
                  </LocalizationProvider>
                </div>
            </div>
            <div class="row mt-3">
            <div class="col-4">
                  <Select id="areas"
                    options={AreasList}
                    placeholder="Select Areas"
                    value={selectedAreas}
                    onChange={handleSelectArea}
                    isSearchable={true}
                    isMulti/>
              </div>
              <div class="col-4">
                  <Select id="fields"
                    options={FieldsList}
                    placeholder="Select Fields"
                    value={selectedFields}
                    onChange={handleSelectField}
                    isSearchable={true}
                    isMulti
                  />
              </div>
              <div class="col-4">

                <Select id="subjects"
                    options={SubjectsList}
                    placeholder="Select Subjects"
                    value={selectedSubjects}
                    onChange={handleSelectSubject}
                    isSearchable={true}
                    isMulti
                  />
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
