
import React,{Component} from 'react'
import { Form, Input, Button, Radio } from 'antd';

class CustomForm extends Component {
    handleSubmit = (event) => {
       let  name = event.target.elements.title.value;
       let  comment = event.target.elements.com.value;


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
            <Button type="primary">Submit</Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default CustomForm;