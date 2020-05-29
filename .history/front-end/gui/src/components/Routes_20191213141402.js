import React from 'react'
import {Route} from 'react-router-dom'
import ArticleList from './../containers/ArticleList'
import ArticleDetail from './../containers/ArticleDetailView'
import LoginPage from './../containers/' 

const BaseRouter =() => (
    <div>
        <Route exact path="/" component={ArticleList}/>
        <Route exact path="/:articleId" component={ArticleDetail}/>
    </div>

);

export default BaseRouter;