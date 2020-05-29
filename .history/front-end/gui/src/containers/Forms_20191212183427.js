
import React,{Component} from 'react'
import { Form, Input, Button, Radio } from 'antd';

class CustomForm extends Component {
    handleSubmit = (event) => {
       let  title = event.target.elements;
    //    let  comment = event.target.elements.comment.value;
       console.log(title,comment)


    }
  
  render() {
    return (
      <div>
        <Form >
          <Form.Item label="Title" >
            <Input name ="title" placeholder="put a title" />
          </Form.Item>
          <Form.Item label="Comment">
            <Input name ="comment" placeholder="put comment here" />
          </Form.Item>
          <Form.Item >
            <Button onClick={this.handleSubmit} type="primary">Submit</Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default CustomForm;