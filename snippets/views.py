from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.parsers import JSONParser

# Create your views here.


def snippet_list(request):
    """
    List all code snippets, or create a new snippet
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return HttpResponse(serializer.data, status=200)

    elif request.method == "POST":
        data = JSONParser().parse(request.data)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)
        return HttpResponse(serializer.error, status=400)


def snippet_detail(request, pk):
    """Retrieve, update, delete a code snippet"""

    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return HttpResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request.data)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            return HttpResponse(serializer.data, status=204)
        return HttpResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
