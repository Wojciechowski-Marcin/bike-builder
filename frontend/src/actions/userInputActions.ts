export const CHANGE_BUDGET = "CHANGE_BUDGET";
export const SELECT_BIKE_TYPE = "SELECT_BIKE_TYPE";

export function changeBudget(budget: number) {
  return {
    type: CHANGE_BUDGET,
    budget
  };
}

export function selectBikeType(bikeType: string) {
  return {
    type: SELECT_BIKE_TYPE,
    bikeType
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

export type IUserInputActionTypes = changeBudgetAction | selectBikeTypeAction;
