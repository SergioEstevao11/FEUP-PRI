import '../App.css';
import React, { useState } from "react";
import Select from "react-select";
import TextField from '@mui/material/TextField';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import tags from '../fixtures/tags.json';
import { useNavigate } from "react-router-dom";




export default function SearchBar() {
  const [selectedAreas, setSelectedAreas] = useState();
  const [selectedFields, setSelectedFields] = useState();
  const [selectedSubjects, setSelectedSubjects] = useState();
  const [oldestDate, setOldestDate] = React.useState(Date.parse("1993-01-01"));
  const [recentDate, setRecentDate] = React.useState(Date.now());

  const navigate = useNavigate();

  // Array of all options
  var AreasList = tags.areas.map((area) => {
    return { value: area, label: area };
  });

  var FieldsList = tags.fields.map((field) => {
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

  function search(){
    let areas = [];
    let fields = [];
    let subjects = [];
    if (selectedAreas !== undefined) 
      areas = selectedAreas.map((area) => area.value);
    if (selectedFields !== undefined)
      fields = selectedFields.map((field) => field.value);
    
    if (selectedSubjects !== undefined)
      subjects = selectedSubjects.map((subject) => subject.value);
    
    let ld = new Date(oldestDate);
    let rd = new Date(recentDate);
    let leftDate = ld.getFullYear() + "-" + (ld.getMonth() + 1) + "-" + ld.getDate();
    let rightDate = rd.getFullYear() + "-" + (rd.getMonth() + 1) + "-" + rd.getDate();

    let queryData = {
      areas: areas,
      fields: fields,
      subjects: subjects,
      oldestDate: leftDate,
      recentDate: rightDate
    }

    //call endpoint

    navigate("/searchresults/query");
    
  }


  return (
    <>
      <div class="container">
          <div class="input-group py-auto">
            <input type="search" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="search-addon" />
            <button type="button" class="btn btn-primary" onClick={showFilters}>Filters</button>     
            <button type="button" class="btn btn-outline-primary" onClick={search}>Search</button>
          </div>
        <div class="form mt-3" id="filters" style={{visibility: "hidden"}}>
        <div class="row">
            <div class="col-6" style={{paddingLeft: 15 + '%'}}>
                <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                    label="Oldest"
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
                    label="Earliest"
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

    </>
  );
}
