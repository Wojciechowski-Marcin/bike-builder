import { connect } from "react-redux";
import { Dispatch, bindActionCreators } from "redux";
import { Typography } from "antd";
import React from "react";

import { changeBikeBuild } from "../../actions/userInputActions";
import {
  getFetchBikePartsResult,
  getFetchBikePartsError,
  getFetchBikePartsPending,
} from "../../reducers/fetchBikePartsReducer";
import { getBikePartSelectorData } from "../../utils/partSelectorCascaderOptions";
import {
  getSelectedBikeType,
  getBudget,
  getBikeBuild,
} from "../../reducers/userInputReducer";
import { IBikeBuild } from "../../data_types/IBikeBuild";
import { IBikePartsAPI } from "../../data_types/IBikePartsAPI";
import { IRootState } from "../../reducers";
import { BuildResult } from "./BuildResults";
import { BikePartSelector } from "./BikePartSelector";
import { fetchBikeParts } from "../../data/fetchBikeParts";
import { openNotification, NotificationType } from "../../utils/Notifications";

const { Title } = Typography;

interface IProps {
  bikeBuild: IBikeBuild;
  bikeParts: IBikePartsAPI;
  budget: number;
  type: string;
  fetchBikePartsError: Error | null;
  fetchBikePartsPending: boolean;
  changeBikeBuild: (bikeBuild: IBikeBuild) => void;
  fetchBikeParts: () => void;
}

interface IState {
  isVisible: boolean;
}

class BikePartSelectorContainer_ extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = { isVisible: this.shouldComponentBeVisible() };
    this.calculateTotalPrice = this.calculateTotalPrice.bind(this);
  }

  shouldComponentBeVisible() {
    return !!this.props.type && !!this.props.budget;
  }

  componentDidMount() {
    this.props.fetchBikeParts();
  }

  componentDidUpdate(prevProps: IProps) {
    const doPropsDiffer =
      prevProps.type !== this.props.type ||
      prevProps.budget !== this.props.budget;

    if (doPropsDiffer) {
      this.setState({
        ...this.state,
        isVisible: this.shouldComponentBeVisible(),
      });
    }
    if (this.props.fetchBikePartsError) {
      openNotification(
        "Could not fetch bike parts",
        "Please try again later",
        NotificationType.ERROR,
      );
    }
  }

  calculateTotalPrice() {
    let totalPrice = 0;
    Object.values(this.props.bikeBuild).map(
      value => (totalPrice += value.price),
    );
    return totalPrice;
  }

  render() {
    let bikePartSelectorData = getBikePartSelectorData(
      this.props.bikeParts,
      this.props.type,
      +this.props.budget - this.calculateTotalPrice(),
      this.props.bikeBuild,
    );
    return !this.state.isVisible ? (
      <Title>Please input data above.</Title>
    ) : (
      <div
        className="bikePartSelectorContainer"
        style={style.bikePartSelectorContainer}
      >
        <BikePartSelector
          bikePartSelectorData={bikePartSelectorData}
          changeBikeBuild={this.props.changeBikeBuild}
          bikeBuild={this.props.bikeBuild}
          totalPrice={this.calculateTotalPrice()}
        />
        <BuildResult />
      </div>
    );
  }
}

const style = {
  bikePartSelectorContainer: {
    display: "flex",
  },
};

const mapStateToProps = (state: IRootState) => ({
  bikeBuild: getBikeBuild(state),
  budget: getBudget(state),
  type: getSelectedBikeType(state),
  bikeParts: getFetchBikePartsResult(state),
  fetchBikePartsError: getFetchBikePartsError(state),
  fetchBikePartsPending: getFetchBikePartsPending(state),
});

const mapDispatchToProps = (dispatch: Dispatch) =>
  bindActionCreators({ changeBikeBuild, fetchBikeParts }, dispatch);

export const BikePartSelectorContainer = connect(
  mapStateToProps,
  mapDispatchToProps,
)(BikePartSelectorContainer_);
