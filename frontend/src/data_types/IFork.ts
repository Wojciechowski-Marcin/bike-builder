import { IAxleType } from "./IAxleType";
import { IBikePart } from "./IBikePart";
import { IBrakeType } from "./IBrakeType";
import { IHeadtubeType } from "./IHeadtubeType";
import { IWheelType } from "./IWheelType";

export interface IFork extends IBikePart {
  wheel_types: IWheelType[];
  suspension_type: string;
  travel: number;
  headtube_type: IHeadtubeType;
  axle_type: IAxleType;
  brake_types: IBrakeType[];
}
