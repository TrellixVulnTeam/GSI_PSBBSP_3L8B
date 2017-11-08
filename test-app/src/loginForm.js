import React, { Component } from 'react';
import {Button, Well, Col, Form, PageHeader, FormControl, FormGroup, ControlLabel} from 'react-bootstrap';

import TemplateSimple from './template-no-sidebar';

class Login extends Component {

  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: ''
    }

    this.redirectRegister = this.redirectRegister.bind(this);
    this.redirectmainpage = this.redirectmainpage.bind(this);
  }

  redirectRegister() {
    console.log(this.props)
    this.props.history.push('./register')
  }
    
  redirectmainpage() {     
    this.props.history.push('./')
  }

  render() {
    return (
        <TemplateSimple>
          <Well bsSize='large'>
            <Col smOffset={2}>
              <PageHeader><small>Login form</small></PageHeader>
            </Col>
            <Form horizontal>
              <FormGroup controlId="formEmail">
                <Col componentClass={ControlLabel} sm={2}>
                  E-mail
                </Col>
                <Col sm={10}>
                  <FormControl
                    type="text"
                    defaultValue="" //com deafultvalue fica alteravel
                    placeholder="Enter Username"
                  />
                </Col>
                  <FormControl.Feedback />
              </FormGroup>
              <FormGroup controlId="formPassword">
                <Col componentClass={ControlLabel} sm={2}>
                  Password
                </Col>
                <Col sm={10}>
                  <FormControl 
                    type="text"
                    defaultValue=""
                    placeholder="Enter Password"
                  />
                </Col>
                <FormControl.Feedback />
              </FormGroup>

              <FormGroup>
                <Col smOffset={2} sm={4} md={3}>
                  <Button type="submit" bsStyle='danger' bsSize='large' onClick={this.redirectmainpage} block>
                    Login
                  </Button>
                </Col>
                <Col sm={4} md={3}>
                  <Button bsStyle='danger' bsSize='large' onClick={this.redirectRegister} block>
                    Register
                  </Button>
                </Col>
              </FormGroup>
            </Form>
          </Well>
        </TemplateSimple>
    );
  }
}

export default Login;