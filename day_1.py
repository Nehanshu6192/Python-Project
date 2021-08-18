weight= int(input("enter your weight(kg): "))
height= float(input("enter your height(m): "))

bmi= round(weight/(height*height))

print(f"your bmi is {bmi}")
if (bmi>25):
    print(
        f"you are over weight\n reduce your weight to {round(21.7*(height*height))}")

