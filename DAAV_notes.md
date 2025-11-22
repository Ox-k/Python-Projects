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












