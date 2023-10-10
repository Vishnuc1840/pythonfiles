enquires=["django","testing","django","bigdata","django","aws","aws","django"]

enq_count={}
for i in enquires:
    if i in enq_count:
        enq_count[i]+=1
    else:
        enq_count[i]=1
print(enq_count)