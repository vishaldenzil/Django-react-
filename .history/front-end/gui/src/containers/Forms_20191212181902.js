
import React,{Component} from 'react'
import { Form, Select, Input, Button } from 'antd';



class CustomForm extends React.Component {
  handleSubmit = e => {
    e.preventDefault();
    
        console.log('Received values of form: ', values);
    
  };

  

  render() {
    const { getFieldDecorator } = this.props.form;
    return (
      <Form labelCol={{ span: 5 }} wrapperCol={{ span: 12 }} onSubmit={this.handleSubmit}>
        <Form.Item label="Note">
          <Input />
        </Form.Item>
        <Form.Item wrapperCol={{ span: 12, offset: 5 }}>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    );
  }
}


export default CustomForm;
