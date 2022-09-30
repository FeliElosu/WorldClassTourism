import random
import string
from datetime import datetime

from django.test import TestCase
from ChatMundial.models import mensaje

class MensajeChatTestCase(TestCase):

    def test_crear_mensaje(self):
        # Test 1: Comprobar si se crea un mensaje del chat correctamente
        lista_letras_value = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_usuario = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_sala = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        value_prueba = "".join(lista_letras_value)
        date_prueba = datetime.now()
        usuario_prueba = "".join(lista_letras_usuario)
        sala_prueba = "".join(lista_letras_sala)
        mensaje_1 = mensaje.objects.create(value=value_prueba, date=date_prueba, usuario=usuario_prueba, sala=sala_prueba)

        self.assertIsNotNone(mensaje_1.id)
        self.assertEqual(mensaje_1.value, value_prueba)
        self.assertEqual(mensaje_1.date, date_prueba)
        self.assertEqual(mensaje_1.usuario, usuario_prueba)
        self.assertEqual(mensaje_1.sala, sala_prueba)
