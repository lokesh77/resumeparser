from rest_framework import viewsets

from parser_app.models import Resume
from .serializers import ParserSerializer


class ParserViewSet(viewsets.ModelViewSet):
    serializer_class = ParserSerializer
    queryset = Resume.objects.all()
