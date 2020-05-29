import React, {Component} from 'react';
import {BrowserRouter as Router} from 'react-router-dom'
import BaseRouter from './components/Routes'
import 'antd/dist/antd.css'; 
import Layout from './containers/Layout'


class App extends  Component{
  render(){

  }

}


const mapStateToProps = (state) => {
  return {
    isAuthenticated: state.token !== null,
  }
}
export default connect(mapStateToProps,null)(App);
