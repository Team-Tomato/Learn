import React, {Component} from 'react';
import img1 from '../images/tomato2.jpg';
import img2 from '../images/logo.jpg';
import img3 from '../images/assistant.jpg';
import img4 from '../images/movie recommand.jpg';
import img5 from '../images/people thoughts.jpg';

class Cards extends Component{
    render(){
        return(
            <div className="container-fluid d-flex .justify content-md-center">
                <div className="row">
                    <div className="col-md-4">
                        <p className="pl-md-5">
                        <div className='card text-center'>
                        <div className='card-body text-dark'>
                                <h4 className='card-title'>Team Tomato</h4>
                            <div  className='overflow'>
                                <img src={img1} alt='Image 1' className="card-img-top"></img>
                            </div>

                                <p className='card-text text-secondary'>
                                Team which is determined to spread the love of open source (oss)
                                </p>
                                <a class="text-primary" href="https://github.com/Team-Tomato/" role="text">Team Tomato site</a>
                            
                                <p className='card-text text-secondary'>
                                Top languages used-Javascript,Python,HTML
                                </p>
                            </div>
                        </div>
                        </p>
                    </div>

                    <div className="col-md-4">
                    <p className="pl-md-5">
                        <div className='card text-center'>
                        <div className='card-body text-dark'>
                                <h4 className='card-title'>One click for CEG</h4>
                            <div  className='overflow'>
                                <img src={img2} alt='Image 2' className="card-img-top"></img>
                            </div>
                           
                                <p className='card-text text-secondary'>
                                Extension which directs to all CEG related websites
                                </p>
                                <a class="text-primary" href="https://github.com/Team-Tomato/oneClick-chrome-extension" role="text">Chrome Extension site</a>
                            
                                <p className='card-text text-secondary'>
                                Done using HTML and Javascript
                                </p>
                            </div>
                        </div>
                        </p>
                    </div>

                    <div className="col-md-4">
                    <p className="pl-md-5 pr-md-2">
                        <div className='card text-center'>
                        <div className='card-body text-dark'>
                                <h4 className='card-title'>Team Tomato Action</h4>
                            <div  className='overflow'>
                                <img src={img3} alt='Image 3' className="card-img-top"></img>
                            </div>
                           
                                <p className='card-text text-secondary'>
                                Google Assistant action for Team Tomato
                                </p>
                                <a class="text-primary" href="https://github.com/Team-Tomato/GAction_TeamTomato" role="text">Assistant site</a>
                                <p className='card-text text-secondary'>
                                This is built with the help of either C++ or Python
                                </p>
                            </div>
                        </div>
                        </p>
                    </div>

                    <div className="col-md-6">
                        <div className="float-md-right">
                    <p className="pr-md-5">
                        <div className='card text-center'>
                        <div className='card-body text-dark'>
                                <h4 className='card-title'>Movie-recommandation Action</h4>
                            <div  className='overflow'>
                                <img src={img4} alt='Image 4' className="card-img-top"></img>
                            </div>
                           
                                <p className='card-text text-secondary'>
                                   -- 
                                </p>
                                <a class="text-primary" href="https://github.com/Team-Tomato/Movie_Recommendation_Backend" role="text">Movie recommandation site</a>
                                <p className='card-text text-secondary'>
                                Done using Python
                                </p>
                            </div>
                        </div>
                        </p>
                        </div>
                    </div>

                  

                    <div className="col-md-6">
                    <p className="pr-md-5">
                        <div className='card text-center'>
                        <div className='card-body text-dark'>
                                <h4 className='card-title'>Thoughts of People</h4>
                            <div  className='overflow'>
                                <img src={img5} alt='Image 5' className="card-img-top"></img>
                            </div>
                           
                                <p className='card-text text-secondary'>
                                ------
                                </p>
                                <a class="text-primary" href="" role="text">People thoughts</a>
                                <p className='card-text text-secondary'>
                                -------------
                                </p>
                            </div>
                    </div>
                    </p>
                    </div>



                </div>
            </div>
        );
    }
}

    
export default Cards;