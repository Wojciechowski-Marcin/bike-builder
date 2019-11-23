import { Button, Table } from "antd";
import { connect } from "react-redux";
import React from "react";
import { IRootState } from "../../reducers";
import { Dispatch, bindActionCreators } from "redux";
import {
  getFetchBuildResult,
  getFetchBuildError,
  getFetchBuildPending,
} from "../../reducers/fetchBuildReducer";
import { fetchBuild } from "../../data/fetchBuild";
import { IBikeBuild } from "../../data_types/IBikeBuild";
import { getBikeBuild } from "../../reducers/userInputReducer";
import { getFetchBikePartsResult } from "../../reducers/fetchBikePartsReducer";
import { IBikePartsAPI } from "../../data_types/IBikePartsAPI";

interface IProps {
  userBuild: IBikeBuild;
  bikeParts: IBikePartsAPI;
  fetchBuildResult: IBikeBuild;
  fetchBuildError: Error | null;
  fetchBuildPending: boolean;
  fetchBuild: (bikeBuild: IBikeBuild) => void;
}

interface IState {
  buttonLoading: boolean;
  bikeBuild: IBikeBuild;
}

class BuildResult_ extends React.Component<IProps, IState> {
  totalPrice = 0;
  totalWeight = 0;

  constructor(props: IProps) {
    super(props);
    this.state = {
      buttonLoading: false,
      bikeBuild: {},
    };
    this.onClick = this.onClick.bind(this);
    this.dataSource = this.dataSource.bind(this);
    this.getFooter = this.getFooter.bind(this);
  }

  componentDidUpdate(prevProps: IProps) {
    if (prevProps !== this.props) {
      this.setState({
        ...this.state,
        buttonLoading: this.props.fetchBuildPending,
      });
    }
  }

  onClick() {
    this.setState({
      ...this.state,
      buttonLoading: true,
    });
    this.props.fetchBuild(this.props.userBuild);
  }

  getPartById(bikeParts: IBikePartsAPI, key: string, id: number) {
    console.log(key, id);
    switch (key) {
      case "frame":
        return bikeParts.Frame.find(obj => obj.id === id);
      case "fork":
        return bikeParts.Fork.find(obj => obj.id === id);
      case "shock":
        return bikeParts.Shock.find(obj => obj.id === id);
      case "crankset":
        return bikeParts.Crankset.find(obj => obj.id === id);
      case "cassette":
        return bikeParts.Cassette.find(obj => obj.id === id);
      case "frontderailleur":
        return bikeParts.FrontDerailleur.find(obj => obj.id === id);
      case "rearderailleur":
        return bikeParts.RearDerailleur.find(obj => obj.id === id);
      case "brake":
        return bikeParts.Brake.find(obj => obj.id === id);
      case "brakelever":
        return bikeParts.BrakeLever.find(obj => obj.id === id);
      case "derailleurlever":
        return bikeParts.DerailleurLever.find(obj => obj.id === id);
      case "rotor":
        return bikeParts.Rotor.find(obj => obj.id === id);
      case "handlebar":
        return bikeParts.Handlebar.find(obj => obj.id === id);
      case "stem":
        return bikeParts.Stem.find(obj => obj.id === id);
      case "seatpost":
        return bikeParts.Seatpost.find(obj => obj.id === id);
      case "wheels":
        return bikeParts.Wheels.find(obj => obj.id === id);
    }
  }

  dataSource() {
    const allBikeParts = this.props.bikeParts;
    const bikeBuild = this.props.fetchBuildResult;
    let index = 0;
    let totalPrice = 0;
    let totalWeight = 0;
    const dataSource = Object.entries(bikeBuild).map(([key, part]) => {
      const bikePart = this.getPartById(allBikeParts, key, part.id);
      const dataSourceElement = {
        key: index,
        type: key,
        model: bikePart!.model,
        weight: bikePart!.weight,
        price: bikePart!.price,
      };
      totalPrice += +bikePart!.price;
      totalWeight += +bikePart!.weight;
      index += 1;
      return dataSourceElement;
    });
    this.totalWeight = totalWeight;
    this.totalPrice = totalPrice;
    return dataSource;
  }

  getFooter() {
    // return {
    //   key: 999,
    //   type: "Summary",
    //   model: "",
    //   weight: this.state.footerSummary.totalWeight,
    //   price: this.state.footerSummary.totalPrice,
    // };
    return (
      "Total price: " +
      this.totalPrice.toFixed(2) +
      "\tTotal weight: " +
      this.totalWeight.toFixed(2)
    );
  }

  render() {
    const columns = [
      {
        title: "Type",
        dataIndex: "type",
        key: "type",
      },
      {
        title: "Model",
        dataIndex: "model",
        key: "model",
      },
      {
        title: "Weight",
        dataIndex: "weight",
        key: "weight",
      },
      {
        title: "Price",
        dataIndex: "price",
        key: "price",
      },
    ];

    return (
      <div className="buildResults" style={style.buildResults}>
        <Button
          type="primary"
          size="large"
          onClick={this.onClick}
          loading={this.state.buttonLoading}
        >
          Build
        </Button>
        <Table
          dataSource={this.dataSource()}
          columns={columns}
          pagination={false}
          footer={this.getFooter}
        />
      </div>
    );
  }
}

const style = {
  buildResults: {
    width: "40%",
    margin: "0 auto",
    display: "flex",
    flexDirection: "column",
  } as React.CSSProperties,
};

const mapStateToProps = (state: IRootState) => ({
  fetchBuildResult: getFetchBuildResult(state),
  fetchBuildError: getFetchBuildError(state),
  fetchBuildPending: getFetchBuildPending(state),
  bikeParts: getFetchBikePartsResult(state),
  userBuild: getBikeBuild(state),
});

const mapDispatchToProps = (dispatch: Dispatch) =>
  bindActionCreators({ fetchBuild }, dispatch);

export const BuildResult = connect(
  mapStateToProps,
  mapDispatchToProps,
)(BuildResult_);
