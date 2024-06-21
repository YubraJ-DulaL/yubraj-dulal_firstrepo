"""
Admission to a professional course is subject to the following conditions:
a.Marks in mathematics >=60
b.Marks in physics >=50
c.Marks in chemistry >=40
d.Total in all three subjects >=200

"""
print("Enter Marks in following subjects:")
# following subjects.
print("|------------------|")
Math=float(input("|Mathematics=")) #input marks of mathematics
print("|------------------|")
Physics=float(input("|Physics=")) #input marks of physics
print("|------------------|")
Chemistry=float(input("|Chemistry=")) #input marks of chemistry
print("|------------------|")

total=Math+Physics+Chemistry #total sum of three subjects

if Math >= 60 and Physics >= 50 and Chemistry >= 40 and total>=200:
    print("\n\n|--------------------------------|")
    print(f"|Average={total} :You are admitted.|")
    print("|--------------------------------|")
else:
    print("\n\n|-----------------------------------|")
    print(f"|Average={total} :You aren't admitted.|")
    print("|-----------------------------------|")
    


