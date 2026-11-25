from pydantic import BaseModel, ConfigDict, Field
from services.university.models.grade_request import MIN_GRADE, MAX_GRADE

class GradeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int = Field(ge=MIN_GRADE, le=MAX_GRADE)
    id: int