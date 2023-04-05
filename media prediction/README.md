# Media Predictions 

Dataset Link: https://www.kaggle.com/datasets/ramjasmaurya/medias-cost-prediction-in-foodmart
PREDICT COST ON MEDIA CAMPAIGNS IN FOOD MART OF USA .
ON THE BASIS OF 60K CUSTOMERS INCOME ,PRODUCT,PROMOTION AND STORE FEATURES.

ABOUT FOODMART:
Food Mart (CFM) is a chain of convenience stores in the United States. The private company's headquarters are located in Mentor, Ohio, and there are currently approximately 325 stores located in the US. Convenient Food Mart operates on the franchise system.

Food Mart was the nation's third-largest chain of convenience stores as of 1988.

The NASDAQ exchange dropped Convenient Food Mart the same year when the company failed to meet financial reporting requirements.

Carden & Cherry advertised Convenient Food Mart with the Ernest character in the 1980s.

Correlation Matrix
Why?
A correlation matrix is a table showing correlation coefficients between variables.

There are three broad reasons for computing a correlation matrix:
To summarize a large amount of data where the goal is to see patterns. In our example above, the observable pattern is that all the variables highly correlate with each other. To input into other analyses. For example, people commonly use correlation matrixes as inputs for exploratory factor analysis, confirmatory factor analysis, structural equation models, and linear regression when excluding missing values pairwise. As a diagnostic when checking other analyses. For example, with linear regression, a high amount of correlations suggests that the linear regression estimates will be unreliable.
A pie chart is a circular statistical chart, which is divided into sectors to illustrate numerical proportion.
If you're looking instead for a multilevel hierarchical pie-like chart, go to the Sunburst tutorial.

Pie chart with plotly express¶

Histograms
In statistics, a histogram is representation of the distribution of numerical data, where the data are binned and the count for each bin is represented. More generally, in Plotly a histogram is an aggregated bar chart, with several possible aggregation functions (e.g. sum, average, count...) which can be used to visualize data on categorical and date axes as well as linear axes.

After the EDA process we do Modeling

# Modeling
in the modeling part we split the data input inputs and target variables after that we divided into train an test data,
This is a regression problem we predict the cost in the dataset.
we use several algorithms to predict the output such as LinearRegressor, DecisionTreeRegressor, RandomForestRegressor,XGBRegressor and LGBRegressor.

From the Above algorithms the DecisionTreeRegressor, RandomForestRegressor,XGBRegressor and LGBRegressor give the better accuracy_score.
