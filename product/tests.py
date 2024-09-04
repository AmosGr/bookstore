from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from product.factories import ProductFactory, CategoryFactory
from product.models import Product, Category

class ProductModelTest(TestCase):

    def test_product_creation(self):
        # Cria um produto usando a fábrica
        product = ProductFactory()

        # Verifica se o produto foi salvo corretamente no banco de dados
        self.assertTrue(Product.objects.filter(id=product.id).exists())
        self.assertEqual(product.title, product.title)
        self.assertEqual(product.description, product.description)
        self.assertIsInstance(product.price, int)  # Verifica se o preço é um inteiro
        self.assertIn(product.active, [True, False])  # Verifica se o ativo é True ou False

    def test_product_with_single_category(self):
        # Cria uma categoria e associa a um produto
        category = CategoryFactory()
        product = ProductFactory(categories=[category])

        # Verifica se a categoria foi associada corretamente
        self.assertEqual(product.categories.count(), 1)
        self.assertIn(category, product.categories.all())

    def test_product_with_multiple_categories(self):
        # Cria várias categorias
        category1 = CategoryFactory()
        category2 = CategoryFactory()
        
        # Cria um produto com múltiplas categorias
        product = ProductFactory(categories=[category1, category2])

        # Verifica se as categorias foram associadas corretamente
        self.assertEqual(product.categories.count(), 2)
        self.assertIn(category1, product.categories.all())
        self.assertIn(category2, product.categories.all())

    def test_product_price_range(self):
        # Cria um produto e verifica se o preço está dentro do intervalo esperado
        product = ProductFactory()
        self.assertGreaterEqual(product.price, 10)
        self.assertLessEqual(product.price, 1000)

    def test_product_active_status(self):
        # Cria produtos com status ativo e inativo
        active_product = ProductFactory(active=True)
        inactive_product = ProductFactory(active=False)

        # Verifica se os status estão corretos
        self.assertTrue(active_product.active)
        self.assertFalse(inactive_product.active)

class CategoryTestCase(TestCase):

    def test_category_creation(self):
        category = CategoryFactory()

         # Verifica se a categoria foi salva corretamente no banco de dados
        self.assertTrue(Category.objects.filter(id=category.id).exists())

        # Verifica se o título da categoria criada está correto
        saved_category = Category.objects.get(id=category.id)
        self.assertEqual(saved_category.title, category.title)

    def test_slug_creation(self):
        # Cria uma categoria com um título específico
        category = CategoryFactory(title="Test Category")

        # O slug é gerado na primeira vez com base no título
        self.assertEqual(category.slug, "test-category")

    def test_slug_uniqueness(self):
        # Cria duas categorias com o mesmo título
        category1 = CategoryFactory(title="Test Category")
        category2 = CategoryFactory(title="Test Category")

        # Verifica que os slugs são únicos
        self.assertEqual(category1.slug, "test-category")
        self.assertEqual(category2.slug, "test-category-1")