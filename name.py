import sys

if len(sys.argv) != 6:
    print("grade evaluation")

name =(sys.argv[1])
sub1 = float(sys.argv[2])
sub2 = float(sys.argv[3])
sub3 = float(sys.argv[4])
sub4 = float(sys.argv[5])
 
total=sub1 + sub2 + sub3 + sub4;
average= total / 4

if(average<=100):
   grade= "a"
elif(average<=80):
    grade ="b"
elif(average<=70):
    grade= "c"
elif(average<=60):
    grade ="d"
else:
    grade ="fail"

print("name",name)
print("sub1",sub1)
print("sub2",sub2)
print("sub3",sub3)
print("sub4",sub4)
print("average",average)
print("grade",grade)