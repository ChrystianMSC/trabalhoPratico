from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ExampleModel, Color

# Create your tests here.

class ExampleModelTests(APITestCase):
    def setUp(self):
        ExampleModel.objects.create(name='Example 1')
        ExampleModel.objects.create(name='Example 2')

    def test_example_list(self):
        response = self.client.get('/api/example/')
        
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(len(response.data), 2)

class ColorTests(APITestCase):
    def setUp(self):
        Color.objects.create(color='#FF5733')
        Color.objects.create(color='#33FF57')

    def test_color_list(self):
        response = self.client.get('/api/colors/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 2)

    def test_color_create(self):
        data = {'color': '#5733FF'}
        response = self.client.post('/api/colors/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(Color.objects.count(), 3)
        self.assertEqual(Color.objects.last().color, '#5733FF')

    def test_color_create_invalid(self):
        data = {'color': 'invalid-color'}
        response = self.client.post('/api/colors/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SystemIntegrationTests(APITestCase):
    def test_create_and_retrieve_color(self):
        # Step 1: Create a new color
        create_data = {'color': '#123456'}
        create_response = self.client.post('/api/colors/', create_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        # Step 2: Retrieve the list of colors
        list_response = self.client.get('/api/colors/')
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)

        # Verify the created color is in the list
        self.assertEqual(len(list_response.data), 1)
        self.assertEqual(list_response.data[0]['color'], '#123456')
        
    def test_retrieve_empty_example_list(self):
        # Retrieve the example list
        response = self.client.get('/api/example/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the list is empty
        self.assertEqual(response.data, [])
    
    def test_invalid_color_creation(self):
        # Attempt to create a color with invalid data
        invalid_data = {'color': 'invalid'}
        response = self.client.post('/api/colors/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify that no colors are created
        self.assertEqual(Color.objects.count(), 0)

    def test_create_and_retrieve_example_model(self):
        # Step 1: Create a new example record
        create_data = {'name': 'Test Example'}
        create_response = self.client.post('/api/example/', create_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # GET-only endpoint

        # Step 2: Verify the list of examples is still empty
        list_response = self.client.get('/api/example/')
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list_response.data), 0)

    def test_interaction_between_models(self):
        # Create a new color
        color_data = {'color': '#654321'}
        color_response = self.client.post('/api/colors/', color_data, format='json')
        self.assertEqual(color_response.status_code, status.HTTP_201_CREATED)

        # Retrieve the example list
        example_response = self.client.get('/api/example/')
        self.assertEqual(example_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(example_response.data), 0)

        # Verify the color list is unaffected
        color_list_response = self.client.get('/api/colors/')
        self.assertEqual(color_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(color_list_response.data), 1)
        self.assertEqual(color_list_response.data[0]['color'], '#654321')
