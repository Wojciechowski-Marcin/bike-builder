import { connect } from "react-redux";
import { Typography } from "antd";
import React from "react";

import { getCascaderOptions } from "../data/partSelectorCascaderOptions";
import { getBikeParts } from "../reducers/fetchReducer";
import { getSelectedBikeType } from "../reducers/userInputReducer";
import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { IRootState } from "../reducers";
import { PartSelector } from "./PartSelector";

const { Title } = Typography;

interface IProps {
  type: string;
  bikeParts: IBikePartsAPI;
}

class BikePartSelector_ extends React.Component<IProps> {
  //   constructor(props: IProps) {
  //     super(props);
  //   }

  render() {
    let allOptions = getCascaderOptions(this.props.bikeParts);
    return (
      <>
        <Title>Select parts you must include!</Title>
        <Title level={4}>
          Or leave an empty box if you want to leave it on us
        </Title>
        {Object.entries(allOptions).map(([label, options]) => {
          return <PartSelector key={label} options={options} label={label} />;
        })}
      </>
    );
  }
}

const mapStateToProps = (state: IRootState) => ({
  type: getSelectedBikeType(state),
  bikeParts: getBikeParts(state)
});

export const BikePartSelector = connect(mapStateToProps)(BikePartSelector_);
