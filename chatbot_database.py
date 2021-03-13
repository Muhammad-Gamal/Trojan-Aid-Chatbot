# Importing Required Modules & Packages
from prettytable import PrettyTable
import sqlite3

# Creating Connection & Cursor
conn = sqlite3.connect("chatbot.db")
curs = conn.cursor()

# Checking if Tables are existed
curs.execute(""" DROP TABLE IF EXISTS Patients""")
curs.execute(""" DROP TABLE IF EXISTS Diseases""")
curs.execute(""" DROP TABLE IF EXISTS Prognosis_Reports""")

# Creating Tables
# Creating [Patients] Table
curs.execute('''CREATE TABLE Patients (
        p_id INTEGER NOT NULL UNIQUE,
        p_name TEXT NOT NULL,
        age INTEGER,
        phone INTEGER UNIQUE,
        email TEXT UNIQUE,
        sex TEXT,
        PRIMARY KEY(p_id)
    );''')

# Inserting in [Patients] Table
curs.execute('''INSERT INTO Patients(p_id, p_name, age, sex, phone, email)
                VALUES(1, "Muhammad", 22, "Male", 010178956300, "mogaml.elhady@gmail.com"),
                      (2, "Ahmed", 33, "Male", 01102715209, "ahmed@yahoo.com"),
                      (3, "Mai", 8, "Female", 0862587369, "mai@gmail.com"),
                      (4, "Amr", 18, "Male", 0862587777, "amr@gmail.com"),
                      (5, "Khalid", 28, "Male", 0862587399, "khalid@hotmail.com"),
                      (6, "Maroline", 16, "Female", 0862587769, "maro@outlook.com"),
                      (7, "Kareem", 35, "Male", 0862583369, "kemo@gmail.com"),
                      (8, "Maged", 40, "Male", 0862587333, "maged@gmail.com"),
                      (9, "Fatma", 45, "Female", 0862584568, "fatma@yahoo.com"),
                      (10, "Saleh", 50, "Male", 0862589821, "seleh@gmail.com")
''')

# Creating [Diseases] Table
curs.execute('''CREATE TABLE Diseases (
        d_id INTEGER NOT NULL UNIQUE,
        d_name TEXT NOT NULL,
        description TEXT,
        symptoms TEXT,
        precautions TEXT,
        PRIMARY KEY(d_id)
    );''')

# Inserting in [Diseases] Table
curs.execute('''INSERT INTO Diseases(d_id, d_name, description, symptoms, precautions)
                VALUES(1, "Malaria", 
"An infectious disease caused by protozoan parasites from the Plasmodium family 
that can be transmitted by the bite of the Anopheles mosquito or by a contaminated needle or transfusion.
Falciparum malaria is the most deadly type.", 
"[1]Chills
[2]Vomiting
[3]High_Fever
[4]Sweating
[5]Headache
[6]Nausea
[7]Diarrhoea
[8]Muscle_Pain
", 
"[1]Consult nearest hospital.
[2]Avoid oily food.
[3]Avoid non veg food.
[4]Keep mosquitoes out."),
(2, "Hepatitis A", 
"Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus. 
The virus is one of several types of hepatitis viruses 
that cause inflammation and affect your liver's ability to function.", 
"[1]Joint Pain.
[2]Vomiting.
[3]Yellowish Skin.
[4]Dark Urine.
[5]Nausea.	
[6]Loss of Appetite.
[7]Abdominal Pain.
[8]Diarrhoea.	
[9]Mild Fever.
[10]Yellowing of Eyes.
[11]Muscle Pain.
",
"[1]Consult nearest hospital.
[2]Wash hands through
[3]Avoid fatty spicy food
[4]Medication"),
(3, "Diabetes", "Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. 
Blood glucose is your main source of energy and comes from the food you eat. 
Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.",
"[1]Fatigue.
[2]Weight Loss.
[3]Restlessness.
[4]Lethargy.
[5]Irregular Sugar Level.
[6]Blurred and Distorted Vision.
[7]Obesity.
[8]Excessive Hunger.
[9]Increased Appetite.
[10]Polyuria.
",
"[1]Have Balanced Diet.
[2]Do Exercises.
[3]Consult doctor.
[4]Follow up Sugar Level."),
(4, "Hypertension", "Hypertension (HTN or HT), also known as high blood pressure (HBP), 
is a long-term medical condition in which the blood pressure in the arteries is persistently elevated. 
High blood pressure typically does not cause symptoms.", 
"[1]Headache.
[2]Chest Pain.
[3]Dizziness.
[4]Loss of Balance.
[5]Lack of Concentration.
",
"[1]Meditation.
[2]Salt Baths.
[3]Reduce Stress.
[4]Get proper sleep."),
(5, "Common Cold", "The common cold is a viral infection of your nose and throat (upper respiratory tract). 
It's usually harmless, although it might not feel that way. Many types of viruses can cause a common cold.",
"[1]Continuous Sneezing.
[2]Chills.
[3]Fatigue.
[4]Cough.
[5]High Fever.
[6]Headache.
[7]Swelled lymph  nodes.
[8]Malaise.
[9]Phlegm.
[10]Throat Irritation.
[11]Redness of Eyes.
[12]Sinus Pressure.
[13]Runny Nose.
[14]Congestion.
[15]Chest Pain.
[16]Loss of Smell.
[17]Muscle Pain.
",
"[1]Drink Vitamin 'C' rich drinks.
[2]Take Vapour.
[3]Avoid Cold Food.
[4]Keep Fever in check."),
(6, "AIDS", "Acquired immunodeficiency syndrome (AIDS) is a chronic, potentially life-threatening condition caused by 
the human immunodeficiency virus (HIV). 
By damaging your immune system, HIV interferes with your body's ability to fight infection and disease.",
"[1]Muscle Wasting.
[2]Patches in throat.
[3]High Fever.
[4]Extra MAterial Contacts.
",
"[1]Avoid open cuts.
[2]Wear PPE if possible.
[3]Consult Doctor.
[4]Follow up.
"),
(7, "Typhoid", "An acute illness characterized by fever caused by infection with the bacterium Salmonella typhi. 
Typhoid fever has an insidious onset, with fever, headache, constipation, malaise, chills, and muscle pain. 
Diarrhea is uncommon, and vomiting is not usually severe.",
"[1]Chills.
[2]Vomiting.
[3]Fatigue.
[4]High Fever.
[5]Headache.
[6]Nausea.
[7]Constipation.
[8]Abdominal Pain.
[9]Diarrhoea.
[10]Toxic look (Typhos).
[11]Belly Pain.
",
"[1]Eat High Calorie Vegitables.
[2]Antiboitic therapy.
[3]Consult Doctor.
[4]Medication"),
(8, "Hepatitis C", "Inflammation of the liver due to the hepatitis C virus (HCV), 
which is usually spread via blood transfusion (rare), hemodialysis, and needle sticks. 
The damage hepatitis C does to the liver can lead to cirrhosis and its complications as well as cancer.",
"[1]Fatigue.
[2]Yellowish Skin.
[3]Nausea.
[4]Loss of Appetite.
[5]Yellowing of Eyes.
[6]Family History.
",
"[1]Consult nearest hospital.
[2]Eat healthy food.
[3]Vaccination.
[4]Medication."),
(9, "Heart attack", "The death of heart muscle due to the loss of blood supply. 
The loss of blood supply is usually caused by a complete blockage of a coronary artery, 
one of the arteries that supplies blood to the heart muscle.", 
"[1]Vomiting.
[2]Breathlessness.
[3]Sweating.
[4]Chest Pain.
",
"[1]Call Ambulance.
[2]Chew or Swallow Asprin.
[3]keep calm."),
(10, "Migraine", "A migraine can cause severe throbbing pain or a pulsing sensation,
usually on one side of the head. It's often accompanied by nausea, vomiting, and extreme sensitivity to light and sound.
Migraine attacks can last for hours to days, 
and the pain can be so severe that it interferes with your daily activities.",
"[1]Acidity.
[2]Indigestion.
[3]Headache.
[4]Blurred and distorted vision.
[5]Excessive Hunger.
[6]Stiff Neck.
[7]Depression.
[8]Irritability.
[9]Visual Disturbances.
",
"[1]Meditation.
[2]Reduce stress.
[3]Use poloroid glasses in sun.
[4]Consult Doctor"); 
''')

# Creating [Prognosis_Report] Table
curs.execute('''CREATE TABLE Prognosis_Reports (
        pr_id INTEGER  PRIMARY KEY NOT NULL UNIQUE,
        pr_date TEXT NOT NULL,
        pr_patient TEXT,
        pr_disease TEXT,
        pr_description TEXT,
        pr_symptoms TEXT,
        pr_precautions TEXT,
        pr_pid INTEGER,
        pr_did INTEGER,
        FOREIGN KEY(pr_pid) REFERENCES Patients(p_id),
        FOREIGN KEY(pr_did) REFERENCES Diseases(d_id)
    );''')

# Inserting in [Prognosis_Reports] Table
curs.execute(
    '''INSERT INTO Prognosis_Reports(pr_id,pr_date, pr_patient, pr_disease, pr_description, pr_symptoms, pr_precautions)
                VALUES(1, current_date, (SELECT p_name from Patients WHERE p_id = 1),
                                        (SELECT d_name from Diseases WHERE d_id = 1),
                                        (SELECT description from Diseases WHERE d_id = 1),
                                        (SELECT symptoms from Diseases WHERE d_id = 1),
                                        (SELECT precautions from Diseases WHERE d_id = 1)),
                                        (2, current_date, (SELECT p_name from Patients WHERE p_id = 2),
                                        (SELECT d_name from Diseases WHERE d_id = 2),
                                        (SELECT description from Diseases WHERE d_id = 2),
                                        (SELECT symptoms from Diseases WHERE d_id = 2),
                                        (SELECT precautions from Diseases WHERE d_id = 2)),
                                        (3, current_date, (SELECT p_name from Patients WHERE p_id = 3),
                                        (SELECT d_name from Diseases WHERE d_id = 3),
                                        (SELECT description from Diseases WHERE d_id = 3),
                                        (SELECT symptoms from Diseases WHERE d_id = 3),
                                        (SELECT precautions from Diseases WHERE d_id = 3)),
                                        (4, current_date, (SELECT p_name from Patients WHERE p_id = 4),
                                        (SELECT d_name from Diseases WHERE d_id = 4),
                                        (SELECT description from Diseases WHERE d_id = 4),
                                        (SELECT symptoms from Diseases WHERE d_id = 4),
                                        (SELECT precautions from Diseases WHERE d_id = 4)),
                                        (5, current_date, (SELECT p_name from Patients WHERE p_id = 5),
                                        (SELECT d_name from Diseases WHERE d_id = 5),
                                        (SELECT description from Diseases WHERE d_id = 5),
                                        (SELECT symptoms from Diseases WHERE d_id = 5),
                                        (SELECT precautions from Diseases WHERE d_id = 5)),
                                        (6, current_date, (SELECT p_name from Patients WHERE p_id = 6),
                                        (SELECT d_name from Diseases WHERE d_id = 6),
                                        (SELECT description from Diseases WHERE d_id = 6),
                                        (SELECT symptoms from Diseases WHERE d_id = 6),
                                        (SELECT precautions from Diseases WHERE d_id = 6)),
                                        (7, current_date, (SELECT p_name from Patients WHERE p_id = 7),
                                        (SELECT d_name from Diseases WHERE d_id = 7),
                                        (SELECT description from Diseases WHERE d_id = 7),
                                        (SELECT symptoms from Diseases WHERE d_id = 7),
                                        (SELECT precautions from Diseases WHERE d_id = 7)),
                                        (8, current_date, (SELECT p_name from Patients WHERE p_id = 8),
                                        (SELECT d_name from Diseases WHERE d_id = 8),
                                        (SELECT description from Diseases WHERE d_id = 8),
                                        (SELECT symptoms from Diseases WHERE d_id = 8),
                                        (SELECT precautions from Diseases WHERE d_id = 8)),
                                        (9, current_date, (SELECT p_name from Patients WHERE p_id = 9),
                                        (SELECT d_name from Diseases WHERE d_id = 9),
                                        (SELECT description from Diseases WHERE d_id = 9),
                                        (SELECT symptoms from Diseases WHERE d_id = 9),
                                        (SELECT precautions from Diseases WHERE d_id = 9)),
                                        (10, current_date, (SELECT p_name from Patients WHERE p_id = 10),
                                        (SELECT d_name from Diseases WHERE d_id = 10),
                                        (SELECT description from Diseases WHERE d_id = 10),
                                        (SELECT symptoms from Diseases WHERE d_id = 10),
                                        (SELECT precautions from Diseases WHERE d_id = 10));
    ''')

# Creating a Report by [PrettyTable]
curs.execute('''
SELECT pr_id as ID, 
       pr_date as Report_Date, 
       pr_patient as Patient_Name, 
       pr_disease as Disease, 
       pr_description as Diagnosis,
       pr_symptoms as Symptoms, 
       pr_precautions as Precautions
FROM Prognosis_Reports ORDER BY pr_id''')

col_names = [cn[0] for cn in curs.description]
rows = curs.fetchall()

y = PrettyTable()
y.padding_width = 3
y.add_column(col_names[0], [row[0] for row in rows])
y.add_column(col_names[1], [row[1] for row in rows])
y.add_column(col_names[2], [row[2] for row in rows])
y.add_column(col_names[3], [row[3] for row in rows])
y.add_column(col_names[4], [row[4] for row in rows])
y.add_column(col_names[5], [row[5] for row in rows])
y.add_column(col_names[6], [row[6] for row in rows])
y.align[col_names[1]] = "l"
y.align[col_names[5]] = "l"
y.align[col_names[6]] = "l"

print(y)
# Creating a Report as a Text File
#
# Tabstring = y.get_string()
#
# output = open("Chatbot Reports Data.txt", "w")
# output.write("Reports Data")
# output.write(Tabstring)
# output.close()

# Committing & Closing the Connection
conn.commit()
conn.close()
