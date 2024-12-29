#you are painting a wall. The instructions on the paint can say that 
#1 can of paint can cover 5 square meters of wall
#give a random height and width of wall
#calculate how many cans of paint you'll need to buy.

#number of cans=(wall height X wall width)/coverage per can

#eg height = 2,width=4,coverage=5

#number of cans=(2*4)/5=1.6

#but because you cant buy 0.6 of a can of paint,the result,should be rounded up to 2 cans

#important:noteice the name of the function and parameter must match those on line 13 for the code to work



def num_paint():
    height=int(input("Enter the height:"))
    width=int(input("Enter the width:"))
    coverage=5
    result=(height*width)%coverage
    print(f"you need {round(result)} cans of paint ")

num_paint()