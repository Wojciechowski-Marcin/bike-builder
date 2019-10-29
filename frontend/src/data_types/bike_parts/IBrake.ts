import { IBikePart } from "./IBikePart";
import { IMaterial } from "../bike_properties/IMaterial";
import { IBrakeType } from "../bike_properties/IBrakeType";

export interface IBrake extends IBikePart {
  pad_material: IMaterial;
  brake_type: IBrakeType;
}
