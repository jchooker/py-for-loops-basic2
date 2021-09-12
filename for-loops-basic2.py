#1-Biggie Size
def biggieSize(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr
a = []
prompt_txt = "Please populate array with new number or provide invalid entry to quit: "
while True:
    try:
        user_input = int(input(prompt_txt))
        a.append(user_input)
    except:
        break
print(biggieSize(a))