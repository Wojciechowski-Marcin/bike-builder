import {
  fetchBikePartsPending,
  fetchBikePartsSuccess,
  fetchBikePartsError,
} from "../actions/fetchBikePartsActions";
import { Dispatch } from "redux";

export function fetchBikeParts() {
  return (dispatch: Dispatch) => {
    dispatch(fetchBikePartsPending());
    fetch("api/bikeparts/")
      .then(res => res.json())
      .then(res => {
        if (res.error) {
          throw res.error;
        }
        dispatch(fetchBikePartsSuccess(res));
        return res;
      })
      .catch(error => {
        dispatch(fetchBikePartsError(error));
      });
  };
}
