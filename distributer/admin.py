from django.contrib import admin

# Register your models here.
from distributer.models import News,NewsImage,Law,Publication,NewsFovourite,LawsFovourite,PublicaFovourite

admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(Law)
admin.site.register(Publication)
admin.site.register(NewsFovourite)
admin.site.register(LawsFovourite)
admin.site.register(PublicaFovourite)