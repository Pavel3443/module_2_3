my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nev = 0
while nev < len(my_list):
   if my_list[nev] < 0:
       break
   if my_list[nev] > 0:
       print(my_list[nev])
   nev += 1



