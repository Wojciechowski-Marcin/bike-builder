import { IBrake } from "./IBrake";
import { IBrakeLever } from "./IBrakeLever";
import { ICassette } from "./ICassette";
import { ICrankset } from "./ICrankset";
import { IDerailleurLever } from "./IDerailleurLever";
import { IFork } from "./IFork";
import { IFrame } from "./IFrame";
import { IFrontDerailleur } from "./IFrontDerailleur";
import { IHandlebar } from "./IHandlebar";
import { IRearDerailleur } from "./IRearDerailleur";
import { IRotor } from "./IRotor";
import { ISaddle } from "./ISaddle";
import { ISeatpost } from "./ISeatpost";
import { IShock } from "./IShock";
import { IStem } from "./IStem";
import { IWheels } from "./IWheels";

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
  Saddle: ISaddle[];
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
  | ISaddle
  | ISeatpost
  | IWheels;
