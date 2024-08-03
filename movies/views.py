from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person, Title
from .serializers import PersonSerializer, TitleSerializer
from rest_framework.permissions import IsAuthenticated


class TitleList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Title.objects.all()
        year = request.query_params.get('year')
        genre = request.query_params.get('genre')
        title_type = request.query_params.get('type')
        person_name = request.query_params.get('person_name')

        if year:
            queryset = queryset.filter(start_year=year)
        if genre:
            queryset = queryset.filter(genres__icontains=genre)
        if title_type:
            queryset = queryset.filter(title_type=title_type)
        if person_name:
            queryset = queryset.filter(known_for_titles__primary_title__icontains=person_name).distinct()

        serializer = TitleSerializer(queryset, many=True)
        return Response(serializer.data)


class PersonList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Person.objects.all()
        name = request.query_params.get('name')
        profession = request.query_params.get('profession')
        title = request.query_params.get('title')

        if name:
            queryset = queryset.filter(primary_name__icontains=name)
        if profession:
            queryset = queryset.filter(primary_profession__icontains=profession)
        if title:
            queryset = queryset.filter(known_for_titles__primary_title__icontains=title).distinct()

        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)
