import { IBikePart } from "./IBikePart";
import { IBrakeType } from "./IBrakeType";

export interface IBrakeLever extends IBikePart {
  brake_type: IBrakeType;
}
