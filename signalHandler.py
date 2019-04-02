import signal

class signalHandler():
    def __init__(self):
        self.stop = False
        signal.signal(signal.SIGINT, self.handle)
        signal.signal(signal.SIGTERM, self.handle)

    def handle(self, signal, frame):
        self.stop = True
