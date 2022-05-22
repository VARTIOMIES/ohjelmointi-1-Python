before_raise = input("Enter the amount of the study benefits: ")
percent = 1.17
multiplier = 1.0117
after_raise = float(before_raise) * multiplier
print("If the index raise is", percent, "percent, the study benefit,")
print("after a raise, would be", after_raise, "euros")
print("and if there was another index raise, the study")
print("benefits would be as much as", after_raise * multiplier, "euros")
