import React from "react";
import { Cascader, Typography } from "antd";

import { IBikeBuild } from "../../data_types/IBikeBuild";
import {
  IPartSelectorData,
  NoAvailablePartsText,
  PartNotSelectedText,
} from "../../utils/partSelectorCascaderOptions";

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
      part => part.id === id,
    )!.price;
  }

  onChange(value: string[]) {
    const currentSelectedPartId = parseInt(value[0]);
    const currentSelectedPartPrice =
      currentSelectedPartId && this.getPartPriceById(currentSelectedPartId);

    let bikeBuild: IBikeBuild = {};
    bikeBuild[this.props.label] = {
      id: currentSelectedPartId,
      price: +currentSelectedPartPrice,
    };
    this.props.changeBikeBuild(bikeBuild);
  }

  displayRender(labels: string[]) {
    const label = labels[0];
    let cascaderLabelStyle = {};

    switch (label) {
      case NoAvailablePartsText:
        cascaderLabelStyle = style.cascaderLabelNoParts;
        break;
      case PartNotSelectedText:
        cascaderLabelStyle = style.cascaderLabelNotSelected;
        break;
      default:
        cascaderLabelStyle = style.cascaderLabelValid;
        break;
    }
    return (
      <span className="cascaderLabel" style={cascaderLabelStyle}>
        {labels[0]}
      </span>
    );
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
          displayRender={this.displayRender}
        />
      </div>
    );
  }
}

const style = {
  cascaderLabelNoParts: {
    borderBottom: "1px solid rgba(240,47,23,0.5)",
    background:
      "radial-gradient(ellipse at center, rgba(254,238,236,1) 0%, rgba(255,255,255,1) 100%)",
  },
  cascaderLabelNotSelected: {
    borderBottom: "1px solid rgba(148,148,148,0.5)",
    background:
      "radial-gradient(ellipse at center, rgba(217,217,217,1) 0%, rgba(255,255,255,1) 100%)",
  },
  cascaderLabelValid: {
    borderBottom: "1px solid rgba(30,214,73,0.5)",
    background:
      "radial-gradient(ellipse at center, rgba(206,248,216,1) 0%, rgba(255,255,255,1) 100%)",
  },
  partSelector: {
    display: "flex",
    justifyContent: "center",
    margin: "5px",
  },
  title: {
    margin: "auto 5px",
  },
  cascader: {
    margin: "auto 5px",
    textAlign: "left",
  } as React.CSSProperties,
};
