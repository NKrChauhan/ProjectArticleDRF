from django.urls import path

from .views.article import ArticleView

urlpatterns = [
    path('', ArticleView.as_view(), name='article_create_list_view'),
    path('<int:article_id>/', ArticleView.as_view(), name='article_detail_update_delete_view'),
]
