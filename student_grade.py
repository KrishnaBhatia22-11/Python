marks = []
for i in range(4):
    mark=float(input("Enter marks for subject"+str(i+1)+":")) 
    marks.append(mark)

total=sum(marks)
aggregate=(total/400)*100 

if aggregate>75:
    grade="Distinction"
elif aggregate>=60:
    grade="First Division"
elif aggregate>=50:
    grade="Second Division"
elif aggregate>=40:
    grade="Third Division"
else:
    grade="Fail"

print("\nTotal Marks:",total)
print("Aggregate:",round(aggregate,2),"%")
print("Grade:",grade)
