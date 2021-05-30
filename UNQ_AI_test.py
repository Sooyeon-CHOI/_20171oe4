class Tensor:

    def __init__(self,data,shape):
        self.data = data
        self.shape = shape

    def shape_data(self) :
        #calculate size of shape
        multi = 1
        for i in range(len(self.shape)):
            multi *= self.shape[i]

        # padding
        if len(self.data) < multi:
            for i in range(multi - len(self.data)):
                self.data.append(0)
        elif len(self.data) > multi:
            self.data = self.data[:multi]

        #resize
        result = self.data
        for s in reversed(self.shape):
            tmp = []
            for i in range(len(result) // s):
                tmp.append(result[i * s:(i + 1) * s])
            result = tmp
        return result[0]

data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape0 = [2, 3, 2]
tensor0 = Tensor(data0, shape0)

data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape1 = [5, 2]
tensor1 = Tensor(data1, shape1)

print(tensor0.shape_data())
print(tensor1.shape_data())

