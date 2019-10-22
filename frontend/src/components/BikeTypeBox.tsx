import React from "react";
import { getSelectedBikeType } from "../reducers/bikeTypeSelectorReducer";
import { connect } from "react-redux";
import { selectBikeType } from "../actions/bikeTypeSelectorActions";
import { bindActionCreators } from "redux";

interface IProps {
  type: string;
  selectedBikeType: string;
  setSelectedBikeType: (type: string) => void;
}

class BikeTypeBox_ extends React.Component<IProps> {
  constructor(props: IProps) {
    super(props);
    this.handleOnClick = this.handleOnClick.bind(this);
    this.isButtonSelected = this.isButtonSelected.bind(this);
  }

  handleOnClick() {
    this.props.setSelectedBikeType(this.props.type);
  }

  isButtonSelected() {
    return this.props.type === this.props.selectedBikeType;
  }

  render() {
    return (
      <button onClick={this.handleOnClick} style={style.button}>
        <div
          className={"bikeTypeBox" + (this.isButtonSelected() ? " active" : "")}
          style={style.bikeTypeBox}
        >
          <h2 className="bikeTypeBoxName" style={style.bikeTypeBoxName}>
            {this.props.type}
          </h2>
        </div>
      </button>
    );
  }
}

const mapStateToProps = (state: any) => ({
  selectedBikeType: getSelectedBikeType(state)
});

const mapDispatchToProps = (dispatch: any) =>
  bindActionCreators(
    {
      setSelectedBikeType: selectBikeType
    },
    dispatch
  );

export const BikeTypeBox = connect(
  mapStateToProps,
  mapDispatchToProps
)(BikeTypeBox_);

const style = {
  bikeTypeBox: {
    borderRadius: "25px",
    background: "linear-gradient(-45deg, #2980b9, #6dd5fa, #ffffff)",
    padding: "5px 0",
    minHeight: "50vh",
    width: "15vw",
    margin: "24px",
    position: "relative",
    display: "flex",
    justifyContent: "center",
    boxShadow: "8px 8px 4px 0px rgba(40,128,182,0.1)"
  } as React.CSSProperties,
  bikeTypeBoxName: {
    position: "absolute",
    top: "50%",
    transform: "translate(0, -50%)",
    fontSize: "150%",
    color: "rgb(0,0,0,1)"
  } as React.CSSProperties,
  button: {
    background: "transparent",
    border: "none",
    color: "transparent"
  }
};
