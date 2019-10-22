import { IApplication } from "./IApplication";
import { IBrand } from "./IBrand";
import { IColor } from "./IColor";
import { IGroup } from "./IGroup";
import { IMaterial } from "./IMaterial";

export interface IBikePart {
  id: number;
  brand: IBrand;
  group: IGroup;
  model: string;
  material: IMaterial;
  weight: number;
  color: IColor;
  price: number;
  applications: IApplication[];
}
