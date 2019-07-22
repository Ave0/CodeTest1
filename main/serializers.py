from rest_framework import serializers
from .models import  Contact
from django.contrib.auth.models import User



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id','username','first_name','email','surname']

