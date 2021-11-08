from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from mox_api.models import Link, Tag
from mox_api.serializers import LinkSerializer, TagSerializer
from mox_api.utils import get_title_from_url


@api_view(['GET'])
def api_root(request):
    return Response({
        'links': reverse('link-list', request=request),
    })


@api_view(['GET', 'POST'])
def link_list(request):
    """
    List all links, or create a new link.
    """
    if request.method == 'GET':
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Extract title from URL
        request.data['title'] = get_title_from_url(request.data['url'])
        
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def link(request, pk):
    """
    Retrieve or delete single link.
    """
    try:
        link = Link.objects.get(pk=pk)
    except Link.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LinkSerializer(link)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tag_list(request):
    """
    List all tags, or create a new tag.
    """
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':        
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def tag(request, pk):
    """
    Retrieve or delete single tag.
    """
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
