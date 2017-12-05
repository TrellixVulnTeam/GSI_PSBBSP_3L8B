import React, { Component } from 'react';
import {PageHeader, Form, Button, Well, FormControl, FormGroup, ControlLabel, Col, MenuItem, DropdownButton, ButtonGroup} from 'react-bootstrap';

import Template from './template'
import * as CRUD from './CRUD';

class NewProject extends Component {

  constructor() {
    super();

    var user = CRUD.getUser();

    this.state = {
      projectName: '',
      selectedTeamLeader: 'Select a team leader',
      selectedSecretary: 'Select a secretary',
      email: user.email,
      role: '----'
    }

    this.listUsers = CRUD.getUsersInOrg();
    this.redirectMainPage = this.redirectMainPage.bind(this);
    this.updateDropdownSecreatary = this.updateDropdownSecreatary.bind(this);
    this.updateDropdownTeamLeader = this.updateDropdownTeamLeader.bind(this);
    this.onChangeProjName = this.onChangeProjName.bind(this);
    this.getUsersForSecretary = this.getUsersForSecretary.bind(this);
    this.getUsersForTeamLeader = this.getUsersForTeamLeader.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  updateDropdownTeamLeader(index) {
    this.setState({selectedTeamLeader: this.listUsers[index].email});
  }
   
  updateDropdownSecreatary(index) {
    this.setState({selectedSecretary: this.listUsers[index].email});
  }

  onChangeProjName(e) {
    this.setState({projectName: e.target.value});
  }

  getUsersForSecretary() {
    return this.listUsers.map((user, index) => 
      <MenuItem key={index} eventKey={index} onSelect={this.updateDropdownSecreatary}>{user.email}</MenuItem>
    );
  }

  getUsersForTeamLeader() {
    return this.listUsers.map((user, index) => 
      <MenuItem key={index} eventKey={index} onSelect={this.updateDropdownTeamLeader}>{user.email}</MenuItem>
    );
  }

  handleSubmit(e) {
    e.preventDefault();
    if (this.state.projectName && this.state.selectedSecretary !== 'Select a secretary' && this.state.selectedTeamLeader !== 'Select a team leader') {
      CRUD.createProject(this.state.projectName, this.state.selectedSecretary, this.state.selectedTeamLeader);
      this.redirectMainPage();
    }
  }

  redirectMainPage(e) {
    this.props.history.push('./')
  }

  render() {
    return (
      <Template history={this.props.history} email={this.state.email} role={this.state.role}>
        <Col md={10}>
          <Well bsSize='large'>
            <Form horizontal onSubmit={this.handleSubmit}>
              <Col smOffset={3} sm={9}>
                <PageHeader><small>New BSP Project</small></PageHeader>
              </Col>
              <FormGroup controlId="projectName">
                <Col componentClass={ControlLabel} sm={3}>Project Name</Col>
                <Col sm={9}>
                  <FormControl 
                    type="text" 
                    placeholder="Enter Project's Name"
                    onChange={this.onChangeProjName}
                  />
                </Col>
              </FormGroup>

              <FormGroup controlId="teamLeaderUser">
                <Col componentClass={ControlLabel} sm={3}>Team Leader</Col>
                <Col sm={9}>
                  <ButtonGroup vertical block>
                    <DropdownButton title={this.state.selectedTeamLeader} id="dropdown-size-medium" block>
                      {this.getUsersForTeamLeader()}
                    </DropdownButton>
                  </ButtonGroup>
                </Col>
              </FormGroup>

              <FormGroup controlId="secretaryUser">
                <Col componentClass={ControlLabel} sm={3}>Secretary</Col>
                <Col sm={9}>
                  <ButtonGroup vertical block>
                    <DropdownButton title={this.state.selectedSecretary} id="dropdown-size-medium">
                      {this.getUsersForSecretary()}
                    </DropdownButton>
                  </ButtonGroup>
                </Col>
              </FormGroup>

              <hr className="darkGrey"/>

              <FormGroup>
                <Col smOffset={8} sm={4}>
                  <Button type="submit" bsStyle='warning' bsSize='large' block>Create</Button>
                </Col>
              </FormGroup>
            </Form>
          </Well>
        </Col>
      </Template>
    );
  }
}


export default NewProject;
