import json
import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	ScrapeWebsiteTool,
	ArxivPaperTool
)





@CrewBase
class MultiAgentContentCreationSystemCrew:
    """MultiAgentContentCreationSystem crew"""

    
    @agent
    def content_researcher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_researcher"],
            
            
            tools=[				SerperDevTool(),
				ScrapeWebsiteTool(),
				ArxivPaperTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def content_writer(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_writer"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def content_editor(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_editor"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def fact_checker(self) -> Agent:
        
        return Agent(
            config=self.agents_config["fact_checker"],
            
            
            tools=[				SerperDevTool(),
				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def content_strategist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_strategist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def research_content_foundation(self) -> Task:
        return Task(
            config=self.tasks_config["research_content_foundation"],
            markdown=False,
            
            
        )
    
    @task
    def define_content_strategy(self) -> Task:
        return Task(
            config=self.tasks_config["define_content_strategy"],
            markdown=False,
            
            
        )
    
    @task
    def create_educational_content(self) -> Task:
        return Task(
            config=self.tasks_config["create_educational_content"],
            markdown=False,
            
            
        )
    
    @task
    def verify_content_accuracy(self) -> Task:
        return Task(
            config=self.tasks_config["verify_content_accuracy"],
            markdown=False,
            
            
        )
    
    @task
    def edit_and_finalize_content(self) -> Task:
        return Task(
            config=self.tasks_config["edit_and_finalize_content"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the MultiAgentContentCreationSystem crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )

    def _load_response_format(self, name):
        # This method is not currently used but kept for future use
        # If needed, implement response format loading here
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())
        # SchemaConverter is not available in current crewai version
        # Return the JSON schema directly if needed
        return json_schema
