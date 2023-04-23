import factory

from user.tests.factories.user import UserFactory
from ...models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence')
    content = factory.Faker('date_this_century')
    banner = factory.django.ImageField(
        filename='test_image.jpg',
        color='blue',
        width=800,
        height=600,
        format='JPEG'
    )
    author = factory.SubFactory(UserFactory)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default _create method to manually handle FileField creation."""
        image_file = kwargs.pop('banner', None)
        obj = super()._create(model_class, *args, **kwargs)
        if image_file:
            obj.banner.save(image_file.name, image_file, save=False)
        return obj
