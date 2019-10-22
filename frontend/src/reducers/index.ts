import { combineReducers } from "redux";

import { fetchReducer } from "./fetchReducer";
import { bikeTypeSelectorReducer } from "./bikeTypeSelectorReducer";

export const rootReducer = combineReducers({
  fetchReducer,
  bikeTypeSelectorReducer
});

export type AppState = ReturnType<typeof rootReducer>;
