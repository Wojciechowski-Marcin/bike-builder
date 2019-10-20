import {
  fetchProductsPending,
  fetchProductsSuccess,
  fetchProductsError,
} from "../actions";

function fetchProducts() {
  return dispatch => {
    dispatch(fetchProductsPending());
    fetch("api/frames/")
      .then(res => res.json())
      .then(res => {
        if (res.error) {
          throw res.error;
        }
        dispatch(fetchProductsSuccess(res));
        return res;
      })
      .catch(error => {
        dispatch(fetchProductsError(error.name));
      });
  };
}

export default fetchProducts;
