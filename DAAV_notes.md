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

