import {
  CHANGE_BUDGET,
  SELECT_BIKE_TYPE,
  CHANGE_BIKE_BUILD,
  IUserInputActionTypes,
  RESET_BIKE_BUILD,
} from "../actions/userInputActions";
import { IRootState } from ".";
import { IBikeBuild } from "../data_types/IBikeBuild";

export interface IUserInputState {
  budget: number;
  bikeType: string;
  bikeBuild: IBikeBuild;
}

const initialState: IUserInputState = {
  budget: 1000000,
  bikeType: "MTB",
  bikeBuild: {
    Frame: { id: -1, price: 0.0 },
    Fork: { id: -1, price: 0.0 },
    Shock: { id: -1, price: 0.0 },
    Crankset: { id: -1, price: 0.0 },
    Cassette: { id: -1, price: 0.0 },
    FrontDerailleur: { id: -1, price: 0.0 },
    RearDerailleur: { id: -1, price: 0.0 },
    Brake: { id: -1, price: 0.0 },
    BrakeLever: { id: -1, price: 0.0 },
    DerailleurLever: { id: -1, price: 0.0 },
    Rotor: { id: -1, price: 0.0 },
    Stem: { id: -1, price: 0.0 },
    Seatpost: { id: -1, price: 0.0 },
    Handlebar: { id: -1, price: 0.0 },
    Wheels: { id: -1, price: 0.0 },
  },
};

export function userInputReducer(
  state = initialState,
  action: IUserInputActionTypes,
): IUserInputState {
  switch (action.type) {
    case CHANGE_BUDGET:
      return {
        ...state,
        budget: action.budget,
      };
    case SELECT_BIKE_TYPE:
      return {
        ...state,
        bikeType: action.bikeType,
      };
    case CHANGE_BIKE_BUILD:
      return {
        ...state,
        bikeBuild: {
          ...state.bikeBuild,
          ...action.bikeBuild,
        },
      };
    case RESET_BIKE_BUILD:
      return {
        ...state,
        bikeBuild: {
          ...initialState.bikeBuild,
        },
      };
    default:
      return state;
  }
}

export const getBudget = (state: IRootState) => state.userInputReducer.budget;
export const getSelectedBikeType = (state: IRootState) =>
  state.userInputReducer.bikeType;
export const getBikeBuild = (state: IRootState) =>
  state.userInputReducer.bikeBuild;
