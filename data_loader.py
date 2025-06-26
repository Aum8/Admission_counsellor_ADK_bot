import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class CourseDataLoader:
    def __init__(self, excel_path: str):
        self.excel_path = Path(excel_path)
        self.courses = self._load_data()
        
    def _load_data(self) -> list[dict]:
        """Load and validate course data from Excel"""
        try:
            df = pd.read_excel(self.excel_path)
            
                
            # Convert to list of dicts with consistent naming
            courses = []
            for _, row in df.iterrows():
                courses.append({
                    'name': str(row[1]),
                    'duration': str(row[2]),
                    'annual_fee': str(row[3]),
                    'fee_after_scholarship': str(row[4])
                })
                
            logger.info(f"Successfully loaded {len(courses)} courses from Excel")
            return courses
            
        except Exception as e:
            logger.error(f"Error loading course data: {str(e)}")
            raise