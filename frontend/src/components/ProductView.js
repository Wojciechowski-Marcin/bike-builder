import React, { Component } from "react";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";

import fetchProductsAction from "../data/fetchProducts";
import { getProductsError, getProducts, getProductsPending } from "../reducers";

// import ProductList from "./ProductList";

class ProductView_ extends Component {
  constructor(props) {
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
    // more tests
    return true;
  }

  render() {
    const { products, error, pending } = this.props;

    if (pending === true) return <div>"Loading"</div>;

    console.log(products);

    return (
      <div className="product-list-wrapper">
        {error && <span className="product-list-error">{error}</span>}
        {products.map(product => {
          return <p key={product.id}>{product.id}</p>;
        })}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  error: getProductsError(state),
  products: getProducts(state),
  pending: getProductsPending(state),
});

const mapDispatchToProps = dispatch =>
  bindActionCreators(
    {
      fetchProducts: fetchProductsAction,
    },
    dispatch,
  );

export const ProductView = connect(
  mapStateToProps,
  mapDispatchToProps,
)(ProductView_);
