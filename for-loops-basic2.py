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
print(sumTotal(inputArray()))