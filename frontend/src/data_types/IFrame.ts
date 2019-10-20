import { IAxleType } from "./IAxleType";
import { IBottomBracketType } from "./IBottomBracketType";
import { IBrakeRotorType } from "./IBrakeRotorType";
import { IBrakeType } from "./IBrakeType";
import { IFrontDerailleurType } from "./IFrontDerailleurType";
import { IHeadtubeType } from "./IHeadtubeType";
import { IRearDerailleurType } from "./IRearDerailleurType";
import { ISeatclampType } from "./ISeatclampType";
import { IShockType } from "./IShockType";
import { IWheelType } from "./IWheelType";
import { IBikePart } from "./IBikePart";

export interface IFrame extends IBikePart {
  headtube_type: IHeadtubeType;
  seatclamp_type: ISeatclampType;
  bottom_bracket_type: IBottomBracketType;
  brake_rotor_type: IBrakeRotorType[];
  recommended_fork_travel: number;
  shock_type: IShockType;
  wheel_types: IWheelType[];
  brake_types: IBrakeType[];
  rear_derailleur_types: IRearDerailleurType[];
  front_derailleur_types: IFrontDerailleurType[];
  axle_type: IAxleType;
}
