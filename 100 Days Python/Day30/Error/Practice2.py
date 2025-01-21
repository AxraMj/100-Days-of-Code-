facebook_posts=[
    {'likes':21,'comments':2},
    {'likes':13,'comments':2,'share':1},
    {'likes':33,'comments':8,'share':3},
    {'comments':4,'share':2},
    {'comments':1,'share':1},
    {'likes':19,'comments':3}
]

total_likes=0
for post in facebook_posts:
    try:
        total_likes=total_likes+post['likes']
    except KeyError:
        pass #code skip and continue running (so that it will exclude likes)
print(total_likes)