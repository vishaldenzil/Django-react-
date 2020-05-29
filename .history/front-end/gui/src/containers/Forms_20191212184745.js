
import React,{Component} from 'react'
import axios from 'axios'
import { Form, Input, Button, Radio } from 'antd';

class CustomForm extends Component {
    handleSubmit = (event,requestType) => {
    event.preventDefault();
    let  title = event.target.elements.title.value;
    let  content = event.target.elements.comment.value;
      switch(requestType){
          case 'post': 
                axios.post(url,{
                    title: title,
                    content: 
                     
                }).then((res)=>{
                    console.log(res) 
                }).catch((e)=>{
                    console.log(e)
                })

          case 'put':
                axios.post(url).then((res)=>{
                    console.log(res)
                }).catch((e)=>{
                    console.log(e)
                })

      }


    }
  
  render() {
    return (
      <div>
        <Form onSubmit={this.handleSubmit}>
          <Form.Item label="Title" >
            <Input name ="title" placeholder="put a title" />
          </Form.Item>
          <Form.Item label="Comment">
            <Input name ="comment" placeholder="put comment here" />
          </Form.Item>
          <Form.Item >
            <Button htmlType="button" type="primary">Submit</Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default CustomForm;