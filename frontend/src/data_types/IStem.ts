import { IBikePart } from "./IBikePart";
import { IHeadtubeType } from "./IHeadtubeType";
import { IHandlebarType } from "./IHandlebarType";

export interface IStem extends IBikePart {
  length: number;
  angle: number;
  headtube_types: IHeadtubeType[];
  handlebar_type: IHandlebarType;
}
