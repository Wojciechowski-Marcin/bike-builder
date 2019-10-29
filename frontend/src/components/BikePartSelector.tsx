import { connect } from "react-redux";
import { Typography } from "antd";
import React from "react";

import { changeBikeBuild } from "../actions/userInputActions";
import { Dispatch, bindActionCreators } from "redux";
import { getBikeParts } from "../reducers/fetchReducer";
import { getCascaderOptions } from "../data/partSelectorCascaderOptions";
import { getSelectedBikeType } from "../reducers/userInputReducer";
import { IBikeBuild } from "../data_types/IBikeBuild";
import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { IRootState } from "../reducers";
import { PartSelector } from "./PartSelector";

const { Title } = Typography;

interface IProps {
  type: string;
  bikeParts: IBikePartsAPI;
  changeBikeBuild: (bikeBuild: IBikeBuild) => void;
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
          return (
            <PartSelector
              key={label}
              actionKey={label}
              options={options}
              label={label}
              changeBikeBuild={this.props.changeBikeBuild}
            />
          );
        })}
      </>
    );
  }
}

const mapStateToProps = (state: IRootState) => ({
  type: getSelectedBikeType(state),
  bikeParts: getBikeParts(state)
});

const mapDispatchToProps = (dispatch: Dispatch) =>
  bindActionCreators({ changeBikeBuild }, dispatch);

export const BikePartSelector = connect(
  mapStateToProps,
  mapDispatchToProps
)(BikePartSelector_);
