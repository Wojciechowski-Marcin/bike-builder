import { SELECT_BIKE_TYPE } from "../actions/bikeTypeSelectorActions";
import { AppState } from ".";

export interface IBikeTypeSelectorState {
  bikeType: string;
}

const initialState: IBikeTypeSelectorState = {
  bikeType: ""
};

export function bikeTypeSelectorReducer(
  state = initialState,
  action: any
): IBikeTypeSelectorState {
  switch (action.type) {
    case SELECT_BIKE_TYPE:
      return {
        ...state,
        bikeType: action.bikeType
      };
    default:
      return state;
  }
}

export const getSelectedBikeType = (state: AppState) =>
  state.bikeTypeSelectorReducer.bikeType;
