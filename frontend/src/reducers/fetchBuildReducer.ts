import {
  FETCH_BUILD_PENDING,
  FETCH_BUILD_SUCCESS,
  FETCH_BUILD_ERROR,
  IFetchBuildActionTypes
} from "../actions/fetchBuildActions";
import { IBikeBuild } from "../data_types/IBikeBuild";
import { IRootState } from ".";

export interface IBuildState {
  pending: boolean;
  error: Error | null;
  build: IBikeBuild;
}

const initialState: IBuildState = {
  pending: false,
  error: null,
  build: {}
};

export function fetchBuildReducer(
  state = initialState,
  action: IFetchBuildActionTypes
): IBuildState {
  switch (action.type) {
    case FETCH_BUILD_PENDING:
      return {
        ...state,
        pending: true
      };
    case FETCH_BUILD_SUCCESS:
      return {
        ...state,
        pending: false,
        build: action.build
      };
    case FETCH_BUILD_ERROR:
      return {
        ...state,
        pending: false,
        error: action.error
      };
    default:
      return state;
  }
}

export const getFetchBuildResult = (state: IRootState) =>
  state.fetchBuildReducer.build;
export const getFetchBuildPending = (state: IRootState) =>
  state.fetchBuildReducer.pending;
export const getFetchBuildError = (state: IRootState) =>
  state.fetchBuildReducer.error;
