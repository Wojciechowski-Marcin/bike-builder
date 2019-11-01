import { combineReducers } from "redux";

import { fetchBikePartsReducer } from "./fetchBikePartsReducer";
import { userInputReducer } from "./userInputReducer";
import { fetchBuildReducer } from "./fetchBuildReducer";

export const rootReducer = combineReducers({
  fetchBikePartsReducer,
  userInputReducer,
  fetchBuildReducer
});

export type IRootState = ReturnType<typeof rootReducer>;
