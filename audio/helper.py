from threading import Lock

class ProtectedList(object):
    def __init__(self, buffer_size=8):
        self.elements = []
        self.buffer_size = buffer_size
        self.lock = Lock()

    def put(self, element):
        self.lock.acquire()

        self.elements.append(element)
        if len(self.elements) > self.buffer_size:
            self.elements.pop(0)

        self.lock.release()
    
    def get(self):
        self.lock.acquire()

        if len(self.elements) > 0:
            element = self.elements[0]
            del self.elements[0]
        
        else:
            element = None

        self.lock.release()
        return element
    
    def __repr__(self):
        self.lock.acquire()

        string = str(self.elements)

        self.lock.release()
        return string