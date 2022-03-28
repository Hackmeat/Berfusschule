#Initializing
values = [4.92, 4.98, 4.97, 5.01, 5.02, 5.01, 5.03, 4.95, 4.96, 5.04]
extrems = []
sum = 0
sumNoExtrem = 0

#Adding up all numbers and catch & print extrem values
def mess_Avg():
    global sum, sumNoExtrem
    base = 5
    i = 0
    while i < len(values):
        sum += values[i]
        if values[i] < base * 1.01 and values[i] > base * 0.99:
            sumNoExtrem += values[i]
        else:
            extrems.append(values[i])
        i += 1
    sum = sum / len(values)
    sumNoExtrem = sumNoExtrem / (len(values) - len(extrems))
    print("\nThe avg value of the values is: " + str(format(sum, ".3f")))
    print("Without the extrems the avg value is " + str(format(sumNoExtrem, ".3f")))    
    
        
def mess_Warn():
    base = 5
    i = 0
    while i < len(values):
        if values[i] > base * 1.01 or values[i] < base * 0.99:
            print("\nOut of range: " + str(values[i]))
        i += 1
        
def mess_Max():
    temp = 0
    i = 0
    while i < len(values):
        if values[i] > temp:
            temp = values[i]
        i += 1
    print("\nThe highest value is " + str(temp))
        
def sort():  
    nocheck = False
    while nocheck == False:
        nocheck = True
        j = 0
        while (j + 1) < len(values): 
            if values[j] > values[j + 1]:
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp
                nocheck = False      
            j += 1
    print(values)
        
#Call FUntions
mess_Avg()
mess_Warn()
mess_Max()
sort()