import React, { Component } from 'react';
import { Layout,Header, Navigation, Drawer, Content,Grid,Cell} from 'react-mdl';
import './App.css';


class App extends Component{
  render(){
    return(
      <div className=''>
      <Layout>
                             
          <Header className="header-color" title="Title" scroll>
            <Navigation>
                
                  <a href="#" className='slider-trigger'>Welcome</a>
                  <a href="#" className='slider-trigger'>Search QP</a>
                  <a href="#">Search Book</a>
                  <a href="#">Template</a>
                  <a href="#">Contributors</a>
                  <a href="#">Projects</a>
                  <a href="#">Contact</a>
                  
              </Navigation>
          </Header>
          <Drawer title="Title">
              <Navigation>
                  <a href="#">Link</a>
                  <a href="#">Link</a>
                  <a href="#">Link</a>
                  <a href="#">Link</a>
              </Navigation>
          </Drawer>
          <Content>
          <Grid className='grid-color'>
                  <Cell col={12}>
                <div>
                        <h1 align="center" id='font'>Refer QP , Search BOOK
                            <br />Try PROJECTS , Grow RESUME
                        </h1>
                        <h3 align="center" id='font'>
                            Keep Learning...Happy Coding...
                        </h3>
                </div>
                
               
                 </Cell>
              </Grid>
              <div id='img'>
                  
                </div>
              <div className='banner-text'>'
              <h3 id='font'>For Contact</h3>        
                </div>
          </Content>
      </Layout>
  </div>
   );
  }
}
export default App;
