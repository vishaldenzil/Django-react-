import React from 'react';
import {BrowserRouter as Router} from 'react-router-dom'
import BaseRouter from './components/Routes'
import 'antd/dist/antd.css'; 
import Layout from './containers/Layout'


function App() {
  return (
    <div className="App">
    <Router>
      <Layout>
          <BaseRouter/>
      </Layout>  
    </Router>
    </div>
  );
}


const mapStateToProps = (state) => {
  return {
    isAuthenticated: state.auth.token !== null,
    authUser: state.auth,
    themeInfo: state.orgLogo.theme
  }
}
export default App;
