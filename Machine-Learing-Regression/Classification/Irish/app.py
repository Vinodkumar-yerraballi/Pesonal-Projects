import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


# load the data
data = pd.read_csv("Iris.csv")
data = data.drop(['Id'], axis=1)

X = data.drop(['Species'], axis=1)
y = data['Species']

# Modeling

model = LogisticRegression()
model.fit(X, y)

# Create the inputes


def main():
    SepalLengthCm = st.slider("Enter SepalLengthCm", 4.3, 7.9, 4.3)
    SepalWidthCm = st.slider("Enter SepalLengthCm", 2.0, 4.4, 2.0)
    PetalLengthCm = st.slider("Enter SepalLengthCm", 1.0, 6.9, 1.0)
    PetalWidthCm = st.slider("Enter SepalLengthCm", 0.1, 2.5, 0.1)

    if st.button("Predict"):
        result = model.predict(
            [[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
        st.success(f'The flower is {result[0]}')


if __name__ == "__main__":
    main()
