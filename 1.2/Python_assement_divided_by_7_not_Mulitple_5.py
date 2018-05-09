
Range_start = 2000 # Start Range Suggest in Question
Range_end   = 3200 # END Range Suggest in Question

# Python have function named as filter used for filtering data one certain condition
# Filter is generator function to obtain result or return from generation list is Used
# Result will be Number divided by 7 But not mulitple of 5
Using_Filter      =  list(filter(lambda x: (x % 7 == 0 and x%5 !=0 ),
                           range(Range_start,Range_end+1)))


# Using List comprehension we can also obtain same Results
Oneliner_Function =  [x for x in range(Range_start,
                                       Range_end+1) if x %7 == 0 and x % 5!=0]


# Here I made Answere little bit User interative

def With_User_Input(): # Define the Function
    global Starting_range # Declare Starting Range as Global to handle expection as well
    global End_range      # same as above comment

    try:  # try with Numerical Digit Only
        # User will provide the Start Range and END Range
        # NOTE : Only Postive Integer Only
        # abs function Convert -ve number to postive number
        print ()
        Starting_range  = abs(int(input("Please Enter Starting Range :\t")))
        End_range       = abs(int(input("Please Enter End Range :\t")))
        print ()


    except ValueError: # USER type any Character program will go back again ask for Integer Value
        print ()
        print ("Enter Numerical Digit Not Character's")
        print ()
        With_User_Input()

    # One liner perform number divided by 7 But not mulitple of 5
    Output  = [x for x in range(Starting_range,
                                       End_range+1) if x %7 == 0 and x % 5!=0]

    return Output # Function Return the Result as per program guidelines


Result = With_User_Input() # Calling Funtion

print ("~*~"*15)
print (" Result Using Filter :\n", Using_Filter)
print ("~^~"*5)
print (" Result Using List comprehension  :\n", Oneliner_Function)
print ("~^~"*5)
print (" Result Using  Function with  User Inteface :\n", Result)
print ("~*~"*15)



