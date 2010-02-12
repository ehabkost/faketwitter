import unittest

import faketwitter.server

class TestStatusPost(unittest.TestCase):
    def setUp(self):
        self.srv = faketwitter.server.TwitterServer()

    def testSimplePost(self):
        self.srv.new_status(user='joe', text='hello, fake world!')
        tl = self.srv.public_timeline(1)
        self.assertEquals(len(tl), 1)

        post = tl[0]
        self.assertEquals(post.user.screen_name, 'joe')
        self.assertEquals(post.text, 'hello, fake world!')
