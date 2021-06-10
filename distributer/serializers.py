from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from distributer.models import News, NewsImage, Law, Publication


class NewsListSerializer(ModelSerializer):
    is_fovourite = SerializerMethodField()

    class Meta:
        model = News
        fields = 'id title short image created is_fovourite'.split()

    def get_is_fovourite(self, obj):
        user = self.context['user']
        if user.is_anonymous:
            return False


class NewsDetailSerializer(ModelSerializer):
    images = SerializerMethodField()

    class Meta:
        model = News
        fields = 'id title description link images'.split()

    def get_images(self, obj):
        return NewsImage.objects.filter(news=obj).values_list('image', flat=True)


class LawListSerializer(ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title type created'.split()


class LawDetailSerializer(ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title description type created'.split()


class PublicationListApiView(ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title created'.split()


class PUBLICATIONDetailSerializer(ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title description type created'.split()
