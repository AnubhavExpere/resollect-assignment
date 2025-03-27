from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.pagination import PageNumberPagination

class ItemListCreateView(generics.ListCreateAPIView):
    queryset= Item.objects.all()
    serializer_class= ItemSerializer
    pagination_class= PageNumberPagination

    def get_queryset(self):
        queryset=super().get_queryset()
        name=self.request.query_params.get("name")
        brand=self.request.query_params.get("brand")
        category=self.request.query_params.get("category")
        
        if name:
            queryset=queryset.filter(name__icontains=name)
        if brand:
            queryset=queryset.filter(brand__icontains=brand)
        if category:
            queryset=queryset.filter(category__icontains=category)

        return queryset
    
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_object(self):
        return super().get_object()
    
