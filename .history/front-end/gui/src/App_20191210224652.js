import React from 'react';
import {Bro}
import BaseRouter from './components/Routes'
import 'antd/dist/antd.css'; 
import Layout from './containers/Layout'


function App() {
  return (
    <div className="App">
     <Layout>
        <Article/>
     </Layout>
    </div>
  );
}

export default App;
