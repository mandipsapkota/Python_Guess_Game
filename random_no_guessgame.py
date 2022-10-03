import random
r=random.randrange(0,10)
print(r)
count=0
yesno=''
yesno=input('You wanna play??(Y/N)')
while (True):
    if yesno.upper()=='Y':
        while count != 3:
            
            numb=input('Guess the number(integer from 0 to 9) :')
            if numb.isdigit():
                
                number=int(numb)
                count+=1
                if number == r:
                    print(f'Congrats!!!you won in {count} guess')
                    quit()
                
                else:
                    
                    left=3-count;
                    if count != 3 :
                        print(f'Next try(guess left :{left})')            
                if count == 3:
                    print('You lost!!! The number was ',r,'.')
                    quit()
            else:
                print('Type a number')
    elif yesno.upper()=='N':
        print('Get lost!!!!!')
        break
    else:
        print('Type Y or N')
        yesno=input('You wanna play??(Y/N)')

