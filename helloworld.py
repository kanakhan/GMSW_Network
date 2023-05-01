import math

class people:
    age = math.sin(40)
    name = '사람'
    def walk(self):
        print('%s이 걷고 있습니다' %self.name)



import keyword

Lee = people()

print(5%2)
print(keyword.kwlist)

c = {'age':30, 'name': '아잉'}

print(c['age']>19)

if(c['age']>19):
    print('%s님은 현재 성인입니다.' %c['name'])


a = [1,2,3,4,5]
b = [x * 2 for x in a]
c = [x * 2 for x in b]

print(c)