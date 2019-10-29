import { IAxleType } from "./IAxleType";
import { IBikePart } from "./IBikePart";
import { IBrakeType } from "../bike_properties/IBrakeType";
import { IHeadtubeType } from "../bike_properties/IHeadtubeType";
import { IWheelType } from "../bike_properties/IWheelType";

export interface IFork extends IBikePart {
  wheel_types: IWheelType[];
  suspension_type: string;
  travel: number;
  headtube_type: IHeadtubeType;
  axle_type: IAxleType;
  brake_types: IBrakeType[];
}
