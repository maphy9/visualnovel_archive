from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

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


    title = req.data["title"]
    formatted_title = title.replace('_', ' ')
    try:
        vn = VisualNovel.objects.get(title=formatted_title)
        serializer = VisualNovelSerializer(vn)
        return Response(data=serializer.data, status=200)
    except VisualNovel.DoesNotExist:
        return Response(status=406)


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
            body: JSON.stringify({ phrase: INSERT_PHRASE }),
        }
    }
    '''


    phrase = req.data["phrase"]
    formatted_phrase = phrase.replace('_', ' ')
    results = VisualNovel.objects.filter(title__istartswith=formatted_phrase)[:5]
    if len(results) == 0:
        return Response(status=406)
    serialized_results = [VisualNovelSerializer(vn).data for vn in results]
    return Response(data=serialized_results, status=200)


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
                genre_name: INSERT_GENRE_NAME,
                page_size: INSERT_PAGE_SIZE,
                page_number: INSERT_PAGE_NUMBER,
            }),
        }
    }
    '''


    genre_name = req.data["genre_name"]
    page_size = req.data["page_size"]
    page_number = req.data["page_number"]
    genre = None
    try:
        genre = Genre.objects.get(name=genre_name)
    except Genre.DoesNotExist:
        return Response(status=406)
    start = page_size * (page_number - 1)
    end = start + page_size
    results = genre.visual_novels.all()[start:end]
    serialized_results = [VisualNovelSerializer(vn).data for vn in results]
    return Response(data=serialized_results, status=200)


@api_view(['POST'])
def create_visual_novel(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/create_visual_novel/',
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
                author_id: INSERT_AUTHOR_ID,
                genre_id_array: INSERT_GENRE_ID_ARRAY,
            }),
        }
    }
    '''


    title = req.data["title"]
    try:
        vn = VisualNovel.objects.get(title=title)
        return Response(status=406)
    except:
        pass
    content = req.data["content"]
    developer = req.data["developer"]
    author_id = req.data["author_id"]
    genre_id_array = req.data["genre_id_array"]

    author = User.objects.get(id=author_id)
    vn = VisualNovel(title=title, content=content, developer=developer, author=author)
    vn.save()

    genres = [Genre.objects.get(id=genre_id) for genre_id in genre_id_array]

    vn.genres.add(*genres)
    vn.save()
    return Response(status=200)


@api_view(['POST'])
def get_user_info(req):
    '''
    REQUEST EXAMPLE:
    {
        'http://127.0.0.1:8000/get_user_info/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                user_id: INSERT_USER_ID,
            }),
        }
    }
    '''


    user_id = req.data["user_id"]
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=200)
    except User.DoesNotExist:
        return Response(status=406)