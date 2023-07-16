from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note






class NoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def setUp(self):
        self.note = Note.objects.create(user=self.user, body='Test note')

    def test_str_method(self):
        expected_str = 'Test note'

        self.assertEqual(str(self.note), expected_str)

    def test_user_field(self):
        self.assertEqual(self.note.user, self.user)

    def test_body_field(self):
        # Проверяем, что поле 'body' содержит ожидаемое значение
        expected_body = 'Test note'
        self.assertEqual(self.note.body, expected_body)

    def test_updated_field_auto_now(self):
        # Проверяем, что поле 'updated' автоматически обновляется при изменении заметки
        previous_updated = self.note.updated
        self.note.body = 'Updated note'
        self.note.save()
        self.assertNotEqual(self.note.updated, previous_updated)

    def test_created_field_auto_now_add(self):
        # Проверяем, что поле 'created' автоматически устанавливается при создании заметки
        self.assertIsNotNone(self.note.created)