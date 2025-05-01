def diagnose():
    print("Welcome to the Medical Diagnosis Expert System.")
    symptoms_input = input("Enter your symptoms (comma-separated): ").strip().lower()
    symptoms = [symptom.strip() for symptom in symptoms_input.split(",")].copy()
    def has(required_symptoms):
        return all(symptom in symptoms for symptom in required_symptoms)
    if has(["fever", "cough", "fatigue"]):
        return "You may have the flu."
    elif has(["fever", "headache", "stiff neck"]):
        return "You may have meningitis. Please consult a doctor immediately."
    elif has(["sneezing", "runny nose", "sore throat"]):
        return "You may have a common cold."
    elif has(["chest pain", "shortness of breath"]):
        return "You may have a heart problem. Seek medical attention immediately."
    elif has(["abdominal pain", "diarrhea"]):
        return "You may have a stomach infection."
    elif has(["itchy eyes", "sneezing", "runny nose"]):
        return "You may be experiencing an allergic reaction."
    else:
        return "Diagnosis not found. Please consult a healthcare professional."
print(diagnose())
