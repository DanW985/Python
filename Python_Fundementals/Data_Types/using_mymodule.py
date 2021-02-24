import mymodule

#print(myfunction()) #error"
print(mymodule.myfunction()) #scoped variant

from mymodule import myfunction #descoped variant

print(myfunction())