import {
  CHANGE_BUDGET,
  SELECT_BIKE_TYPE,
  IUserInputActionTypes
} from "../actions/userInputActions";
import { IRootState } from ".";

export interface IUserInputState {
  budget: number;
  bikeType: string;
}

const initialState: IUserInputState = {
  budget: 0,
  bikeType: ""
};

export function userInputReducer(
  state = initialState,
  action: IUserInputActionTypes
): IUserInputState {
  switch (action.type) {
    case CHANGE_BUDGET:
      return {
        ...state,
        budget: action.budget
      };
    case SELECT_BIKE_TYPE:
      return {
        ...state,
        bikeType: action.bikeType
      };
    default:
      return state;
  }
}

export const getBudget = (state: IRootState) => state.userInputReducer.budget;
export const getSelectedBikeType = (state: IRootState) =>
  state.userInputReducer.bikeType;
