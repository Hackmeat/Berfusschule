#Initializing
values = [4.92, 4.98, 4.97, 5.01, 5.02, 5.01, 5.03, 4.95, 4.96, 5.04]
extrems = []
sum = 0
sumNoExtrem = 0
base = 5
i = 0

#Adding up all numbers and catch & print extrem values
def getAvrage():
    global sum, sumNoExtrem, base, i
    while i < len(values):
        sum += values[i]
        if values[i] > base * 1.01 or values[i] < base * 0.99:
            print("Out of range: " + str(values[i]))
            extrems.append(values[i])
        else:
            sumNoExtrem += values[i]
        i += 1
     
#Get the avarage value   
getAvrage()

sum = sum / len(values)
sumNoExtrem = sumNoExtrem / (len(values) - len(extrems))

#Print
print("\nThe avg value of the values is: " + str(format(sum, ".2f")))
print("Without the extrems the avg value is " + str(format(sumNoExtrem, ".2f")))