import React, {Component} from 'react';
import { Col, Container, Row } from 'reactstrap';
import {Grid, Cell} from 'react-mdl';


class Main extends Component{

    constructor(){
        super();
    }

  
    render() {
      let resumeData=this.props.resumeData;

        return(
          <div>
              <div>
                <Grid className="landing-grid">
                  <Cell col={12}>
                    <img
                      src="https://www.vexels.com/media/users//3/145908/raw/52eabf633ca6414e60a7677b0b917d92.jpg"
                      alt="avatar"
                      className="avatar-img"
                      />
        
                    <div className="bannertext">
                          <h1>Yogesh Thiru</h1>
            
            
                          <p>Student at Anna University, Chennai</p>
            
                        <div className="social-links">
            
                            {/* LinkedIn */}
                            <a href="https://www.linkedin.com/in/yogeshthiru01/" rel="noopener noreferrer" target="_blank">
                              <i className="fa fa-linkedin-square" aria-hidden="true" />
                            </a>
                  
                            {/* Github */}
                            <a href="https://github.com/YogeshThiru01/" rel="noopener noreferrer" target="_blank">
                              <i className="fa fa-github-square" aria-hidden="true" />
                            </a>
          
                          </div>
                    </div>
                  </Cell>
                
              

              <Cell  col={12}>
              <section id="about">
                  <div>
                    <div>
                            <h2>About Me</h2>
                            <p>
                            {
                              resumeData.aboutme
                            }
                            </p>

                            <div className="row">

                                <div className="contact-details">

                                <h2>Contact Details</h2>
                                <p className="address">
                                <span>{resumeData.name}</span>
                                  <br></br>
                                  <span>
                                  {resumeData.address}
                                  </span>
                                </p>
                                <p>
                                <span>{resumeData.mail}</span>
                                </p>
                                <p>
                                <span>{resumeData.contact}</span>
                                </p>
                                </div>
                            </div>
                      </div>
                  </div>
              </section>
              </Cell>


              <Cell  col={12}>
                <section id="resume">

                    <div className="row education">

                      <div className="three columns header-col">
                          <h1><span>Education</span></h1>
                      </div>

                      <div className="nine columns main-col">
                        {
                          resumeData.education && resumeData.education.map((item)=>{
                            return(
                              <div className="row item">
                                  <div className="twelve columns">
                                    <h3>{item.UniversityName}</h3>
                                    <p className="info">
                                    {item.specialization} 
                                    <span>&bull;</span> <em className="date">{item.MonthOfPassing} {item.YearOfPassing}</em></p>
                                    <p>
                                    {item.Percentage}
                                    </p>
                                  </div>
                              </div>
                            )
                          })
                        }
                      </div>
                    </div>
                    
                    <div className="row skill">

                      <div className="three columns header-col">
                          <h1><span>Skills</span></h1>
                      </div>

                      <div className="nine columns main-col">
                       <div className="bars">

                        <ul className="skills">
                          {
                            resumeData.skills && resumeData.skills.map((item) => {
                              return(
                                <li>
                                <span className={`bar-expand ${item.skillname.toLowerCase()}`}>
                                </span><em>{item.skillname}</em>
                                </li>
                              )
                            })
                          }

                        </ul>

                      </div>

                    </div>

                    </div>
                </section>
                </Cell>

                              <Cell>
                                <section id="portfolio">
                                      <div className="row">
                                        <div className="twelve columns collapsed">
                                          <h1>Check Out Some of My Works.</h1>
                                          <div id="portfolio-wrapper" className="bgrid-quarters s-bgrid-thirds cf">
                                          {
                                            resumeData.portfolio && resumeData.portfolio.map((item)=>{
                                              return(
                                                <div className="columns portfolio-item">
                                                  <div className="item-wrap">
                                                    <a href="https://github.com/YogeshThiru01/">
                                                      <img src="data:image/png;base64,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" className="item-img"/>
                                                      <div className="overlay">
                                                        <div className="portfolio-item-meta">
                                                          <h4>{item.name}</h4>
                                                          <p>{item.description}</p>
                                                        </div>
                                                      </div>
                                                    </a>
                                                  </div>
                                                </div>
                                              )
                                            })
                                          }
                                          </div>
                                        </div>
                                      </div>
                                  </section>
                                  </Cell>


                   <Cell>
                      <section id="testimonials">
                        <div className="text-container">
                          <div className="row">
                            <div className="two columns">
                              <h1 id="postion-head"><span>Positions</span></h1>
                            </div>
                            <br/><br/>
                            <br/>
                            <br/>
                            <div className="ten columns flex-container">
                              <div className="flexslider">
                                <ul className="slides">
                                  {
                                    resumeData.testimonials && resumeData.testimonials.map((item)=>{
                                      return(
                                        <li>
                                          <blockquote>
                                            <p>
                                            {item.description}
                                            </p>
                                            <cite>{item.name}</cite>
                                          </blockquote>
                                        </li>
                                      )
                                    })
                                  }
                                </ul>
                              </div> {/* div.flexslider ends */}
                            </div> {/* div.flex-container ends */}
                          </div> {/* row ends */}
                        </div>  {/* text-container ends */}
                      </section>
                   </Cell>


        </Grid>
       </div>
     
          </div>
        )
    }
}

export default Main;
