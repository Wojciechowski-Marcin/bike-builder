import { bindActionCreators, Dispatch } from "redux";
import { connect } from "react-redux";
import { InputNumber, Typography } from "antd";
import React from "react";

import { changeBudget } from "../actions/userInputActions";
import { getBudget } from "../reducers/userInputReducer";
import { IRootState } from "../reducers";

const { Title } = Typography;

interface IProps {
  budget: number;
  changeBudget: (budget: number) => void;
}

class BudgetInput_ extends React.Component<IProps> {
  constructor(props: IProps) {
    super(props);
    this.onChange = this.onChange.bind(this);
  }

  onChange(value: number | undefined) {
    value && this.props.changeBudget(value);
  }

  render() {
    return (
      <>
        <Title>Insert your budget and scroll down!</Title>
        <div style={style.inputNumberContainer}>
          {/* TODO Don't let input letters */}
          <InputNumber min={0} size="large" onChange={this.onChange} />
          <Title level={4} style={style.title}>
            €
          </Title>
        </div>
      </>
    );
  }
}

const mapStateToProps = (state: IRootState) => ({
  budget: getBudget(state)
});

const mapDispatchToProps = (dispatch: Dispatch) =>
  bindActionCreators({ changeBudget }, dispatch);

export const BudgetInput = connect(
  mapStateToProps,
  mapDispatchToProps
)(BudgetInput_);

const style = {
  title: {
    margin: "auto 5px"
  },
  inputNumberContainer: {
    display: "flex",
    justifyContent: "center"
  } as React.CSSProperties
};
