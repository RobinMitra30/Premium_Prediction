### END TO END MACHINE LEARNING PROJECT ###

Insurance Premium Prediction:
To give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. I am considering variables as age, sex, BMI, number of children, smoking habits and living region to predict the premium. This can assist a person in concentrating on the health side of an insurance policy rather than the ineffective part.

_ Data source _: https://www.kaggle.com/noordeen/insurance-premium-prediction

Approach:

Loading the dataset using Pandas and performing basic checks like the data type of each column and any missing values.
Performed Exploratory data analysis:
Visualized each predictor or independent feature with the target feature and found that there's a direct proportionality between cement and the target feature while there's an inverse proportionality between water and the target feature.
To get even more better insights, plotted both Pearson and Spearman correlations, which showed the same results as above.
The distribution of the target feature, expenses was in Normal distribution with a very little right skewness.
Checked for the presence of outliers in all the columns

Experimenting with various ML algorithms:
First, tried Linear regression models. Performance metrics are calculated for the approach. The test RMSE score is a little bit lesser compared to other approaches. Then, performed a residual analysis and the model satisfied all the assumptions of linear regression.
Next, tried various tree based models, performed hyperparameter tuning using the GridSearchCV, and found the best hyperparameters for each model. Then, pick the top features as per the feature importance of each model. Models, evaluated on both the training and testing data and recorded the performance metrics.
Based on the performance metrics of both the linear and the tree-based models, the gradient-boosting regressor performed the best, followed by the random forest regressor. 

Deployment: 
Deployed the Gradient Boosting regressor model using Flask, which works in the backend part while for the frontend UI Web page, used HTML5.


So, now we can find the insurance premium quickly by just passing the mentioned details as input to the web application 

Screenshots
![deployment](https://github.com/RobinMitra30/Premium_Prediction/assets/115272817/af01332a-77a2-4324-836f-4ca236993488)
