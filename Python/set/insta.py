all_users=["sachin","rahul","rohit","kohli","dravid","laxman","ganguli"]

sachin_follower=["rahul","ganguli","dravid"]


sachin_su=set(all_users).difference(set(sachin_follower))
sachin_su.remove("sachin")
print(sachin_su)