from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..api_services.article import ArticleAPIService


class ArticleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, article_id=None):
        """
        GEt list of articles for the user or 1 details of the articles
        """
        if article_id:
            article_data = ArticleAPIService.get_article(article_id=article_id, article_author_id=request.user.id)
        else:
            article_data = ArticleAPIService.get_articles(article_author_id=request.user.id)
        return Response(data=article_data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create the article using the data
        """
        saved_article_data = ArticleAPIService.create_article(article_data=request.data, article_author_id=request.user.id)
        return Response(data=saved_article_data, status=status.HTTP_201_CREATED)

    def put(self, request, article_id):
        """
        Update the article data
        """
        updated_article_data = ArticleAPIService.update_article(article_id=article_id, article_data=request.data, article_author_id=request.user.id)
        return Response(data=updated_article_data, status=status.HTTP_200_OK)

    def delete(self, request, article_id):
        """
        Delete an article
        """
        ArticleAPIService.delete_article(article_id=article_id, article_author_id=request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)
