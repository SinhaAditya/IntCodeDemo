class IntCode(object):

    position = 0

    def step(self):
        self.position = self.position + 4
