# Insulin Dose Calculator
# Calculates insulin dose based on meal type, carbohydrate intake, and blood sugar level.
# Includes correctional dose logic and considers recent insulin use.

BLOOD_SUGAR_MIN = 4
BLOOD_SUGAR_MIN_CORRECTION = -1
BLOOD_SUGAR_MAX = 7
BLOOD_SUGAR_MAX_CORRECTION = 1

DOSAGE_RATIO = {
    'breakfast': 2,
    'lunch': 1.5,
    'dinner': 1.5,
    'snack': 1.5,
}


def get_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def main():
    prompt = f"What type of dose is it ({'/'.join(DOSAGE_RATIO.keys())}): "

    while (dose_type := input(prompt).strip().lower()) not in DOSAGE_RATIO:
        print("Invalid dose type. Try again.")

    ratio = DOSAGE_RATIO[dose_type]
    carbs = get_float("How many carbs are you eating? ")

    dose = ratio * carbs / 10

    recent_dose = input("Have you had a dose of insulin in the last 90 minutes? (yes/no): ").strip().lower()
    if recent_dose == "yes":
        print(f"You need {round(dose)} units of insulin (no correction applied).")
        return

    blood_sugar = get_float("What is your current blood sugar reading? ")

    correction = 0
    if blood_sugar > BLOOD_SUGAR_MAX:
        correction = (blood_sugar - BLOOD_SUGAR_MAX) * BLOOD_SUGAR_MAX_CORRECTION
    elif blood_sugar < BLOOD_SUGAR_MIN:
        correction = (blood_sugar - BLOOD_SUGAR_MIN) * BLOOD_SUGAR_MIN_CORRECTION

    total_dose = round(dose + correction)

    print(f"You need {total_dose} units of insulin (including correction of {round(correction)}).")


if __name__ == '__main__':
    main()