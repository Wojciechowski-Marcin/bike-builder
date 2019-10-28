import React, { Component } from "react";
import { connect } from "react-redux";
import { bindActionCreators, Dispatch } from "redux";

import fetchProductsAction from "../data/fetchProducts";
import {
  getBikePartsFetchError,
  getBikeParts,
  getBikePartsFetchPending
} from "../reducers/fetchReducer";
import { IBikePartsAPI, IBikePartType } from "../data_types/IBikePartsAPI";
import { IRootState } from "../reducers";

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

const mapStateToProps = (state: IRootState) => ({
  error: getBikePartsFetchError(state),
  products: getBikeParts(state),
  pending: getBikePartsFetchPending(state)
});

const mapDispatchToProps = (dispatch: Dispatch) =>
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
