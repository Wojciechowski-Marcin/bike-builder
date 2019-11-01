import { IBikePartsAPI } from "../data_types/IBikePartsAPI";

export const FETCH_BIKE_PARTS_PENDING = "FETCH_BIKE_PARTS_PENDING";
export const FETCH_BIKE_PARTS_SUCCESS = "FETCH_BIKE_PARTS_SUCCESS";
export const FETCH_BIKE_PARTS_ERROR = "FETCH_BIKE_PARTS_ERROR";

export function fetchBikePartsPending() {
  return {
    type: FETCH_BIKE_PARTS_PENDING
  };
}

export function fetchBikePartsSuccess(bikeParts: IBikePartsAPI) {
  return {
    type: FETCH_BIKE_PARTS_SUCCESS,
    bikeParts
  };
}

export function fetchBikePartsError(error: Error) {
  return {
    type: FETCH_BIKE_PARTS_ERROR,
    error
  };
}

interface fetchBikePartsPendingActionType {
  type: typeof FETCH_BIKE_PARTS_PENDING;
}

interface fetchBikePartsSuccessActionType {
  type: typeof FETCH_BIKE_PARTS_SUCCESS;
  bikeParts: IBikePartsAPI;
}

interface fetchBikePartsErrorActionType {
  type: typeof FETCH_BIKE_PARTS_ERROR;
  error: Error;
}

export type IFetchBikePartsActionTypes =
  | fetchBikePartsPendingActionType
  | fetchBikePartsSuccessActionType
  | fetchBikePartsErrorActionType;
