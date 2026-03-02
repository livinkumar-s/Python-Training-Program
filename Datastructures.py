# a="hello guys!!!!"
# print(a[-2])

# print(a[6:]) #"guys!!!!"
# print(a[:6]) #"hello "
# print(a[2:7]) 
# print(a[::-1])

# List 
# lis1=[1,2,3,4,"Hello","Hi",True,False,22,33,33,[22,33,44]]
# print(len(lis1))
# print(lis1[5])
# print(lis1[3:7]) #[]
# print(lis1[0:7:2]) 

# lis1.append(2)
# lis1[3]+=2

# print(lis1)

# lis2.append([3,4,5])
# lis2.append("Hello")
# lis2.extend([5,6,7,8])

# lis2.append(2)
# lis2.extend(2)
lis2=[213,234,234,234,3,5,234]
# names=["Rohit","Virat","Dhoni","Rohit","Rohit"]

# lis2.insert(4,"Hello")
# lis2.remove(234)
# lis2.pop(3)
# lis2.pop()
# lis2.clear()
# lis2.sort()
# lis2.reverse()
# print(lis2)
# print(lis2[::-1])

# Tuple 

tup1=(1,2,3,4,3,2,1,"Hello","Hi")
# tup1[3]=44
# print(tup1.index("Hello world"))
# print(tup1[3])
# print(tup1.count(2))

# tup2=1,2,3
# print(tup2)

# person1="vijay",51,"GOAT",68

# name=person1[0]
# age=person1[1]

# name,age,lastMovie,noOfMovies=person1

# print(age)

# Set 

# set1={1, 2, 3, 5, 6, 7, 8, 10}
# set2={7,8,9,10,11,12,13}

# print(set1[2])
# set1.add(10)
# set1.remove(8)
# set1.clear()

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))

# for i in set1:
#     print(i)


# Dict 

studentDetail={
    "name":"Prem",
    "class":12,
    "allClear":True
}

# print(studentDetail["name"])
# studentDetail["class"]=11
# studentDetail["mark"]=498

# print(studentDetail.keys())
# print(studentDetail.values())
# studentDetail.pop("allClear")
# print(studentDetail)

# for i in studentDetail:
#     print(studentDetail[i])

# personDetail={
#     "name":"Vijay",
#     "age":51,
#     "lastMovie":"Beast",
#     "noOfMovies":68,
#     "favMovies":[
#         "Master",
#         "Mersal",
#         "Bigil",
#         "Sarkar"
#     ],
#     "lastmovieDetail":{
#         "name":"Beast",
#         "director":"Nelson",
#         "releaseDate":"13th April 2022"
#     }
# }
# print(personDetail["favMovies"][2])