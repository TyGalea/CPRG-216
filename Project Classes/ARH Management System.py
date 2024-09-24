# ARH Management System - CPRG216 Project Classes
#
# This program allows the user to manage a list of doctors or patients. The user can choose in both to
# veiw the list of doctors or patients. They can also search for a specific doctor or patient by entering
# their id. A doctor can be found by entering its name. The user can add doctor or patient to the list if
# a doctor or patient with the same id doesn't exist. The user can also edit doctor or patient in the list
# by entering ist id. All updates to the list of doctors or patients will be added to the respective text file
# when the user is finished.
# 
# Author Tyler Galea, Urooba Ejaz, Lakshita Sethi
# Version 2023-04-24


# Doctor class with the attributes doctor_id, name, specialty, schedule, qualification, and room_number
class Doctor:
    def __init__(self, doctor_id = '', name = '', specialty = '', schedule = '', qualification = '', room_number = ''):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialty = specialty
        self.__schedule = schedule
        self.__qualification = qualification
        self.__room_number = room_number
    
    # Doctor class setter for doctor_id
    def set_doctor_id(self, new_id):
            self.__doctor_id = new_id

    # Doctor class getter for doctor_id
    def get_doctor_id(self):
            return self.__doctor_id
        
    # Doctor class setter for name
    def set_name(self, new_name):
            self.__name = new_name

    # Doctor class getter for name       
    def get_name(self):
            return self.__name

    # Doctor class setter for specialty
    def set_specialty(self, new_specialty):
            self.__specialty = new_specialty

    # Doctor class getter for specialty
    def get_specialty(self):
            return self.__specialty

    # Doctor class setter for schedule
    def set_schedule(self, new_schedule):
            self.__schedule = new_schedule

    # Doctor class getter for schedule        
    def get_schedule(self):
            return self.__schedule

    # Doctor class setter for qualification
    def set_qualification(self, new_qualification):
            self.__qualification = new_qualification

    # Doctor class getter for qualification
    def get_qualification(self):
            return self.__qualification

    # Doctor class setter for room_number
    def set_room_number(self, new_room_number):
            self.__room_number = new_room_number

    # Doctor class getter for room_number
    def get_room_number(self):
            return self.__room_number
    
    # This function in Doctor class prints out all of the attributes of a Doctor object seperated by an underscore
    def format_file_layout(self):
        return f"{self.__doctor_id}_{self.__name}_{self.__specialty}_{self.__schedule}_{self.__qualification}_{self.__room_number}\n"

    # This function in Doctor class prints out all of the attributes of a Doctor object with the aprropriate spacing when printed
    def __str__(self):
        return format(self.__doctor_id, "<5s") + format(self.__name, "<20s") + format(self.__specialty, "<20s") + format(self.__schedule, "<15s") + format(self.__qualification, "<18s") + format(self.__room_number, ">8s")


# Patient class with the attributes patient_id, name, diagnosis, gender, and age
class Patient:
    def __init__(self, patient_id = '', name = '', diagnosis = '', gender = '', age = ''):
        self.__patient_id = patient_id
        self.__name = name
        self.__diagnosis = diagnosis
        self.__gender = gender
        self.__age = age
    
    # Patient class setter for patient_id
    def set_patient_id(self, new_Id):
            self.__patient_id = new_Id

    # Patient class getter for patient_id       
    def get_patient_id(self):
            return self.__patient_id
        
    # Patient class setter for name
    def set_name(self, new_name):
            self.__name = new_name

    # Patient class getter for name
    def get_name(self):
            return self.__name

    # Patient class setter for diagnosis
    def set_diagnosis(self, new_diagnosis):
            self.__diagnosis = new_diagnosis

    # Patient class getter for diagnosis 
    def get_diagnosis(self):
            return self.__diagnosis

    # Patient class setter for gender
    def set_gender(self, new_gender):
            self.__gender = new_gender

    # Patient class getter for gender
    def get_gender(self):
            return self.__gender

    # Patient class setter for age
    def set_age(self, new_age):
            self.__age = new_age

    # Patient class getter for age
    def get_age(self):
            return self.__age
    
    # This function in Patient class prints out all of the attributes of a Patient object seperated by an underscore
    def format_file_layout(self):
        return f"{self.__patient_id}_{self.__name}_{self.__diagnosis}_{self.__gender}_{self.__age}\n"

    # This function in Patient class prints out all of the attributes of a Patient object with the aprropriate spacing when printed
    def __str__(self):
        return format(self.__patient_id, "<5s") + format(self.__name, "<20s") + format(self.__diagnosis, "<25s") + format(self.__gender, "<10s") + format(self.__age, ">3s")


#  Function: manage_dr
#
#  This function creates a list of doctors from the read_doctors_file function, calls the approprite
#  function to modify the doctor list based off the user's choice, and calls the write_drs_list_to_file
#  function to write the the new doctor list to a text file.
#
#  Parameters: None
#  Returns   : None
def manage_dr():
    doctorList = []
    read_doctors_file(doctorList)
    menuDictionary = ["1 - List of Doctors", 
                      "2 - Search for Doctor by ID",
                      "3 - Search for Doctor by Name/Partial Name",
                      "4 - Add new Doctor",
                      "5 - Edit Doctors Info",
                      "0 - Return to Main Menu",]
    menuOption = menu("    Doctor's Menu", menuDictionary)
    while menuOption != 0:
        match menuOption:
            case 1:
                display_list_of_drs(doctorList)
            case 2:
                doctorID = input("Enter Dr ID: ")
                doctorFound = find_dr_by_id(doctorList, doctorID)
                if(doctorFound == -1):
                    print("Doctor with ID", doctorID, "not found")
            case 3:
                match_dr_by_name(doctorList)
            case 4:
                add_dr_to_list(doctorList)
            case 5:
                edit_dr_info(doctorList)
        print()
        menuOption = menu("    Doctor's Menu", menuDictionary)
    write_drs_list_to_file(doctorList)

#  Function: read_doctors_file
#
#  This function reads the "doctorss.txt" file and appends each doctor to the the doctorList.
#
#  Parameters: doctorList - required parameter (List of Doctor) - a list of all doctors
#  Returns   : None
def read_doctors_file(doctorList):
    doctorFile = open(r'doctors.txt', 'r')
    line = doctorFile.readline()
    while line != '':
        items = line.strip('\n').split('_')
        doctor = Doctor(items[0], items[1], items[2], items[3], items[4], items[5])
        doctorList.append(doctor)
        line = doctorFile.readline()
    doctorFile.close()

#  Function: find_dr_by_id
#
#  This function checks if a doctor with a certain id exists in the doctor list. If
#  it does then it will print and return the doctor, otherwise it will return -1.
#
#  Parameters: doctorList - required parameter (List of Doctor) - a list of all doctors
#  Parameters: doctorID - required parameter (String) - a doctor id
#  Returns   : None
def find_dr_by_id(doctorList, doctorID):
    for doctor in doctorList:
        if doctorID == doctor.get_doctor_id():
            print(doctor)
            return doctor
    return -1

#  Function: match_dr_by_name
#
#  This function asks the user for a name and prints out all doctors that contain that
#  in their name.
#
#  Parameters: doctorList - required parameter (List of Doctor) - a list of all doctors
#  Returns   : None
def match_dr_by_name(doctorList):
    doctorName = input("Enter the doctor name: ").lower()
    foundDoctor = False
    for doctor in doctorList:
        if doctor.get_name().lower().find(doctorName) != -1:
            print (doctor)
            foundDoctor = True
    if not foundDoctor:
        print("Doctor with the name", doctorName, "not found")

#  Function: edit_dr_info
#
#  This function asks the user for an id and checks if it is in the doctor list. If
#  it is, it will then asks for the doctors name, specialty, schedule, qualifications, and age and chages 
#  this information for the doctor with the same id.
#
#  Parameters: doctorList - required parameter (List of Doctor) - a list of all doctors
#  Returns   : None
def edit_dr_info(doctorList):
    doctorID = input("Enter ID of Doctor to be edited: ")
    foundDoctor = False
    for doctor in doctorList:
        if doctorID == doctor.get_doctor_id():
            print(doctor)
            name = input("Enter new name: ")
            doctor.set_name(name)
            specialty = input("Enter new specialty in: ")
            doctor.set_specialty(specialty)
            schedule = input("Enter new schedule: ")
            doctor.set_schedule(schedule)
            qualification = input("Enter new qualifications: ")
            doctor.set_qualification(qualification)
            room = input("Enter new room number: ")
            doctor.set_room_number(room)
            print("Doctor with id", doctorID, "successfully modified\n")
            foundDoctor = True
    if not foundDoctor:
        print("Doctor with ID", doctorID, "not found\n")
    display_list_of_drs(doctorList)

#  Function: display_list_of_drs
#
#  This function will print out all of the the doctors in the doctor list
#
#  Parameters: doctorList - required parameter (List of Doctor) - a list of all doctors
#  Returns   : None
def display_list_of_drs(doctorList):
    for doctor in doctorList:
        print(doctor)

#  Function: write_drs_list_to_file
#
#  This function writes all the doctors in the in the doctor list to the "doctors.txt" 
#  file in the format from format_file_layout() in the Doctor class.
#
#  Parameters: doctorList - required parameter (List of Doctor) - a list of all doctors
#  Returns   : None
def write_drs_list_to_file(doctorList):
    doctorFile = open(r'doctors.txt', 'w')
    for doctor in doctorList:
        doctorFile.write(doctor.format_file_layout())
    doctorFile.close()

#  Function: add_dr_to_list
#
#  This function asks the user for an id and checks if it is in the doctor list. If
#  it isn't, it will then asks for the doctors name, specialty, schedule, qualifications, and age and appends this
#  doctor to the end of the doctor list.
#
#  Parameters: doctorList - required parameter (List of Doctor) - a list of all doctors
#  Returns   : None
def add_dr_to_list(doctorList):
    doctorID = input("Enter Dr ID: ")
    doctorFound = find_dr_by_id(doctorList, doctorID)
    if(doctorFound != -1):
        print("Doctor with ID", doctorID, "already exists - cannot add")
    else:
        name = input("Enter Dr name: ")
        specialty = input("Enter Dr specialty: ")
        schedule = input("Enter Dr schedule: ")
        qualifications = input("Enter Dr qualifications: ")
        room = input("Enter Dr room number: ")
        doctor = Doctor(doctorID, name, specialty, schedule, qualifications, room)
        doctorList.append(doctor)
        print("Doctor with id", doctorID, "successfully added")


#  Function: manage_patient
#
#  This function creates a list of patients from the read_patients_file function, calls the approprite
#  function to modify the patient list based off the user's choice, and calls the write_patients_list_to_file
#  function to write the the new patient list to a text file.
#
#  Parameters: None
#  Returns   : None
def manage_patient():
    patientList = []
    read_patients_file(patientList)
    menuDictionary = ["1 - List of Patients", 
                      "2 - Search for Patient by ID",
                      "3 - Add new Patient",
                      "4 - Edit Patient Info",
                      "0 - Return to Main Menu",]
    menuOption = menu("    Patient's Menu", menuDictionary)
    while menuOption != 0:
        match menuOption:
            case 1:
                display_list_of_patients(patientList)
            case 2:
                patientID = input("Enter Patient ID: ")
                patientFound = find_patient_by_id(patientList, patientID)
                if(patientFound == -1):
                    print("Patient with ID", patientID, "not found")
            case 3:
                add_patient_to_list(patientList)
            case 4:
                edit_patient_info(patientList)
        print()
        menuOption = menu("    Patient's Menu", menuDictionary)
    write_patients_list_to_file(patientList)

#  Function: read_patients_file
#
#  This function reads the "patients.txt" file and appends each patient to the the patientList.
#
#  Parameters: patientList - required parameter (List of Patient) - a list of all patients
#  Returns   : None
def read_patients_file(patientList):
    patientFile = open(r'patients.txt', 'r')
    line = patientFile.readline()
    while line != '':
        items = line.strip('\n').split('_')
        patient = Patient(items[0], items[1], items[2], items[3], items[4])
        patientList.append(patient)
        line = patientFile.readline()
    patientFile.close()

#  Function: find_patient_by_id
#
#  This function checks if a patient with a certain id exists in the patient list. If
#  it does then it will print and return the patient, otherwise it will return -1.
#
#  Parameters: patientList - required parameter (List of Patient) - a list of all patients
#  Parameters: patientID - required parameter (String) - a patient id
#  Returns   : None
def find_patient_by_id(patientList, patientID):
    for patient in patientList:
        if patientID == patient.get_patient_id():
            print(patient)
            return patient
    return -1

#  Function: edit_patient_info
#
#  This function asks the user for an id and checks if it is in the patient list. If
#  it is, it will then asks for the patients new name, diagnosis, gender and age and chages 
#  this information for the patient with the same id.
#
#  Parameters: patientList - required parameter (List of Patient) - a list of all patients
#  Returns   : None
def edit_patient_info(patientList):
    patientID = input("Enter ID of Patient to be edited: ")
    foundPatient = False
    for patient in patientList:
        if patientID == patient.get_patient_id():
            print(patient)
            name = input("Enter new name: ")
            patient.set_name(name)
            diagnosis = input("Enter new diagnosis: ")
            patient.set_diagnosis(diagnosis)
            gender = input("Enter new gender: ")
            patient.set_gender(gender)
            age = input("Enter new age: ")
            patient.set_age(age)
            print("Patient with id", patientID, "successfully modified\n")
            foundPatient = True
    if not foundPatient:
        print("Patient with ID", patientID, "not found\n")
    display_list_of_patients(patientList)

#  Function: display_list_of_patients
#
#  This function will print out all of the the patients in the patient list
#
#  Parameters: patientList - required parameter (List of Patient) - a list of all patients
#  Returns   : None
def display_list_of_patients(patientList):
    for patient in patientList:
        print(patient)

#  Function: write_patients_list_to_file
#
#  This function writes all the patients in the in the patient list to the "patients.txt" 
#  file in the format from format_file_layout() in the Patient class.
#
#  Parameters: patientList - required parameter (List of Patient) - a list of all patients
#  Returns   : None
def write_patients_list_to_file(patientList):
    patientFile = open(r'patients.txt', 'w')
    for patient in patientList:
        patientFile.write(patient.format_file_layout())
    patientFile.close()

#  Function: add_patient_to_list
#
#  This function asks the user for an id and checks if it is in the patient list. If
#  it isn't, it will then asks for the patients name, diagnosis, gender, and age and appends this
#  patient to the end of the patient list.
#
#  Parameters: patientList - required parameter (List of Patient) - a list of all patients
#  Returns   : None
def add_patient_to_list(patientList):
    patientID = input("Enter Patient ID: ")
    patientFound = find_patient_by_id(patientList, patientID)
    if(patientFound != -1):
        print("Patient with ID", patientID, "already exists - cannot add")
    else:
        name = input("Enter Patient name: ")
        diagnosis = input("Enter Patient diagnosis: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        patient = Patient(patientID, name, diagnosis, gender, age)
        patientList.append(patient)
        print("Patient with id", patientID, "successfully added")


#  Function: menu
#
#  This function asks the user to pick an option from a list and returns it
#
#  Parameters: menuName - required parameter (String) - the menu header
#            : menuDictionary - - required parameter (List of String) - the list of options
#  Returns   : menuOption - (int) - the chosen menu option
def menu(menuName, menuDictionary):
    print("ARH Management System")
    print(menuName + "\n")
    for menuItem in menuDictionary:
        print(menuItem)
    while True:
        menuOption = input("Enter option: ")
        if(menuOption.isdigit() and int(menuOption) >= 0 and int(menuOption) < len(menuDictionary)):
             print()
             return int(menuOption)

#  Function: main
#
#  This function lets the user choose to manage Doctors or Patient. The user can choose to close 
#  application to end the program.
#
#  Parameters: None
#  Returns   : None
def main():
    menuDictionary = ["1 - Doctor", 
                      "2 - Patient",
                      "0 - Close Application",]
    menuOption = menu("    Main Menu", menuDictionary)
    while menuOption != 0:
        match menuOption:
            case 1:
                manage_dr()
            case 2:
                manage_patient()
        menuOption = menu("    Patient's Menu", menuDictionary)
    print("ARH Management System successfully closed")

if __name__ == "__main__":
    main()