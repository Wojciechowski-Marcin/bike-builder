import { IBikePart } from "./IBikePart";
import { IShockType } from "../bike_properties/IShockType";

export interface IShock extends IBikePart {
  shock_type: IShockType;
  suspension_type: string;
}
