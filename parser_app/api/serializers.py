from rest_framework import serializers

from parser_app.models import Resume


class ParserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'name', 'email', 'mobile_number', 'education', 'educations',
                  'skills', 'experience', 'experiences', 'uploaded_on')
