from django.test import SimpleTestCase
from django.urls import reverse,resolve
from api.views import list_view,textDetail,createView

class TestUrl(SimpleTestCase):

    def test_url_list_view(self):
        url=reverse('home')
        # print(resolve(url))
        self.assertEqual(resolve(url).func,list_view)

    def test_url_detail_view(self):
        url=reverse('detail',args=['samir1'])
        self.assertEqual(resolve(url).func,textDetail)
    #
    def test_url_create_view(self):
        url=reverse('create_view')
        # print(url)
        self.assertEqual(resolve(url).func,createView)