from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import Customer ,  orders




class HomePageTest(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get('/')
        view = Customer ()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('environment', context)

class ordersPageTest(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get('/')
        view =  orders()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('environment', context)        