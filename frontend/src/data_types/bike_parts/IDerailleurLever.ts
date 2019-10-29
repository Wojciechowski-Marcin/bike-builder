import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "../bike_properties/ISpeedCompatibility";

export interface IDerailleurLever extends IBikePart {
  speed_compatibilities: ISpeedCompatibility[];
}
