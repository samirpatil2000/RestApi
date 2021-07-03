from django.test import SimpleTestCase, TestCase, Client
from api.models import Text
from api.views import createView,list_view,textDetail
from django.urls import reverse

import json
import random
class TestView(TestCase):
    #use as a constructor
    def setUp(self) -> None:
        self.client=Client()
        self.home_url=reverse('home')
        slug_="text"+str(random.randint(99,9999))
        self.detail_url=reverse('detail',args=[slug_])
        self.create_url=reverse('create_view')
        textTest1=Text.objects.create(
            slug=slug_,
            name="Test1",
            num=2,
        )

    def test_list_views(self):

        response=self.client.get(self.home_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')

    def test_text_detail(self):

        response=self.client.get(self.detail_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')


    def test_text_create(self):
        data={
            "num":20,
            "name":'test2',
            "slug":'test1slug'+str(random.randint(99,999))
        }
        response=self.client.post(self.create_url,data=data)
        self.assertEquals(response.status_code,200)
        print(response)

        self.assertIn(data['slug'], response.content.decode())
        print(data['slug'],"88888888888888888888888888")
        print(Text.objects.get(slug=data["slug"]))

        # self.detail_url=reverse('detail',data['slug'])
        #
        # response_detailView = self.client.get(self.detail_url)
        # self.assertEqual(response_detailView.status_code, 200)
        # self.assertTemplateUsed(response_detailView,'index.html')






