l1 = []

#1a)
def create_list():
    for i in range(5):
        l1.append(input())

def remdup():
    return list(set(l1))

create_list()
print(remdup())

print([ i for i in range(28) if i%2 == 0])

l3 = ["This","is","XYZ","Here"]
print(l3[::-1])