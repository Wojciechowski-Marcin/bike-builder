import {
  FETCH_BIKE_PARTS_PENDING,
  FETCH_BIKE_PARTS_SUCCESS,
  FETCH_BIKE_PARTS_ERROR,
  IFetchBikePartsActionTypes,
} from "../actions/fetchBikePartsActions";
import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { IRootState } from ".";

export interface IFetchState {
  pending: boolean;
  bikeParts: IBikePartsAPI;
  error: Error | null;
}

const initialState: IFetchState = {
  pending: false,
  bikeParts: {
    Frame: [],
    Fork: [],
    Shock: [],
    Crankset: [],
    Cassette: [],
    FrontDerailleur: [],
    RearDerailleur: [],
    Brake: [],
    BrakeLever: [],
    DerailleurLever: [],
    Rotor: [],
    Stem: [],
    Seatpost: [],
    Handlebar: [],
    Wheels: [],
  },
  error: null,
};

export function fetchBikePartsReducer(
  state = initialState,
  action: IFetchBikePartsActionTypes,
): IFetchState {
  switch (action.type) {
    case FETCH_BIKE_PARTS_PENDING:
      return {
        ...state,
        pending: true,
      };
    case FETCH_BIKE_PARTS_SUCCESS:
      return {
        ...state,
        pending: false,
        bikeParts: action.bikeParts,
      };
    case FETCH_BIKE_PARTS_ERROR:
      return {
        ...state,
        pending: false,
        error: action.error,
      };
    default:
      return state;
  }
}

export const getFetchBikePartsResult = (state: IRootState) =>
  state.fetchBikePartsReducer.bikeParts;
export const getFetchBikePartsPending = (state: IRootState) =>
  state.fetchBikePartsReducer.pending;
export const getFetchBikePartsError = (state: IRootState) =>
  state.fetchBikePartsReducer.error;
