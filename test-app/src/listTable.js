import React, { Component } from 'react';
import {Table, Glyphicon, Col} from 'react-bootstrap';

const ListTableLine = ({index, name, deleteFunc}) => (
  <tr>
    <td>{index}</td>
    <td>{name}</td>
    <td>
      <Col sm={6}>
        <a onClick={deleteFunc}>
          <Glyphicon glyph="remove" className="red"/>
        </a>
      </Col>
    </td>
  </tr>
)

const ListTableLineEdit = ({index, name, editFunc, deleteFunc}) => (
  <tr>
    <td>{index}</td>
    <td>{name}</td>
    <td>
      <Col sm={6}>
        <a onClick={editFunc}>
          <Glyphicon glyph="pencil" className="darkGrey"/>
        </a>
      </Col>
      <Col sm={6}>
        <a onClick={deleteFunc}>
          <Glyphicon glyph="remove" className="red"/>
        </a>
      </Col>
    </td>
  </tr>
)

class ListTable extends Component {
  constructor(props) {
    super(props);
    this.state={};
    this.enableEdit = true && !this.props.disableEdit;
    this.getTableLines = this.getTableLines.bind(this);
  }

  getTableLines() {

    if (this.enableEdit) {
      return this.props.data.map((entity) => 
        <ListTableLineEdit
          key={entity.index}
          index={entity.index} 
          name={entity.name} 
          editFunc={this.props.editFunc} 
          deleteFunc={this.props.deleteFunc}
        />
      );
    }
    else {
      return this.props.data.map((entity) => 
        <ListTableLine
          key={entity.index}
          index={entity.index} 
          name={entity.name} 
          deleteFunc={this.props.deleteFunc}
        />
      );
    }
  }

  render() {
    return (
      <Table striped bordered condensed hover>
        <thead>
          <tr>
            <th>#</th>
            <th>{this.props.entityName}</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {this.getTableLines()}
        </tbody>
      </Table>
    )
  }
}


export default ListTable;