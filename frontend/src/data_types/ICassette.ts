import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "./ISpeedCompatibility";

export interface ICassette extends IBikePart {
  gradiation: string;
  speed_compatibilities: ISpeedCompatibility[];
}
