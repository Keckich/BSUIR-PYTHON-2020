class Vector:
    def __init__(self, *args):
        self.vector = list(args)

    def get(self):
        return self.vector

    def __add__(self, vector2):
        if len(self.vector) == len(vector2):
            res_vector = Vector()
            for i in range(len(vector2)):
                res_vector.vector.append(self.vector[i] + vector2[i])
            return res_vector
        else:
            return 'ERROR: Vectors of different sizes'

    def __sub__(self, vector2):
        if len(self.vector) == len(vector2):
            res_vector = Vector()
            for i in range(len(vector2)):
                res_vector.vector.append(self.vector[i] - vector2[i])
            return res_vector
        else:
            return 'ERROR: Vectors of different sizes'

    def __mul__(self, vector2):
        res_vector = Vector()
        if type(vector2) is int or type(vector2) is float:
            for i in range(len(self.vector)):
                res_vector.vector.append(self.vector[i] * vector2)
            return res_vector
        if len(self.vector) == len(vector2):
            for i in range(len(self.vector)):
                res_vector.vector.append(self.vector[i] * vector2[i])
            return res_vector
        else:
            return 'ERROR: Vectors of different sizes'

    def __eq__(self, vector2):
        if len(self.vector) == len(vector2):
            i = 0
            while self.vector[i] == vector2[i]:
                i += 1
                if i == len(vector2):
                    return True
            return False
        else:
            return False

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, item):
        return self.vector[item]

    def __str__(self):
        string = ''
        for obj in self.vector:
            string += str(obj) + ', '
        string = string[:-2]
        return string


