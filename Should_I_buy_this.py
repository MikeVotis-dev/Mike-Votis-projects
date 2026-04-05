# --------------------------------------------------------------------Should I buy it------------------------------------------------------------------------------------------------
# Generated-programmed by MIKE VOTIS
# IDEA BY GEMINI

import math


print("SHOULD I BUY IT?")
print("               ")
print("GENERATED-PROGRAMMED BY MIKE VOTIS")
print("               ")
print("Idea by AI MACHINE (Gemini)")
print("                ")

item_for_buy = input("What do you want to buy? ")
print("Ok,", item_for_buy, "is a very good choice.")

price_of_item = int(input("What is the price of the product? "))

budget = int(input("What is your budget? "))

monthly_saving = int(input("How much money can you save for this product per month? (If nothing, type 0): "))

remaining = price_of_item - budget


if remaining <= 0:
    print("You can buy it now!")
elif monthly_saving <= 0:
    print("Your monthly saving must be more than 0.")
else:
    exact_months = remaining / monthly_saving
    needed_months = math.ceil(exact_months)
    exact_weeks = exact_months * 4.345

    saved_after_months = needed_months * monthly_saving
    leftover = saved_after_months - remaining

    print(f"You still need {remaining:.2f} euros.")
    print(f"You will need about {exact_months:.2f} months.")
    print(f"That is about {exact_weeks:.1f} weeks.")
    print(f"In practice, you will be able to buy it in {needed_months} months.")
    print(f"At that point, you will have {leftover:.2f} euros left.")