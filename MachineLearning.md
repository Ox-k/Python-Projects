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






