import { IBikePart } from "./IBikePart";
import { IShockType } from "./IShockType";

export interface IShock extends IBikePart {
  shock_type: IShockType;
  suspension_type: string;
}
