"""
WAP to count number of vowels in string.
"""
string=['p','r','o','g','r','a','m','m','i','n','g']
count=0
i=0
while i<=11:
    if string [i]=='a' or string [i]=='e' or string [i]=='i' or string [i]=='o' or string [i]=='u':
        count=count+1
    else:
        print(string[i])
    i=i+1
