from config.config import AnthropicKey
from anthropic import Anthropic

from config.constants import ANTHROPIC_BASE_MODEL


class ClaudeBase(AnthropicKey):
    def __init__(self):
        super().__init__()
        self.client  = Anthropic(
    api_key=self.key
            )

    def get_basic_response(self, message):

        message = self.client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        model=ANTHROPIC_BASE_MODEL
    )

        return message.content[0].text

if __name__ == "__main__":
    cl = ClaudeBase()
    print(cl.get_basic_response("hi"))
