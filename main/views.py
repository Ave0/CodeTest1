from django.shortcuts import render
from .models import  Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .serializers import ContactSerializer



# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def testview(request):
    return render(request, 'main/index2.html')


class ListContactView(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleContactView(RetrieveUpdateDestroyAPIView ):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
