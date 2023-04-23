from rest_framework.test import APITestCase
from rest_framework import status
from ..factories.article import ArticleFactory
from rest_framework.reverse import reverse


class ArticleViewTests(APITestCase):
    def setUp(self):
        self.article = ArticleFactory.create(title='Test title', content='content of Author')
        self.client.force_authenticate(user=self.article.author)

    def test_get_all_articles(self):
        response = self.client.get(reverse('article_create_list_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.article.title)
        self.assertEqual(response.data[0]['content'], self.article.content)

    def test_get_single_article(self):
        response = self.client.get(reverse('article_detail_update_delete_view', args=[self.article.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.article.title)
        self.assertEqual(response.data['content'], self.article.content)

    def test_get_non_existing_article(self):
        response = self.client.get(reverse('article_detail_update_delete_view', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_article(self):
        data = {'title': 'New title', 'content': 'New Content'}
        response = self.client.post(reverse('article_create_list_view'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])

    def test_update_article(self):
        data = {'title': 'Updated title', 'content': 'Updated Author content'}
        response = self.client.put(reverse('article_detail_update_delete_view', args=[self.article.id]),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])

    def test_delete_article(self):
        response = self.client.delete(reverse('article_detail_update_delete_view', args=[self.article.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
