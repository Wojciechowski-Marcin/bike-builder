import { IApplication } from "../bike_properties/IApplication";
import { IBrand } from "../bike_properties/IBrand";
import { IColor } from "../bike_properties/IColor";
import { IGroup } from "../bike_properties/IGroup";
import { IMaterial } from "../bike_properties/IMaterial";

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
