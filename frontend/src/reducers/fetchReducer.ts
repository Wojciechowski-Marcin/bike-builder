import {
  FETCH_PRODUCTS_PENDING,
  FETCH_PRODUCTS_SUCCESS,
  FETCH_PRODUCTS_ERROR
} from "../actions/fetchActions";
import { IBikePartsAPI } from "../data_types/IBikePartsAPI";
import { AppState } from ".";

export interface IFetchState {
  pending: boolean;
  products: IBikePartsAPI;
  error: Error | null;
}

const initialState: IFetchState = {
  pending: false,
  products: {
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

export function fetchReducer(state = initialState, action: any): IFetchState {
  switch (action.type) {
    case FETCH_PRODUCTS_PENDING:
      return {
        ...state,
        pending: true
      };
    case FETCH_PRODUCTS_SUCCESS:
      return {
        ...state,
        pending: false,
        products: action.products
      };
    case FETCH_PRODUCTS_ERROR:
      return {
        ...state,
        pending: false,
        error: action.error
      };
    default:
      return state;
  }
}

export const getProducts = (state: AppState) => state.fetchReducer.products;
export const getProductsPending = (state: AppState) =>
  state.fetchReducer.pending;
export const getProductsError = (state: AppState) => state.fetchReducer.error;
