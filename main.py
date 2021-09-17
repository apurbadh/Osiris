import numpy as np
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

symptoms = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech',
'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
'red_sore_around_nose', 'yellow_crust_ooze']

diseases = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcerdiseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension', ' Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)', 'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis', 'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']

df = pd.read_csv("training.csv")

df.replace({'prognosis' : {'Fungal infection' : 0, 'Allergy' : 1, 'GERD' : 2, 'Chronic cholestasis' : 3,
'Drug Reaction' : 4, 'Peptic ulcer diseae' : 5, 'AIDS' : 6, 'Diabetes ' : 7, 'Gastroenteritis'
: 8, 'Bronchial Asthma' : 9, 'Hypertension ' : 10, 'Migraine' : 11, 'Cervical spondylosis' : 12, 'Paralysis (brain hemorrhage)' : 13, 'Jaundice' : 14, 'Malaria' : 15, 'Chicken pox' : 16, 'Dengue' : 17, 'Typhoid' : 18, 'hepatitis A' : 19, 'Hepatitis B' : 20, 'Hepatitis C' : 21, 'Hepatitis D' : 22, 'Hepatitis E' : 23, 'Alcoholic hepatitis' : 24, 'Tuberculosis' : 25, 'Common Cold' : 26, 'Pneumonia' : 27, 'Dimorphic hemmorhoids(piles)' : 28, 'Heart attack' : 29, 'Varicose veins' : 30, 'Hypothyroidism' : 31, 'Hyperthyroidism' : 32, 'Hypoglycemia' : 33, 'Osteoarthristis' : 34, 'Arthritis' : 35, '(vertigo) Paroymsal  Positional Vertigo' : 36, 'Acne' : 37, 'Urinary tract infection' : 38, 'Psoriasis' : 39, 'Impetigo' : 40}},inplace=True)


X= df[symptoms]
y = df[["prognosis"]]

np.ravel(y)

testing_df = pd.read_csv("testing.csv")
testing_df.replace({'prognosis' : {'Fungal infection' : 0, 'Allergy' : 1, 'GERD' : 2, 'Chronic cholestasis' : 3,
'Drug Reaction' : 4, 'Peptic ulcer diseae' : 5, 'AIDS' : 6, 'Diabetes ' : 7, 'Gastroenteritis'
: 8, 'Bronchial Asthma' : 9, 'Hypertension ' : 10, 'Migraine' : 11, 'Cervical spondylosis' : 12, 'Paralysis (brain hemorrhage)' : 13, 'Jaundice' : 14, 'Malaria' : 15, 'Chicken pox' : 16, 'Dengue' : 17, 'Typhoid' : 18, 'hepatitis A' : 19, 'Hepatitis B' : 20, 'Hepatitis C' : 21, 'Hepatitis D' : 22, 'Hepatitis E' : 23, 'Alcoholic hepatitis' : 24, 'Tuberculosis' : 25, 'Common Cold' : 26, 'Pneumonia' : 27, 'Dimorphic hemmorhoids(piles)' : 28, 'Heart attack' : 29, 'Varicose veins' : 30, 'Hypothyroidism' : 31, 'Hyperthyroidism' : 32, 'Hypoglycemia' : 33, 'Osteoarthristis' : 34, 'Arthritis' : 35, '(vertigo) Paroymsal  Positional Vertigo' : 36, 'Acne' : 37, 'Urinary tract infection' : 38, 'Psoriasis' : 39, 'Impetigo' : 40}},inplace=True)

X_test = testing_df[symptoms]
y_test = testing_df[["prognosis"]]

np.ravel(y_test)

def decisionTree():
	model = DecisionTreeClassifier()   
	model = model.fit(X,y)
	return model



def randomForest():
	model = RandomForestClassifier()
	model = model.fit(X,np.ravel(y))
	return model



def naiveBayes():
	model = GaussianNB()
	model = model.fit(X,np.ravel(y))
	return model


descisionTreeModel = decisionTree()
randomForestModel = randomForest()
naiveBayesModel = naiveBayes()   

#Desicion Tree
y_pred = descisionTreeModel.predict(X_test)
tree_accuracy = accuracy_score(y_test, y_pred)
print(f"Desicion Tree : {int(tree_accuracy * 100)} %")

#Random Forest
y_pred = randomForestModel.predict(X_test)
forest_accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest : {int(forest_accuracy * 100)} %")

#Naive Bayes
y_pred = naiveBayesModel.predict(X_test)
naive_accuracy = accuracy_score(y_test, y_pred)
print(f"Naive Bayes : {int(naive_accuracy * 100)} %")


pickle.dump(descisionTreeModel, open("desicionTree.model", "wb"))
pickle.dump(randomForestModel,  open("randomForest.model", "wb"))
pickle.dump(naiveBayesModel, open("naiveBayes.model", "wb"))

def predict(lst):
	num_list = []
	for i in symptoms:
		if i in lst:
			num_list.append(1)
		else:
			num_list.append(0)
	return [num_list]

def prediction(lst):
	answer = ""
	answer1 = descisionTreeModel.predict(predict(lst))
	answer2 = randomForestModel.predict(predict(lst))
	answer3 = naiveBayesModel.predict(predict(lst))

	answer = [answer1, answer2, answer3]
	return diseases[most_frequent(answer)[0]]

ans = prediction(['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever'])
print(ans)