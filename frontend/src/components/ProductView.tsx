import React, { Component } from "react";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";

import fetchProductsAction from "../data/fetchProducts";
import {
  getProductsError,
  getProducts,
  getProductsPending
} from "../reducers/fetchReducer";
import { IBikePartsAPI, IBikePartType } from "../data_types/IBikePartsAPI";

interface IProps {
  products: IBikePartsAPI;
  error: Error | null;
  pending: boolean;
  fetchProducts: () => void;
}

class ProductView_ extends Component<IProps> {
  constructor(props: IProps) {
    super(props);
    this.shouldComponentRender = this.shouldComponentRender.bind(this);
  }

  componentDidMount() {
    const { fetchProducts } = this.props;
    fetchProducts();
  }

  shouldComponentRender() {
    const { pending } = this.props;
    if (pending === false) return false;
    return true;
  }

  render() {
    const { products, error, pending } = this.props;

    if (pending === true) return <div>"Loading"</div>;

    return (
      <div className="product-list-wrapper">
        {error && <span className="product-list-error">{error}</span>}
        {products &&
          Object.entries(products).map(([bikeparts, val]) => {
            return val.map((bikepart: IBikePartType) => {
              return <p key={bikepart.id}>{JSON.stringify(bikepart)}</p>;
            });
          })}
      </div>
    );
  }
}

const mapStateToProps = (state: any) => ({
  error: getProductsError(state),
  products: getProducts(state),
  pending: getProductsPending(state)
});

const mapDispatchToProps = (dispatch: any) =>
  bindActionCreators(
    {
      fetchProducts: fetchProductsAction
    },
    dispatch
  );

export const ProductView = connect(
  mapStateToProps,
  mapDispatchToProps
)(ProductView_);
