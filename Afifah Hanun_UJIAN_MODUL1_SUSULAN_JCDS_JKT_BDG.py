#NOMOR 1

# class Solution:
#    def solve(self, nums):
#       odds = [num for num in nums if num % 2 == 0]
#       evens = [num for num in nums if num % 2 != 0]
#       odds.sort()
#       evens.sort(reverse=True)
#       even_i = 0
#       odd_i = 0
#       for index in range(len(nums)):
#          if nums[index] % 2 == 0:
#             nums[index] = evens[even_i]
#             even_i += 1
#          else:
#             nums[index] = odds[odd_i]
#             odd_i += 1
#       return nums
# print(ob.solve([-9, 8, 23, 88, -6, 5])) #contoh list angka untuk ngetes output

#NOMOR 2

# i= int(input('Please input a number: '))
# j= int(input('Please Input Another Number: '))
# for row in range(1, 10):
#     print("  ", i, end = '')
#     for col in range(1, 10):
#         num = row * col
#         if num < 10:
#             empty = "  "
#         else:
#             if num < 100: 
#                 empty  = " " 
#         print(empty, num, end = '')
#     print()

#NOMOR 3

# import json

# with open ("ccNasabah.json", "r") as x:
#     out = json.load(x)

# valid =[]
# invalid = []
# for i in range(len(out)):
#     kontenCC = out[i].get("noCreditCard")
#     if kontenCC[4] == "-":
#         newKontenCC = kontenCC.replace("-","")
#     else:
#         newKontenCC = kontenCC
#     jmlKarakter = len(list(newKontenCC))
#     if jmlKarakter == 16 and int(newKontenCC[0]) in range(4,7) and newKontenCC.isdigit() is True:
#         valid.append(out[i])
#     else:
#         invalid.append(out[i])

# with open ("ccValid.json", "w") as y:
#     json.dump(valid,y)

# with open ("ccInvalid.json", "w") as m:
#     json.dump(invalid,m)
