from schemas.products.Product import Product

class ProductListRead(Product):
    id: int
    
    class Config:
        from_attributes = True