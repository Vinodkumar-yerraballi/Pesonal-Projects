# Personal Projects

## 1. Bigbasket Analysis:
[link](https://github.com/Vinodkumar-yerraballi/Pesonal-Projects/blob/main/BigBasker_analysis/Big%20Basket.ipynb)
    
Bigbasket is the largest online grocery supermarket in India. Was launched somewhere around in 2011 since then they've been expanding their business. Though some new competitors have been able to set their foot in the nation such as Blinkit etc. but BigBasket has still not loose anything - thanks to ever expanding popular base and their shift to online buying.

Firstly, we received the dataset and started with data preprocessing steps such as loading the data, checking information and null values, and checking for duplicate values. After that, we performed some EDA using matplotlib, seaborn, and plotly libraries, where we created pie charts, bar charts, pivot tables, and boxplots. As the dataset had a description column which was text-based, we utilized natural language processing techniques to convert it into a vector format. We also converted the categorical columns into numerical format using labelencoder. Once all these techniques were applied, the data was ready for modeling. This was a regression problem, where we aimed to predict the price of a product using several regression algorithms. Finally, we used the accuracy_score metric to evaluate the performance of the Linear Regression and DecisionTreeRegressor models.

## 2. Commanwealth-games-2022
[link](https://github.com/Vinodkumar-yerraballi/Pesonal-Projects/tree/main/Commanwealth-games-2022)

This is the data for the 2022 Commonwealth Games. As usual, we followed the data preprocessing steps and then asked questions about the data while visualizing it. Here are some of the questions that were asked.
  '''
  EXPLORATORY DATA ANALYSIS
  Questions :

How is the descriptive analysis of the data?
What are 10 countries that have highest number of total gold medal?
What are 10 countries that have highest number of total silver medal?
What are 10 countries that have highest number of total bronze medal?
What are 10 countries that have highest number of total medal?
What are 10 countries that have lowest number of total gold medal?
What are 10 countries that have lowest number of total silver medal?
What are 10 countries that have lowest number of total bronze medal?
What are 10 countries that have lowest number of total medal?
How is the distribution of total gold medal between countries?
How is the distribution of total silver medal between countries?
How is the distribution of total bronze medal between countries?
Are total gold medal, total silver medal, total bronze medal affect the country rank in 2022 Common Wealth Games Medal Standings?
How is the correlation between rank with total gold medal, total silver medal and total bronze medal?
  '''
We asked these type of questions to the data

## 3. Credit card frud detection
[link](https://github.com/Vinodkumar-yerraballi/Pesonal-Projects/tree/main/Credit-card_fraud-detection)

In the project, we used two datasets. The first dataset was an imbalanced dataset, and the second one was a classification problem. We started with the usual data preprocessing steps, such as loading the data, removing null values, and dropping duplicates. After that, we performed some EDA to gain insights into the data. Then, we applied various techniques to balance the imbalanced data, such as SMOTE, NearMiss, and RandomOver. By doing so, we balanced the label data, and the data became ready for modeling. Since it was a classification problem, we applied various classification algorithms, and we got good accuracy with the RandomForest classifier.

In the second dataset, we used a statistical method called variance inflation factor to identify the columns with a VIF value greater than 5 and remove them from the data. After that, we applied several classification algorithms, and BernoulliNB gave the best accuracy score for the data.

## 4. E-Commerce Projects
[link](https://github.com/Vinodkumar-yerraballi/Pesonal-Projects/blob/main/E-commecre/E-Commerce.ipynb)

This is an E-commerce project aimed at predicting products. The dataset contains several columns such as brand, size, price, selling price, etc. We begin the project by loading the dataset and checking its data types, preprocessing, null values, and duplicate values. During data preprocessing, we remove extra keywords and apply NLP techniques to the "details" column to replace unknown values with the right values. Next, we perform some EDA with the data, including box plots, bar charts, and scatter charts. Finally, the data is ready for modeling, and we reserve 25% for testing and use the remaining data for training. Since it is a regression problem, we apply regression algorithms to predict the root mean squared error, and we find the least root mean squared error for the data.

## EDA 
[EDA](https://github.com/Vinodkumar-yerraballi/Pesonal-Projects/tree/main/EDA)

We have worked with multiple datasets, including world population, customer shopping, Netflix, and sales data. Our first step is always to preprocess the data, including handling missing values and duplicates. Next, we perform exploratory data analysis (EDA) using various visualization techniques like bar plots, pie charts, tables, boxplots, histograms, and scatter plots to identify patterns and ask relevant data science questions.

For the world population dataset, we focused on visualizing the countries with the highest and lowest populations. For the customer shopping dataset, we plan to apply clustering techniques after converting categorical columns to numerical and standardizing the data. The Netflix dataset allowed us to visualize the number of movies released in each year, the most common directors, and the countries with the most movies released. Finally, for the sales data, we used EDA techniques like bar plots, pie charts, and scatter plots.

After completing EDA, we reserve 25% of the data for testing and use the remaining data for training. Since it is a regression problem, we apply regression algorithms to predict the root mean squared error, and we find the least root mean squared error for the data. Additionally, we used an ANN method using TensorFlow and achieved a low mean-squared-error. Overall, our experience in data preprocessing, EDA, and modeling has prepared us for this position.


## 5.Flight delay project 
[Flight delay projects](https://github.com/Vinodkumar-yerraballi/Pesonal-Projects/blob/main/Flight_delay/Flight_Delay_prediction_.ipynb)

 The dataset was taken from Kaggle and loaded into Jupyter Notebook for data preprocessing. Techniques such as removing null values, duplicates, and correcting data types were applied. EDA was then performed to identify the busiest airlines and airports at different times. Various questions were asked of the data, and visualizations were created using matplotlib, seaborn, and plotly. The groupby and pivot table functions were utilized to extract meaningful information from the data. All categorical columns were converted into numerical values using label encoder. The data was split into training and testing sets, and classification algorithms were applied as this was a classification problem. Logistic Regression and Random Forest were used, which achieved an accuracy score of 60%. To improve the model, ANN was used with Tensorflow libraries, resulting in an accuracy score of around 68% after 20 epochs.

## 6.Frud detection

[Frud detection](https://github.com/Vinodkumar-yerraballi/Pesonal-Projects/blob/main/Frud_detection/INSAD%20Data%20science%20.ipynb)

This is the beginning of my data science journey. I obtained a dataset from Kaggle and loaded it into Jupyter Notebook. I performed some EDA on the data, visualizing the data using bar plots, box plots, and pie charts. I then converted all categorical columns into numerical values and created two variables, one independent and the other dependent. Once I divided the data into training and testing sets, I normalized it using the standard scaler. We applied classification algorithms to the data, as it was a classification problem, which resulted in a good accuracy score. I also visualized the classification report and confusion matrix