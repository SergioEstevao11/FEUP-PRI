import './App.css';
// import Alert from 'react-bootstrap/Alert';
import React, { useEffect, useState } from "react";
import Select from "react-select";
import TextField from '@mui/material/TextField';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import tags from './fixtures/tags.json';



function App() {
  const [selectedAreas, setSelectedAreas] = useState();
  const [selectedFields, setSelectedFields] = useState();
  const [selectedSubjects, setSelectedSubjects] = useState();
  const [oldestDate, setOldestDate] = React.useState(Date.parse("1993-01-01"));
  const [recentDate, setRecentDate] = React.useState(Date.now());

  // Array of all options
  var AreasList = tags.areas.map((area) => {
    return { value: area, label: area };
  });

  var FieldsList = FieldsList = tags.fields.map((field) => {
    return { value: field, label: field };
  });

  var SubjectsList = tags.subjects.map((subject) => {
    return { value: subject, label: subject };
  });

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
    if (document.getElementById("filters").style.visibility === "hidden")
      document.getElementById("filters").style.visibility = "visible";
    else
      document.getElementById("filters").style.visibility = "hidden";
    
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
                      value={oldestDate}
                      onChange={(oldestDate) => {
                        setOldestDate(oldestDate);
                      }}
                      renderInput={(params) => <TextField {...params} />}
                    />
                  </LocalizationProvider>
              </div>
              <div class="col-6">
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <DatePicker
                      label="Basic example"
                      value={recentDate}
                      onChange={(recentDate) => {
                        setRecentDate(recentDate);
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
