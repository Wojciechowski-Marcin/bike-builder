import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "../bike_properties/ISpeedCompatibility";
import { IBottomBracketType } from "../bike_properties/IBottomBracketType";

export interface ICrankset extends IBikePart {
  gradiation: string;
  speed_compatibilities: ISpeedCompatibility[];
  bottom_bracket_type: IBottomBracketType;
  arm_length: number;
}
