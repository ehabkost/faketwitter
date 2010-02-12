# the "fake twitter server"

from faketwitter import objects

class TwitterServer:
    def __init__(self):
        self._all_statuses = []
        self._cur_time = 0

    def cur_time(self):
        return self._cur_time

    def set_time(self, t):
        self._cur_time = t

    def advance_time(self, delta):
        self._cur_time += delta

    def _new_status(self, st):
        self._all_statuses.append(st)

    def new_status(self, user, text):
        s = objects.Status()

        #FIXME: use formatted time
        s.add('created_at', str(self.cur_time()))
        s.add('text', text)
        u = s.add('user')
        u.add('screen_name', user)

        self._new_status(s)

    def public_timeline(self, count):
        return self._all_statuses[-count:]
