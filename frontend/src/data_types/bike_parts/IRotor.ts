import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "../bike_properties/ISpeedCompatibility";
import { IBottomBracketType } from "../bike_properties/IBottomBracketType";
import { IBrakeRotorType } from "../bike_properties/IBrakeRotorType";

export interface IRotor extends IBikePart {
  brake_rotor_type: IBrakeRotorType;
}
