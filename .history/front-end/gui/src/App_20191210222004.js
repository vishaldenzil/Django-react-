import React from 'react';
import 'antd/dist/antd.css'; 
import Layout from './containers/Layout'
import Article from './containers/ArticleList'

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
