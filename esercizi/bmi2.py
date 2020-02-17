def BMI2(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height**2

print(BMI2(80.8,1.83))
