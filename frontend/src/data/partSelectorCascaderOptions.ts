import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { IBikePart } from "../data_types/bike_parts/IBikePart";
import { CascaderOptionType } from "antd/lib/cascader";

export function getCascaderOptions(bikeParts: IBikePartsAPI) {
  interface IReturnValue {
    [key: string]: CascaderOptionType[];
  }
  let returnValue: IReturnValue = {};
  Object.entries(bikeParts).map(([label, parts]) => {
    returnValue[label] = getBikepartCascaderOptions(parts);
    return null;
  });
  return returnValue;
}

export function getBikepartCascaderOptions(bikeParts: IBikePart[]) {
  let returnArray: CascaderOptionType[] = [];
  bikeParts.forEach(bikePart => {
    returnArray.push(getFrame(bikePart));
  });
  return returnArray;
}

function getFrame(bikePart: IBikePart) {
  return {
    value: `${bikePart.id}`,
    label: bikePart.brand.name + bikePart.model
  };
}
