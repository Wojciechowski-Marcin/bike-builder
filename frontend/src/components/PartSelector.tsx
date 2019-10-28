import React from "react";
import { Cascader, Typography } from "antd";
import { CascaderOptionType } from "antd/lib/cascader";

const { Title } = Typography;

interface IProps {
  options: CascaderOptionType[];
  label: string;
}

export class PartSelector extends React.Component<IProps> {
  //   constructor(props: IProps) {
  //     super(props);
  //   }

  render() {
    return (
      <div style={style.partSelector}>
        <Title level={4} style={style.title}>
          {this.props.label}
        </Title>
        <Cascader options={this.props.options} style={style.cascader} />
      </div>
    );
  }
}

const style = {
  partSelector: {
    display: "flex",
    justifyContent: "center",
    margin: "5px"
  },
  title: {
    margin: "auto 5px"
  },
  cascader: {
    margin: "auto 5px"
  }
};
