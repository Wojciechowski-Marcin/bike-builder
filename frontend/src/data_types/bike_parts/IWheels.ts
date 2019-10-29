import { IBikePart } from "./IBikePart";
import { IWheelType } from "../bike_properties/IWheelType";
import { IBrakeType } from "../bike_properties/IBrakeType";
import { IAxleType } from "./IAxleType";

export interface IWheels extends IBikePart {
  wheel_type: IWheelType;
  brake_type: IBrakeType;
  axle_type: IAxleType;
}
