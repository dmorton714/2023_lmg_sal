import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def OT(year):
    df_filtered = df[df['CalYear'] == year]
    df_filtered = df_filtered[df_filtered['Overtime_Rate'] > df_filtered['Regular_Rate']]
    # df_filtered = df_filtered.sort_values(by='YTD_Total', ascending=False)
    return df_filtered

def Dep_yearly(year):
    pd.options.display.float_format = '{:.2f}'.format
    department = df[df['CalYear'] == year]
    department = department.groupby(['CalYear', 'Department'])['YTD_Total'].sum().reset_index()
    department = department.sort_values(by='YTD_Total', ascending=False)
    department.head()
    return department

def process_salary_data(url):
    df = pd.read_csv(url)
    df['Hr_Rate'] = df['Regular_Rate'] / 2080
    df['Ot_Rate'] = df['Hr_Rate'] * 1.5
    df['Hr_Worked'] = df['Overtime_Rate'] / df['Ot_Rate'] / 52 + 40
    df = df.sort_values(by='Hr_Worked', ascending=False)
    return df

data_url = "data/Louisville_Metro_KY_-_Employee_Salary_Data.csv"
df = process_salary_data(data_url)
df

def millions_formatter(x, pos):
    return f'{x / 1e6:.0f}M'

def a_dep(df):
    ax = df.plot.bar(x='Department')
    ax.legend_ = None
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.gcf().set_size_inches(10, 6)
    plt.ylabel('Millions USD')
    plt.title('Annual Salary Spend by Department')
    plt.show()

def OT_E(dataframe):
    top_20 = dataframe.head(20)
    top_20.plot.bar(x='Employee_Name', y='Hr_Worked')
    plt.xticks()
    plt.xlabel('Employee Name')
    plt.ylabel('Hours Worked')
    plt.title('Top 15 Employees by Hours Worked')
    plt.show()

def plot_department_counts(dataframe):
    department_counts = dataframe['Department'].value_counts()
    department_counts.plot(kind='bar')
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.title('Department Counts')
    plt.show()