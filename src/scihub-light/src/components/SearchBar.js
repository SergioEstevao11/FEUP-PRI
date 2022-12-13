import '../App.css';
import React, { useEffect, useState } from "react";
import Select from "react-select";
import TextField from '@mui/material/TextField';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import tags from '../fixtures/tags.json';
import { useNavigate } from "react-router-dom";
import Axios  from 'axios';




export default function SearchBar({setResults, orderChanged, setOrderChanged}) {
  const [selectedAreas, setSelectedAreas] = useState();
  const [selectedFields, setSelectedFields] = useState();
  const [selectedSubjects, setSelectedSubjects] = useState();
  const [oldestDate, setOldestDate] = React.useState(Date.parse("1993-01-01"));
  const [recentDate, setRecentDate] = React.useState(Date.now());

  const navigate = useNavigate();

  useEffect(() => {
    if (orderChanged) search();
  }, [orderChanged]);

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

    
    let search = document.getElementById("query_search").value;
    let sortType;
    if (document.getElementById("orderBySelect")) {
      sortType = document.getElementById("orderBySelect").value;
    } else {
      sortType = "Relevance";
    }
    let ld = new Date(oldestDate);
    let rd = new Date(recentDate);
    let leftDate = ld.getFullYear() + "-" + (ld.getMonth() + 1) + "-" + ld.getDate() + "T00:00:00Z";
    let rightDate = rd.getFullYear() + "-" + (rd.getMonth() + 1) + "-" + rd.getDate() + "T00:00:00Z";

    let queryData = {
      query: search,
      sort: sortType,
      areas: JSON.stringify({areas: areas}),
      fields: JSON.stringify({fields: fields}),
      subjects: JSON.stringify({subjects: subjects}),
      date: JSON.stringify({date:[leftDate, rightDate]})
    }

    Axios.get("http://localhost:3001/search",{params: queryData}).then((response) => {
      console.log(response);
      let data = response.data;
      
      for (let i = 0; i < data.papers.length; i++) {
        for (let key in data.hightlightings[data.papers[i].id]) {
          let value = data.hightlightings[data.papers[i].id][key];
          if (key === "title" || key === "summary"){
            let to_match = value[0].replace("<b>", "").replace("</b>", "");
            let match_index = data.papers[i][key].indexOf(to_match);
            let start = data.papers[i][key].substring(0, match_index);
            let end = data.papers[i][key].substring(match_index + to_match.length);
            data.papers[i][key] = start + value[0] + end;
          }
          else{
            data.papers[i][key] = value;
          }
          
        }
        
      }

      setOrderChanged(false);

      if (data.papers.length > 0){
        document.getElementById("orderBySelect").style.visibility = "visible";
        document.getElementById("moreLikeThisBtn").style.visibility = "visible";
      }else{
        document.getElementById("orderBySelect").style.visibility = "hidden";
        document.getElementById("moreLikeThisBtn").style.visibility = "hidden";
      }
      setResults(data);
    }).catch((error) => {
      console.log(error);
    });

    navigate("/searchresults");
    
  }


  return (
    <>
      <div className="container">
          <div className="input-group py-auto">
            <input type="search" className="form-control" placeholder="Search" aria-label="Search" aria-describedby="search-addon" id="query_search"/>
            <button type="button" className="btn btn-primary" onClick={showFilters}>Filters</button>     
            <button type="button" className="btn btn-outline-primary" onClick={search}>Search</button>
          </div>
        <div className="form mt-3" id="filters" style={{visibility: "hidden"}}>
        <div className="row">
            <div className="col-6" style={{paddingLeft: 15 + '%'}}>
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
            <div className="col-6">
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
        <div className="row mt-3">
        <div className="col-4">
                <Select id="areas"
                options={AreasList}
                placeholder="Select Areas"
                value={selectedAreas}
                onChange={handleSelectArea}
                isSearchable={true}
                isMulti/>
            </div>
            <div className="col-4">
                <Select id="fields"
                options={FieldsList}
                placeholder="Select Fields"
                value={selectedFields}
                onChange={handleSelectField}
                isSearchable={true}
                isMulti
                />
            </div>
            <div className="col-4">

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
