from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from distributer.models import News, Law, Publication
from distributer.serializers import NewsListSerializer, NewsDetailSerializer, LawListSerializer, LawDetailSerializer, \
    PUBLICATIONDetailSerializer, PublicationListApiView

@permission_classes([IsAuthenticated])
class NewsListApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer

    def list(self, request, *args, **kwargs):
        news = News.objects.all()
        data = self.serializer_class(news, many=True,
                                     context={'user': request.user}).data
        return Response(data=data)

class NewsDetailApiView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'id'

class LawListApiView(ListAPIView):
    queryset = Law.objects.all()
    serializer_class = LawListSerializer

    def list(self, request, *args, **kwargs):
        laws = Law.objects.all()
        data = self.serializer_class(laws, many=True ,
                                     context={'user': request.user}).data
        return Response(data=data)

class LawsDetailApiView(RetrieveAPIView):
    queryset = Law.objects.all()
    serializer_class = LawDetailSerializer
    lookup_field = 'id'

class PublicationListApiView(ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationListApiView

    def list(self, request, *args, **kwargs):
        publica = Publication.objects.all()
        data = self.serializer_class(publica, many=True,
                                     context={'user': request.user}).data
        return Response(data=data)

class PublicationDetailApiView(RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PUBLICATIONDetailSerializer
    lookup_field = 'id'

@api_view(['POST'])
def login_View(request):
    if request.method=='POST':
        username=request.data['username']
        password=request.data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            tokens=Token.objects.filter(user=user)
            tokens.delete()
            token=Token.objects.create(user=user)
            return Response(data={'key':token.key})
        else:
            return Response(data={'message':'ERROR'})