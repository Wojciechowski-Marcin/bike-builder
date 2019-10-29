import React from "react";
import { Cascader, Typography } from "antd";
import { CascaderOptionType } from "antd/lib/cascader";

import { IBikeBuild } from "../data_types/IBikeBuild";

const { Title } = Typography;

interface IProps {
  options: CascaderOptionType[];
  label: string;
  actionKey: string;
  changeBikeBuild: (bikeBuild: IBikeBuild) => void;
}

export class PartSelector extends React.Component<IProps> {
  constructor(props: IProps) {
    super(props);
    this.onChange = this.onChange.bind(this);
  }

  onChange(value: string[]) {
    let bikeBuild: IBikeBuild = {};
    bikeBuild[this.props.label] = parseInt(value[0]);
    this.props.changeBikeBuild(bikeBuild);
  }

  render() {
    return (
      <div style={style.partSelector}>
        <Title level={4} style={style.title}>
          {this.props.label}
        </Title>
        <Cascader
          defaultValue={["0"]}
          options={this.props.options}
          onChange={this.onChange}
          style={style.cascader}
        />
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
