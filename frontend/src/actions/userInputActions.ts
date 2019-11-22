import { IBikeBuild } from "../data_types/IBikeBuild";

export const CHANGE_BUDGET = "CHANGE_BUDGET";
export const SELECT_BIKE_TYPE = "SELECT_BIKE_TYPE";
export const CHANGE_BIKE_BUILD = "CHANGE_BIKE_BUILD";
export const RESET_BIKE_BUILD = "RESET_BIKE_BUILD";

export function changeBudget(budget: number) {
  return {
    type: CHANGE_BUDGET,
    budget,
  };
}

export function selectBikeType(bikeType: string) {
  return {
    type: SELECT_BIKE_TYPE,
    bikeType,
  };
}

export function changeBikeBuild(bikeBuild: IBikeBuild) {
  return {
    type: CHANGE_BIKE_BUILD,
    bikeBuild,
  };
}

export function resetBikeBuild() {
  return {
    type: RESET_BIKE_BUILD,
  };
}

interface changeBudgetAction {
  type: typeof CHANGE_BUDGET;
  budget: number;
}

interface selectBikeTypeAction {
  type: typeof SELECT_BIKE_TYPE;
  bikeType: string;
}

interface changeBikeBuildAction {
  type: typeof CHANGE_BIKE_BUILD;
  bikeBuild: IBikeBuild;
}

interface resetBikeBuildAction {
  type: typeof RESET_BIKE_BUILD;
}

export type IUserInputActionTypes =
  | changeBudgetAction
  | selectBikeTypeAction
  | changeBikeBuildAction
  | resetBikeBuildAction;
