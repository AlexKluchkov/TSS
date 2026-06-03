from schemas.Product import Product

class ProductListRead(Product):
    id: int
    
    class Config:
        from_attributes = True