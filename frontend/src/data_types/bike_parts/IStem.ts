import { IBikePart } from "./IBikePart";
import { IHeadtubeType } from "../bike_properties/IHeadtubeType";
import { IHandlebarType } from "../bike_properties/IHandlebarType";

export interface IStem extends IBikePart {
  length: number;
  angle: number;
  headtube_types: IHeadtubeType[];
  handlebar_type: IHandlebarType;
}
