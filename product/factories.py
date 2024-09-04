import factory
import factory.fuzzy

from product.models import Product
from product.models import Category



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker('word') # Gera uma palavra aleatória como título
    description = factory.Faker('sentence', nb_words=20) # Corrigido: Gera uma frase de 20 palavras
    active = factory.Iterator([True, False]) # Alterna entre True e False



class ProductFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = Product

    title = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=22) # Corrigido: Gera uma frase de 20 palavras
    price = factory.fuzzy.FuzzyInteger(low=10, high=1000)
    
    
    @factory.post_generation
    def categories(self,create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for category in extracted:
                self.categories.add(category)
        else: 
            # a
            category = CategoryFactory()
            self.categories.add(category)
    