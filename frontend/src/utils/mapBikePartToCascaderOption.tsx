import React from "react";

import { IBikePart } from "../data_types/bike_parts/IBikePart";
import { BikePartCascaderOption } from "../components/bikePartSelector/BikePartCascaderOption";

function objectToHTML(object: Object, skip_id = false, only_values = false) {
  // TODO Fix popover
  return Object.entries(object).map(([key, value]) => {
    const keyUpperFirstLetter = key[0].toUpperCase() + key.slice(1);
    return (
      !!key &&
      !!value &&
      (skip_id ? key !== "id" && key !== "model" : true) &&
      (typeof value !== "object" ? (
        <p key={key}>
          {only_values
            ? value.toString()
            : `${keyUpperFirstLetter.replace(/_/g, " ")}: ${value.toString()}`}
        </p>
      ) : (
        ""
        // <p>
        //   {keyUpperFirstLetter} {objectToHTML(value, true, true)}
        // </p>
      ))
    );
  });
}

export function mapBikePartToCascaderOption(bikePart: IBikePart) {
  const popoverContent = <div>{objectToHTML(bikePart, true)}</div>;

  const bikePartName = `${bikePart.brand.name} ${bikePart.model}`;

  return {
    value: `${bikePart.id}`,
    label: (
      <BikePartCascaderOption
        title={bikePartName}
        content={popoverContent}
        placement="right"
      >
        {bikePartName}
      </BikePartCascaderOption>
    ),
  };
}
