from crewai import Task
from app.crews.agents import fetch_agent, analyze_agent, output_agent
from app.crews.utils.fetch_reddit_data import fetch_reddit_data
from app.crews.utils.analyze_data import analyze_data
from app.crews.utils.output_data import output_data

def create_tasks(request_data):
    fetch_task = Task(
        description="Fetch top 5 relevant Reddit users for the given request data.",
        expected_output="List of relevant Reddit user data.",
        agent=fetch_agent,
        function=fetch_reddit_data,
        function_kwargs={"request_data": request_data}
    )

    analyze_task = Task(
        description="Analyze Reddit user data and calculate influence metrics.",
        expected_output="A pandas DataFrame with analysis.",
        agent=analyze_agent,
        context=[fetch_task],
        function=analyze_data
    )

    output_task = Task(
        description="Output the analyzed data to an Excel file.",
        expected_output="Saved Excel file with analysis.",
        agent=output_agent,
        context=[analyze_task],
        function=output_data
    )

    return [fetch_task, analyze_task, output_task]
