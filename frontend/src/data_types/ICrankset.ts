import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "./ISpeedCompatibility";
import { IBottomBracketType } from "./IBottomBracketType";

export interface ICrankset extends IBikePart {
  gradiation: string;
  speed_compatibilities: ISpeedCompatibility[];
  bottom_bracket_type: IBottomBracketType;
  arm_length: number;
}
