import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';


export default function ArticleCard({data}) {
    const date = (new Date(data.date)).toString().split(" ").slice(1,4).join(" ");

    const card = (
        <React.Fragment>
          <CardContent>
            <Typography sx={{ fontSize: 12 }} color="text.secondary" gutterBottom>
              Areas:  <span dangerouslySetInnerHTML={{__html: data.areas}}></span> ; Fields:  <span dangerouslySetInnerHTML={{__html: data.fields}}></span> ; Subjects:  <span dangerouslySetInnerHTML={{__html: data.subjects}}></span>
            </Typography>
            <Typography variant="h5" component="div">
                <div dangerouslySetInnerHTML={{__html: data.title}}></div>
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
            <div dangerouslySetInnerHTML={{__html: data.authors}}></div>
                <br/>
                {date}
                
            </Typography>
            <Typography variant="body2">
                <div dangerouslySetInnerHTML={{__html: data.summary}}></div>
              <br />
            </Typography>
          </CardContent>
          <CardActions>
            <Button size="small" href={data.link} target="_blank">Learn More</Button>
          </CardActions>
        </React.Fragment>
      );
  return (
    <Box sx={{ minWidth: 275}} key={data.id}>

      <Card variant="outlined">
        <div className="d-flex" style={{marginLeft: "90%"}}>
            <input type="checkbox" className="result_checkbox" id={data.id}/>
            <label for={data.id}>This!</label>
        </div>
      {card}
      </Card>
    </Box>
  );
}