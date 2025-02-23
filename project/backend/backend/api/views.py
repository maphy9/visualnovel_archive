from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Count
from .models import *
from .serializers import *
from .request_serializers import *
from random import randint
from datetime import datetime

@api_view(['POST'])
def get_popular_visual_novels(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_popular_visual_novels/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
            }),
        }
    }
    '''

    request_serializer = Request_get_best_visual_novels_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]

    start = page_size * (page_number - 1)
    end = start + page_size
    visual_novels = VisualNovel.objects.order_by("-views")[start:end]
    results = []
    for visual_novel in visual_novels:
        image = req.build_absolute_uri(visual_novel.image.url) if visual_novel.image else None
        object = {
            "title": visual_novel.title,
            "description": visual_novel.description,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_new_visual_novels(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_new_visual_novels/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
            }),
        }
    }
    '''

    request_serializer = Request_get_best_visual_novels_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]

    start = page_size * (page_number - 1)
    end = start + page_size
    visual_novels = VisualNovel.objects.order_by("-created_at")[start:end]
    results = []
    for visual_novel in visual_novels:
        image = req.build_absolute_uri(visual_novel.image.url) if visual_novel.image else None
        object = {
            "title": visual_novel.title,
            "description": visual_novel.description,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_most_liked_visual_novels(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_most_liked_visual_novels/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
            }),
        }
    }
    '''

    request_serializer = Request_get_best_visual_novels_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]

    start = page_size * (page_number - 1)
    end = start + page_size
    visual_novels = VisualNovel.objects.annotate(like_count=Count("likes")).order_by("-like_count")[start:end]
    results = []
    for visual_novel in visual_novels:
        image = req.build_absolute_uri(visual_novel.image.url) if visual_novel.image else None
        object = {
            "title": visual_novel.title,
            "description": visual_novel.description,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_random_visual_novel(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_random_visual_novel/',
        {
            method: "GET",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        }
    }
    '''

    ids = VisualNovel.objects.values_list('id', flat=True)
    random_id = randint(0, len(ids)-1)
    visual_novel = VisualNovel.objects.get(id=ids[random_id])
    image = req.build_absolute_uri(visual_novel.image.url) if visual_novel.image else None
    object = {
        "title": visual_novel.title,
        "description": visual_novel.description,
        "image": image
    }
    return Response(object, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_popular_discussions(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_popular_discussions/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
            }),
        }
    }
    '''

    request_serializer = Request_get_best_discussions_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]

    start = page_size * (page_number - 1)
    end = start + page_size
    discussions = Discussion.objects.order_by("-views")[start:end]
    results = []
    for discussion in discussions:
        image = req.build_absolute_uri(discussion.image.url) if discussion.image else None
        object = {
            "title": discussion.title,
            "description": discussion.description,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_new_discussions(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_new_discussions/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
            }),
        }
    }
    '''

    request_serializer = Request_get_best_discussions_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]

    start = page_size * (page_number - 1)
    end = start + page_size
    discussions = Discussion.objects.order_by("-created_at")[start:end]
    results = []
    for discussion in discussions:
        image = req.build_absolute_uri(discussion.image.url) if discussion.image else None
        object = {
            "title": discussion.title,
            "description": discussion.description,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_most_replied_to_discussions(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_most_replied_to_discussions/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
            }),
        }
    }
    '''

    request_serializer = Request_get_best_discussions_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]

    start = page_size * (page_number - 1)
    end = start + page_size
    discussions = Discussion.objects.annotate(reply_count=Count("replies")).order_by("-reply_count")[start:end]
    results = []
    for discussion in discussions:
        image = req.build_absolute_uri(discussion.image.url) if discussion.image else None
        object = {
            "title": discussion.title,
            "description": discussion.description,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_most_active_users(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_most_active_users/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
            }),
        }
    }
    '''

    request_serializer = Request_get_best_users_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]

    start = page_size * (page_number - 1)
    end = start + page_size
    users = User.objects.annotate(reply_count=Count("replies")).order_by("-reply_count")[start:end]
    results = []
    for user in users:
        image = req.build_absolute_uri(user.profile_picture.url) if user.profile_picture else None
        joined = user.date_joined.strftime("%d.%m.%Y")
        object = {
            "username": user.username,
            "role": user.role,
            "image": image,
            "joined": joined
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def find_visual_novels(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/find_visual_novels/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
                phrase,
            }),
        }
    }
    '''

    request_serializer = Request_find_by_phrase(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]
    phrase = data["phrase"]

    start = page_size * (page_number - 1)
    end = start + page_size
    visual_novels = VisualNovel.objects.filter(title__icontains=phrase)[start:end]
    results = []
    for visual_novel in visual_novels:
        image = req.build_absolute_uri(visual_novel.image.url) if visual_novel.image else None
        object = {
            "title": visual_novel.title,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def find_discussions(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/find_discussions/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
                phrase,
            }),
        }
    }
    '''

    request_serializer = Request_find_by_phrase(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]
    phrase = data["phrase"]

    start = page_size * (page_number - 1)
    end = start + page_size
    discussions = Discussion.objects.filter(title__icontains=phrase)[start:end]
    results = []
    for discussion in discussions:
        image = req.build_absolute_uri(discussion.image.url) if discussion.image else None
        object = {
            "title": discussion.title,
            "image": image
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)


@api_view(['POST'])
def find_users(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/find_users/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                page_size,
                page_number,
                phrase,
            }),
        }
    }
    '''

    request_serializer = Request_find_by_phrase(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data = request_serializer.validated_data

    page_size = data["page_size"]
    page_number = data["page_number"]
    phrase = data["phrase"]

    start = page_size * (page_number - 1)
    end = start + page_size
    users = User.objects.filter(username__icontains=phrase)[start:end]
    results = []
    for user in users:
        image = req.build_absolute_uri(user.profile_picture.url) if user.profile_picture else None
        object = {
            "title": user.username,
            "image": image,
        }
        results.append(object)
    return Response(results, status=status.HTTP_200_OK)