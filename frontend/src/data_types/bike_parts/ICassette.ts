import { IBikePart } from "./IBikePart";
import { ISpeedCompatibility } from "../bike_properties/ISpeedCompatibility";

export interface ICassette extends IBikePart {
  gradiation: string;
  speed_compatibilities: ISpeedCompatibility[];
}
