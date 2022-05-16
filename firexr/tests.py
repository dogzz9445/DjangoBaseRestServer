from urllib import response
from django.test import TestCase
from django.urls import include, path, reverse

# Create your tests here.
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework.test import APIClient

client = APIClient()
client.login(username='test', password='test')

class TransformTests(APITestCase):
    url = '/unit/transform'

    def test_get(self):
        response = client.get(self.url, format='json')
    
    def test_post(self):
        data = {
            "Type": 1,
            "Name": "name",
            "PositionX": 1,
            "PositionY": 1,
            "PositionZ": 1,
            "RotationX": 1,
            "RotationY": 1,
            "RotationZ": 1,
            "ScaleX": 1,
            "ScaleY": 1,
            "ScaleZ": 1,
            "Desc": "desc"
        }
        response = client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 301)
    
    def test_get_id(self):
        response = client.get(self.url + '/1', format='json')

    def test_put_id(self):
        data = {
            "ID": 1,
            "Type": 2,
            "Name": "patched",
            "PositionX": 2,
            "PositionY": 2,
            "PositionZ": 2,
            "RotationX": 2,
            "RotationY": 2,
            "RotationZ": 2,
            "ScaleX": 2,
            "ScaleY": 2,
            "ScaleZ": 2,
            "Desc": "desc"
        }
        response = client.put(self.url + '/1', data, format='json')
    
    def test_patch_id(self):
        data = {
            "ID": 1,
            "Type": 2,
            "Name": "patched",
            "PositionX": 2,
            "PositionY": 2,
            "PositionZ": 2,
            "RotationX": 2,
            "RotationY": 2,
            "RotationZ": 2,
            "ScaleX": 2,
            "ScaleY": 2,
            "ScaleZ": 2,
            "Desc": "desc"
        }
        response = client.patch(self.url + '/1', data, format='json')

    def test_delete_id(self):
        response = client.delete(self.url + '/1', format='json')


class InteractionPointTests(APITestCase):
    url = '/unit/interactionpoint'

    def test_get(self):
        response = client.get(self.url, format='json')
    
    def test_post(self):
        transform = TransformTests()
        transform.test_post()

        data = {
            "Facility": 1,
            "LocalTransform": 1,
            "Type": "abc",
            "Contents": "abc",
            "Desc": "abc"
        }
        response = client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 301)
    
    def test_get_id(self):
        response = client.get(self.url + '/1', format='json')

    def test_put_id(self):
        data = {
            "Facility": 1,
            "LocalTransform": 1,
            "Type": "abcd",
            "Contents": "abcd",
            "Desc": "abcd"
        }
        response = client.put(self.url + '/1', data, format='json')
    
    def test_patch_id(self):
        data = {
            "Facility": 1,
            "LocalTransform": 1,
            "Type": "abce",
            "Contents": "abce",
            "Desc": "abce"
        }
        response = client.patch(self.url + '/1', data, format='json')

    def test_delete_id(self):
        response = client.delete(self.url + '/1', format='json')
    
class CutSceneTests(APITestCase):
    url = '/unit/cutscene'

    def test_get(self):
        response = client.get(self.url, format='json')
    
    def test_post(self):
        transform = TransformTests()
        transform.test_post()

        data = {
            "Type": "1",
            "FileName": "1",
            "Desc": "1"
        }
        response = client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 301)
    
    def test_get_id(self):
        response = client.get(self.url + '/1', format='json')

    def test_put_id(self):
        data = {
            "Type": "1",
            "FileName": "1",
            "Desc": "1"
        }
        response = client.put(self.url + '/1', data, format='json')
    
    def test_patch_id(self):
        data = {
            "Type": "1",
            "FileName": "1",
            "Desc": "1"
        }
        response = client.patch(self.url + '/1', data, format='json')

    def test_delete_id(self):
        response = client.delete(self.url + '/1', format='json')
    
class ObjectInfoTests(APITestCase):
    url = '/unit/cutscene'

    def test_get(self):
        response = client.get(self.url, format='json')
    
    def test_post(self):
        transform = TransformTests()
        transform.test_post()

        data = {
            "ActivateObjects": [1, 2],
            "DeactivateObjects": [1, 2],
            "Name": "abc",
            "Facility": 1,
            "Type": "abc",
            "FileName": "abca",
            "ActivatedEventDelay": 1,
            "Desc": "abc"
        }
        response = client.post(self.url, data, format='json')

        data = {
            "ID": 100,
            "ActivateObjects": [1000],
            "DeactivateObjects": [10000],
            "Name": "abc",
            "Facility": 1,
            "Type": "abc",
            "FileName": "abca",
            "ActivatedEventDelay": 1,
            "Desc": "abc"
        }
        response = client.post(self.url, data, format='json')

        listdata = [{
            "ActivateObjects": [2],
            "DeactivateObjects": [],
            "Name": "ㅠ",
            "Facility": 1,
            "Type": "ㅠ",
            "FileName": "ㅠ",
            "ActivatedEventDelay": 1,
            "Desc": "ㅁ"
        },
        {
            "ActivateObjects": [1],
            "DeactivateObjects": [],
            "Name": "ㅁ",
            "Facility": 1,
            "Type": "ㅁ",
            "FileName": "ㅁ",
            "ActivatedEventDelay": 1,
            "Desc": "ㅁ"
        }]
        response = client.post(self.url, listdata, format='json')
        self.assertEqual(response.status_code, 301)
    
    def test_get_id(self):
        response = client.get(self.url + '/1', format='json')

    def test_put_id(self):
        data = {
            "ActivateObjects": [1, 2],
            "DeactivateObjects": [1, 2],
            "Name": "abc",
            "Facility": 1,
            "Type": "abc",
            "FileName": "abca",
            "ActivatedEventDelay": 1,
            "Desc": "abc"
        }
        response = client.put(self.url + '/1', data, format='json')
    
    def test_patch_id(self):
        data = {
            "ActivateObjects": [1, 2],
            "DeactivateObjects": [1, 2],
            "Name": "abc",
            "Facility": 1,
            "Type": "abc",
            "FileName": "abca",
            "ActivatedEventDelay": 1,
            "Desc": "abc"
        }
        response = client.patch(self.url + '/1', data, format='json')

    def test_delete_id(self):
        response = client.delete(self.url + '/1', format='json')
