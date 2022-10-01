from django.test import TestCase
from Acceso.forms import UserRegisterForm

# Test 1: Ver correspondiente archivo tests.py dentro de app 'ChatMundial'.
# Test 2: Ver correspondiente archivo tests.py dentro de app 'AppMundial'.

class UserCreationFormTest(TestCase):
    # Test 3: Ver si toma como válido el formulario de registro
    def test_form(self):
        data = {
            'last_name': 'Ronaldo',
            'first_name': 'Cristiano',
            'username': 'cronaldo7',
            'email':'cronaldo7@example.com',
            'password1': 'Portugal123',
            'password2': 'Portugal123',
        }

        form = UserRegisterForm(data)

        self.assertTrue(form.is_valid())