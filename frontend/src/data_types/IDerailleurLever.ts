import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "./ISpeedCompatibility";

export interface IDerailleurLever extends IBikePart {
  speed_compatibilities: ISpeedCompatibility[];
}
