import { Dispatch } from "redux";

import {
  fetchBuildPending,
  fetchBuildSuccess,
  fetchBuildError,
} from "../actions/fetchBuildActions";
import { IBikeBuild } from "../data_types/IBikeBuild";

function createFetchParametersFromBikeBuild(bikeBuild: IBikeBuild) {
  let parameters = "?";

  Object.entries(bikeBuild).map(
    ([key, value]) => (parameters += `${key.toLowerCase()}=${value.id}&`),
  );

  return parameters;
}

export function fetchBuild(
  bikeBuild: IBikeBuild,
  bikeType: string,
  budget: number,
) {
  const parameters = createFetchParametersFromBikeBuild(bikeBuild);
  return (dispatch: Dispatch) => {
    dispatch(fetchBuildPending());
    fetch(`api/builder/${parameters}biketype=${bikeType}&budget=${budget}`)
      .then(res => res.json())
      .then(res => {
        if (res.error) {
          throw res.error;
        }
        dispatch(fetchBuildSuccess(res));
        return res;
      })
      .catch(error => {
        dispatch(fetchBuildError(error));
      });
  };
}
