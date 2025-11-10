# app/agents/travel_agent.py

import os
from langchain_groq import ChatGroq
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain import hub

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

tools = [
    Tool(
        name="web_search",
        func=DuckDuckGoSearchRun().run,
        description="A web search engine. Use this to find information about train and bus availability, prices, and schedules."
    )
]

prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)

travel_planner_agent = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True  # <-- ADD THIS LINE
)

def get_travel_plan(origin: str, destination: str, date: str):
    """Runs the travel planner agent with a specific trip request."""
    prompt_input = f"""
    You are a travel planning assistant for a student in Hyderabad, India.
    Your goal is to find the most economical travel options (focus on trains or buses) for a trip.
    Plan a trip from '{origin}' to '{destination}' on or around the date '{date}'.
    Provide a summary of 2-3 of the best options you find. For each option, include the name (e.g., train name or bus service), approximate timings, and estimated price in INR.
    """

    response = travel_planner_agent.invoke({
        "input": prompt_input
    })

    return response['output']