import { IBikeBuild } from "../data_types/IBikeBuild";

export const FETCH_BUILD_PENDING = "FETCH_BUILD_PENDING";
export const FETCH_BUILD_SUCCESS = "FETCH_BUILD_SUCCESS";
export const FETCH_BUILD_ERROR = "FETCH_BUILD_ERROR";

export function fetchBuildPending() {
  return {
    type: FETCH_BUILD_PENDING
  };
}

export function fetchBuildSuccess(build: IBikeBuild) {
  return {
    type: FETCH_BUILD_SUCCESS,
    build
  };
}

export function fetchBuildError(error: Error) {
  return {
    type: FETCH_BUILD_ERROR,
    error
  };
}

interface fetchBuildPendingAction {
  type: typeof FETCH_BUILD_PENDING;
}

interface fetchBuildSuccessAction {
  type: typeof FETCH_BUILD_SUCCESS;
  build: IBikeBuild;
}

interface fetchBuildErrorAction {
  type: typeof FETCH_BUILD_ERROR;
  error: Error;
}

export type IFetchBuildActionTypes =
  | fetchBuildPendingAction
  | fetchBuildSuccessAction
  | fetchBuildErrorAction;
