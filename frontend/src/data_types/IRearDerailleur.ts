import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "./ISpeedCompatibility";
import { IRearDerailleurType } from "./IRearDerailleurType";

export interface IRearDerailleur extends IBikePart {
  speed_compatibilities: ISpeedCompatibility[];
  rear_derailleur_type: IRearDerailleurType;
}
