import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = GaussianNB()       # no scaling needed
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(confusion_matrix(y_test, pred))

new_student = X_test.iloc[[0]]         # one student from the test set
print("Pass probability:", model.predict_proba(new_student)[0][1].round(2))