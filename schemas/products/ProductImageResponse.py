from pydantic import BaseModel, ConfigDict


class ProductImageResponse(BaseModel):
    id: int
    offer_id: int
    original_url: str
    local_path: str

    model_config = ConfigDict(
        from_attributes=True
    )