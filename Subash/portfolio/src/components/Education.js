import React, { Component } from "react";
export default class Resume extends Component {
  render() {
    let resumeData = this.props.resumeData;
    return (
      <section id="education">
        <div>
          <div className="row">
            <div className="three columns header-col">
              <h1>
                <span>Education</span>
              </h1>
            </div>

            <div className="nine columns main-col">
              {resumeData.education &&
                resumeData.education.map((item) => {
                  return (
                    <div className="row">
                      <div className="twelve columns">
                        <h3>{item.UniversityName}</h3>
                        <p className="info">
                          {item.specialization}
                          <span>&bull;</span>{" "}
                          <em className="date">
                            {item.MonthOfPassing} {item.YearOfPassing}
                          </em>
                        </p>
                        <p>{item.Achievements}</p>
                      </div>
                    </div>
                  );
                })}
            </div>
          </div>
        </div>
      </section>
    );
  }
}
