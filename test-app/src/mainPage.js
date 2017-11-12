import React, { Component } from 'react';
import {Button, Well, FormControl, FormGroup, ControlLabel, Row, Col, Image} from 'react-bootstrap';

import Template from './template';
import CircleGroup from './circleGroup'
import YouSeeing from './youSeeing'
import EntityButton from './entityButton'

const plus = 'assets/plus.png';
const lookup = 'assets/lookup.png';

class MainPage extends Component {

  constructor() {
    super();
    this.state = {
      user: ''
    }
    
    this.redirectNewProject = this.redirectNewProject.bind(this);
    this.redirectRegister = this.redirectRegister.bind(this);
    this.redirectProjectPage = this.redirectProjectPage.bind(this);
    this.redirectOUsPage = this.redirectOUsPage.bind(this);
    this.redirectSSsPage = this.redirectSSsPage.bind(this);
    this.editProject = this.editProject.bind(this);
    this.removeProject = this.removeProject.bind(this);
  }
    
  redirectNewProject() {
    this.props.history.push('./newProject')
  }

  redirectRegister() {
    this.props.history.push('./register')
  }
    
  redirectProjectPage() {
    this.props.history.push('./projectPage')
  }

  redirectOUsPage() {
    this.props.history.push('./listOrganizationUnits')
  }

  redirectSSsPage() {
    this.props.history.push('./listSupportSystems')
  }

  editProject(index) {
    return (e) => {
      console.log(index);
    };
  }

  removeProject(index) {
    return (e) => {
      console.log(index);
    }
  }

  render() {
    return (
      
      <Template history={this.props.history}>
        <YouSeeing title="Your BSP Projects"/>
        <Row>
          <Col md={3} sm={4} className="circle-create-col">
            <CircleGroup name="Create New Project" func={this.redirectNewProject} image={plus}/>
            <CircleGroup name="Add New User" func={this.redirectRegister} image={plus}/>
            <CircleGroup name="Organization Units" func={this.redirectOUsPage} image={lookup}/>
            <CircleGroup name="Support Systems" func={this.redirectSSsPage} image={lookup}/>
          </Col>

          <Col lg={6} md={7} sm={8}>
            <EntityButton
              title="Project #1"
              onClickFunc={this.redirectProjectPage}
              onClickEditFunc={this.editProject(1)}
              onClickRemoveFunc={this.removeProject(1)}
            />
            <EntityButton
              title="Project #2"
              onClickFunc={this.redirectProjectPage}
              onClickEditFunc={this.editProject(2)}
              onClickRemoveFunc={this.removeProject(2)}
            />
            <EntityButton
              title="Project #3"
              onClickFunc={this.redirectProjectPage}
              onClickEditFunc={this.editProject(3)}
              onClickRemoveFunc={this.removeProject(3)}
            />
          </Col>
        </Row>
      </Template>
       
       
    );
  }
}


export default MainPage;
