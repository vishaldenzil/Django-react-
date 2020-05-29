


import React,{Component} from 'react'
import Article from './Article'
import axios from 'axios'


class ArticleList extends  Component{
    state ={ 
        articles : []
    }

    componentDidMount(){
      let articleId = this.props.ma
      let url = `http://localhost:8000/api/{}`
      axios.get(url).then((res)=>{
          this.setState({
              articles : res.data
          })
          console.log(res.data)
      })
    }


 render(){
        return(
            <div>
                <Article data={this.state.articles }/>
            </div>
        )
    } 
}

export default ArticleList;