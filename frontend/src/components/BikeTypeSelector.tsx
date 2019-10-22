import React from "react";
import { BikeTypeBox } from "./BikeTypeBox";
import { BikeTypeBoxTypes } from "../data/BikeTypeBoxTypes";

export class BikeTypeSelector extends React.Component {
  render() {
    return (
      <div className="bikeTypeSelector" style={style.bikeTypeSelector}>
        <BikeTypeBox type={BikeTypeBoxTypes.CITY} />
        <BikeTypeBox type={BikeTypeBoxTypes.ROAD} />
        <BikeTypeBox type={BikeTypeBoxTypes.MTB} />
        <BikeTypeBox type={BikeTypeBoxTypes.TREKKING} />
      </div>
    );
  }
}

const style = {
  bikeTypeSelector: {
    margin: "24px",
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "center"
  } as React.CSSProperties
};
