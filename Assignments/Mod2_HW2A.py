'''Shira Krausz's Minutes to Hours and Minutes
In this assignment I'm going to convert a user's input of minutes into hours and minutes using a function'''

'''This function will ask the user for minutes, convert it to hours and minutes, and print'''
def minutes_to_hours_and_minutes():

   # We ask the user to input a number of minutes. We convert the input string into an integer.
    mnt = int(input("Hi! Enter an amount of minutes to convert")) #mnt is the user's input as an integer

#divide minutes by 60 to get an integer which will be the amount of whole hours
    hrs = mnt//60 # hrs is number of hours

# find the remainder after you divided by 60 to get remaining minutes
    min = mnt % 60 # min is the number of remaining minutes

# We print their input converted into hours (hrs) and the remaining minutes (min)
    print ("That is", hrs, "hours and", min, "minutes.")

#We run our function
minutes_to_hours_and_minutes()
