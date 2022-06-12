import random
from colorama import Fore,Style,init
init()

daycount = 1
endings = [1,2]
adoptionchance = [0,1]
amountoforphans = [1,2,3]
amountofcarers = [1,2]
neworphanschoice = [0,1]

print(Fore.RED+'Welcome to The Orphanage')
print(Style.RESET_ALL)
print()
carers = int(input('Amount of available carers:  '))
orphans = int(input('Amount of orphans:  '))

ending = random.choice(endings)

print()
print()

if ending == 1:
  if carers == 0:
    print()
    print()
    print(Fore.RED+'There are no carers left to look after the orphans and the orphans remain in the orphanage for the rest of their lives')
    print(Style.RESET_ALL)
    quit()
  while orphans > 0:
    for x in range(7):
      print()
    print(Fore.GREEN+'Day',daycount)
    print(Style.RESET_ALL)
    daycount += 1
    print()
    print()
    carerincrease = random.randint(1,5)
    carers += carerincrease
    print('A new carer has dropped by (x'+str(carerincrease)+')')
    print()
    for x in range(random.randint(1,5)):
      adopt = random.choice(adoptionchance)
      if adopt == 0:
        print()
        print('Waiting for carers...')
        print()
      if adopt == 1:
        print()
        print()
        carersnumber = random.choice(amountofcarers)
        orphansnumber = random.choice(amountoforphans)
        if carers > 1:
          carers -= carersnumber
        else:
          carers = 0
        if orphans > 2:
          orphans -= orphansnumber
        else:
          orphans = 0
        print(Fore.CYAN+str(carersnumber),'carer(s) have just adopted',orphansnumber,'orphan(s)')
        print(Style.RESET_ALL)
        print()
        print('There are',orphans,'orphan(s) left and',carers,'carer(s) available')
  if orphans == 0:
    print()
    print()
    print(Fore.RED+'All the orphans found new homes after',str(daycount - 1),'days')
    print(Style.RESET_ALL)
    quit()



          
if ending == 2:
  if carers == 0:
    print()
    print()
    print(Fore.RED+'There are no carers left to look after the orphans and the orphans remain in the orphanage for the rest of their lives')
    print(Style.RESET_ALL)
    quit()
  while orphans > 0:
    for x in range(7):
      print()
    print(Fore.GREEN+'Day',daycount)
    print(Style.RESET_ALL)
    daycount += 1
    print()
    print()
    orphanincrease = random.randint(1,3)
    orphans += orphanincrease
    print('A new orphan has dropped by (x'+str(orphanincrease)+')')
    carerincrease = random.randint(1,5)
    carers += carerincrease
    print('A new carer has dropped by (x'+str(carerincrease)+')')
    print()
    for x in range(random.randint(1,5)):
      adopt = random.choice(adoptionchance)
      if adopt == 0:
        print()
        print('Waiting for carers...')
        print()
      if adopt == 1:
        print()
        print()
        carersnumber = random.choice(amountofcarers)
        orphansnumber = random.choice(amountoforphans)
        if carers > 1:
          carers -= carersnumber
        else:
          carers = 0
        if orphans > 2:
          orphans -= orphansnumber
        else:
          orphans = 0
        print(Fore.CYAN+str(carersnumber),'carer(s) have just adopted',orphansnumber,'orphan(s)')
        print(Style.RESET_ALL)
        print()
        print('There are',orphans,'orphan(s) left and',carers,'carer(s) available')
  if orphans == 0:
    print()
    print()
    print(Fore.RED+'All the orphans found new homes after',str(daycount - 1),'days')
    print(Style.RESET_ALL)
    quit()

    

if ending == 3:
  print()
  print(Fore.RED+'An asteroid hit the planet and wiped out all life')
  print(Style.RESET_ALL)
  quit()



if ending == 4:
  print()
  print(Fore.RED+'A deadly virus wipes out humankind')
  print(Style.RESET_ALL)
  quit()
  


pass