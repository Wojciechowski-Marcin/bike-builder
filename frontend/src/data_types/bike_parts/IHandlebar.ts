import { IBikePart } from "./IBikePart";
import { IHandlebarType } from "../bike_properties/IHandlebarType";

export interface IHandlebar extends IBikePart {
  width: number;
  handlebar_type: IHandlebarType;
}
