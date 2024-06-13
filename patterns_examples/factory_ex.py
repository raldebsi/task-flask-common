class Math:
    def sum(self, *args):
        return sum(*args)
    
    def avg(self, *args):
        return sum(*args)/len(args)
    
    def min(self, *args):
        return min(*args)
    
    def max(self, *args):
        return max(*args)
    
class MathSumAverageFactory:
    def __init__(self):
        pass

    def __new__(cls) -> "MathSumAverage":
        return MathSumAverage()
    
class MathSumAverageFactory:
    def __init__(self):
        self.obj = MathSumAverage()

    def get(self):
        return self.obj

class MathSumAverage:
    def __init__(self):
        self.obj = Math()

    def process(self, arg):
        return self.obj.sum(arg) + self.obj.avg(arg)

class MathSumMin:
    def __init__(self):
        self.obj = Math()

    def process(self):
        ...