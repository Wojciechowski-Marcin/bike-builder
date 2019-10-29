import { IAxleType } from "./IAxleType";
import { IBottomBracketType } from "../bike_properties/IBottomBracketType";
import { IBrakeRotorType } from "../bike_properties/IBrakeRotorType";
import { IBrakeType } from "../bike_properties/IBrakeType";
import { IFrontDerailleurType } from "../bike_properties/IFrontDerailleurType";
import { IHeadtubeType } from "../bike_properties/IHeadtubeType";
import { IRearDerailleurType } from "../bike_properties/IRearDerailleurType";
import { ISeatclampType } from "../bike_properties/ISeatclampType";
import { IShockType } from "../bike_properties/IShockType";
import { IWheelType } from "../bike_properties/IWheelType";
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
