
import React,{Component} from 'react'
import { Form, Input, Button, Radio } from 'antd';

class CustomForm extends Component {
    handleSubmit = (event) => {
        event.preventDefault();
       let  title = event.target.elements.title.value;
       let  comment = event.target.elements.comment.value;
       console.log(title,comment)


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