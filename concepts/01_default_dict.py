from collections import defaultdict

def func():
    return 'geeks'

my_dict=defaultdict(func)
print(my_dict.keys())
my_dict['name']='Suhail'
my_dict['age']='40'
print(my_dict.keys())
print(my_dict['hobbies'])
print(my_dict)

#using list as default factory

d=defaultdict(list)
d['names']=['rohan','ali']
d['age']=[24,31]
print(d)
print(d['class'])
print(d.items())

#using int as default factory
d=defaultdict(int)
d['scores']+=1
d['scores']+=1
print(d)
print(d['names'])

#using int as default factory
d=defaultdict(float)
d['mean']=3.5
d['median']+=2.34
print(d)
print(d['mode'])