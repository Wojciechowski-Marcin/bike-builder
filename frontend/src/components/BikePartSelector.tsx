import { connect } from "react-redux";
import { Typography } from "antd";
import React from "react";

import { changeBikeBuild } from "../actions/userInputActions";
import { Dispatch, bindActionCreators } from "redux";
import { getBikeParts } from "../reducers/fetchReducer";
import { getBikePartSelectorData } from "../data/partSelectorCascaderOptions";
import {
  getSelectedBikeType,
  getBudget,
  getBikeBuild
} from "../reducers/userInputReducer";
import { IBikeBuild } from "../data_types/IBikeBuild";
import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { IRootState } from "../reducers";
import { PartSelector } from "./PartSelector";

const { Title } = Typography;

interface IProps {
  bikeBuild: IBikeBuild;
  bikeParts: IBikePartsAPI;
  budget: number;
  type: string;
  changeBikeBuild: (bikeBuild: IBikeBuild) => void;
}

interface IState {
  isVisible: boolean;
}

class BikePartSelector_ extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = { isVisible: this.shouldComponentBeVisible() };
    this.calculateTotalPrice = this.calculateTotalPrice.bind(this);
  }

  shouldComponentBeVisible() {
    return !!this.props.type && !!this.props.budget;
  }

  componentDidUpdate(prevProps: IProps) {
    const doPropsDiffer =
      prevProps.type !== this.props.type ||
      prevProps.budget !== this.props.budget;

    if (doPropsDiffer) {
      this.setState({
        ...this.state,
        isVisible: this.shouldComponentBeVisible()
      });
    }
  }

  calculateTotalPrice() {
    let totalPrice = 0;
    Object.values(this.props.bikeBuild).map(
      value => (totalPrice += value.price)
    );
    return totalPrice;
  }

  render() {
    let bikePartSelectorData = getBikePartSelectorData(
      this.props.bikeParts,
      this.props.type,
      +this.props.budget - this.calculateTotalPrice(),
      this.props.bikeBuild
    );
    return !this.state.isVisible ? (
      <>
        <Title>Please input data above!</Title>
      </>
    ) : (
      <>
        <Title>Select parts you must include!</Title>
        <Title level={4}>
          Or leave an empty box if you want to leave it on us
        </Title>
        {Object.entries(bikePartSelectorData).map(
          ([label, partSelectorData]) => {
            return (
              <PartSelector
                key={label}
                actionKey={label}
                changeBikeBuild={this.props.changeBikeBuild}
                currentPrice={this.props.bikeBuild[label].price}
                label={label}
                partSelectorData={partSelectorData}
              />
            );
          }
        )}
        <Title>Current total price: {this.calculateTotalPrice()}</Title>
      </>
    );
  }
}

const mapStateToProps = (state: IRootState) => ({
  type: getSelectedBikeType(state),
  bikeParts: getBikeParts(state),
  budget: getBudget(state),
  bikeBuild: getBikeBuild(state)
});

const mapDispatchToProps = (dispatch: Dispatch) =>
  bindActionCreators({ changeBikeBuild }, dispatch);

export const BikePartSelector = connect(
  mapStateToProps,
  mapDispatchToProps
)(BikePartSelector_);
