# app/agents/study_agent.py

import os
from langchain_groq import ChatGroq
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain import hub

# 1. Initialize the Groq LLM with the latest Llama 3.1 model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 2. Define the list of tools the agent can use
tools = [
    Tool(
        name="web_search",
        func=DuckDuckGoSearchRun().run,
        description="A web search engine. Use this to find articles, tutorials, and video links."
    )
]

# 3. Pull the prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")

# 4. Create the agent
agent = create_react_agent(llm, tools, prompt)

# 5. Create the Agent Executor
study_assistant_agent = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def get_study_materials(topic: str):
    """Runs the study assistant agent with a specific topic."""
    prompt_input = f"Find the best 3-4 online resources (articles or videos) for a student to learn about '{topic}'. For each, provide a short summary and the link."

    response = study_assistant_agent.invoke({
        "input": prompt_input
    })

    return response['output']