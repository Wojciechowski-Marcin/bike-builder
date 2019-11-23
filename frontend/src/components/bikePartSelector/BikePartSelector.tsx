import { Typography } from "antd";
import React from "react";

import { IBikeBuild } from "../../data_types/IBikeBuild";
import { IBikePartSelectorData } from "../../utils/partSelectorCascaderOptions";
import { PartSelector } from "./PartSelector";

const { Title } = Typography;

interface IProps {
  refreshPartSelector: boolean;
  bikeBuild: IBikeBuild;
  bikePartSelectorData: IBikePartSelectorData;
  totalPrice: number;
  changeBikeBuild: (bikeBuild: IBikeBuild) => void;
}

export class BikePartSelector extends React.Component<IProps> {
  render() {
    return (
      <div>
        <Title>Select parts you must include!</Title>
        <Title level={4}>
          Or leave an empty box if you want to leave it on us
        </Title>
        {Object.entries(this.props.bikePartSelectorData).map(
          ([label, partSelectorData]) => {
            return (
              <PartSelector
                refreshPartSelector={this.props.refreshPartSelector}
                key={`partSelector-${label}`}
                actionKey={label}
                changeBikeBuild={this.props.changeBikeBuild}
                currentPrice={this.props.bikeBuild[label].price}
                label={label}
                partSelectorData={partSelectorData}
              />
            );
          },
        )}
        <Title>Current total price: {this.props.totalPrice.toFixed(2)}</Title>
      </div>
    );
  }
}
