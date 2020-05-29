import React from 'react'
import {Route} from 'react-router-dom'
import ArticleList from './../containers/ArticleList'

const BaseRouter =() => (
    <div>
        <Route exact path="/" component={ArticleList}/>
        <Route exact path="/:a" component={ArticleList}/>
    </div>

);

export default BaseRouter;