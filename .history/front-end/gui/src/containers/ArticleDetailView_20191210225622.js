


import React,{Component} from 'react'
import Card from 'antd'
import axios from 'axios'


class ArticleList extends  Component{
    state ={ 
        article : {}
    }

    componentDidMount(){
      let articleId = this.props.match.params.articleId;
      let url = `http://localhost:8000/api/{}`
      axios.get(url).then((res)=>{
          this.setState({
              article : res.data
          })
          console.log(res.data)
      })
    }


 render(){
        return(
            <div>
               <Card title={this.state.article.title}>
                <p>{this.state.a</p>
               </Card>
            </div>
        )
    } 
}

export default ArticleList;