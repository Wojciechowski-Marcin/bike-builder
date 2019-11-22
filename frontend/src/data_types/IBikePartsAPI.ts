import { IBrake } from "./bike_parts/IBrake";
import { IBrakeLever } from "./bike_parts/IBrakeLever";
import { ICassette } from "./bike_parts/ICassette";
import { ICrankset } from "./bike_parts/ICrankset";
import { IDerailleurLever } from "./bike_parts/IDerailleurLever";
import { IFork } from "./bike_parts/IFork";
import { IFrame } from "./bike_parts/IFrame";
import { IFrontDerailleur } from "./bike_parts/IFrontDerailleur";
import { IHandlebar } from "./bike_parts/IHandlebar";
import { IRearDerailleur } from "./bike_parts/IRearDerailleur";
import { IRotor } from "./bike_parts/IRotor";
import { ISeatpost } from "./bike_parts/ISeatpost";
import { IShock } from "./bike_parts/IShock";
import { IStem } from "./bike_parts/IStem";
import { IWheels } from "./bike_parts/IWheels";

export interface IBikePartsAPI {
  Frame: IFrame[];
  Fork: IFork[];
  Shock: IShock[];
  Crankset: ICrankset[];
  Cassette: ICassette[];
  FrontDerailleur: IFrontDerailleur[];
  RearDerailleur: IRearDerailleur[];
  Brake: IBrake[];
  BrakeLever: IBrakeLever[];
  DerailleurLever: IDerailleurLever[];
  Rotor: IRotor[];
  Handlebar: IHandlebar[];
  Stem: IStem[];
  Seatpost: ISeatpost[];
  Wheels: IWheels[];
}

export type IBikePartType =
  | IFrame
  | IFork
  | IShock
  | ICrankset
  | ICassette
  | IFrontDerailleur
  | IRearDerailleur
  | IBrake
  | IBrakeLever
  | IDerailleurLever
  | IRotor
  | IHandlebar
  | IStem
  | ISeatpost
  | IWheels;
