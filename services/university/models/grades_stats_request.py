from pydantic import BaseModel, ConfigDict


class GradesStatsRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    student_id: int | None = None
    teacher_id: int | None = None
    group_id: int | None = None