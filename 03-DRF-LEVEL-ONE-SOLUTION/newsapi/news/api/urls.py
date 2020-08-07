from django.urls import path
from news.api.views import (ArticleDetailAPIView, ArticleListCreateAPIView,
                            JournalistListCreateAPIView)
# from news.api.views import (article_detail_api_view,
#                             article_list_create_api_view)

"""Solution from Task 3: Urls
Model Serializer changed the first structure of the 2nd task
Solution derived from exercises.
"""

urlpatterns = [
    path("articles/", 
         ArticleListCreateAPIView.as_view(), 
         name="article-list"),

    path("articles/<int:pk>/", 
         ArticleDetailAPIView.as_view(), 
         name="article-detail"),

    path("journalists/", 
         JournalistListCreateAPIView.as_view(), 
         name="journalist-list")
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>/", article_detail_api_view, name="article-detail")
]