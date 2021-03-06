import requests
from st2common.runners.base_action import Action

class ExampleAction(Action):
    def __init__(self, config) -> None:
        super(ExampleAction, self).__init__(config=config)

    def run(self):
        headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
        }

        json_data = {
            'data': 'string',
            'status': 'pending',
            'rule': 'rule2',
        }

        response = requests.post('http://a4ff-2402-4000-2280-bb75-d2ab-3b0a-8063-f152.ngrok.io/order', headers=headers, json=json_data)
        self.logger.info("Successfully req to awsbill")

