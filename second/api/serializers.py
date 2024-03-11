from rest_framework import serializers
from greeting.models import add_details
from django.contrib.auth.models import User
class add_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=add_details
        fields='__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=[
            'username',
            'email',
            'password',
        ]

