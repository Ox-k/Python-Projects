<h1 align="center">Machine Learning</h1>

Machine learn is when a __model's algorithm__ is exposed to vast amount of data to make it more __proficient__ at doing its task.

it enables computers to __learn__ and __Adapt__
<br>

<h3>Machine learning categories</h3>
The categories of machine learning:

* Supervised
* un-supervised
* re-inforcement

<br>

__1️⃣ Supervised__ <br>

This is when the algorithm is provided with labeled data and the correct answer is know from the start. <br>
The algorithm can create new data based on a reference data.<br>

_its like learning in a textbook whose quizzes have answers at the end of the textbook_ <br><br>

Some common examples are:

* Image recognition: classifies images based on their content
* Spam filtering: filters emails based on pre-defined characteristics
* Predictive modelling: forcasts future trends based on historical data
<br>

__2️⃣ Un-supervised Learning__ <br>

This inolves presenting the algorithm with un-labeled data.

In this case, the correct output or answers are not provided.

The algorithm has to discover hidden patterns without guide.


_its like exploring a new city without a map_


__where is it used__

* customer segmentation
* Anomaly detection
* Dimensionality reduction


__4️⃣ Re-enforcement learning__

This has an agent learner, and interracts with external environment to improve from feedback

__where it is used__

* Game playong
* Robotics
* Personalized recommendations

### Key termininologies in machine learning

__Features__ : The descriptive attributes

These categorise the data that we work with.

They have individual pieces of information that provides insights into patterns in the data

These could be like:

* customer name
* customer age
* purchase history
* browsing behaviour
* thier demographic information
* and so on


For the model's algorithm to make accurate predictions and generalizations,
we need to select relevant and informative features

Features can be combined to come up with new features.

_example_

_Combining customer age and purchase history to represent thier loyalty to the store_
<br><br>

__labels__ : The target outcome

labels serve as the desired out put for a given set of features.

_example_

_marking a purchase as "1" or "0" indicates the quantity of the customer purchase history_

These are particulary important in __supervised learning__ .

Labels also determine the accuracy and effectiveness of a learning model.
<br><br>

__Models__ : The mathematical representation

A model is the representation of the output data.
It is a mathematical representatuin of the relationship between features and labels.

__Common models__

* __Lenear regression__ : this models the relationship between features and continous label using a linear equation.
<br> it is often used for predecting  nunmerical values like house prices and dales figures
* __Decision trees__ : creates a tree-like decision baed on featurev values, leading to a predicted label.
* __Support vector machines__
* __Neural Networks__: mimics the human brain's structuer wuth interconnected laters of artificial neurons.
<br> These are capable of learning highly complex patterns.<br><br>


__Algorithms__ : The learning process

they provide the instructions and procedures that guide the model's learning process.

They also define how the model extracts patterns from the data, adjusts its internal parameters and make predictions<br><br>

__Overfitting__ : When models learn too much.

In this case, the machine learning becomes excessively specialized in the training data.

This hinders it to generalize to new, unseen data.

An ovderfitted model will perform extermely well on training data but perform poorely on new data

__How to mitigate overfitting__

* __Regularization__ : adding penalty terms to model's loss of function
* __Early stoppint__ : stop the training beore the model starts memorizing instead if generalizing
* __Coss-validation__ : dividing training data into multiple subsets/folds.<br>
the model is trained on some folds and then evaluated on the remaining unseen folds.

<br><br>

### Model Evaluation


#### Key benefits of Model Evaluation

* Identify and fix error to market target improvements
* avoid over-fitting
* Choose the best model for the problem and data
* Built trust

#### Techniques and Metrics

* Accuracy: measures the proportions of the correct predictivnesss measured by a model.
* recesion and recall: focus on specific type of errors. Precision tells how many of the false positives predicted by the model were actually correct minimizing false positive. 
* Recall is how many false  positives the model was actuall able to recall
* F-1 Score: this measures the false positives and negatives by giving them a weight. This is used when a model posiive and negative predictions are crucial to the data analysis at hand.

```
This is particulary useful in spam email detection by filtering out most of the spams and letting couple slip through so that it does not mis-classify an important email as spam
```

* Confusion matrix: This is a table that shows true positives and negatives as well as false positives and negatives to show a comphrensive view of the model across different classes of data.

##### Digging deep into confusion matrix

Confusion matrix assesses the effectiveness of a model and and their performance as they work.

It shows model's predictions againts the data labels

|![consufion matrix](image.png)

__What does this mean__

In a confusion matrix, the cells represent the following:

- **True Positives (TP)**: This is typically located in the **top left cell**. It indicates the number of instances where the model correctly predicted a positive outcome.

- **True Negatives (TN)**: This is found in the **bottom right cell**. It shows the number of instances where the model correctly predicted a negative outcome.

- **False Positives (FP)**: This is located in the **top right cell**. It represents the instances where the model incorrectly predicted a positive outcome.

- **False Negatives (FN)**: This is in the **bottom left cell**. It indicates the instances where the model incorrectly predicted a negative outcome.


__Limitations of confusions matrix__

* It can oversimplify the complexities of multi-class classification problems. As the number of classes to analysi increanses, above the above cell represenation, it can be harder to represent this accurarately. 

This can be corrected by using __HeatMaps__ instead where the intensity of the color represents the frequency of the predictions.

* Multi-classification struggles: confusion matrix is greate at predicting __X__ or __Not X__ type of scenarios.

__example__

_Willthe customer __buy__ or __not buy__ something today_

When categories go beyond this it struggles  to accurately predict outcomes.

__Example__

_if emails had various categoris such as __spam__, __not spam__, __social__, __promotions_ and so on._

In this case, each class would have its own set or positives and negatives creating a muhch harder matrix that can be hard to interprete.

* A confusion matrix predicts and assing high scores to higher accuracies.  That means if we are trying to predicts teh positives but the negatives outnumber the positives, it will show higher accuracy of the negatives.

##### HeatMaps

- HeatMaps providesa much easier predection of class frequency by assigning higher intensitity color to the more frequent predictions
- a heatmap basically use color intensity to visualize prediction frequency of a class

### Best Practices of Analyzing and Presenting Datasets

#### 1 Understanding the Data: _The foundation of insight_

Deep understanding of the dataset you are working with.

__Explore the data's__

* Structure: to understand relationship between variables
* variables
* A summary of its statistical properties: quick view of the data


This step takes care of issues such as:

- missing data ... addressed through _imputation_nor fully _removed_
- outliers
- biases

##### Pro tips

__Tip 1__ Always start with data exploration.

Use functions like _.head(), .info(), and .describe()_ to understand the dataset's strucutre and identify missing values or outliers

__Tip 2__ Missing values?

Try simpler techniques like _mean imputation_ first. for _outliers_ visualize them using box plots before deciding to remove or transform

__Tip 3__ Clean and pre-process your data thoroughly. Good data preparations leads to better analysis and modeling outcomes


#### 2 Feature Engineering: _Crafting predictive power_

Cretively construct new features from the data or transform existing features to enhance the predictive power of machine learning models.

```yml
Basicall : taking raw data, adding labels and titles and other features that will help a learning model make better predictions
```


__Example__

_by leveraging a customers purchase habits, you can create a feature such as __Customer Life Time Value__ a feature that identifies high value customers, to whom we can craft retention-advertisment instead of attraction-advertisment_


##### Feature Engineering Pro-Tips

__Tip 1__ Focus on creating features that are directly related to the business problem.

__Tip 2__ Analyse customer behaviour pattern for early signs of chirn. Example, look for trends in usage or dissatisfaction metrics.


#### 3 Model Selection and Training: _Choosing the right tool_

In this stage, we choose the the appropriate machine learning model for the churn prediction.

For example, if we are dealing with binary classification problems, we could use __Logictic regression__, this is a model that predicts outcomes that have two possible categories, _true_ or _false_ .

__Consider this scenario to illustrate this__

_Imagine you're trying to decide whether to bring an umbrella based on the weather. You might consider factors like cloud cover, humidity, and temperature. __Logistic regression__ does something similar by weighing these factors to give you a probability score between 0 and 1, indicating how likely it is that a customer will churn. If the score is above a certain threshold (like 0.5), you might predict that the customer will leave; if it's below, you predict they will stay._

##### Decision trees and Random Forests

__Decision tree__ partitions data  based on feature values:

* Each leaf represents a prediction

__Random Forest__ is the ensemble of several dicision tree.

#### Model evaluation and selection

Evaluating the preformance of various models and select the most suitable one.


### Regression Metrics
