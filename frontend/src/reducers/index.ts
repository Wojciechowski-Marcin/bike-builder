import { combineReducers } from "redux";

import { fetchReducer } from "./fetchReducer";
import { userInputReducer } from "./userInputReducer";

export const rootReducer = combineReducers({
  fetchReducer,
  userInputReducer
});

export type IRootState = ReturnType<typeof rootReducer>;
