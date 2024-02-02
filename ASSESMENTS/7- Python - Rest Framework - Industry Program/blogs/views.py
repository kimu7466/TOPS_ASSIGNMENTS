from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogsSerializers
from .models import Blogs

@api_view(['GET', 'POST'])
def BlogListAPI(request):
    if request.method == 'GET':
        querySet = Blogs.objects.all()
        serializer = BlogsSerializers(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BlogsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def BlogDetailAPI(request, blog_id):

    try:
        querySet = Blogs.objects.get(id=blog_id)
    except Blogs.DoesNotExist:
        return Response({'message': "Data Not Found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogsSerializers(querySet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = BlogsSerializers(querySet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = BlogsSerializers(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        querySet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

