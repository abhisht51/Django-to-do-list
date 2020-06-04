from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from .models import Item

# Create your views here.

@api_view(['GET'])
def test(request):     
    return Response("Hello world")

@api_view(['GET'])
def itemList(request):
    items = Item.objects.all().order_by('-id')
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def itemUpdate(request,pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def itemDelete(request,pk):
    items = Item.objects.get(id=pk)
    items.delete()
    return Response("Success")
