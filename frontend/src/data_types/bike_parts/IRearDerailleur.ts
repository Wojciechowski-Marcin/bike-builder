import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "../bike_properties/ISpeedCompatibility";
import { IRearDerailleurType } from "../bike_properties/IRearDerailleurType";

export interface IRearDerailleur extends IBikePart {
  speed_compatibilities: ISpeedCompatibility[];
  rear_derailleur_type: IRearDerailleurType;
}
