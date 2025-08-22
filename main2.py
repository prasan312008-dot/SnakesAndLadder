import random

level=str(input("Choose Your Difficulty level (Hard/Easy)"))
if level=="Hard":
   snakes = [(16,1) ,(23,4), (31, 11), (43, 2), (56, 9), (64, 2), (87, 24), (93, 73), (95, 75), (98, 1)]
   ladders = [(4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67),(78,96)]
   initial =[0,0]
   x=0
   num=100
   S=(16,23,31,43,56,64,87,93,95,98)
   L=(4,9,21,28,36,51,78)
   n=(1,2,3,4,5,6,7,8,9)
   for i in range (1,11):
       for j in range (1,11):
           if num in S:
               print("🐍", end=' ')
           elif num in L:
               print("🪜", end=' ')
           elif num in n :
               print(num, end='  ')
           else:
               print(num , end=' ')
           num-=1
       print()




else :
   snakes = [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)]
   ladders = [(2, 38), (4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100)]
   initial = [0, 0]
   num = 100
   x=0
   S= [16,47,49,56,62,64,87,93,95,97]
   l= [1,4,9,21,28,37,51,71,80]
   n=[1,2,3,4,5,6,7,8,9]
   for i in range(1, 11):
       for j in range(1, 11):
            if num in S:
                print("🐍" ,end=' ')
            elif num in l:
               print('🪜', end=' ')
            elif num in n :
               print(num,end='  ')
            else:
                print(num, end=' ')
            num-=1
       print()







while True:
           input(" Press Enter to roll the dice.")
           roll = random.randint(1, 6)
           print(" You rolled a",roll)
           x+=1




           for i in range (1):
             initial[i] += roll




           for snake in snakes:
               if initial[i]== snake[0]:
                   initial[i]= snake[1]
                   print("Oops! You got bitten by a snake and moved to position",initial[i])
                   break


           for ladder in ladders:
               if initial[i] == ladder[0]:
                   initial[i] = ladder[1]
                   print("Wow! You climbed a ladder and moved to position",initial[i])
                   break


           print("You are now at position",initial[i])


           if initial[i] >= 100:
               print(" You won !")
               break


if x<=15:
    print ('Great Performance ')
elif 15<x<=25:
    print (' Average Performance ')
else :
   print('Poor Performance ')


