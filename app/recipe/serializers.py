"""
Serilaizers for recipe APIs
"""
from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serialzer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """"serilalizer for recipe detail view."""

    class Mete(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
