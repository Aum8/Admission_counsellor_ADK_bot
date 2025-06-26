import logging
from typing import Optional, Dict
from google.adk.tools import ToolContext
from .data_loader import CourseDataLoader

logger = logging.getLogger(__name__)
course_loader = CourseDataLoader("/home/web-h-060/Code/ADK/Admission_counselor/courses.xlsx")

def get_course(course_name: str) -> dict | None:
    """Find course by name (partial match)"""
    for course in course_loader.courses:
        if course_name.lower() in course["name"].lower():
            return course
    return None

def get_all_course_names() -> list[str]:
    """Return list of all course names"""
    return [course["name"] for course in course_loader.courses]


def get_course_information(
    course_name: str,
    info_requested: Optional[str] = None
) -> Dict:
    """
    Retrieves information about a specific course including duration, fees, and scholarship details.
    
    Args:
        course_name: Name or partial name of the course (e.g., "BBA", "BSc IT")
        info_requested: Specific information needed (optional)
                        Can be "duration", "annual_fee", or "fee_after_scholarship"
        context: Tool context for conversation tracking
    
    Returns:
        Dictionary with course information or error message
        
    Example:
        >>> get_course_information("BBA")
        {
            'status': 'success',
            'course': 'BBA (with industry certificates)',
            'duration': '3 yrs',
            'annual_fee': '1,12,000',
            'fee_after_scholarship': '89,600'
        }
    """
    try:
        course = get_course(course_name=course_name)
        if not course:
            return {
                'status': 'error',
                'message': f"No course found matching '{course_name}'"
            }
        
        if info_requested:
            # Handle specific information requests
            if info_requested in course:
                return {
                    'status': 'success',
                    'course': course['name'],
                    info_requested: course[info_requested]
                }
            return {
                'status': 'error',
                'message': f"Course information '{info_requested}' not available"
            }
        
        # Return all course information if no specific request
        return {
            'status': 'success',
            **course
        }
        
    except Exception as e:
        logger.error(f"Error getting course information: {str(e)}")
        return {
            'status': 'error',
            'message': "Technical error retrieving course information"
        }


def escalate_to_human(
    reason: str,
    user_query: str
) -> Dict:
    """
    Escalates the conversation to a human counselor when the question is out of scope.
    
    Args:
        reason: Reason for escalation (e.g., "out_of_scope", "complex_question")
        user_query: The original user query that couldn't be answered
        context: Tool context for conversation tracking
    
    Returns:
        Dictionary with escalation confirmation
        
    Example:
        >>> escalate_to_human("out_of_scope", "What's the campus nightlife like?")
        {
            'status': 'success',
            'response': "I'm afraid I don't have that information yet, but I can pass your query to our human counselor"
        }
    """
    logger.info(f"Escalating to human: {reason} - Query: {user_query}")
    
    return {
        'status': 'success',
        'response': "A human counselor will be with you shortly"
    }