# import psycopg2
# from faker import Faker
# import random
# from datetime import datetime
# import string


# fake = Faker()
# DB_HOST = 'localhost'
# DB_NAME = 'medical clinic'
# DB_USER = 'postgres'
# DB_PASS = '1234'


# # connection with database
# conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
#                         password=DB_PASS, host=DB_HOST)


# # cursor
# cur = conn.cursor()


# def loadingData():
#     doctorData = []
#     cur.execute("SELECT patient_id, patient.name, patient.address, patient.phone, doctor.name FROM patient INNER JOIN doctor ON patient.doctor_id = doctor.doctor_id")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#         doctorData.append(row)
#     return doctorData


# doctor = loadingData()


# # function with fake data for table clinic


# def fakeDataClinic():
#     for i in range(1, 6):
#         fId = i
#         fName = fake.name() + ' Clinic'
#         fCountry = fake.country()
#         fCity = fake.city()
#         fMPQ = i + random.randint(10, 50)
#         query = "INSERT INTO clinic (clinic_id, name, country, city, max_patients_quantity) values (%s, %s, %s, %s, %s)"
#         values = (fId, fName, fCountry, fCity, fMPQ)
#         cur.execute(query, values)
#     return


# # function with fake data for table block:


# def fakeDataBlock():
#     blockNames = ['cardiology', 'neurology', 'orthopedics', 'intensive care', 'pulmonology',
#                   "children's ward", 'chemotherapy', 'otolaryngology', 'neonatology', 'hospital emergency ward']
#     for i in range(1, 20):
#         randomBlock = random.randint(0, len(blockNames))
#         fId = i
#         fName = blockNames[randomBlock-1]
#         fFloor = random.randint(1, 5)
#         fRoom = random.randint(1, 20)
#         fClinic = random.randint(1, 5)
#         query = "INSERT INTO block (block_id, name, floor, room_quantity, clinic_id) values (%s, %s, %s, %s, %s)"
#         values = (fId, fName, fFloor, fRoom, fClinic)
#         cur.execute(query, values)
#     return


# # function with fake data for table room


# def fakeDataRoom():
#     for i in range(1, 80):
#         fId = i
#         fNumber = random.randint(1, 80)
#         fBQ = random.randint(1, 6)
#         fBlock = random.randint(1, 19)
#         query = "INSERT INTO room (room_id, number, bed_quantity, block_id) values (%s, %s, %s, %s)"
#         values = (fId, fNumber, fBQ, fBlock)
#         cur.execute(query, values)
#     return


# # function with fake data for table doctor


# def fakeDataDoctor():
#     for i in range(1, 20):
#         fId = i
#         fName = fake.name()
#         fAge = random.randint(30, 70)
#         fClinic = random.randint(1, 5)
#         query = "INSERT INTO doctor (doctor_id, name, age, clinic_id) values (%s, %s, %s, %s)"
#         values = (fId, fName, fAge, fClinic)
#         cur.execute(query, values)
#     return


# # function with fake data for table nurse


# def fakeDataNurse():
#     for i in range(1, 40):
#         fId = i
#         fName = fake.name()
#         fAge = random.randint(30, 70)
#         fClinic = random.randint(1, 5)
#         query = "INSERT INTO nurse (nurse_id, name, age, clinic_id) values (%s, %s, %s, %s)"
#         values = (fId, fName, fAge, fClinic)
#         cur.execute(query, values)
#     return


# # function with fake data for table stay


# def fakeDataStay():
#     for i in range(1, 200):
#         fId = i
#         fStart = fake.date_between_dates(date_start=datetime(
#             2020, 1, 1), date_end=datetime(2020, 12, 31))
#         fEnd = fake.date_between_dates(
#             date_start=datetime(2021, 1, 1), date_end=datetime(2021, 9, 9))
#         query = "INSERT INTO stay (stay_id, start_time, end_time) values (%s, %s, %s)"
#         values = (fId, fStart, fEnd)
#         cur.execute(query, values)
#     return


# # function with random block of chars


# def random_char(y):
#     return ''.join(random.choice(string.ascii_letters) for x in range(y))


# # function with fake data for table medicines


# def fakeDataMedicines():

#     brandNames = ['Roche', 'Novartis', 'Merck', 'Sanofi', 'GSK', 'Gilead', 'Pfizer', 'J&J',
#                   'AbbVie', 'Bayer' 'AstraZeneca', 'Amgen', 'Teva', 'Eli Lilly', 'Bristol-Myers']
#     typeNames = ['antibiotic', 'anti-depressant', 'anti- inflammatory drug', 'antiseptic', 'aspirin', 'capsule', 'cough sweet', 'ear drops', 'eye drops', 'hydrogen peroxide',
#                  'insulin', 'iodine', 'laxative', 'ointment', 'pain killer', 'sedative', 'suppository', 'lozenges', 'vaccine', 'vitamin']
#     for i in range(1, 200):
#         randomBrand = random.randint(0, len(brandNames))
#         randomTypes = random.randint(0, len(typeNames))
#         fId = i
#         fBrand = brandNames[randomBrand-1]
#         fTypes = typeNames[randomTypes-1]
#         fName = random_char(7)
#         fDesc = fake.sentence(nb_words=8)
#         query = "INSERT INTO medicines (medicines_id, brand, type, name, description) values (%s, %s, %s, %s, %s)"
#         values = (fId, fBrand, fTypes, fName, fDesc)
#         cur.execute(query, values)
#     return


# # function with fake data for table patient


# def fakeDataPatient():
#     for i in range(200):
#         fId = i
#         fName = fake.name()
#         fAddress = fake.address()
#         fPhone = fake.phone_number()
#         fMedicines = random.randint(1, 199)
#         fStay = random.randint(1, 199)
#         fRoom = random.randint(1, 79)
#         fDoctor = random.randint(1, 19)
#         fNurse = random.randint(1, 39)
#         query = "INSERT INTO patient (patient_id, name, address, phone, medicines_id, stay_id, room_id, doctor_id, nurse_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#         values = (fId, fName, fAddress, fPhone, fMedicines,
#                   fStay, fRoom, fDoctor, fNurse)
#         cur.execute(query, values)
#     return


# # query execute
# # fakeDataClinic()
# # fakeDataBlock()
# # fakeDataRoom()
# # fakeDataDoctor()
# # fakeDataNurse()
# # fakeDataStay()
# # fakeDataMedicines()
# # fakeDataPatient()
# # loadingData()


# # commit changes
# conn.commit()

# # cursor close
# cur.close()

# # close connection with database
# conn.close()
