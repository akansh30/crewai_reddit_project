from app.crews.crew_manager import kickoff_crew

if __name__ == "__main__":
    request_data = {
    "request_name": "SaaS marketing contacts",
    "purpose": "Identify and contact individuals for SaaS marketing and potential product sales.",
    "subreddits": ["/rSaaS"],
    "keywords": ["SaaS marketing", "SaaS growth", "lead generation"],
    "duration": "month"
}
    result = kickoff_crew(request_data)
    print(result)
