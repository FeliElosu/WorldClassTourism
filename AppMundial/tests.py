import random
import string

from django.test import TestCase
from AppMundial.models import Posts

 # Test 1: Comprobar la creación de un post.
class PostsTestCase(TestCase):
    
    def test_create_posts(self):
        lista_letras_titulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        print(lista_letras_titulo)
        lista_letras_equipo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        titulo_prueba = "".join(lista_letras_titulo)
        equipo_prueba = "".join(lista_letras_equipo )
        print(titulo_prueba)
        print(equipo_prueba)
        post_1 = Posts.objects.create(titulo=titulo_prueba, equipo =equipo_prueba)

        self.assertIsNotNone(post_1.id)
        self.assertEqual(post_1.titulo, titulo_prueba)
        self.assertEqual(post_1.titulo, equipo_prueba)