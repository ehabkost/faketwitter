# the "fake twitter server"

from faketwitter import objects

class TwitterServer:
    def __init__(self):
        self._all_statuses = []

    def _new_tatus(self, st):
        self._all_statuses.append(st)
        
    def new_status(self, user, text):
        s = objects.Status()
        s.add('text', text)
        u = s.add('user')
        u.add('screen_name', user)
        self._new_tatus(s)

    def public_timeline(self, count):
        return self._all_statuses[-count:]
