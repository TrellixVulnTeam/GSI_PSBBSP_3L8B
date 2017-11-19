import React, {Component} from 'react';
import { PageHeader, Col, Grid, Row} from 'react-bootstrap';
import {Switch, Route} from 'react-router-dom';

import './template.css';

import Login from './loginForm';
import Register from './register';
import MainPage from './mainPage';
import ListOrganizationUnits from './listOrganizationUnits'
import ListSupportSystems from './listSupportSystems'
import NewProject from './newProject';
import EditProject from './editProject';
import ProjectPage from './projectPage';
import NewProcess from './newProcess';
import ShowMatrices from './showMatrices';
import NewDataClass from './newDataClass';
import Subsystem from './subsystemPage';
import ProblemsSolutions from './problemsSolutions';

class Content extends Component {
  render() {
    return (
        <Switch>
          <Route path={'/'} exact component={MainPage}></Route>
          <Route path={'/login'} exact component={Login}></Route>
          <Route path={'/register'} exact component={Register}></Route>
          <Route path={'/listOrganizationUnits'} exact component={ListOrganizationUnits}></Route>
          <Route path={'/listSupportSystems'} exact component={ListSupportSystems}></Route>
          <Route path={'/newProject'} exact component={NewProject}></Route>
          <Route path={'/project/:number'} exact component={EditProject}></Route>
          <Route path={'/projectPage'} exact component={ProjectPage}></Route>
          <Route path={'/newProcess'} exact component={NewProcess}></Route>
          <Route path={'/showMatrices'} exact component={ShowMatrices}></Route>
          <Route path={'/newDataClass'} exact component={NewDataClass}></Route>
          <Route path={'/subsystemPage'} exact component={Subsystem}></Route>
          <Route path={'/problemsSolutions'} exact component={ProblemsSolutions}></Route>
        </Switch>
    );
  }
}

class App extends Component {
  render() {
    return (
      <Grid fluid>
        <Row>
          <PageHeader className="center-text">Business System Planning</PageHeader>
        </Row>
        <Content/>
      </Grid>
    );
  }
}

export default App;