import { IBikePart } from "./IBikePart";
import { ISeatclampType } from "../bike_properties/ISeatclampType";

export interface ISeatpost extends IBikePart {
  length: number;
  seatclamp_type: ISeatclampType;
  travel: number;
}
