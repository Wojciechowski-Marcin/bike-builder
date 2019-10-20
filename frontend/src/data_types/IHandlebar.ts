import { IBikePart } from "./IBikePart";
import { IHandlebarType } from "./IHandlebarType";

export interface IHandlebar extends IBikePart {
  width: number;
  handlebar_type: IHandlebarType;
}
