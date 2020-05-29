import React from 'react'
import {Route} from 'react-router-dom'
import ArticleList from './'

const BaseRouter =() => (
    <div>
        <Route exact path="/" component={ArticleList}
    </div>

);

export default BaseRouter;