from pydantic import BaseModel, ConfigDict, Field


class GradesStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int
    min: int | None = Field(default=None, ge=2, le=5)
    max: int | None = Field(default=None, ge=2, le=5)
    avg: float | None = Field(default=None, ge=2, le=5)