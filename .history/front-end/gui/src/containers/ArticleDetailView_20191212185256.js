


import React,{Component} from 'react'
import {Card} from 'antd'
import axios from 'axios'
import CustomForm from './Forms'


class ArticleList extends  Component{
    state = { 
        article : {}
    }

    componentDidMount(){
      let articleId = this.props.match.params.articleId;
      let url = `http://localhost:8000/api/${articleId}`
      axios.get(url).then((res)=>{
          this.setState({
              article : res.data
          })
      }).catch((e)=>{
          console.log(e)
      })
    }


 render(){
        return(
            <div>
               <Card title={this.state.article.title}>
                <p>{this.state.article.content} </p>
               </Card>
               <CustomForm requestType="put" id={this.props.match.params.articleId />
            </div>
        )
    } 
}

export default ArticleList;