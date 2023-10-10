from json import load

path="C:\\Users\\DIGI HUB\\OneDrive\\Desktop\\Python\\movies\\mdb.json"


with open(path,encoding="utf-8")as f:
    filims=load(f)


    # print total number of filims

    # print(len(filims))


# print all movies released in 2015

# movie_filter=[f.get("title") for f in filims if f.get("year")=="2015"]
# print(movie_filter)

# print comedy genre movie title

# funny_movies=[f.get("title") for f in filims if "Comedy" in f.get("genres")]
# print(funny_movies)

# id in range(20,30) and run time>130

# m_filter=[f.get("title") for f in filims if f.get("id") in range(20,30) and f.get("runtime")>="110"]
# print(m_filter)

#title with single word 

# title_filter=[f.get("title") for f in filims if len(f.get("title").split(" "))==1]
# print(title_filter)


# genre=drama with max runtime 

# drama_movies=[f for f in filims if "Drama" in f.get("genres")]
# lengthy_movie=max(drama_movies,key=lambda f:int(f.get("runtime")))
# print(lengthy_movie)



# print all genres
# []

# which year more movies released

# num_mv={}
# for f in filims:
#     if f.get("year") in num_mv:
#         num_mv[(f.get("year"))]+=1
#     else:
#         num_mv[(f.get("year"))]=1
# most=max(num_mv,key=lambda d:num_mv[d])
# print(most)


#  sir
wc={}
for m in filims:
    year=m.get("year")

    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1

# out=max(wc,key=lambda k:wc.get(k))
# print(out)


print(max((v,k) for k,v in wc.items()))

