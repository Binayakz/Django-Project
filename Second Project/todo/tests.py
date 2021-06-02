from django.test import TestCase
from django.urls import reverse, resolve
from todo.views import index
from .models import Todo


# Create your tests here.
class BaseTest(TestCase):

    def setUp(self):
        
        self.index_url = reverse('index')

        Todo.objects.create(tasks="Learn coding")
        Todo.objects.create(tasks="Drink water")

        return super().setUp()

    def test_todo_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_can_access_index_page(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/index.html')

    def test_add_task(self):

        object1 = Todo.objects.get(pk=1)
        object2 = Todo.objects.get(pk=2)
        self.assertEqual(object1.tasks, "Learn coding")
        self.assertEqual(object2.tasks, "Drink water")

    def test_update_task(self):

        Todo.objects.update(tasks="Focus on testing")

        object1 = Todo.objects.get(pk=1)
        self.assertEqual(object1.tasks, "Focus on testing")

    # def test_delete_task(self):
    #
    #     Todo.objects.filter(pk=1).delete()
    #
    #     object1 = Todo.objects.get(pk=1)
    #     self.assertEqual(object1.tasks, 404)
