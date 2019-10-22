import { IFrame } from "../data_types/IFrame";

export const FETCH_PRODUCTS_PENDING = "FETCH_PRODUCTS_PENDING";
export const FETCH_PRODUCTS_SUCCESS = "FETCH_PRODUCTS_SUCCESS";
export const FETCH_PRODUCTS_ERROR = "FETCH_PRODUCTS_ERROR";

export function fetchProductsPending() {
  return {
    type: FETCH_PRODUCTS_PENDING
  };
}

export function fetchProductsSuccess(products: IFrame[]) {
  return {
    type: FETCH_PRODUCTS_SUCCESS,
    products: products
  };
}

export function fetchProductsError(error: any) {
  return {
    type: FETCH_PRODUCTS_ERROR,
    error: error
  };
}