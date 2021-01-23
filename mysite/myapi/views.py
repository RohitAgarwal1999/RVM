# views.py
from rest_framework import viewsets

from .serializers import employSerializer
from .models import employ


class employViewSet(viewsets.ModelViewSet):
    queryset = employ.objects.all().order_by('name')
    serializer_class = employSerializer
