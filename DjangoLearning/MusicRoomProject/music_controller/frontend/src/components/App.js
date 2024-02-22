import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";


export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <HomePage />
       
       React Component: {this.props.name}
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App name="Rakesh Raushan" />, appDiv);