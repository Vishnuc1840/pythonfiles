all_users=["mohanlal","mammootty","dileep","prithviraj","tovino","dulquar","nivin pauly"]

dileep_friends=["mohanlal","prithviraj",]

# list suggessions fo dileep

for u in all_users:
    if u not in dileep_friends:
        print(u)