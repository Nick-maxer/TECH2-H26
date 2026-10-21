import numpy as np
def tax(income):

    if income < 300000:
     return(income)
    
    elif 300000<= income <= 700000:
       return(income*0.8)
   
    else: return(income*0.65)


incomes =  np.linspace(0,12000000, 13)
print(incomes)

taxes_loop = np.empty(len(incomes))

for income in incomes:
   taxes = tax(incomes)
   taxes_loop.append(taxes)

   print(taxes_loop)







