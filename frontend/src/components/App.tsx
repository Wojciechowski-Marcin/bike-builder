import React from "react";
import { Layout, Menu, Typography } from "antd";
import { BikeTypeSelector } from "./BikeTypeSelector";
import { ProductView } from "./ProductView";
import { BikePartSelector } from "./BikePartSelector";

const { Header, Content, Footer } = Layout;
const { Title } = Typography;

function App() {
  return (
    <div className="App">
      <Layout className="layout">
        <Header style={style.header}>
          <div className="logo" />
          <Menu
            mode="horizontal"
            defaultSelectedKeys={["1"]}
            style={style.menu}
          >
            <Menu.Item key="1">Home</Menu.Item>
            <Menu.Item key="2">Categories</Menu.Item>
            <Menu.Item key="3">Build</Menu.Item>
          </Menu>
        </Header>
        <Content style={style.content}>
          <Title style={style.title}>Build your dream bike!</Title>
          <BikeTypeSelector />
        </Content>
        <Content style={style.content}>
          <BikePartSelector />
        </Content>
        <div style={style.productView}>
          <ProductView />
        </div>
        <Footer>Marcin Wojciechowski ©2019</Footer>
      </Layout>
    </div>
  );
}

const style = {
  menu: {
    lineHeight: "64px",
    backgroundColor: "white"
  },
  title: {
    margin: "48px 0 24px"
  },
  content: {
    padding: "0 50px",
    height: "calc(100vh - 64px)",
    marginTop: 64
  },
  productView: {
    background: "#fff",
    padding: 24,
    height: "auto"
  },
  header: {
    position: "fixed",
    width: "100%",
    zIndex: 1,
    backgroundColor: "white"
  } as React.CSSProperties
};

export default App;
