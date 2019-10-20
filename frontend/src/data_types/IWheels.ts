import { IBikePart } from "./IBikePart";
import { IWheelType } from "./IWheelType";
import { IBrakeType } from "./IBrakeType";
import { IAxleType } from "./IAxleType";

export interface IWheels extends IBikePart {
  wheel_type: IWheelType;
  brake_type: IBrakeType;
  axle_type: IAxleType;
}
