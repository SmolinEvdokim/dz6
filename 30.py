a1 = int(input())  
d = int(input())   
n = int(input())   

progression = []   

for i in range(n):
    an = a1 + i * d   
    progression.append(an)   

output = ', '.join(map(str, progression))   

print(output)   
