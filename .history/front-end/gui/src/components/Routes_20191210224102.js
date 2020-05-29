import React from 'react'
import {Route} from 'react-router-dom'
import ArticleList from './../containers/'

const BaseRouter =() => (
    <div>
        <Route exact path="/" component={ArticleList}
    </div>

);

export default BaseRouter;