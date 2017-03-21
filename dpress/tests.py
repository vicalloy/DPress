# -*- coding: UTF-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

class ViewsBaseCase(TestCase):

    fixtures = ['test_dpress_users.json', 
            'test_dpress_posts.json']

class ViewsSimpleTest(ViewsBaseCase):

    def test_index(self):
        resp = self.client.get(reverse('dpress_index'))
        self.assertEqual(resp.status_code, 200)

    def test_archive(self):
        resp = self.client.get(reverse('dpress_month_archive', args=("2012", "8", )))
        self.assertEqual(resp.status_code, 200)

    def test_category(self):
        resp = self.client.get(reverse('dpress_category', args=("default", )))
        self.assertEqual(resp.status_code, 200)

    def test_tag(self):
        resp = self.client.get(reverse('dpress_tag', args=("testtag", )))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('dpress_tag', args=("notag", )))
        self.assertEqual(resp.status_code, 404)

    def test_post(self):
        resp = self.client.get(reverse('dpress_post', args=("2012", "08", "dpress")))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('dpress_post', args=("2012", "08", "noslug")))
        self.assertEqual(resp.status_code, 404)

    def test_feed(self):
        resp = self.client.get(reverse('dpress_feeds'))
        self.assertEqual(resp.status_code, 200)
