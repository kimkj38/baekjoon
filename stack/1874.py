n = int(input())
stack = []
count = 0
result = []
error = False

for i in range(n):
    x = int(input())
    
    while count < x:
        result.append("+")
        stack.append(count+1)
        count += 1
        
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        error = True
        break

if error == True:
    print("NO")
else:
    print("\n".join(result))
