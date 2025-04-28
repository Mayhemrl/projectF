import unittest
from app import app  # Убедитесь, что файл app.py находится в той же директории

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Добро пожаловать в наш интернет-магазин!', response.data.decode('utf-8'))

    def test_add_to_cart(self):
        response = self.app.post('/add_to_cart', data={'product': 'Товар 1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Товар 1', response.data.decode('utf-8'))

    def test_view_cart_empty(self):
        response = self.app.get('/view_cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Корзина пуста.', response.data.decode('utf-8'))

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Описание кода', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()