import React from "react";
import { Cascader, Typography } from "antd";

import { IBikeBuild } from "../data_types/IBikeBuild";
import { IPartSelectorData } from "../data/partSelectorCascaderOptions";

const { Title } = Typography;

interface IProps {
  actionKey: string;
  currentPrice: number;
  label: string;
  partSelectorData: IPartSelectorData;
  changeBikeBuild: (bikeBuild: IBikeBuild) => void;
}

export class PartSelector extends React.Component<IProps> {
  constructor(props: IProps) {
    super(props);
    this.onChange = this.onChange.bind(this);
    this.getPartPriceById = this.getPartPriceById.bind(this);
  }

  getPartPriceById(id: number) {
    return this.props.partSelectorData.availableParts.find(
      part => part.id === id
    )!.price;
  }

  onChange(value: string[]) {
    const currentSelectedPartId = parseInt(value[0]);
    const currentSelectedPartPrice =
      currentSelectedPartId && this.getPartPriceById(currentSelectedPartId);

    let bikeBuild: IBikeBuild = {};
    bikeBuild[this.props.label] = {
      id: currentSelectedPartId,
      price: +currentSelectedPartPrice
    };
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
          options={this.props.partSelectorData.options}
          onChange={this.onChange}
          style={style.cascader}
          allowClear={false}
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
