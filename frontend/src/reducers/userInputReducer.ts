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
  bikeBuild: {
    Frame: { id: 0, price: 0.0 },
    Fork: { id: 0, price: 0.0 },
    Shock: { id: 0, price: 0.0 },
    Crankset: { id: 0, price: 0.0 },
    Cassette: { id: 0, price: 0.0 },
    FrontDerailleur: { id: 0, price: 0.0 },
    RearDerailleur: { id: 0, price: 0.0 },
    Brake: { id: 0, price: 0.0 },
    BrakeLever: { id: 0, price: 0.0 },
    DerailleurLever: { id: 0, price: 0.0 },
    Rotor: { id: 0, price: 0.0 },
    Stem: { id: 0, price: 0.0 },
    Saddle: { id: 0, price: 0.0 },
    Seatpost: { id: 0, price: 0.0 },
    Handlebar: { id: 0, price: 0.0 },
    Wheels: { id: 0, price: 0.0 }
  }
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
export const getBikeBuild = (state: IRootState) =>
  state.userInputReducer.bikeBuild;
