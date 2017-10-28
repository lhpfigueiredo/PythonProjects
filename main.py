import numpy as np

DEBUG = 0

def simpleFunction(weightedInputs:list):
    result = 0

    for i in weightedInputs:
        result += i

    return result


class neuron():

    id = -1
    gain =[]
    transferFuntion = None

    n = 0

    @classmethod
    def name(cls):
        n = cls.n
        cls.n += 1
        return n


    def __init__(self, transferFunction):
        self.name = self.name()
        print("Sou ", self.name) if DEBUG == 1 else None
        self.transferFuntion = transferFunction

    def adjustGain(self, gain:list):
        print("Ajustando Ganhos: ", gain) if DEBUG == 1 else None
        self.gain = gain


    def execute(self, inputs:list)->int:
        print("inputs: ", inputs) if DEBUG == 1 else None
        weightedInputs = np.multiply(inputs, self.gain)
        print("weightedInputs: ", weightedInputs) if DEBUG == 1 else None
        y = self.transferFuntion(weightedInputs)
        print("Out", self.name, ": ", y)
        return y


class machine():

    transferFunction = None

    nNeurouns = -1
    neuronsList = []

    nLayers = -1
    layersList = []

    def __init__(self, transferFunction, neuronsNumber):
        self.transferFunction = transferFunction
        self.nNeurouns = neuronsNumber

    def create(self):
        for i in range(0, self.nNeurouns):
            self.neuronsList.append(neuron(self.transferFunction))

    def adjust(self, gain:list):
        for neuron in self.neuronsList:
            neuron.adjustGain(gain)

    def calculate(self, inputs:list):
        result = 0
        for neuron in self.neuronsList:
            result += neuron.execute(inputs)
        return result

    def execute(self, inputs:list):
        self.create()

        gain = [1, 2, 3]

        self.adjust(gain)
        print("Machine :", self.calculate(inputs))

        pass


def main():

    m = machine(simpleFunction, 2)
    m.execute([3,2,1])


    #n1 = neuron(simpleFunction)
    #n1.adjustGain([1,2,3])
    #y = n1.execute([1,1,1])


main()
