import { IBikePart } from "./IBikePart";
import { IBrakeType } from "../bike_properties/IBrakeType";

export interface IBrakeLever extends IBikePart {
  brake_type: IBrakeType;
}
