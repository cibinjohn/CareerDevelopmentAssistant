from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

from config.constants import ANTHROPIC_BASE_MODEL

load_dotenv()

class ClaudeLangchain:
    def __init__(self):

        self.llm = ChatAnthropic(
            model=ANTHROPIC_BASE_MODEL,  # fast & cheap (good for dev)
            temperature=0.7,
            streaming=True
        )


    def get_basic_streaming_response(self, message:str):

        response = self.llm.stream([HumanMessage(content=message)])

        return response

    
