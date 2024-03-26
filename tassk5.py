tassk5.py
def calculate_bmi(weight, height):
    """
    BMI hesablayan funksiya
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    BMI kateqoriyasını təyin edən funksiya
    """
    if bmi < 18.5:
        return "Az çəki"
    elif 18.5 <= bmi < 25:
        return "Normal çəki"
    elif 25 <= bmi < 30:
        return "Artıq çəki"
    else:
        return "Piylənmə"

def main():
    weight = float(input("Çəkini kiloqramla daxil edin: "))
    height = float(input("Boyunuzu metrlə daxil edin: "))

    bmi = calculate_bmi(weight, height)
    print("BMI-niz:", bmi)

    bmi_category = get_bmi_category(bmi)
    print("BMI kateqoriyası:", bmi_category)

if __name__ == "__main__":
    main()
