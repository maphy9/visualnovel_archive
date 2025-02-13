from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from .request_serializers import *

@api_view(['POST'])
def get_visualnovel(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_visualnovel/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ title: INSERT_TITLE }),
        }
    }
    '''

    request_serializer = Request_get_visualnovel_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    data = request_serializer.validated_data

    title = data["title"]
    try:
        visual_novel = VisualNovel.objects.get(title=title)
        serialized_visual_novel = VisualNovelSerializer(visual_novel).data
        return Response(data=serialized_visual_novel, status=status.HTTP_200_OK)
    except VisualNovel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def get_visualnovels_by_genre(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_visualnovels_by_genre/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                genre: INSERT_GENRE,
                page_size: INSERT_PAGE_SIZE,
                page_number: INSERT_PAGE_NUMBER,
            }),
        }
    }
    '''

    request_serializer = Request_get_visualnovels_by_genre_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    genre = data["genre"]
    page_size = data["page_size"]
    page_number = data["page_number"]
    start = page_size * (page_number - 1)
    end = start + page_size
    visual_novels = genre.visual_novels.all()[start:end]
    serialized_visual_novels = [VisualNovelSerializer(visual_novel).data for visual_novel in visual_novels]
    return Response(data=serialized_visual_novels, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_visualnovels_by_developer(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_visualnovels_by_developer/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                developer: INSERT_DEVELOPER,
                page_size: INSERT_PAGE_SIZE,
                page_number: INSERT_PAGE_NUMBER,
            }),
        }
    }
    '''

    request_serializer = Request_get_visualnovels_by_genre_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    developer = data["developer"]
    page_size = data["page_size"]
    page_number = data["page_number"]
    start = page_size * (page_number - 1)
    end = start + page_size
    visual_novels = developer.visual_novels.all()[start:end]
    serialized_visual_novels = [VisualNovelSerializer(visual_novel).data for visual_novel in visual_novels]
    return Response(data=serialized_visual_novels, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_visualnovels_by_publisher(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_visualnovels_by_publisher/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                publisher: INSERT_PUBLISHER,
                page_size: INSERT_PAGE_SIZE,
                page_number: INSERT_PAGE_NUMBER,
            }),
        }
    }
    '''

    request_serializer = Request_get_visualnovels_by_publisher_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    publisher = data["publisher"]
    page_size = data["page_size"]
    page_number = data["page_number"]
    start = page_size * (page_number - 1)
    end = start + page_size
    visual_novels = publisher.visual_novels.all()[start:end]
    serialized_visual_novels = [VisualNovelSerializer(visual_novel).data for visual_novel in visual_novels]
    return Response(data=serialized_visual_novels, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_user_by_username(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_user_by_username/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: INSERT_USERNAME,
            }),
        }
    }
    '''

    request_serializer = Request_get_user_by_username_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    username = data["username"]
    try:
        user = User.objects.get(username=username)
        serialized_user = UserSerializer(user).data
        return Response(data=serialized_user, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def search_visualnovel(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/search_visualnovel/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                phrase: INSERT_PHRASE,
                count: INSERT_COUNT,
            }),
        }
    }
    '''

    request_serializer = Request_search_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    phrase = data["phrase"]
    count = data["count"]
    visual_novels = VisualNovel.objects.filter(title__istartswith=phrase)[:count]
    serialized_visual_novels = [VisualNovelSerializer(visual_novel).data for visual_novel in visual_novels]
    return Response(data=serialized_visual_novels, status=status.HTTP_200_OK)


@api_view(['POST'])
def search_genre(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/search_genre/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                phrase: INSERT_PHRASE,
                count: INSERT_COUNT,
            }),
        }
    }
    '''

    request_serializer = Request_search_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    phrase = data["phrase"]
    count = data["count"]
    genres = Genre.objects.filter(name__istartswith=phrase)[:count]
    serialized_genres = [GenreSerializer(genre).data for genre in genres]
    return Response(data=serialized_genres, status=status.HTTP_200_OK)


@api_view(['POST'])
def search_developer(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/search_developer/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                phrase: INSERT_PHRASE,
                count: INSERT_COUNT,
            }),
        }
    }
    '''

    request_serializer = Request_search_serializer(data=req.data)
    if not request_serializer.is_valid():
        print(req.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    phrase = data["phrase"]
    count = data["count"]
    developers = Developer.objects.filter(name__istartswith=phrase)[:count]
    serialized_developers = [DeveloperSerializer(developer).data for developer in developers]
    return Response(data=serialized_developers, status=status.HTTP_200_OK)


@api_view(['POST'])
def search_publisher(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/search_publisher/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                phrase: INSERT_PHRASE,
                count: INSERT_COUNT,
            }),
        }
    }
    '''

    request_serializer = Request_search_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    phrase = data["phrase"]
    count = data["count"]
    publishers = Publisher.objects.filter(name__istartswith=phrase)[:count]
    serialized_publishers = [PublisherSerializer(publisher).data for publisher in publishers]
    return Response(data=serialized_publishers, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_visualnovel(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/create_visualnovel/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                title: INSERT_TITLE,
                content: INSERT_CONTENT,
                developer: INSERT_DEVELOPER,
                publishers: INSERT_PUBLISHERS,
                user: INSERT_USER,
                genres: INSERT_GENRES,
            }),
        }
    }
    '''

    request_serializer = Request_create_visualnovel_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    title = data["title"]
    if VisualNovel.objects.filter(title__iexact=title).exists():
        return Response(status=status.HTTP_409_CONFLICT)
    content = data["content"]
    user = data["user"]
    developer = data["developer"]
    publishers = data["publishers"]
    genres = data["genres"]

    visual_novel = VisualNovel(title=title, content=content, developer=developer, user=user)
    visual_novel.save()
    visual_novel.genres.add(*genres)
    visual_novel.publishers.add(*publishers)

    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def create_genre(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/create_genre/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: INSERT_NAME,
            }),
        }
    }
    '''

    request_serializer = Request_create_genre_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    name = data["name"]
    if Genre.objects.filter(name__iexact=name).exists():
        return Response(status=status.HTTP_409_CONFLICT)
    genre = Genre(name=name)
    genre.save()

    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def create_developer(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/create_developer/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: INSERT_NAME,
            }),
        }
    }
    '''

    request_serializer = Request_create_developer_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    name = data["name"]
    if Developer.objects.filter(name__iexact=name).exists():
        return Response(status=status.HTTP_409_CONFLICT)
    developer = Developer(name=name)
    developer.save()

    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def create_publisher(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/create_publisher/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: INSERT_NAME,
            }),
        }
    }
    '''

    request_serializer = Request_create_publisher_serializer(data=req.data)
    if not request_serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data

    name = data["name"]
    if Publisher.objects.filter(name__iexact=name).exists():
        return Response(status=status.HTTP_409_CONFLICT)
    publisher = Publisher(name=name)
    publisher.save()

    return Response(status=status.HTTP_200_OK)