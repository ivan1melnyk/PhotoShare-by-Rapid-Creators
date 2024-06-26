from datetime import datetime
from pydantic import BaseModel
from src.schemas.users import UserResponse


class RatingSchema(BaseModel):
    image_id: int
    rating: int

    class Config:
        from_attributes = True


class RatingResponse(BaseModel):
    id: int = 1
    image_id: int
    user: UserResponse
    rating: int
    created_at: datetime | None

    class Config:
        from_attributes = True


class RatingAverageResponse(BaseModel):
    image_id: int
    average_rating: float | None

    class Config:
        from_attributes = True
