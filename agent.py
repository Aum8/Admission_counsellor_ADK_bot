import logging
import warnings
from google.adk import Agent
from .config import Config
from .prompt import INSTRUCTION
from .tools import (
    get_course_information,
    get_all_course_names,
    escalate_to_human
)

warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")

configs = Config()

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class CourseDatabase:
    """In-memory database for course information"""
    COURSES = [
        {
            "id": 1,
            "name": "BSc IT (with industry certificates)",
            "duration": "3 yrs",
            "annual_fee": "1,12,000",
            "fee_after_scholarship": "89,600"
        },
        {
            "id": 2,
            "name": "BCA (with industry certificates)",
            "duration": "3 yrs",
            "annual_fee": "1,12,000",
            "fee_after_scholarship": "89,600"
        },
        # Add other courses from your data table here
    ]

    @classmethod
    def get_course(cls, course_name):
        """Find course by name (partial match)"""
        for course in cls.COURSES:
            if course_name.lower() in course["name"].lower():
                return course
        return None

    @classmethod
    def get_all_course_names(cls):
        """Return list of all course names"""
        return [course["name"] for course in cls.COURSES]

# Main agent configuration
root_agent = Agent(
    model=configs.agent_settings.model,
    instruction=INSTRUCTION,
    name=configs.agent_settings.name,
    tools=[
        get_course_information,
        get_all_course_names,
        escalate_to_human
    ]
)

def initialize_agent():
    """Initialize and return the configured agent"""
    logger.info("Initializing Admissions Counselor Agent")
    return root_agent

if __name__ == "__main__":
    agent = initialize_agent()
    agent.share()