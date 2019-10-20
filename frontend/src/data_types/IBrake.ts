import { IBikePart } from "./IBikePart";
import { IMaterial } from "./IMaterial";
import { IBrakeType } from "./IBrakeType";

export interface IBrake extends IBikePart {
  pad_material: IMaterial;
  brake_type: IBrakeType;
}
