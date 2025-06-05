### Project Overview: Reddit Data Analysis with Crew AI and Groq LLM

## What is Crew AI?

**Crew AI** is a framework designed to orchestrate multiple AI agents, each with a specific role, to work together like a team. Each agent can handle a distinct task, and they collaborate in a pipeline-like process to complete a complex workflow.

## How does it fit in this project?

In this project, Crew AI is used to:

- Define multiple agents, for example:
  - A **Researcher agent** to find relevant Reddit users.
  - An **Analyst agent** to compute user metrics like karma, activity level, etc.
  - An **Output agent** to save the final processed data into a file (like Excel).

- Orchestrate these agents to work together in sequence:
  - Each agent performs its role and passes the result to the next agent.
  - Crew AI manages this collaboration and ensures smooth data flow.

## Role of Groq LLM

Groq LLM is the underlying language model that powers the NLP tasks of Crew AI agents. It acts as the “brain” behind the agents:

- Each agent uses Groq’s LLM to perform tasks like summarization, data analysis, and interpretation.
- The LLM provides fast and accurate text processing for these tasks.

This is similar to using other language models like OpenAI’s GPT, but Groq’s LLM offers high-speed inference with the `llama-3.3-70b-versatile` model in this project.

## How it works in this project

- `fetch_reddit_data.py`: Fetches data about Reddit users and their karma.
- `analyze_data.py`: Performs data analysis, like calculating engagement scores.
- `output_data.py`: Exports the final data to an Excel file.
- `crew_manager.py`: Uses Crew AI to manage the workflow, assigning tasks to agents.
- `train_crew.py`: Executes the entire process by calling the `kickoff_crew` function.

The agents work in sequence:
1. Fetch data.
2. Analyze data.
3. Save the data.
