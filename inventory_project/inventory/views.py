from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer

# Create Item
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Read Item
@api_view(['GET'])
def read_item(request, item_id):
    item = cache.get(f'item_{item_id}')
    if not item:
        try:
            item = Item.objects.get(id=item_id)
            cache.set(f'item_{item_id}', item)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

# Update Item
@api_view(['PUT'])
def update_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.set(f'item_{item_id}', item)  # Update cache
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Item
@api_view(['DELETE'])
def delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        item.delete()
        cache.delete(f'item_{item_id}')  # Remove from cache
        return Response({"message": "Item deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
