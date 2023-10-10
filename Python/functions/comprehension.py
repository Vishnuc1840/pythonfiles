lst=[4,5,6,7,8,2,1]

# squares

squares=[n**2 for n in lst ]
print(squares)

cubes=[n**3 for n in lst ]
print(cubes)

even=[n for n in lst if n %2==0]
print(even)

odd=[n for n in lst if n %2!=0]
print(odd)

num_gtfive=[n for n in lst if n>=5]
print(num_gtfive)


