import os
import json

from config.constants import KEY_FILE_LOC


class AnthropicKey:
    def __init__(self):
        with open(KEY_FILE_LOC, 'r') as f:
            self.key = json.load(f).get('claude_key')




# if __name__ == '__main__':
#     x = ClaudeBase()
#     print(x.key)