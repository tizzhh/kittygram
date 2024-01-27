from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cats.views import CatDetail, CatList, CatViewSet


router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]
