class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m

    @property
    def bmi(self):
       bmi = self.weight_in_kg / self.height_in_m ** 2
       return bmi
    @property
    def category(self):
        bmi = self.weight_in_kg / self.height_in_m ** 2
        if bmi < 18.5:
            return "underweight"
        elif bmi > 18.5 and bmi < 25:
            return "normal"
        elif bmi > 25:
            return "overweight"

# Write your code here
