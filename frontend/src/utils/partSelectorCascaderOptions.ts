import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { IBikePart } from "../data_types/bike_parts/IBikePart";
import { CascaderOptionType } from "antd/lib/cascader";
import { IBikeBuild } from "../data_types/IBikeBuild";
import { mapBikePartToCascaderOption } from "./mapBikePartToCascaderOption";

export interface IBikePartSelectorData {
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
  bikeBuild: IBikeBuild,
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
          label,
        ),
      }),
  );
  let cascaderOptionsKeys = Object.keys(cascaderOptions);
  cascaderOptionsKeys.sort();
  let sortedCascaderOptions: IBikePartSelectorData = {};
  for (var i = 0; i < cascaderOptionsKeys.length; i++) {
    const key = cascaderOptionsKeys[i];
    sortedCascaderOptions[key] = cascaderOptions[key];
  }
  return sortedCascaderOptions;
}

export const NoAvailablePartsText = "Your budget is out! :(";
export const PartNotSelectedText = "Not selected";

function getBikepartCascaderOptions(
  bikeParts: IBikePart[],
  selectedApplicationName: string,
  budget: number,
  bikeBuild: IBikeBuild,
  label: string,
) {
  let returnArray: CascaderOptionType[] = [
    {
      value: "-1",
      label: PartNotSelectedText,
    },
  ];

  const selectedBikePartPrice = bikeBuild[label].price;

  bikeParts.forEach(bikePart => {
    const isApplicationSelected = bikePart.applications.some(
      application => application.name === selectedApplicationName,
    );
    const isLowerThanBudget = bikePart.price < budget + selectedBikePartPrice;

    if (isApplicationSelected && isLowerThanBudget)
      returnArray.push(mapBikePartToCascaderOption(bikePart));
  });

  return returnArray.length > 1
    ? returnArray
    : [{ value: "-1", label: NoAvailablePartsText }];
}
