import React from "react";

import { BikeTypeBox } from "./BikeTypeBox";
import { BikeTypeBoxTypes } from "../../data_types/BikeTypeBoxTypes";
import { BudgetInput } from "./BudgetInput";

export class BikeTypeSelector extends React.Component {
  render() {
    return (
      <>
        <div className="bikeTypeSelector" style={style.bikeTypeSelector}>
          {Object.entries(BikeTypeBoxTypes).map(([key, val]) => {
            return <BikeTypeBox key={key} type={val} />;
          })}
        </div>
        <BudgetInput />
      </>
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
