from ..services.article import ArticleService
from ..serializers.article import ArticleSerializer


class ArticleAPIService:
    serializer = ArticleSerializer

    @classmethod
    def create_article(cls, article_data, article_author_id):
        article_data = cls.serializer(data=article_data)
        article_data.is_valid(raise_exception=True)
        validated_article_data = article_data.validated_data

        article = ArticleService(article_author_id=article_author_id).create_article(validated_article_data)

        post_create_article_data = cls.serializer(instance=article)
        return post_create_article_data.data

    @classmethod
    def update_article(cls, article_data, article_id, article_author_id):
        article_data = cls.serializer(partial=True, data=article_data)
        article_data.is_valid(raise_exception=True)
        validated_article_data = article_data.validated_data

        article = ArticleService(article_author_id=article_author_id).update_article(validated_article_data, article_id)

        post_update_article_data = cls.serializer(instance=article)
        return post_update_article_data.data

    @classmethod
    def delete_article(cls, article_id, article_author_id):
        is_article_deleted = ArticleService(article_author_id=article_author_id).delete_article(article_id)
        return is_article_deleted

    @classmethod
    def get_articles(cls, article_author_id):
        articles = ArticleService(article_author_id=article_author_id).get_articles()
        serialized_articles = cls.serializer(articles, many=True)
        return serialized_articles.data

    @classmethod
    def get_article(cls, article_id, article_author_id):
        article = ArticleService(article_author_id=article_author_id).get_article(article_id)
        serialized_articles = cls.serializer(instance=article)
        return serialized_articles.data
