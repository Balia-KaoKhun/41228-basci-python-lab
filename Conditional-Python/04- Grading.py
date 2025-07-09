work = int(input("ur work score : "))
mid = int(input("ur midterm score : "))
final = int(input("ur final score : "))
sum = (work+mid+final)

if sum <= 49 :
    print("F")
elif sum <= 54 :
    print("D")
elif sum <= 59 :
    print("D+")
elif sum <= 64 :
    print("C")
elif sum <= 69 :
    print("C+")
elif sum <= 74:
    print("B")
elif sum <= 79 :
    print("B+")
else :print("A")    