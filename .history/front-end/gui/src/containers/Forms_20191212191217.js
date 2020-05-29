
import React,{Component} from 'react'
import axios from 'axios'
import { Form, Input, Button } from 'antd';

class CustomForm extends Component {

    handleSubmit = (event,requestType,id) => {
    event.preventDefault();
    let  title = event.target.elements.title.value;
    let  content = event.target.elements.comment.value;
    console.log("aaa")
    let url = "http://localhost:8000/api/"
      switch(requestType){
          case 'post': 
                axios.post(url,{
                    title: title,
                    content: content
                     
                }).then((res)=>{
                    console.log(res) 
                }).catch((e)=>{
                    console.log(e)
                })
                break;

          case 'put':
                axios.put(`http://localhost:8000/api/${id}/`,{
                    title: title,
                    content: content  
                }).then((res)=>{
                    console.log(res)
                }).catch((e)=>{
                    console.log(e)
                })

      }


    }
  
  render() {
    return (
      <div>
        <Form onSubmit={(event) => this.handleSubmit(event,this.props.requestType, this.props.id)}>
          <Form.Item label="Title" >
            <Input name ="title" placeholder="put a title" />
          </Form.Item>
          <Form.Item label="Comment">
            <Input name ="comment" placeholder="put comment here" />
          </Form.Item>
          <Form.Item >
            <Button htmlType="submit" type="primary">Submit</Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default CustomForm;