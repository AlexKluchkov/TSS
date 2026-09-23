from schemas.products.AboutProduct import AboutProduct

class AboutProductRead(AboutProduct):
    id: int
    
    class Config:
        from_attributes = True  # важно!