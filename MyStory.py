import random
when = ["A few years ago","Yesterday","One month ago","Today","One week ago"]
who = ["A rabbit", "An elephant","A mouse","A turtle","A cat"]
name = ["divyesh","Shubham","Aarav","Shaurya","Shiven"]
residence = ["India", "Spain", "U.S.A","France","Russia"]
went = ["School","Amusement Park","Play Ground","Cinema","Meuseum"]
happened = ["Had Fun", "Ate Some Burger","Found a best friend","Solved Quetion","Wrote a book"]
print(random.choice(when) + ', ' + random.choice(who) + ' ' + random.choice (name) + ' that lived in ' + random.choice(residence) +
', went to the ' + random.choice(went) + ' and ' + random.choice(happened))