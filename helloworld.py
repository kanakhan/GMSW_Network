import math

class people:
    age = math.sin(40)
    name = '사람'
    def walk(self):
        print('%s이 걷고 있습니다' %self.name)


Lee = people()

Lee.walk()
Lee.name = str(input())
Lee.walk()
