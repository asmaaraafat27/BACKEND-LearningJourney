# Exercise : Make a cup of coffee

### Input 

## Ingredients required:
# 1- Cup
# 2- Hot water
# 3- Coffee granules

## Optional:
# 1- Milk
# 2- Cream 
# 3- sugar

water = True
Cup = " "
def cup_of_coffee(optional):
    if water == True:
         coffee = 'french'
         Cup=coffee
         Cup+=" " 
         
    if optional == 'cream'  or optional == 'suger' or optional == 'milk':
        Cup+= optional
    return Cup

print('Your coffee is ready!','Ingredients:',cup_of_coffee(input()))
