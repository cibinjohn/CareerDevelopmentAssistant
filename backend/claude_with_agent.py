from langchain_anthropic import ChatAnthropic
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from backend.tools import add_tool, career_info_tool
from config.constants import ANTHROPIC_BASE_MODEL

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    chunks: list[str]



class ClaudeLangchainAgent:
    def __init__(self):
        self.tools = [add_tool, career_info_tool]

        self.llm = ChatAnthropic(
            model=ANTHROPIC_BASE_MODEL,  # fast & cheap (good for dev)
            temperature=0.7,
            streaming=True
        )

        self.parser = PydanticOutputParser(pydantic_object=ResearchResponse)


    def get_basic_streaming_response(self, message:str):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    You are a career assistant that will help answer user queries.
                    Answer the user query and use neccessary tools. 
                        
                    IMPORTANT: Always use the tool result as the answer if you use 'add' tool
                    IMPORTANT: When the queries are related to IT/software related professions, always use the results from career_info_tool as reference.  If nothing is returned, Say that you do not have information regarding to the query
                    IMPORTANT: When you use career_info_tool, copy the raw returned text chunks directly 
    into the 'chunks' field of your response as a list of strings. 
    If career_info_tool was not used, set chunks to an empty list []
    
                    Wrap the output in this format and provide no other text\n{format_instructions}
                    """,
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{query}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        ).partial(format_instructions=self.parser.get_format_instructions())

        agent = create_tool_calling_agent(
            llm=self.llm,
            prompt=prompt,
            tools=self.tools
        )

        agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True)

        raw_response = agent_executor.invoke({"query": message})
        try:
            structured_response = self.parser.parse(raw_response.get("output")[0]["text"])
            print("structured_response :",structured_response)
            return  {"type": "structured", "data": structured_response.model_dump()}
        except Exception as e:
            print("Error parsing response", e, "Raw Response - ", raw_response)
            raw_text = raw_response.get("output", [{}])[0].get("text", "No response.")
            return {"type": "text", "data": raw_text}

if __name__ == "__main__":
    agent = ClaudeLangchainAgent()
    agent.get_basic_streaming_response("What is 3+3?")


