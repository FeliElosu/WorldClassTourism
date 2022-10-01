import random
import string

from django.test import TestCase
from AppMundial.models import Posts
from django.contrib.auth.models import User

# Test 1: Ver correspondiente archivo tests.py dentro de app 'ChatMundial'.
 
class PostsTestCase(TestCase):
    # Test 2: Comprobar la creación de un post.
    def test_create_posts(self):
        lista_letras_titulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        print(lista_letras_titulo)
        lista_letras_equipo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        titulo_prueba = "".join(lista_letras_titulo)
        equipo_prueba = "".join(lista_letras_equipo )
        posteo_prueba="Esta es una prueba 1234567890 /&%#$"
        autor_prueba=User.objects.create(id=1)
        print(titulo_prueba)
        print(equipo_prueba)
        post_1 = Posts.objects.create(titulo=titulo_prueba, equipo =equipo_prueba, 
                                      autor=autor_prueba,posteo=posteo_prueba)

        self.assertIsNotNone(post_1.id)
        self.assertEqual(post_1.titulo, titulo_prueba)
        self.assertEqual(post_1.equipo, equipo_prueba)
        self.assertEqual(post_1.posteo, posteo_prueba)
        
# Test 3: Ver correspondiente archivo tests.py dentro de app 'Acceso'.