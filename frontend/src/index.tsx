import "./index.css";
import "antd/dist/antd.css";

import { Provider } from "react-redux";
import React from "react";
import ReactDOM from "react-dom";

import App from "./components/App";
import { configureStore } from "./store/index";

const store = configureStore();

const Root = () => (
  <Provider store={store}>
    <App />
  </Provider>
);

ReactDOM.render(<Root />, document.getElementById("root"));
