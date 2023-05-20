#leap year checker

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("LEAP YEAR")
            else:
                print("NOT LEAP YEAR")            
        else:
            print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")

is_leap_year(2000)

  
