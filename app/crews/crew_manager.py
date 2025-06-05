from crewai import Crew, Process
from app.crews.tasks import create_tasks
from app.crews.agents import fetch_agent, analyze_agent, output_agent
from dotenv import load_dotenv

load_dotenv()

def kickoff_crew(request_data):
    tasks = create_tasks(request_data)
    crew = Crew(
        agents=[fetch_agent, analyze_agent, output_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    result = crew.kickoff()
    return result
