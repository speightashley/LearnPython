from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"patient {patient} is not taking warfarin")
    print(patient, prescription)
