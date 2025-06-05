from crewai import LLM, Agent

groq_llm = LLM(model="groq/meta-llama/llama-4-scout-17b-16e-instruct")

fetch_agent = Agent(
    role="Reddit Data Collector",
    goal="Fetch relevant Reddit users based on research inputs.",
    backstory="You extract Reddit authors from relevant posts using keywords, subreddits, and duration.",
    llm=groq_llm,
    verbose=True
)

analyze_agent = Agent(
    role="Data Analyzer",
    goal="Analyze Reddit user data for influence and relevance.",
    backstory="You calculate metrics like influence score and provide insights.",
    llm=groq_llm,
    verbose=True
)

output_agent = Agent(
    role="Output Writer",
    goal="Output the final analysis to an Excel file.",
    backstory="You save the results neatly for the user.",
    llm=groq_llm,
    verbose=True
)
