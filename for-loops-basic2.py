#prologue - function for taking input from user
#Need version that will work after getting no input from user (i.e. length of 0)
def inputArray():
    a = []
    prompt_txt = "Please populate array with new number or provide invalid entry to quit: "
    while True:
        try:
            user_input = int(input(prompt_txt))
            a.append(user_input)
        except:
            break
    return a

#1-Biggie Size
# def biggieSize(arr):
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             arr[i] = "big"
#     return arr
# print(biggieSize(inputArray()))

# a = []
# prompt_txt = "Please populate array with new number or provide invalid entry to quit: "
# while True:
#     try:
#         user_input = int(input(prompt_txt))
#         a.append(user_input)
#     except:
#         break
# print(biggieSize(a))

#2 - Count positives
# def countPos(arr):
#     posCt = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             posCt+=1
#     arr[len(arr)-1] = posCt
#     return arr
# print(countPos(inputArray()))

#3 - Sum total
def sumTotal(arr):
    sum = 0
    for i in arr:
        sum+=i 
    return sum 
# print(sumTotal(inputArray()))

#4 - Average
def avg(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum/(len(arr))
# print(avg(inputArray()))

#5 - Length
def length(arr):
    ct = 0
    for i in arr:
        ct+=1
    return ct
# print(length(inputArray()))

#6 - Minimum
def minim(arr):
    newMin = 0
    if not arr:
        print("Empty list")
    else:
        newMin = arr[0]
        for i in arr:
            if i < newMin:
                newMin = i
    return newMin
# print(minim(inputArray()))

#7 - Maximum
def maxim(arr):
    newMax = 0
    if not arr:
        print("Empty List")
    else:
        newMax = arr[0]
        for i in arr:
            if i > newMax:
                newMax = i
    return newMax
# print(maxim(inputArray()))

#8 - Ultimate analysis
def ultAnalysis(arr):
    analyzedArr = {'sumTotal':sumTotal(arr), 'average':avg(arr), 'minimum':minim(arr), 'maximum':maxim(arr), 'length':length(arr)}
    return analyzedArr
# print(ultAnalysis(inputArray()))

#9 - Reverse list
#no distinction made re: even vs odd lists given that "int(...)" rounds DOWN
def reverseList(arr):
    temp = 0
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr) - (i+1)]
        arr[len(arr) - (i+1)] = temp
    return arr
print(reverseList(inputArray()))
