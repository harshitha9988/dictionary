x={'India':'0091',
   'Australia':'0025',
   'Nepal':'00977'}

print("Country code for India -")
print(x.get('India', "Not Found"))

print("Country code for Japan -")
print(x.get('Japan', "Not Found"))