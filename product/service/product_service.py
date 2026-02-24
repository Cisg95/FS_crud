from ..model.models import Product

class ProductService:
    @staticmethod
    def create_product(**data):
        return Product.objects.create(**data)
    @staticmethod
    def list_products():
        return Product.objects.all().order_by('id')
    @staticmethod
    def get_product(prod):
        product = Product.objects.filter(id=prod).first()
        if not product:
            raise Exception("Product not found")
        return product
    @staticmethod
    def delete_product(prod):
        product = Product.objects.filter(id=prod).first()
        if not product:
            raise Exception("Product not found")
        product.delete()
    @staticmethod
    def update_product(prod, **data):
        product = Product.objects.filter(id=prod).first()
        if not product:
            raise Exception("Product not found")
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product