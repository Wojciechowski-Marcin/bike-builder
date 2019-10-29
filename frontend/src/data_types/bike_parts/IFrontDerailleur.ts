import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "../bike_properties/ISpeedCompatibility";
import { IFrontDerailleurType } from "../bike_properties/IFrontDerailleurType";

export interface IFrontDerailleur extends IBikePart {
  speed_compatibilities: ISpeedCompatibility[];
  front_derailleur_type: IFrontDerailleurType;
}
