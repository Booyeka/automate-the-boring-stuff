




# practice by creating a function that utilizes the collatz sequence



def collatz(number):
  
    if number % 2 == 0:
        number = number /2
        print(number)
        return number
        
    else:
        number = (3*number)+1
        print(number)
        return number
            
        
while True:            
    try:
        number = int(input('enter number:\n'))
        break
    except ValueError:
        print('That wasn\'t a number...\n')
        continue

''' first attempt - works, but confusing
count = 1
while count >= 1 and number != 1 or count ==1 and number == 1:
    count+=1
    number = collatz(number)

'''
   
# second attempt - more concise
while True:
    number = collatz(number)
    if number == 1:
        break