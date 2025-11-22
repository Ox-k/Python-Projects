<h1 align="center">Data Analysis and Visualization with Python</h1>
<h2 align="Center"><b>Data Analysis</b> Illuminating the past to inform the present</h2>
<p>Transforming raw data into actionable insights</p>
<h3>Tools</h3>
<ul>
  <li>Python Libraries (pandas, NumPy): </br>
Pandas: provide data structures like DataFrames which are mainly tables</li>
</br>
  NumPy: Enables efficient numerical orpations on data with a single command
  <li>Data Visualization Software (Microsoft PowerBI)</li>
</ul>
<h2 align="center">Careers in data Science</h2>

 ![Static Badge](https://img.shields.io/badge/Careers%20in%20data%20Science-8A2BE2)

 <h3 align="center">Data Engineer</h3>
 <p align="center">The collect and clean data</p>
 <h3 align="center">Data Analysts</h3>
 <p align="center">The clean data and analysi it</p>
 <h3 align="center">Machine learning engineers</h3>
 <p align="center">Theese take the cleaned and explained data and model and deploy them</p>
  <h3 align="center">Data Scientist</h3>
 <p align="center">These are experts at everything above</p>

<br>


<h3 align="center">data analysis</h3>

```
So basically
Data analysis is:
  * Primary goal  : Describe and summerize data to gain insights
  * Skill emphasis: clean data, manipulation, visualization, SQL and domain experience
  * Tools         : Python (Pandas, NumPy), Excel, BI tools and SQL
  * Output        : Reports, Dashboards, Presentations, actioanable recommendations
  * Typical Qs    : What happened? how did it happen? What can we learn from the past
  * Application   : Business intelligence, marketing analytics, financial analysis, fraud detection
```

<h3 align="center">data Science</h3>

```
So basically
Data science is:
  * Primary goal   : Build predictive models and systems to automote decisions and uncover hidded patterns
  * Skills emphasis:  Machine learning, stats, programming, alg design, experimentation
  * Tools          : Python (scikit-learn, PyTorch 🔦), R, could platforms, stats software
  * Output         : Predictive models, alg, automated systems, data products
  * Typical ques   : What will happen, how can we optimize it, can we automate this process
  * Industries     : Recommendation systems, fraud detection, personalization, automation
```


<h3 align="center">data analysis Process</h3>

```
  Collect cata
    ↘️
       define your question about the  data
       collect all the necessary information
       ↘️
          Clean the data
          Use python
          ↘️
            Model the data into visualization
            Use suitable python libraries
            ↘️
              share you findings with colleagues 🧑‍🤝‍🧑
```
 <p><b>Population</b>: subject from where we get the data</p>
 <p><b>Sample</b>: Portion of the population that represents the entire population</p>
 <p><b>Variables</b>: This is issue that we are investigating</p>

 <br>
 <code>Review stats for more info about variables</code>
 <br>
 <u>Example</u>
 <br>
 <p>Consider the code below:</p>
 
```python
import pandas as pd

# Sample data
data = {'age': [25, 30, 35, 40], 
        'gender': ['male', 'female', 'male', 'female'], 
        'income': [50000, 60000, 75000, 55000]}

# Create a DataFrame
df = pd.DataFrame(data)
print(df)
print()
```

<br>
<p>This puts the data into a table form that looks as such</p>
<br>

  
```yml
       age    gender    income
0      25     male       50000
1      30     female     60000
2      35     male       75000
3      40     female     55000
```
<br>
<h3 align="center">Environment for Data Analysis</h3><br>
<code>Jupypter Notebook: Web code editor that lets your control chunks of code</code><br>
<code>Pandas : cleans and organise data</code><br>
<code>NumPy: Math on data</code><br>
<code>MatPlotlib & Apache Superset: Data Visualization</code><br>

<h3 align="center">Jupyter notebook tricks and tips</h3><br>

```yml
Jupyter has:
  - code cells: where code is written. to run code: Shift + Enter
  - Markdown  : allows to format text and add images
      🌟 you can add titles
      🌟 you can add mathematical equations
      🌟 you can add images
      🌟 you can add formatted text
      🌟 you can add hyper links and so on
- AI code generation and auto completion


```
<br>


<img width="568" height="213" alt="Screenshot 2025-11-22 at 11 17 26" src="https://github.com/user-attachments/assets/0d1eeaad-6da9-4378-a099-a9d4dbb44775" />

<br>


```yml
To create a heading: # text

```
<br>
<h3 align="center">Jupyter short cuts</h3><br>

```yml
up 🔼 / down 🔽: these allow you to move up or down cells
Modes:
  Edit mode: editing the content of a cell
  Command mode: lets perform action on a cell.
     Press "esc": to enter command mode
          "A"             : to insert a cell above
          "B"             : to insert a cell below
          "D"x2           : to delete a cell
          "M"             : to switch to "markdown"
          "Y"             : to switch to code
          "Ctrl + Enter"  : to run code [stay in the same cell]
          "Shift + Enter" : to run code [Move to the next cell]

  There are many more other commands.
  Press:
    "Escape" to enter command mode
  Then:
    "H" to pull up the drop dowm menu of the short cuts

  Reminder on some piece of code:
    - write the function
    - press "Shift" + "TAB"
  This will open a hover little documentation of the function implementation

```
<br>

<h3 align="center">Magic functions</h3>
These help you go beyond regular python code
they start with a <code>%</code> sign.<br>
These commands tell jupyter to display the result of the command right there in the book
<br>
<br>
<h4>Example</h4>
<br>

```yml
        %matplotlin inline: this place above the code, will draw the graph of what the data represents
        %%timeit: this added above the code will time how long the code runs
        !pip install library: this will install the library right in the notebook
```

<br>

<h4>Example:</h4>

```yml
        SHOWCASING pandas AND matplotlib
```

```python

import random
import pandas as pd

# 1. Define possible customers
customer_names = [
    "Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince",
    "Ethan Hunt", "Fiona Clarke", "George Miller", "Hannah Davis",
    "Ian Wright", "Jessica Lee"
]
# 2. Define possible items
purchase_item_list = [
    "Laptop", "Mouse", "Smartphone", "Headphones", "Keyboard",
    "Tablet", "Camera", "Tripod", "Monitor", "Printer",
    "Smartwatch", "Speaker", "External Hard Driver", "Router", "Charger"
]
# 3. Generate a data set with 100 random customers
expanded_data = {
    # Random customer name for each row
    "Customer Name": [
        # choose a single name in customer_name list, do it x100
        random.choice(customer_names) for _ in range(100)
    ],

    # Random, from the list "purchase_itel_list", choose 1 - 3 items
    # join them together using a space
    # repeat this 100 times
    "Purchase Items": [
        ", ".join(
            random.sample(
                purchase_item_list,          # from this list
                random.randint(1, 3)         # choose between 1 and 3 items
            )
        )
        for _ in range(100)
    ],

    # Random purchase cost between 50 and 1500, rounded to 2 decimals
    "Purchase Cost": [
        # this says: give me a value between 50 and 1500
        # all values in this range should have an equal probability of getting chosen
        # Then round it to 2 decimal places
        # do this x100 more times
        round(random.uniform(50, 1500), 2) for _ in range(100)
    ]
}
# 4. Convert to a DataFrame (specifically a TABLE)
customer_dataset = pd.DataFrame(expanded_data)

# Show first 10 rows
customer_dataset.head(10)

# give me the count, mean, std, min, max, etc
customer_dataset.describe()

# group values by a certain condition and give me a sum of any numeric value they have
grouped_dataset = customer_dataset.groupby("add one of the dectionary keys").sum(numeric_only=Tue)

# display the grouped data by simply calling "grouped_data_set"
grouped_data_set

#Draw graph from the data
%matplotlib inline    # this allows to plot graph with jupyter
import matplotlib.pyplot as plt  # this is a library that helps to plot graphs

# plot a 12 inches x 5 inches figure, this creates a plotting canvas
plt.figure(figsize=(12,5))

# In the figure, create a bar chart
plt.bar(
  # get the referencepoint in the data above,
  # remember we grouped the data based on "Customer Name" a.k.a index or x-axis
  x=grouped_dataset.index

  # each bar is the height of the total price of each "purchase cost"
  height=grouped_dataset["Purcahse Cost"]
)

# plot the 'x' lable

# this adds label under the x-axis
plt.xlabel("Customer Name")

#this adds lable under the y-axis
plt.ylabel("Total Purchase Cost")

# this adds title above the graph
plt.title("Total Purchase Cost per Customer")

# rotate the labels on the x-axis by 45-deg and ["horizontal  alignment" = "right-aligned"]
plt.xticks(rotation=45, ha="right")

# automatically fix the layout, nothing overlaps or get cut-off
plt.tight_layout()

#  display the graph
plt.show()

# NOTE
# The graph could also be customezed using other python libraries as follows

# Import the library that is respoonsible for creting a range of colord bars
import matplotlib.cm as cm

plt.figure(figsize=(15,5))

# compile a theme
# themes: plasma, inferno, magma, cividis, cool, Wistia and rainbow ... your choice
colors = cm.plasma(norm_values)
plt.bar(
    x=grouped_dataset.index, 
    height=grouped_dataset["Purchase Cost"],

    # assign the color theme
    color=colors
)
plt.xticks(rotation=90)
plt.show()

```

<br>
<h3 align="center">NumPy</h3>
provides <code>ndarray</code> <u>n-dimensional array</u>.<br>
thisis capableof housing numeracal data of various types.<br>
<b>NumPy</b> also has vector capabilities which allow to process calculations on vast numbers <br>
This is better than a traditional loop <br>
<h4>Example</h4>
Suppose that we want to calcuate a 











