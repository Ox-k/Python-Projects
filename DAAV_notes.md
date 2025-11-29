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
Suppose that we want to add a vector
<br> we need to import <b>NumPy</b>: <code>import numpy as np</code><br>
Then let us create a vector. Remember a vector is an array of value, so,<br>
We need to transform a list into an array and <b>numpy</b> has just a tool for that<br>
<code>pieces = np.array([100, 200, 300, 400])</code><br>
Now we want to perform this math: <br><br>


```yml
    [200, 300, 400]
  - [400, 300, 200]
...................
    [-200, 0, 200]

```

<br>
<br>
This is done as: <code>prices[1:] - prices[:-1]</code>
<br><br>
Essentially slicing
<br><br>
This can also be achieved using a loop bu it would look messy and possibly introduce errors
<br><br>
<b>NumPy</b> also support other powerful operation that would otherwise be impossible with a loop<</br>
we can calculate operations on vectors that are not compatible by reshaping the smaller one to match the bigger
<h4>Example</h4>
<code>[1,2,3] + [1,2]</code> .... this would not work because they do not have the same dimensions
<br>
We can instead apply <b>r.reshape(row, cols)
</b>


```yml
  arr0 = np.array([1,2,3])
  arr1 = np.array([1,2])

  Then reshape arr1 to be 1x2 ➡️ 2x1 as such
  new_arr1 = arr1.reshape(1,3)

  Basically, it fleeps the array around to match the other one for operations ????
  if they do no math. This is called BROADCASTING

  Reshaping: breaks down an array into subarrays
  Broadcasting: rea-arranges the dimension of the array

  you can PAD an array and add a 0 at the end
  padded_Arry = np.pad(arr1, (0,1))  ... means add one 0 at end

```
<br>
<br>
Before applying broadcasting, observe shape of you arrays and imagine how <code>numpy</code> will<br>
expand the dimenstions to match and ensure that the operations aligns with your intent.<br>
<br>
Use <code>reshape()</code> and <code>newaxis()</code> to broadcast your arrays to align to your desired <br>
manipulations.<br>
Print shapes of the arrayat various steps as a debugging technique.
<h3 align="center">Reshape VS broadcast</h3>
Reshape: does not duplicate values, it simply changes the dimension of the array<br>
Broadcasting: duplicates the values to fill up the rest of the missing positions
<br>
<br>

```yml

  Numpy:
    broadcasting lets you add arrays of diff shapes if their sizes are compatible
    basically if their shape is the same. (see what shape is below table)

     

```

<br><br>

|Name          | Shape           |  Meaning                                |
|:-------------|:----------------|----------------------------------------:|
|1D array      | (n, )           | n elements -NO row or columns           |
|Row vector    | (1, n)          | 1 row, no columns                       |
|Column vector | (n, 1)          | n rows, 1 column                        |

<br><br>
<h3>How to tell if a vector or an array?</h3>
<code>if it's a <b>1D</b>, its an <b>array</b>: [1,2,4], if rows and columns appear, then its a vector</code><br>
<h4>Example</h4>
<code>np.array([[1,2,3]]) .... this is a row vector (1,3); and np.array([[],[],[]]) is a (3,1) col vector</code>
<br><br>

<h3>Multi-Dimensional arrays can not have different sizes</h3>
<br>
This would be illegal 👇
<br>
<br>



```lua
    [[1,2,3],[4,5]]   

```

<br>
Because a <b>2D</b> array must be a perfect parallegram.
<br>
<h3>Broadcasting compares from right to left</h3>
Broadcasting simplifies operations between arrays pf different shapes.<br>
it does this by automatically expanding the deimesion of the smaller array to match the larger one
<br>
This allows to perform element operations without needing a loop
<br><br>
Normally arrays can be added if they have the same shape<br>
<h4>Example</h4>

```scss

  These calculations can be performed:
  👉 [1, 2, 3] + [4, 5, 6]   ✔️
  👉  [1] [2]
      [3]+[4]                 ✔️
      [5] [6]

  and so on ....
  this is because every value has a corresponing value to be added to

```

<br><br>
However these would not work in regualar array arithematic
<br>

```scss

  These calculations can be performed:
  👉 [1, 2, 3, 9] + [4, 5, 6]   🛑
  👉  [1] [2]
      [3]+[4]                   🛑
      [5] [6]
          [7]

  and so on ....
  this is because NOT every value has a corresponing value to be added to

```

<br><br>
This is where <b>reshape</b> and <b>broadcasting</b> comes to the rescues,by expanding incompatible (smaller) arrays to be <br>
the same szie as the larger array
<br>
<h5>how does broadcasting do this?...</h5>
Take these two arrays:
<br>


```python
    import numpy as np

     # this is an array of shape (2,3)
  👉 array0  = np.array ([[1, 2, 3], [4, 5, 6]])

     # this is an array of shape (2, )
  👉 array1  = np.array([10,20])


```
<br>
NOTE: in this context <b>SHAPE</b> is not the same as <b>SIZE</b>.
<br>
<br>

Now what <code>Boradcasting</code> does is: <b>Compare the "SHAPES" of the arrays from RIGHT to LEFT</b>
<br>
This means that it is going to look at the shapes and <q>stack</q> them on each other , <code> from right to left</code>
<br>
<h4>Example</h4>
<br>


```scss

  Take the SHAPE of array0, write it down
  Take the SHAPE of second array, just below array0, write it down
  BUT: this time start with the right most digit, and write it under the right most digit of array0

  Example:
  shape of array0 -> (2, 3)
  shape of array1 -> (2,  )

  Then stack them according to the trick specified above:
  (2, 3)
     (2, )

```

<br><br>
Now how does  <b> RESHAPES</b>ing the array work?<br>
We use the method <code> array_name.reshape(a, b)</code>
<br>
Where: <br>
a: <code> is the number of rows </code>
<br>
and <br>
b: <code> is the number of columns </code>
<br><br>
<h4>Example</h4>
<br>

```python
  newarray1 = array1.reshape(2, 1)

```
<br><br>
This makes the <b>array1</b> look like a column vector below<br>
```scss

  👉  [10]
      [20]

```
<br><br>
And how we can perform arithmatic operations on the two arrays because the shapes are:
<br>

```scss

(2, 3)
(2, 1)

```

<br><br>
Now <b>NmuPy Broadcasting</b> can compare and see if they have compatible shapes and add them
<br>It does that by following the following rules (also outlined in the table above/earlier)<br>
<b>Rule one</b><br>
<code>if the shape of the array0 is (a, 1) and shape of array1 is (a, b), expand shape of array0 to be (a, b)</code>
<br>

This means: duplicate the column <code>a</code> across the array to match the columns of the other array<br>
<h4>Example</h4>
<br>

```scss
  We know that after reshaping the array1 from shape (2, ) to shape (2, 1)
  We have the following array:
      10
      20

  Now "exapnding" this means that we need to copy the columns to match the size of array0 columns
  To do this, we copy the value of each row to fill up the rest of the row:
      10 10 10
      20 20 20

```

<br><br>
Now this looks exactly the "array0"and we can stack them on top of each other<br>
and each value will have a corresponding value from the other array.<br><br>

<h4>Example</h4>
<br>

```scss

    (2, 3)          (2, 1)
      👇              👇
    [1  2  3]      [10  10  10]     AND    array0 + array1   👉  [11  12  13]
    [4  5  6]      [20  20  20]                                  [24  25  26]
  
    All this without having to implement a loop

```
<br><br>

<h2 align="center">Use cases for python libraries</h2>
<h3>Data Collection</h3>
There are several places where you can find publicly available data for use.<br>
Alwasy read the licence that comes with the data so that you know what you can do and not do<br>
with the data. (This will help to avoid any legal issues if you need to scale you use of data)
<br>
<br>

```yml
      Microsoft Azure: curated data for machine learning and AI applications
      Microsoft Research Data Repository: data from microsoft research initiatives covering large domains
      APIs: Many websites offer API that explains what data you can get access and how to access the data
      World Bank: insights into global development challenges
      Microsoft Planetary Computer: geospatial and environment analysis
      Microsoft Azure Marketplace: financial data and other curated financial related stuff (paid)
      Microsoft AI for Health Initiaive: Health data for research and innovation

```
<br><br>
<h2 align="center">Data Cleaning 101</h2>
<h4>Common data quality problems</h4>
<br>

```yml
      Missing Values: due to entery errors or un-availability of the data
      Outliers: Data that is significantly different from others (anomalies)
      Inconsistences: due to entry errors, change in data collection methods, merging datasets

```

<br><br>

<h4>Strategies to address data quality problems</h4>
<br>

```yml
      Removing dataset: remove entire segements that are missing the rest of the data
      Imputing missing values: "imputing" ... meaning to assign substitude values for missing ones
                              This can be like putting the mean, media, average to represent a missing
                              value to fill in gaps and create a more complete dataset
      Dealing with outliers: cap the limit of value threshold.
      Resolve inconsistence:  standardize data formats, correct errors, remove or correct conflicting data
                            Pandas has a tool called "replace()" that allows to replace specific values
                            and "apply()" to apply custom functions to the data

```

<br><br>
Data cleaning should be done with care to avoid either adding more data (in attempt to collect) <br>
missing values and distorted the final representation of the data<br><br>

<h3>Manipulating Data with Pandas</h3>
<h4>The basics</h4>
The structure of dataframes<br>
DataFrame is a super charged spread-sheet. 2D table-like structure where data is organised into rows and colmuns<br>
Each <code>column</code> represents a specific variable and each <code>row</code> corresponds to a specific <br>
observation of data point.<br>
<h4>DataFrame components & commo operations</h4>
<br>


```yml
      Data    : content of the column; numerical textual or a mix of both
      Index   : identifies each row in the data frame
      Column  : identifies the different variables int he dataset; has a name and associated data type

      Operations
      Indexing  : Allow to access specific element in a file, by rows, columns etc
      Slicing   : allows to select a range of data to select a portion of data
      Filtering : Allow to select data/rows based on a specific criteria

```

<br><br>
<h4>Pandas indexing</h4>
Pandas library provides a library called <code>DataFrame</code> that is used to analyze structured data<br>
It allows to locate and retrieve data through indexing's many methods.<br>

<h5>Fundamental Indexing Methods</h5>
<code>.loc</code>:<br>
Label-based, it uses rows and columns labels to access data.<br>
This means that you use the actual names of the rows and columns or index lables to retrieve data<br>

<h6>Example</h6>
<br>

```python

      .loc['customer_1', 'purchase_amount']
            .... retrieves purchase amount for customer with id "customer_1"

      ALSO NOTE: the lodic in the brackets is ['condition', 'what is returned']

```
<br>
<br>
<code>.iloc</code>:<br>
This is position based.<br>
You use integer position starting from 0 to locate data with the DataFrame.<br>
This works regardless of the labels, and is useful when working with datasets of missing values<br>
It supports slicing allowing you to select a range of rows or columns<br>

<h6>Example of accessing data with <code>.iloc</code></h6>
<code>.iloc[5, 2]</code>: This would access the value in the 3<sup>rd</sup> column of 6<sup>th</sup> row.<br>
<br>
<h5>Understanding <code>.iloc</code></h5>
<br>

```yml
      ".iloc" can be trick to grasp
      .iloc[row, column] ... starts indexing at 0 like an array.
      That means if you want to access a value at a particular position, specify the "position - 1"
      for both rows and columns
      SO:
        To get a value that is in the 10th row and 12 column: .iloc[(10-1), (12-1)]

```

<br><br>
<h4>Boolean indexing</h4>
This is also known as <q>Filtering data with precision</q> or <q>Mask indexing</q>
<br>
This is used by creating a <code>boolean mask</code>, this is an array of <code>True</code> and <code>False</code>
<br>values that indicate which rows or columns meet specific criteria.<br>
Then use this mask to return only the data that corresponds  to the true values.<br>
<h6>Example</h6>
Suppose you own a high-end luxury store, and you want to see a customer that has:<br>
<li>Platinum membership</li>
<li>purchases more than 10</li>
<br>

Boolean indexing allows you to do this as follows: <br>


```python
      df[(df['membership_level'] == 'platnum') & (df[purchases] >10)]

    "df" is an alias for DataFrame as in: from pandas import DataFrame as df

```
<br><br>
Boolean indexing is powerful because it allows you to select specific information with precision<br>
It also allows you to combine boolean expression for more powerful selection and data retreival.<br>
You can use the following logical operators:<br>

```yml
      & for AND
      | for OR
      ~ for NOT

```
<br><br>
<h4>Other indexing methods</h4>
When we want to modify a single value at a position or a label based location, we can use<br>

```yml
      .at : this is lable based, like .loc but for a single value
      .iat : this is label based, like iloc but for a single value

```
<br>
These can be very useful in larger datasets where performance us crucial
.<br>
Indexing allows you to modify and update values in the dataset easily and fast where performance matters
<h6>Example</h6>
Suppose that we want to update the <code>Membership</code> of a client to <code>Platinum</code><br>

```yml
      df.loc['customer_1', 'membership'] = 'Gold'

```
<br><br>
<h4>Multi-level indexing</h4>
Sometimes whn the data is organised in <code>hierarchies</code>, multi-level indexing with <code>pandas</code> help<br>
access and retrieval data in a dataframe with easy and fast.<br>
<h6>Example of multi-level indexing</h6>
<br>

```python

      import pandas as pd

      # Sample data
      data = {
                  'Sales': [200, 300, 250, 400, 500, 600],
                  'Profit': [50, 80, 60, 100, 120, 150]
      }

      # Create a MultiIndex
      index = pd.MultiIndex.from_tuples(
          [('2021', 'Electronics'), ('2021', 'Clothing'),
             ('2022', 'Electronics'), ('2022', 'Clothing'),
             ('2023', 'Electronics'), ('2023', 'Clothing')
          ],
          names=['Year', 'Category']
      )

      # Create the DataFrame
      df = pd.DataFrame(data, index=index)

      print(df)

      # Accessing sales for electronics in 2022
      sales_2022_electronics = df.loc[('2022', 'Electronics'), 'Sales']
      print(sales_2022_electronics)  # Output: 250

      # Accessing all sales for specific year
      sales_2021 = df.loc['2021']
      print(sales_2021)

      # Aggregating sales data across categories or yeas
      total_sales_per_year = df.groupby(level='Year').sum()
      print(total_sales_per_year)

```

<br><br>
<h4>Query method</h4>
This offers <code>SQL</code> like syntax for querying data frames.<br>
It allows you to express a query in a more readable  and more easy to understand.
<h6>Example</h6>
<br>

```python

    # Sample DataFrame
    import pandas as pd

    data = {
        'Employee_ID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Performance_Rating': ['Excellent', 'Good', 'Excellent', 'Average', 'Excellent'],
        'Projects_Completed': [6, 3, 7, 2, 8]
    }

    df = pd.DataFrame(data)

    # Using the query() method to filter data
    excellent_employees = df.query("Performance_Rating == 'Excellent' and Projects_Completed > 5")

    print(excellent_employees)


```

<br>
Using <code>query()</code> can be more efficient in terms of performance for certain operations
<br>

<h4>Best practices for indexing</h4>
👉 Choose the right method: know labesl? <code>.iloc</code> & <code>.loc</code>, single values and lightening fast? <code>.at</code> & <code>.iat</code><br>
👉 Chaining for efficiency: chain multiple methods for more concise and readable code. Pandas allows it<br>
👉 Clarity over cleverness: prioritize core readability, think of others reading your code<br>
👉 Handle missing data: use methods like <code>.fillna()</code> or <code>.dropna()</code> to handle <code>NaN</code> data<br>
👉 Leverage multi-level indexing: if your data has hierarchal structure.<br>

<h3>Loading and inspecting datasets in pandas</h3>
Suppose you have a <code>.csv</code> file that contains dtaa of cars. It could look like:
<br>
<code>cars.csv</code>
<br>

```yml
      Car_Name,Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner
      Toyota0,2014,3.35,5.59,27000,Petrol,Dealer,Manual,0
      Toyota1,2014,3.35,5.59,27000,Petrol,Dealer,Manual,0
      Toyota2,2014,3.35,5.59,27000,Petrol,Dealer,Manual,0
      Toyota3,2014,3.35,5.59,27000,Petrol,Dealer,Manual,0
      Toyota4,2014,3.35,5.59,27000,Petrol,Dealer,Manual,0
      .... and so on.....

```

<br><br>
Note: In the data above, the fist row represent the <code>Headers</code> of the columns. <br>
Note that at the end of the row, on the last value, there is no comma, that is because that is the end of the row<br>
Next line represent the end of the column.<br>
First, we need to bring in Pandas module, it like a swiss knife
<br>

```python
      import pandas as pd

```
<br><br>
Then we need to use the <code>.read_csv</code> to read our <code>.csv</code> file<br>

```python
      dataset = pd.read_csv("cars.csv")

```

<br><br>
What this does it, it pulls the data from the file and organise it in a structured format so that you can used it.<br>
Then we have functions like: <br>
Showing a few initial portion of the table

```python
      dataset.head()

```
<br><br>
Showing the information that is contained in the table such as <br>
<li>data types used</li>
<li>column names</li>
<li>memory usage</li>
...and so on...
<br>

```python
      dataset.info()

```

<br><br>
Then we can also see an overview <code>statistics</code> of the data<br>

```python
      dataset.describe()

```

<br><br>
This will show information of each numerical content such as the:
<li>Mean</li>
<li>Standard Deviation</li>
<li>Min</li>
<li>Max</li>
<li>Percentiles such as: 25%, 50% and 75%</li>
<li>Count</li>
<br> 
<h3>Data transformation</h3>
This including:<br>

```yml
      merging .... pd.merge()
      concantenating ...pd.concat()
      sorting ....df.sort_Value()
      grouping ....df.groupby()
      aggregating ...df.agg()

```

<br><br>
<h3>Creating and Inspecting DataFrames</h3>
Python offers a <code>DataFrame</code> data structure that transforms data into neat <code>Rows</code> and <code>Columns</code>
<br>
Coupled with <code>Dictionaries</code>, dictionaries are ideal for structured data, where:
<br>
<code>Keys</code>: represent the columns<br>
<code>Values</code>: represent the corresponding column data
<br>
<h6>Example</h6>
Int his example, we use a <code>dictionary</code>, where <code>keys</code> and explicitly column headers and the rest is <br>
column data<br>

```python
      # bring in the pandas library
      import pandas as pd

      # Define data .... a dictionary in this example
      data = {'Name': ['alice','bob','charlie'], 'Age':[25,30,28]}

      # transform it into a dataframe ... structual with rows and columns
      df = pd.DataFrame(data)

      # in jupyter, this prints out a formatted table
      df

```

<br>
<h6>Outcome</h6>
<img width="231" height="123" alt="image" src="https://github.com/user-attachments/assets/0e4d77d1-9831-43a9-8ac0-5b80b17d16a4" />
<br>
<br>
Sometimes we can use data that has been stored in a list. in this case, we need to define the headers of our columns
<h6>Example</h6>
<br>

```python
      import pandas as pd

      # This is a list of lists
      data = [['alice',6],['bob',89],['charlie',25]]

      # we create a dataframe and dictate what the headers are going to be
      df = pd.DataFrame(data, columns=['Label','Count'])
      df

```

<br>
<h6>Outcome</h6>
<img width="373" height="129" alt="image" src="https://github.com/user-attachments/assets/c2e4e535-11fe-4486-8528-4194b9680cfc" />
<br><br>
<h3>Working with other file formats</h3>
Python offers function to read other file types.<br>
<h6>Example</h6><br>

```python
      pd.read_csv('csv_file.csv')
      pd.read_excel('excel_file.xsls')
      pd.read_json('json_file.json')
      pd.read_sql('sql_file.sql')

```

<br><br>
<h3>Inspecting DataFrame</h3>
This is a way of exploring the contents in a <code>DataFrame</code> after creating one <br>
This is crucial when you want a quick glance at the content and the nature of your data
<br>
Display the first <q>default 5</q> rows of the table
<br><br>

```python
      df.head()

```
<br>
Display the last <q>default 5</q> rows of the table/dataset
<br><br>

```python
      df.tail()

```
<br>
Display the dimension of the dataframe, i.e, number of rows and columns
<br><br>

```python
      df.shape

```

<br>
Generate a summary of the dataframe, <q>column</q> names, <q>data types</q> contained int eh dataframe<br>
presence of missing values.
⁉️ This is very important and helps you to know how to use the dataset accordingly.
<br><br>

```python
      df.info()

```

<br>
Describe statically the dataframe, i.e; mean, median and so on .... <br><br>

```python
      idf.describe()

```
<br><br>
<h3>Selecting and Filtering the DataFrame</h3>
Pandas are powerful at giving the ability to precisely control how data is accessed in a dataFrame<br>
After running any of the methods above that describte the data set, you will have the exact headers <br>
of the dataframe.<br>
You can then use these headers to retrieve information as needed
<br>
<b>Single column selection</b>: <br>
This is when we want to select a single column of the table/dataframe
<br><br>

```python
      # this return the values... not in table format
      df['column_header']

      # this returns the values as a dataframe ... in a table format
      df[['column_header']]

```

<br><br>

<b>Mutliple column selection</b>: <br>
This is when we want to select a portion of the data frame but specific columns
<br><br>

```python
      df[['first_header', 'second_header']]

```

<br><br>
So far the methods above are used to select <b>columns</b>. For rows, we use indexing<br>
We can selecting rows based on their index labels using a function that we saw earlier<br>
<br><br>

```python
      df.loc[index_of_interrest, 'column_header']  # returns a single cell
      df.lov[index_of_interrest']    # returns an entire row

```

<br><br>
So if we want to see the row at position 10, we would input 11 as the index.
<h6>Example</h6>
<br><br>

```python
      df.loc[11]

```

<br><br>
We can also select a specific number of row, not necessarily the index, simply the integer position<br>
Note that indexing and integer position all start at 0 as the first item returned.
<br>
<h6>Example</h6>
<br><br>

```python
      df.iloc[6] # returns row 7

```

<br><br>
<b>Filtering data</b>
This is done using boolean indexing
<br>
This is done by creating a boolean mask of <code>True</code> or <code>False</code> by <br>
applying one or more logical comparison to one or more columns. This will return the columns <br>
with the rows that meet the conditions.
<h6>Example</h6>
<br><br>

```python
      # filter rows where 'Age' is greater than 25
      df[df['Age'] > 25]

      # Note ⚠️: the innner 'df['Age'] > 25, will rwo-filter and return a series of true/false value list
      # Where as df['header'] is row column selection

```

<br><br>
Here is another example where we can apply multiple filters on a dataframe<br>
Suppose that we want to filter all people in our dataframe who meet these conditions<br>
<li>Above 30</li>
<li>From Los Angeles</li>
<br> and we want to return various attributes of users in form of a dataframe
<br>
<h6>Example</h6>
<br><br>

```python
      # return names and ages of users whose age > 30 and are from los-angeles
      # return them as a dataframe
      df[df['age'] > 30]][df['city' == 'los-angeles'][['name','age']]] ❌

      # this could also be written as
      df.loc[(df['age'] > 30) & (df['city'] == 'los-angeles'), [['name', 'age']]] ✅

      # 📝 you can also extract a condition and give it a name for cleaner code
      # example:
      mask = (df['age'] > 30) & (df[ ... condition]) & .. so on 

      # return the name and city of users whose age is above 30 as a data frame
      df[df['age'] > 30][['name', 'city']] ✅

```

<br><br>
<h3>Querrying Data</h3>
Using <code>qury()</code> helps makes the code more <code>SQL</code> like and readable thats all.<br>
The structure is : 
<br><br>

```yml
      df.query("condition")[return values or dataframe]

      📝 you can use legural selectors such as : & >=, <= !=
      📝 you can also use natural language such as: and, or, in, not in, not
      String matching: "city.str.contains('sub-string')
      reference: define a variable and refer to it as @variable. e.g: age = 30, "20> @age"
      Arithmatic operations works the same too as in python

```

<br><br>

Filtering data can also extend to looking up data in a dataframe using indeces.<br>
When you create a dataframe off a dataset, they are indexed from 0.<br>
Therefore, you can specify a condition to filter a dataframe using indeces
<h6>Example</h6>
<br><br>

```python
      # return rowns starting from 41 ....
      df.query("index > 40")

```

<br><br>
Query returns rows, btu sometimes we want to return <b>columns</b>
<br> 
This is where <code>axis</code> comes in handy <br>
<h6>Example</h6>
<br><br>

```python

      # return the columns whose name contains "value_in_dataframe"
      df.filter(regex="values_in_dataframe", axis=1)

      # then you can qury rows on that
      df.filter(regex="...", axis=value).query("condition")

```

<br><br>
‼️ This where the distinction between <code>filter</code> and <code>query</code> is highlighted<br>
In query, we are dealing with rows, but filter, we are dealing with columns.
<br>
<h3>Handling Missing Data</h3>
Missing values known as <b>NaN</b> are common in most dataset collected.<br>
Pandas provide mechanism to deal with these missing values.
<br><br>

```python
      # returning a series of boolean values for missing values of a certain header
      df['header'].isnull()

      # Generating a boolean dataframe to mirror an original missing value.
      # Missing: true
      # Not missing: false
      # This could be useful when we are filling a table with a dataset and fill true or false if value is missing
      df.isnull()

      # removes rows containing any missing values
      df.dropna()

      # replacing missing values with a specific placeholder value
      df.fillna(value)

    # imputing missing values in a column with its mean while conserving memory
    # inplace=True: means modify the existing dataframe directly instead of creating and returning a copy
    df['age'].fillna(df['age'].mean(), inplace=True)
    # Or a better approach
    df = df.fiilna(df.mean())   # RECOMMENDED ✅

```

<br><br>
<h5>Other data transformation methods.....</h5>
<code>SORTING</code><br>
This is done by <code>df.sorted_values()</code><br>
<h6>Example</h6>
<br><br>

```python

      df..sorted_values(by="column header here", ascending=False/True 👈 optional)

```

<br><br>
Applying custom functions to dataframes
<h6>Example</h6>
<br><br>

```python

      # define a function
      def calculate_discount(sales):
          return sales * 0.9

      # then you can apply it do a data transformation
      df["Discounted_Sales"] = df["sales"].apply(calculate_discount)

      # print the dataframe returned
      print(df.head())

```

<br><br>
Creating a pivot table
<h6>Example</h6>
Given a dataframe with many columns and rows but among them are: <br>
<code>regions</code><br>
<code>products</code><br>
<code>sales</code><br><br>
And you want a table where<br>
rows = <code>regions</code><br>
columns = <code>products</code><br>
cells contains = <code>total sales</code>
<br><br>

```python

      df_pivot_table = df.pivot_table(
                index="column desired",
                columns="specific column desired",
                 values = "same logic"))

      #example
      df_pvt = df.pivot_table(
          index = "regions",    # if more thatn 1 index, enclose them in 👉 []
          columns = "products",
          values = "sales",
          aggfunc = "sum"    #all all them together at the last row
      )

```

<br><br>

Then we call the cleaning methods such as <code>.fillna(0)</code> or <code>.dropva()</code> to clean table.
<br>
Concatenating dataframes
<br>
Suppose that we have the following dataframes
<h6>Example</h6>
<br><br>

```python

    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})

    #if we call:
    df_concatenated = pd.conact([df1, df2])

```
<br>
This will created a a new table with the two data stacked together as a single table
<br><br>

|  |A|B|
|:-|:-|-:|
|0|1|3|
|1|2|4|
|0|5|7|
|1|6|8|


<br><br>
Merging dataframes<br>
This is when we want to marge two dataframes based on a shared or common column
<h6>Example</h6>
<br><br>

```python

      df1 = pd.DataFrame({'key': [values in here ], .... more ....})
      df2 = pd.DataFrame({'key': [exactly in here], .... more ....})

      # then call the method to cancat
      dg_merged = pd.merge(df1, df2, on="key")
```

<br><br>
<h3>Exploratory Data Analysis</h3>
Becoming a data detective to uncover hidden anomalies.<br>
Cleaning data is such a crucial step in data analysis. when your data is clean of errors, it<br>
provides accurate and reliable insights that can be used to un-hide alot<br>
<h6>Example</h6>
<br><br>

```yml

      Imagine you have a dataset of customers information and their
      purchasing behaviour. And the customer information contains details like
      thier:
        names
        address
        emails
      You may decide to send markeing emails to your custmer offering varioys customazied
      discounts. if there is a typo in emails, you might end up sending the marketing
      email to the wrong customers.

```

<br><br>
Cleaned data:
<ul>
  <li>Enahnces the accuracy and reliability of your analysis</li>
  <li>Helps identify and troubleshoot issues</li>
  <li>Facilitate the development of features</li>
  <li>Support data-driven decision making</li>
  <li>Promotes effective communication and collaboration</li>
</ul>
<br>

<h6>Ways to clean data</h6>
<ul>
  <li>Indentify and nderstand your data</li>
  <li>Look for missing values</li>
  <li>Address inconsistencies and errors in your data</li>
  <li>Transform and aggregate the data as needed</li>
  <li>Validate and verify the cleaned data</li>
</ul>

<h3>Data Cleaning Tactics</h3>
Pandas provide function like the one below to fill missing values with <br>
specified value as a replacement.
<br><br>

```python

      pandas.DataFrame({...data ...}).fillna(placeholder_Value)

```

<br><br>
Or you can remove the entire row that is missing values using:

<br><br>

```python

      df.dropna()

```

<br><br>
Sometime you have the data but it is inconsistent in some dataset.<br>
This data could have different data formats ir varying units of measurements
<br>
To correct this, we can define a <code>regular expression </code> to standardize formats.<br>
Pandas also offer the method below to make all values in the column the same type:
<br><br>

```python

      import pandas as pd
      data = {'Age' :['23', '12', '56', 89, 23.56]}
      df = pd.DataFrame(data)

      # convert the data into an integer
      df['Age'] = df['Age'].astype(int)

```

<br><br>
Pandas also have method to remove duplicates in data that may skew the conclusion

<br><br>

```python
      import pandas as pd
      data = {'Scores': [1,1,2,2,3,3,4,4,5,5]}

      df = pd.DataFrame(data)
      unique_scores = df.drop_duplicates()

```

<br><br>
<h6>Data Reshaping and Transformation</h6>
This is when we <code>re-arrange/modify</code> the structure of the data to meet specific requirements
<br>
<h6>Example</h6>
Creating <code>pivot_table</code> to summerize the data based on one or more index columns<br>
This is useful when you want to <code>aggregate data across different dimensions</code>
<br><br>

```python

      df.pivot_table(index=["...", " ..." ], columns=["...", "..."], values=["...", "..."])

```

<br><br>

<code>melt()</code> undoes what <code>pivot_tables()</code> does.<br>
It converts data from a wide dataframe to a long dataframe by turning rows into columns.
<h6>Example</h6>
Suppose you have this data: <br><br>

|product|Jan|Feb|Mar|
|:------|:--|:--|--:|
|A|100|150|200|
|B|120|130|180|

<br><br>
And you want to convert it into a vertical table. Applying <code>.melt()</code> function as this 👇🏼
<h6>Example</h6>
<br><br>

```python

      import pandas as pd

      # Create a dataframe
      data = {
          'Product': ['A', 'B'],
          'Jan': [100, 200],
          'Feb': [150, 130],
          'Mar': [200, 180]
      }

      # create a data frame
      df = pd.DataFrame(data)

      # Melt the data to reshape the DataFrame
      melted_df = pd.melt(df, id_vars=['Product'], var_name='Month', value_name='Sales')

    """
      Note the general structure of a melt() function:
      pandas.melt(
              dataframe,
              id_var=[axis name already in the dataframe],
              var_name='custom column header,
              valeu_name='custom column header'
      )
    """

```

<br><br>
Note that these <br><br>
```python

      
      id_vars
      var_name
      value_name

```

<br><br>
are reserved keywords for pandas that are used with the <code>melt()</code> function.<br>
The resulting out come is: <br><br>
|Product|Month|Sales|
|:------|:----|----:|
|A|Jan|100|
|A|Feb|150|
|A|Mar|200|
|B|Jan|120|
|B|Feb|130|
|B|Mar|180|

<br><br>
<h5>Stack and Unstack</h5>
<code>stack</code> is used to pile up data vertically <br>
<code>unstack</code> is used to spread the data horizontally<br>
Assentially what this does is turn this 👇🏼
<br><br>

|product|jan|feb|
|:------|:--|--:|
|a|100|150|
|b|200|250|
|c|300|350|

<br><br>
By 
<h6>Example</h6>
<br><br>

```python

      import pandas as pd
      data = {'product': ['a'','b','c'],
              'jan':[100, 200, 300],
              'feb': [150, 250, 350]
      }

      # stacking the dataframe
      df = pd.DataFrame(data)
      stacked = df.set_index('product').stack()

      # to unstack them
      stack.unstack()

```

<br><br>
To this:
<br><br>

|product| | |
|:------|:-|-:|
|a|jan|100|
| |feb|150|
|b|jan|200|
| |feb|250|
|c|jan|300|
| |feb|350|

<br><br>

<h3>Aggregation and summarization</h3>
This is when we condense data by applying calculation on a group of data in a dataframe's rows or columns
<br>
We use:<br>
<code>groupby</code>
<br> function in pandas to group data based on one or more columns, creating a group object<br>
and then chain any of these methods to obtain desired results
<h6>Example</h6>
<br><br>

```python

     .sum()
     .mean()
     .count()
     .min()
     .max()

     # there are other statistical methods that are used for various purposes

```

<br><br>

<h3>Merging and Joining</h3>
<code>join</code> works like merge, but it combines dataframes based on indeces. <br>
This is particulary useful when you want to combine Dataframes with hierarchail indices or row labels

<h6>Example</h6>
<br><br>

```python

      import pandas as pd

      # Create two DataFrames
      employees = pd.DataFrame({'EmployeeID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
      departments = pd.DataFrame({'DepartmentID': [1, 2, 3], 'Department': ['HR', 'IT', 'Finance']})

      # Set EmployeeID as the index for the join
      employees.set_index('EmployeeID', inplace=True)
      departments.set_index('DepartmentID', inplace=True)

      # Join the DataFrames
      combined = employees.join(departments)
      print(combined)

```

<br><br>
<h3>Identifying and handling missing data</h3>
<br>
When approaching a dataset with missing data<br>
<code>How much data is missing</code><br>
Is it a lot a few details here and there such that if they are deleted,<br>
this will not skew the result the data represent?<br>
<code>The type of data that is missing.</code><br>
Is this a must have data or optional<br>
<code>The purpose of the data missing</code><br>
Is this a response to a question that users are skipping or are users sparsely not answering<br>

<h5>Handling the missing values</h5>
<code>Imputation: </code> <br> filling in missing values with calculated values such as mean, median
<br>Regression analysis imputation predicts missing variables based on existing data 
<br>Multiple imputations involves creatign multiple imputed values, each with different values <br>
for the missing data.<br>

<code>Deletion</code> <br>
This is straight forward deleting rows that are missing data
<br>
<code>Create a category for the missing values </code>
<br>
<code>Collect more data to hit all the points</code>
<br>
<code>Use machine learning algorithms to fill data </code> .... not necessarily imputed data <br>

<h5>Handling Duplicates</h5>
Debloating data. <br>
These dups happen due to human errors when entering the data, merging data, or software bugs!
<br>
To handle this, python <code>pandas</code> have a tool just for that called <code>.duplicated()</code><br>
that is chained on the data.
<br>
In addition to this, you can prevent duplicates right at the stage of data input and using unique id in a database.<br>
This is called <code>Data Validation</code>

<h6>Example</h6>
<br><br>

```python

      import pandas as pd

      data = pd.read_csv('data_file.csv')
      duplicates = data.duplicated()

      # you can access individual rows as follows and drop them
      duplucate_rows = data[data.duplicated()]
      data = data.drop_duplicates()

      # keeping the duplicated
      data = data.drop_duplicates(keep='last')  #keeps the last occurence of each duplicate

      # keep the first occurence of each duplicate (default)
      data = data.drop_duplicates(keep='first')

      # Remove all duplicate rows
      data = data.drop_duplicates(keep=False)  #True ... is the default

```

<br><br>

<h5>Addressing missing data</h5>
The initial step in managing missig data is to pinpoitn its location in a dataset.<br>
Pandas offers <code>.notnull()</code> and <code>.isnull()</code> to create boolean marks. <br>
These marks highlight the missing values in the dataframe.
<br>
<code>When to remove the missing rows</code>: <br>
This is when the missing data is small and appears to be random. Pandas offer <code>.dropna()</code>
<br> to romove these rows or columns.<br>

<h5>Handling outliers</h5>
Using panads <code>describe()</code> and  <code>.quantile()</code> along with visualization tools <br>
helps to see the nature of the data and identifiers outliers, deciding if they are needed or not. <br>

<h5>Conversion of data types</h5>
Sometimes when there is a mismatch in data format in columns, this can be corrected using: <br>
<code>.astype()</code>, <code>.to_numeric()</code> and <code>.to_datetime()(</code> allowing handling of potential errors.
<br>

<h6>Working through an example</h6>
Lets imitate a sample data frame with missing values
<br><br>
<h6>import data analysis tools</h6>
<br>

```python

      import pandas as pd
      import numpy as np


```

<br><br>
<h6>Create a sample dataframe with missing values</h6>

<br>

```python

     data = {
         'Name' : ['Alice', 'Bob', np.nan, 'David'],
         'Age' : [20, 30, np.nan, 35],
         'City' : ['New York', np.nan, 'London', 'Paris']
     }
     df = pd.DataFrame(data)

```

<br><br>
<h6>Identifying missing values using pandas</h6>
<br>

```python
      # remember, at this point we have a table
      print('Missing value counts per column:\n', df.isnull().sum()

```

<br><br>

<h6>Removing missing values from the dataframe</h6>
<br>

```python

     df_dropped = df.dropna()
     print('\nDataFrame after dropping rows with any missing values:\n', df_dropped)

```

<br><br>

<h6>Imputing or replacing the missing values with the mean (for numerical columns only)</h6>
<br>

```python

      df_fiiled_mean = df.fillna(df.mean(numeric_only=True))
      print('\nDataFrame after filling missing 'Age' with the mean:\n', df_filled_mean)

```

<br><br>

<h6>Imputing with the median (for numerical columns only)</h6>
<br>

```python

      df_filled_median = df.fillna(df.median(numeric_only=True))
      print("\nDataFrame after filling missing 'Age' with median:\n", df_filled_median)

```

<br><br>

<h6>Handling outliers (demo with age), assume 40+ is an outlier</h6>
<br>

```python

      df['Age_capped'] = df['Age'].clip(upper=40)
      print("\nDataFrame with age capped at 40:\n", df)

```

<br><br>

<h6>Data type conversion</h6>
<br>

```python
      # convert to numeric and handle errors
      df['Age'] = pd.numeric(df['Age'], = errors='coerce')
      print("\nData types after conversion:\n", df.dtypes)

```

<br><br>

<h6>Group by some condition and aggregate</h6>
<br>

```python

      grouped_data = df.groupby('City')['Age'].mean()
      print("\nAverage age by city:\n", grouped_data)

```

<br><br>

<h3>Data Cleaning</h3>
<h6>Taming messy data with pandas</h6>
(see notes earlier....😊)

<h2 align="center">Data Visualization </h2>
This is the process of transforming raw data into visual representations such as charts and graphs.
<br>
<br>
<h6>Real life areas where visualization is used:</h6>
<code>Business</code>
<br>
tracking how the business is doing in sales over time, employee performance and areas of improvememts
<br>
<code>Science</code>
<br>
Simulation of natural disasters, tracking spread of diseases, etc
<br>
<code>and so on.....</code>
<br>
<h6>Why data visualization is important</h6>
It helps to unveil patterns and trends, spotlight outliers, facilitate comparisons, enhance communication<br>
convey easy to understand message to non-savy individuals.
<br>

<h6>Common visualizations</h6>
<b>Pie Chart</b>: portion of the pie representes quantity proportions and dominance<br>
These are used to represents small data representations with less segments.<br>
Can be confusing when proportions are almost the same size.<br><br>
<b>Bar Charts</b>: Handle a range of data types with clear readability<br>
Can be come bulky if categories are to many<br><br>
<b>Histograms</b>: group data into bins and histograms. <br>
Ideal for summerizing and representing large data set and poin point out outliers <br><br>
<b>Line Charts</b>: ideal for representing series data by connecting data points.
<br>They clearly show directions and trends.
<br>These required spaced data and no overlapping lines<br><br>
<b>Scatter Plots</b>: idal for regression but required addition analysis to be effecient ??
Tables: group data.<br>

<h3>MatPlotLib</h3>
Tool for reperesenting data using various data representation plots.<br>
<br>
<h5>Anatomy of MatPlotLib</h5>
<h6>Figure</h6>
serves as the overall container for your plot, providing the boundaries and context for visualization<br>

<br>

<h6>Example</h6>
<br>

```python
      
      #
      import matplotlib.pyplot as plt

      # Create a canvas
      fig = plt.figure(figsize=(width, height))  #note that the measurements and in INCHES

```

<br><br>

<h6>Lengend</h6>
Decods the symbols, colors, or line styles used in the plot, helping viewers understand<br>
the representation of different data series

<br><br>

<h6>Example</h6>
<br>

```python
      
      # import library
      import matplotlib.pyplot as plt

      x = [1,2,3]
      y1 = [4,5,6]
      y2 = [7,8,9]

      plt.plot(x, y1, label= 'name 1')
      plt.plot(x, y2, label = 'name 2')

      plt.legend()
      plt.show

```
<br>
This shows something like this 👇<br><br>

<img width="644" height="417" alt="Screenshot 2025-11-29 at 12 58 13" src="https://github.com/user-attachments/assets/b973e840-ce17-48e3-ad54-e950881b9c74" />

<br><br>
<h6>Customization</h6>
Matplotlib allows extensive customization of plots, enabling users to control colors,<br> fonts and styles for better visual appeal and clarity <br>

<h6>Ticks</h6>
These are marks along the axes indicating specific values. <br>
While tick labesl show the corresponding values, they aid in data interpretation
<br>
They serve a guide for interpreting the scale. <br>
<code>Example</code>: if you want to show the <b>hourly</b> temperature readings, you customize teh <br>
'xticks' to spread out at a 1hr interval.

<br><br>

<h6>Example</h6>
<br>

```python
      import numpy as np

      # get the plotting library
      import matplotlib.pyplot as plt

      # define axes values
      x = np.linspace(0, 10, 100)    # this means linspace(start, end, evenly-spaced-points)
      y = np.sin(x)

      # set the tick locations and labesl for the x-axis
      plt.xticks(np.arange(0,11,2), ['0', '2', '4', '6', '8', '10'])

      """
        np.arrage(start, end-1, steps) generates numbers from start inclussive, end exclussive and step counts
        the array: ['0' .... ['10']  represents the label that will be displayed at each of thise ticks.
      """

      # Optional: rotate bales for readability
      plt.xticks(rotation=45)

      # show the plot
      plt.show()

      # ESSENTIAL WE ARE DRAWING THE SIGN CURVE

```

<br><br>
This creates this 👇<br>

<img width="739" height="433" alt="Screenshot 2025-11-29 at 12 58 06" src="https://github.com/user-attachments/assets/1ffa95a2-6c66-4d57-9466-15df41a699e5" />

<br><br>

<h6>Labels</h6>
They provide context to the axes, clalifying what each axis represnts and enhancing understanding of the plot.
<br>
The <code>xlabel</code> and <code>ylabel</code> describe what each axis represents, giving meaning to the numeric scales.

<br><br>

<h6>Example</h6>
<br>

```python

      # import the plotting library
      import matplotlib.pyplot as plt

      # define the segements on the x and y axis
      # Note: unless specified, matplotlib will decide what the scale is
      x = [1, 2, 3]    # this is a line that goes from x=1 ...to .... x = 4
      y = [4, 5, 6]    # this is a line that goes from y=4 ...to .... y = 6

      # Define the title of the graph
      plt.title('title in here')

      # Define the name of the x-axis
      plt.xlabel(' name in here')

      # Define the name of the y axis
      plt.ylabel('name here')

      # Show the canvas
      plt.plot(x, y)

```

<br><br>


<h6>Axes</h6>
These are the areas within the figure where data is plotted <br>
functioning as a grid of organising and desplaying data points<br>
These can be nested too
<br><br>

<h6>Example</h6>
<br>

```python

      # import thr matplot library
      import matplotlib.pyplot as plt

      # create a figure with 2 ROWS and 2 COLUMNS of subplots
      fig, ax = plt.subplots(2,2)    # this reads as 👉 within the fig, plot ax

      # access individual subplots using indexing

      # top-left subplot
      ax[0, 0].plot([1, 2, 3], [4, 5, 6])

      # Top right subplot
      ax[0, 1].bar(['A', 'B', 'C'], [7, 8, 9])

      # Bottom left subplot
      ax[1, 0].scatter([10, 20, 30], [11, 12, 13])

      # bottom right subplot
      ax[1, 1].hist([1, 1, 2, 3, 3, 3])

      # show the plot
      plt.show()

```

<br><br>
Here are the figure and the subplots that were created in the figure<br><br>

<img width="669" height="427" alt="Screenshot 2025-11-29 at 12 16 30" src="https://github.com/user-attachments/assets/dcc8b2c7-8407-4de3-8305-12aafbedd9d0" />

<br><br>
<h3>Matplotlib Library</h3>


  

<code>to be continued .... </code>
