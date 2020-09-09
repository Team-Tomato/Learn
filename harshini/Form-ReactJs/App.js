import React from 'react';
import {Container, Row, Col } from 'reactstrap';
import FormDetail from './Component/form';
import Header from './Component/header';
function App() {
  return (
    <Container>
      <Row>
        <Col>
        <Header />
        </Col>
      </Row>
      <Row>
        <Col md = {5}>
        <FormDetail />
        </Col>
      </Row>
    </Container>
      
  );
}

export default App;
