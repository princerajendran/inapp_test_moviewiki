from rest_framework import serializers
from .models import Person, Title


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    known_for_titles = TitleSerializer(many=True, read_only=True)  # Use 'many=True' for ManyToManyField

    class Meta:
        model = Person
        fields = '__all__'
