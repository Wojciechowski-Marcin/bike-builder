import {
  fetchProductsPending,
  fetchProductsSuccess,
  fetchProductsError
} from "../actions/fetchActions";

function fetchProducts() {
  return (dispatch: any) => {
    dispatch(fetchProductsPending());
    fetch("api/bikeparts/")
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
