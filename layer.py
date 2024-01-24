#creating layer class

class Layer(object):
    def __init__(self) -> None:
        self.input = None
        self.output = None

    def forward(self, input):
        #TODO: reurn output
        pass

    def backward(self, output_gradient, learning_rate):
        #
        pass