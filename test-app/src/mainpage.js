/*
import React, { Component } from 'react';
import {Button, Well, FormControl, FormGroup, ControlLabel, ButtonToolbar} from 'react-bootstrap';


import ReactDOM from "react-dom"


class Mainpage extends React.Component {
    
render() {
      //console.log("fyy");
    return (
        
     
            <h2> Isto só devia aparecer após o click no login </h2>
       
        
  
    );
    

  
//console.log("fyy");
  }
    
     
}


/*
class Tentativa extends React.Component{
    render(){
        return(
            <h2> Funciona  </h2>
        );
    }
} */

/*

    const appl = document.getElementById('root');
 ReactDOM.render(<Mainpage/>,appl);
export default Mainpage;
*/

import React, { Component } from 'react';
import {Button, Well, FormControl, FormGroup, ControlLabel} from 'react-bootstrap';

class MainPage extends Component {

  constructor() {
    super();
    this.state = {
      user: ''
    }
    
        this.redirectnewbsp = this.redirectnewbsp.bind(this);
        this.redirectprojectpage = this.redirectprojectpage.bind(this);
  }
    
     redirectnewbsp() {
       
    this.props.history.push('./newbsp')
  }
    
    redirectprojectpage() {
       
    this.props.history.push('./projectpage')
  }
   

  render() {
      
      var estilo_menu ={
          
          height: "500px",
          width: "30%",
          backgroundColor: "#f04f57",
          marginLeft: "-34%",
          marginTop: "3%",
          borderRadius: "15px"
     }
      
      var container_username={
          textAlign: "center",
          paddingTop: "0.1px"
      }
      
      var username = {
          fontSize: "25px",
          fontWeight: "normal",
          color: "white",
          opacity: "0.9"
      }
      
      var botao_new_bsp = {
          backgroundColor: "red",
          width: "70px",
          height: "70px",
          marginTop: "-60%",
          marginLeft: "10%",
          borderRadius: "100px",
          border: "1px solid white",
          backgroundColor: "#c3c3c9",
          textAlign: "center"
          
      }
      
      var plus ={
          fontSize: "35px",
          fontWeight: "lighter",
          color: "white",
          opacity: "0.9",
          marginTop: "10px"
      }
      
       var container_bsps ={
          
          height: "200px",
          width: "40%",
          border: "2px solid white",
          borderStyle: "dotted", 
          marginLeft: "32%",
          marginTop: "-9%",
          borderRadius: "15px",
           textAlign: "center"
     }
       
       var info_bsp={
          fontSize: "25px",
          fontWeight: "lighter",
          color: "white",
          opacity: "0.9",
           marginTop: "-13%",
           
       }
       
       var lista_bsps={
             borderRadius: "15px",
           textAlign: "center",
           backgroundColor: "#f8c97f",
           width: "80%",
           height: "20%",
          
           margin: "auto",
           textAlign: "center"
       }
      
       var project_text = {
             fontSize: "25px",
          fontWeight: "bold",
          color: "white",
          opacity: "0.9",
          
       }
       
    return (
        
    <div>    
      <div style={estilo_menu} >
        
        <div style={container_username}>
        <h2 style={username}> John Surname 
        </h2>
        </div>
       
      </div>
        
        
        <div style={botao_new_bsp}  onClick={this.redirectnewbsp}>
         <h2 style={plus}> + 
        </h2>
        </div>
        
        
        <div style={container_bsps}>
        <h2 style={info_bsp}> Your BSP Projects
        </h2>
        
        <div  style={lista_bsps}>    
         <h2 style={project_text} onClick={this.redirectprojectpage}> Project #1
        </h2>
        </div>
        
        <div  style={lista_bsps} onClick={this.redirectprojectpage}>    
         <h2 style={project_text}> Project #2
        </h2>
        </div>
        
        </div>
        
    </div>    
        
       
       
       
    );
  }
}


export default MainPage;
