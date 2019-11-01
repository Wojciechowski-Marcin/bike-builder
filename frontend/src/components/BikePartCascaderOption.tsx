import React from "react";
import { Popover } from "antd";

interface IProps {
  title: string;
  content: React.ReactNode;
  placement: string;
}

export class BikePartCascaderOption extends React.Component<IProps> {
  render() {
    return (
      <Popover
        title={this.props.title}
        content={this.props.content}
        placement="right"
      >
        <div style={style.div}>{this.props.children}</div>
      </Popover>
    );
  }
}

const style = {
  div: {
    width: "100%"
  }
};
