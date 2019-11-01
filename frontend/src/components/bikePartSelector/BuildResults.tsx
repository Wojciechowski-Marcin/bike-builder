import { Button } from "antd";
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

interface IProps {
  userBuild: IBikeBuild;
  fetchBuildResult: IBikeBuild;
  fetchBuildError: Error | null;
  fetchBuildPending: boolean;
  fetchBuild: (bikeBuild: IBikeBuild) => void;
}

interface IState {
  buttonLoading: boolean;
}

class BuildResult_ extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      buttonLoading: false,
    };
    this.onClick = this.onClick.bind(this);
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

  render() {
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
        {/* TEMPORARY RESULT PRINT */}
        {Object.entries(this.props.fetchBuildResult).map(([key, value]) => {
          return (
            <p key={key}>
              {key}: {value}
            </p>
          );
        })}
        {/* TEMPORARY RESULT PRINT END */}
      </div>
    );
  }
}

const style = {
  buildResults: {
    margin: "0 auto",
    display: "flex",
    flexDirection: "column",
  } as React.CSSProperties,
};

const mapStateToProps = (state: IRootState) => ({
  fetchBuildResult: getFetchBuildResult(state),
  fetchBuildError: getFetchBuildError(state),
  fetchBuildPending: getFetchBuildPending(state),
  userBuild: getBikeBuild(state),
});

const mapDispatchToProps = (dispatch: Dispatch) =>
  bindActionCreators({ fetchBuild }, dispatch);

export const BuildResult = connect(
  mapStateToProps,
  mapDispatchToProps,
)(BuildResult_);
