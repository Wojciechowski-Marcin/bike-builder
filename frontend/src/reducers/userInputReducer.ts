import {
  CHANGE_BUDGET,
  SELECT_BIKE_TYPE,
  CHANGE_BIKE_BUILD,
  IUserInputActionTypes
} from "../actions/userInputActions";
import { IRootState } from ".";
import { IBikeBuild } from "../data_types/IBikeBuild";

export interface IUserInputState {
  budget: number;
  bikeType: string;
  bikeBuild: IBikeBuild;
}

const initialState: IUserInputState = {
  budget: 0,
  bikeType: "",
  bikeBuild: {}
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
    case CHANGE_BIKE_BUILD:
      return {
        ...state,
        bikeBuild: {
          ...state.bikeBuild,
          ...action.bikeBuild
        }
      };
    default:
      return state;
  }
}

export const getBudget = (state: IRootState) => state.userInputReducer.budget;
export const getSelectedBikeType = (state: IRootState) =>
  state.userInputReducer.bikeType;
