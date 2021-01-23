# serializers.py
from rest_framework import serializers

from .models import employ

class employSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employ
        fields = ('name', 'sirname')