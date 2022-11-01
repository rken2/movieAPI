from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
@api_view(["GET"])
def getMovies(request):
    data = {}
    try:
        instance = Movie.objects.all()
    except:
        data["error"] = "Movie not found"
        return Response(data)

    if instance:
        # Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes 
        # that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
        # allowing parsed data to be converted back into complex types, after first validating the incoming data.
        data = MovieSerializer(instance, many=True).data

    # Response takes a Python data type and converts it to a byte string JSON response or whatever response type you need
    return Response(data)

@api_view(["GET"])
def getMovieByYear(request, year):
    data = {}
    try:
        instance = Movie.objects.get(year=year)
    except:
        data["error"] = "Movie not found"
        return Response(data)

    if instance:
        data = MovieSerializer(instance).data

    return Response(data)

@swagger_auto_schema(methods=['post'], request_body=MovieSerializer)
@api_view(["POST"])
def addMovie(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['put'], request_body=MovieSerializer)
@api_view(["PUT"])
def updateMovie(request):
    body = request.data
    data = []

    try:
        instance = Movie.objects.get(title=body.get("title"))
    except:
        data["error"] = "Movie not found"
        return Response(data)

    serializer = MovieSerializer(instance, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteMovie(request, title):
    data = {}

    try:
        instance = Movie.objects.get(title=title)
    except:
        data["error"] = "Movie not found"
        return Response(data)

    if instance:
        instance.delete()
        data["success"] = "Movie deleted"

    return Response(data)