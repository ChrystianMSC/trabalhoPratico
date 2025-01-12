from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ExampleModel, Color

# Create your tests here.

class ExampleModelTests(APITestCase):
    def setUp(self):
        ExampleModel.objects.create(name='Example 1')
        ExampleModel.objects.create(name='Example 2')

    def test_example_list_status_code(self):
        response = self.client.get('/api/example/')
        self.assertEqual(response.status_code, 200)

    def test_example_list_length(self):
        response = self.client.get('/api/example/')
        self.assertEqual(len(response.data), 2)

    def test_example_model_creation_name(self):
        example = ExampleModel.objects.create(name='Example 3')
        self.assertEqual(example.name, 'Example 3')

    def test_example_model_creation_instance(self):
        example = ExampleModel.objects.create(name='Example 3')
        self.assertTrue(isinstance(example, ExampleModel))

    def test_example_model_name(self):
        example = ExampleModel.objects.get(name='Example 1')
        self.assertEqual(example.name, 'Example 1')

    def test_example_model_count(self):
        count = ExampleModel.objects.count()
        self.assertEqual(count, 2)

    def test_example_model_update(self):
        example = ExampleModel.objects.get(name='Example 1')
        example.name = 'Updated Example'
        example.save()
        updated_example = ExampleModel.objects.get(id=example.id)
        self.assertEqual(updated_example.name, 'Updated Example')

    def test_example_model_delete(self):
        example = ExampleModel.objects.get(name='Example 2')
        example.delete()
        with self.assertRaises(ExampleModel.DoesNotExist):
            ExampleModel.objects.get(name='Example 2')


class ColorTests(APITestCase):
    def setUp(self):
        Color.objects.create(color='#FF5733')
        Color.objects.create(color='#33FF57')

    def test_color_list_status_code(self):
        response = self.client.get('/api/colors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_color_list_length(self):
        response = self.client.get('/api/colors/')
        self.assertEqual(len(response.data), 2)

    def test_color_create_status_code(self):
        data = {'color': '#5733FF'}
        response = self.client.post('/api/colors/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_color_create_count(self):
        data = {'color': '#5733FF'}
        response = self.client.post('/api/colors/', data, format='json')
        self.assertEqual(Color.objects.count(), 3)

    def test_color_create_color(self):
        data = {'color': '#5733FF'}
        response = self.client.post('/api/colors/', data, format='json')
        self.assertEqual(Color.objects.last().color, '#5733FF')

    def test_color_create_invalid(self):
        data = {'color': 'invalid-color'}
        response = self.client.post('/api/colors/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SystemIntegrationTests(APITestCase):
    def test_create_and_retrieve_color_create_status_code(self):
        create_data = {'color': '#123456'}
        create_response = self.client.post('/api/colors/', create_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

    def test_create_and_retrieve_color_list_status_code(self):
        create_data = {'color': '#123456'}
        create_response = self.client.post('/api/colors/', create_data, format='json')
        list_response = self.client.get('/api/colors/')
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)

    def test_create_and_retrieve_color_list_length(self):
        create_data = {'color': '#123456'}
        create_response = self.client.post('/api/colors/', create_data, format='json')
        list_response = self.client.get('/api/colors/')
        self.assertEqual(len(list_response.data), 1)

    def test_create_and_retrieve_color_list_color(self):
        create_data = {'color': '#123456'}
        create_response = self.client.post('/api/colors/', create_data, format='json')
        list_response = self.client.get('/api/colors/')
        self.assertEqual(list_response.data[0]['color'], '#123456')

    def test_retrieve_empty_example_list(self):
        response = self.client.get('/api/example/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_invalid_color_creation(self):
        invalid_data = {'color': 'invalid'}
        response = self.client.post('/api/colors/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_color_creation_count(self):
        invalid_data = {'color': 'invalid'}
        response = self.client.post('/api/colors/', invalid_data, format='json')
        self.assertEqual(Color.objects.count(), 0)

    def test_create_and_retrieve_example_model_list_status_code(self):
        create_data = {'name': 'Test Example'}
        create_response = self.client.post('/api/example/', create_data, format='json')
        list_response = self.client.get('/api/example/')
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)


    def test_interaction_between_models_create_status_code(self):
        color_data = {'color': '#654321'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        self.assertEqual(color_response.status_code, status.HTTP_201_CREATED)

    def test_interaction_between_models_example_list_status_code(self):
        color_data = {'color': '#654321'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        example_response = self.client.get('/api/example/')
        self.assertEqual(example_response.status_code, status.HTTP_200_OK)

    def test_interaction_between_models_example_list_length(self):
        color_data = {'color': '#654321'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        example_response = self.client.get('/api/example/')
        self.assertEqual(len(example_response.data), 0)

    def test_interaction_between_models_color_list_status_code(self):
        color_data = {'color': '#654321'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        color_list_response = self.client.get('/api/colors/')
        self.assertEqual(color_list_response.status_code, status.HTTP_200_OK)

    def test_interaction_between_models_color_list_length(self):
        color_data = {'color': '#654321'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        color_list_response = self.client.get('/api/colors/')
        self.assertEqual(len(color_list_response.data), 1)

    def test_interaction_between_models_color_list_color(self):
        color_data = {'color': '#654321'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        color_list_response = self.client.get('/api/colors/')
        self.assertEqual(color_list_response.data[0]['color'], '#654321')

    def test_create_and_retrieve_multiple_colors(self):
        colors_data = [
            {'color': '#FF0000'},
            {'color': '#00FF00'},
            {'color': '#0000FF'}
        ]
        for color_data in colors_data:
            self.client.post('/api/colors/', color_data, format='json')

        response = self.client.get('/api/colors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_and_retrieve_multiple_colors_length(self):
        colors_data = [
            {'color': '#FF0000'},
            {'color': '#00FF00'},
            {'color': '#0000FF'}
        ]
        for color_data in colors_data:
            self.client.post('/api/colors/', color_data, format='json')

        response = self.client.get('/api/colors/')
        self.assertEqual(len(response.data), 3)

    def test_create_and_retrieve_multiple_colors_color(self):
        colors_data = [
            {'color': '#FF0000'},
            {'color': '#00FF00'},
            {'color': '#0000FF'}
        ]
        for color_data in colors_data:
            self.client.post('/api/colors/', color_data, format='json')

        response = self.client.get('/api/colors/')
        self.assertEqual(response.data[0]['color'], '#FF0000')
        self.assertEqual(response.data[1]['color'], '#00FF00')
        self.assertEqual(response.data[2]['color'], '#0000FF')
    
    def test_create_and_retrieve_example_with_related_color_status_code(self):
        color_data = {'color': '#56A1FF'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        example_data = {'name': 'Example with Color'}
        example_response = self.client.post('/api/example/', example_data, format='json')
        self.assertEqual(example_response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_example_with_color(self):
        example_response = self.client.get('/api/example/')
        self.assertEqual(example_response.status_code, status.HTTP_200_OK)


