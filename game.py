

# turns=0
# user=0
# pc=0
# if turns<=5:
#     n=int(input('enter your number: '))
#     if n in range (1,5):
#         user+=1
#     elif n in range (6,11):
#             pc+=1
#     turns+=1
#     elif user>pc:
#         print('user won',user)
#     else:
#         print('pc won',pc)
# print('use:',user,'pc:',pc)
   
# f=open('hi_score.txt','a')
# if game(n)
def game():
    return 109876
score=game()
with open('hiscore.txt') as f:
    hi_score=f.read()
if str(hi_score)=='':
    with open ('hiscore','w') as f:
        f.write(str(score))
elif int(hi_score)<=score:
    with open ('hiscore.txt','w') as f:
        f.write(str(score))

        



    