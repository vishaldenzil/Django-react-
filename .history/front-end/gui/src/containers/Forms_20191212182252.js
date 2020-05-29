import { Form, Input, Button, Radio } from 'antd';

class CustomForm extends React.Component {
  
  render() {
    return (
      <div>
        <Form >
          <Form.Item label="Field A" >
            <Input placeholder="put a title" />
          </Form.Item>
          <Form.Item label="Field B">
            <Input placeholder="put comment" />
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