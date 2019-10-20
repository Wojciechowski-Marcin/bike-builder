import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "./ISpeedCompatibility";
import { IBottomBracketType } from "./IBottomBracketType";
import { IBrakeRotorType } from "./IBrakeRotorType";

export interface IRotor extends IBikePart {
  brake_rotor_type: IBrakeRotorType;
}
