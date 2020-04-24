import React, {Component} from 'react';
import img1 from '../images/tomato.jpg';
import img2 from '../images/logo.jpg';
import img3 from '../images/assistant.jpg';
import img4 from '../images/movie recommand.jpg';
import img5 from '../images/people thoughts.jpg';


class Card extends Component{
    render(){
        return(
            <div className="container-fluid d-flex justify-content-center">
                <div className='row'>
                    <div className='col-md-6 col-sm-4'>
                        
                <h4 className='card-title'>Team Tomato</h4>
                
                <img src={img1} alt='Image 1' className='card-img-top'/>
            
            
            <div className="card-body text-dark">
                <p className="card-text text-secondary">
                    Team which is determined to spread the love of open source (oss)
                </p>
                <a href='#' className='btn btn-outline-success'>https://github.com/Team-Tomato/</a>
                <p className="tech-stack text-secondary">
                    Top languages used-Javascript,
                    Python,
                    HTML
                </p>
            </div> 
            </div>
            <div className='col-md-6 col-sm-4'>
            <h4 className='card-title'>One click for CEG</h4>
            
                <img src={img2} alt='Image 2' className='card-img-top'/>
                
            
            <div className="card-body text-dark">
                
                <p className="card-text text-secondary">
                    Extension which directs to all CEG related websites
                </p>
                <a href='#' className='btn btn-outline-success'>https://github.com/Team-Tomato/oneClick-chrome-extension</a>
                <p className="tech-stack text-secondary">
                    Done using HTML and Javascript
                </p>
            </div> 
            </div>
            <div className='col-md-6 col-sm-4'>
                        
                        <h4 className='card-title'>Movie-recommandation Action</h4>
                       
                        <img src={img4} alt='Image 4' className='card-img-top'/>
                        
                    
                    <div className="card-body text-dark">
                        <p className="card-text text-secondary">
                            -----------------
                        </p>
                        <a href='#' className='btn btn-outline-success'>https://github.com/Team-Tomato/Movie_Recommendation_Backend</a>
                        <p className="tech-stack text-secondary">
                            Done using Python
                        </p>
                    </div> 
                    </div>
           
            
            </div>
            <div className='row'>
             <div className='col-md-9 col-sm-3'>
            <h4 className='card-title'>Team Tomato Action</h4>
            
            
                <img src={img3} alt='Image 3' className='card-img-top'/>
                
            
            <div className="card-body text-dark">
                
                <p className="card-text text-secondary">
                    Google Assistant action for Team Tomato
                </p>
                <a href='#' className='btn btn-outline-success'>https://github.com/Team-Tomato/GAction_TeamTomato</a>
                <p className="tech-stack text-secondary">
                    This is built with the help of either C++ or Python
                </p>
            </div> 
            </div>       

            <div className='col-md-9 col-sm-3'>
            <h4 className='card-title'>Thoughts of People</h4>
         
                <img src={img5} alt='Image 5' className='card-img-top'/>
                
            
            <div className="card-body text-dark">
                
                <p className="card-text text-secondary">
                    ---------------------
                </p>
                <a href='#' className='btn btn-outline-success'>repo url</a>
                <p className="tech-stack text-secondary">
                ------------------
                </p>
            </div> 
            </div>
           
        </div>
           
            
            </div>
    
           
                  
        )
    }
}

export default Card;