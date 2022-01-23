import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pickle

# Load the csv file
url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
df = pd.read_csv(url)
print(df.head())

# Select independent and dependent variable
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test= sc.transform(X_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

new_samples = np.array([[5.1, 3.5, 1.4, 0.2], [5.8, 3.1, 5.0, 1.7]], dtype=np.float32)
predictions = classifier.predict(new_samples)

print(predictions)



# Make pickle file of our model
pickle.dump(classifier, open("model.pkl", "wb"))


