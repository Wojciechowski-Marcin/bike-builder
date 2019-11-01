import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { IBikePart } from "../data_types/bike_parts/IBikePart";
import { CascaderOptionType } from "antd/lib/cascader";
import { IBikeBuild } from "../data_types/IBikeBuild";
import { mapBikePartToCascaderOption } from "./mapBikePartToCascaderOption";

interface IBikePartSelectorData {
  [key: string]: IPartSelectorData;
}

export interface IPartSelectorData {
  availableParts: IBikePart[];
  options: CascaderOptionType[];
}

export function getBikePartSelectorData(
  bikePartsAPI: IBikePartsAPI,
  selectedApplicationName: string,
  budget: number,
  bikeBuild: IBikeBuild
) {
  let cascaderOptions: IBikePartSelectorData = {};
  Object.entries(bikePartsAPI).map(
    ([label, bikeParts]) =>
      (cascaderOptions[label] = {
        availableParts: bikeParts,
        options: getBikepartCascaderOptions(
          bikeParts,
          selectedApplicationName,
          budget,
          bikeBuild,
          label
        )
      })
  );
  return cascaderOptions;
}

function getBikepartCascaderOptions(
  bikeParts: IBikePart[],
  selectedApplicationName: string,
  budget: number,
  bikeBuild: IBikeBuild,
  label: string
) {
  let returnArray: CascaderOptionType[] = [
    {
      value: "0",
      label: "Not selected"
    }
  ];

  const selectedBikePartPrice = bikeBuild[label].price;

  bikeParts.forEach(bikePart => {
    const isApplicationSelected = bikePart.applications.some(
      application => application.name === selectedApplicationName
    );
    const isLowerThanBudget = bikePart.price < budget + selectedBikePartPrice;

    if (isApplicationSelected && isLowerThanBudget)
      returnArray.push(mapBikePartToCascaderOption(bikePart));
  });

  return returnArray.length > 1
    ? returnArray
    : [{ value: "0", label: "Your budget is out! :(" }];
}