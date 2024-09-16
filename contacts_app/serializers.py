from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    