from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.serializers import ProductSerializer
from product.service.product_service import ProductService

class ProductListCreateView(APIView):
    def get(self, request):
        products = ProductService.list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = ProductService.create_product(**serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):    
    def get(self, request, prod):
        product = ProductService.get_product(prod)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, prod):
        try:
            ProductService.delete_product(prod)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, prod):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = ProductService.update_product(prod, **serializer.validated_data)
                return Response(ProductSerializer(product).data)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)