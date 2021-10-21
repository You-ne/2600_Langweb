# Version remise aux étudiants
import random

### 

class AddExpr:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.result = 0

    def __repr__(self) -> str:
        return repr(self.lhs) + ' + ' + repr(self.rhs)

    def throw(self) -> int:
        if self.result == 0:
            a = self.lhs.throw()
            b = self.rhs.throw()
            self.result = a + b
        return self.result

class Pool:
    def __init__(self, op):
        self.op = op

    def throw(self):
        return self.op.throw()

    def __add__(self, rhs):
        if type(rhs) is int:
            rhs = FrozenDice(rhs)
        return Pool(AddExpr(self, rhs))

    def __repr__(self) -> str:
        return repr(self.op)

class AbstractResult(Pool):
    min = 1
    max = 1
    def __init__(self):
        self.result = 0

    def __repr__(self):
        return type(self).__name__

    def throw(self):
        if self.result == 0:
            self.result = random.randint(type(self).min, type(self).max)
        return self.result

    def seed(s):
        random.seed(s)

class FrozenDice(AbstractResult):
    def __init__(self, v):
        self.result = v
        self.min = v
        self.max = v

    def __repr__(self):
        return str(self.result)

    def throw(self):
        return self.result

####

class D4(AbstractResult):
        max=4

d4 = D4()
