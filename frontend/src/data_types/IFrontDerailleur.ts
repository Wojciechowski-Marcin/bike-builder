import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "./ISpeedCompatibility";
import { IFrontDerailleurType } from "./IFrontDerailleurType";

export interface IFrontDerailleur extends IBikePart {
  speed_compatibilities: ISpeedCompatibility[];
  front_derailleur_type: IFrontDerailleurType;
}
