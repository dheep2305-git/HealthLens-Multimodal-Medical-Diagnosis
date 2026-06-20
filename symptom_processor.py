import pandas as pd

def process_patient_data(age, gender, smoking, alcohol, fever, fatigue):

    patient_data = {
        "Age": age,
        "Gender": gender,
        "Smoking": smoking,
        "Alcohol": alcohol,
        "Fever": fever,
        "Fatigue": fatigue
    }

    df = pd.DataFrame([patient_data])

    return df


def calculate_risk_score(smoking, alcohol, fever, fatigue):

    score = 0

    if smoking:
        score += 3

    if alcohol:
        score += 2

    if fever:
        score += 2

    if fatigue:
        score += 1

    return score


# Example Test

if __name__ == "__main__":

    patient = process_patient_data(
        age=45,
        gender="Female",
        smoking=True,
        alcohol=False,
        fever=True,
        fatigue=True
    )

    risk = calculate_risk_score(
        smoking=True,
        alcohol=False,
        fever=True,
        fatigue=True
    )

    print(patient)
    print("Risk Score:", risk)