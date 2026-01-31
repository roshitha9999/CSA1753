import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain',
                'Overcast','Sunny','Sunny','Rain','Sunny','Overcast',
                'Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool',
                    'Mild','Cool','Mild','Mild','Mild','Mild',
                    'Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal',
                 'Normal','High','Normal','Normal','Normal','High',
                 'Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong',
             'Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes',
                    'No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)


le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])


X = df.drop('PlayTennis', axis=1)
y = df['PlayTennis']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



model = DecisionTreeClassifier()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
