# app/agents/recommendation_agent.py

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
        description="Use this to find current movie recommendations, ratings, and new learning resources or tutorials."
    )
]

prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)

recommendation_agent = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def get_recommendation(recommend_type: str):
    """Runs the recommendation agent based on the user's request."""

    if recommend_type == "movie":
        prompt_input = """
        You are a movie recommendation expert.
        Suggest 3 good, family-friendly movies that are currently popular or highly-rated.
        For each movie, provide a one-sentence summary and why it's a good watch for a family.
        """
    elif recommend_type == "learn":
        prompt_input = """
        You are a tech and learning advisor. The user is a student interested in AI and Python.
        Suggest 3 new, interesting skills or topics they could start learning this weekend.
        For each suggestion, provide a one-sentence description and a link to a good starting tutorial or article.
        """
    else:
        return "Invalid recommendation type."

    response = recommendation_agent.invoke({
        "input": prompt_input
    })

    return response['output']