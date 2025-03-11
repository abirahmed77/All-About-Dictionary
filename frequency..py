test_dict = {
    "Codingal" : 2,
    "is" : 2,
    "Best" : 5,
    "for" : 2,
    "Coding" : 1
}
print(f"The Original Dictionary : {test_dict}")

k = 2
res = 0

for key in test_dict:
    
    if test_dict[key] == k:
        res = res + 1
        
print(f"Frequency of K {k} is : {res}")