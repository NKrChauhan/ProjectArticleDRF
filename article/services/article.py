from django.shortcuts import get_object_or_404

from ..models.article import Article


class ArticleService:
    def __init__(self, article_author_id):
        self.article_author_id = article_author_id

    def create_article(self, article_data):
        article = Article.objects.create(author_id=self.article_author_id, **article_data)
        return article

    def update_article(self, article_data, article_id):
        article = Article.objects.filter(author_id=self.article_author_id, pk=article_id)
        article.update(**article_data)
        return article.first()

    def delete_article(self, article_id):
        article = Article.objects.get(author_id=self.article_author_id, pk=article_id)
        article.delete()
        return True

    def get_articles(self):
        articles = Article.objects.filter(author_id=self.article_author_id)
        return articles

    def get_article(self, article_id):
        article = get_object_or_404(Article, author_id=self.article_author_id, pk=article_id)
        return article
