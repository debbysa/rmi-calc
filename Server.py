import Pyro4

daemon = Pyro4.Daemon(host='localhost', port=8000)
@Pyro4.expose
class Calculator(object):

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def cek(self, x, y):
        if x > y:
            return '{} lebih besar dari {}'.format(x, y)
        return '{1} lebih besar dari {0}'.format(x, y)


uri = daemon.register(Calculator)

# print the uri so we can use it in the client later
print("Ready. Object uri =", uri)
daemon.requestLoop()