import {
  FETCH_BIKE_PARTS_PENDING,
  FETCH_BIKE_PARTS_SUCCESS,
  FETCH_BIKE_PARTS_ERROR,
  IFetchActionTypes
} from "../actions/fetchActions";
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
    Saddle: [],
    Seatpost: [],
    Handlebar: [],
    Wheels: []
  },
  error: null
};

export function fetchReducer(
  state = initialState,
  action: IFetchActionTypes
): IFetchState {
  switch (action.type) {
    case FETCH_BIKE_PARTS_PENDING:
      return {
        ...state,
        pending: true
      };
    case FETCH_BIKE_PARTS_SUCCESS:
      return {
        ...state,
        pending: false,
        bikeParts: action.bikeParts
      };
    case FETCH_BIKE_PARTS_ERROR:
      return {
        ...state,
        pending: false,
        error: action.error
      };
    default:
      return state;
  }
}

export const getBikeParts = (state: IRootState) => state.fetchReducer.bikeParts;
export const getBikePartsFetchPending = (state: IRootState) =>
  state.fetchReducer.pending;
export const getBikePartsFetchError = (state: IRootState) =>
  state.fetchReducer.error;
