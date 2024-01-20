import pandas as pd
import numpy as np
from datetime import datetime

df = pd.merge(linkedin_projects, linkedin_emp_projects, how = 'inner',left_on = ['id'], right_on=['project_id'])
df1 = pd.merge(df, linkedin_employees, how = 'inner',left_on = ['emp_id'], right_on=['id'])
df1['project_duration'] = (pd.to_datetime(df1['end_date']) - pd.to_datetime(df1['start_date'])).dt.days
df_expense = df1.groupby('title')['salary'].sum().reset_index(name='expense')
df_budget_expense = pd.merge(df1, df_expense, how = 'left',left_on = ['title'], right_on=['title'])
df_budget_expense['prorated_expense'] = np.ceil(df_budget_expense['expense']*(df_budget_expense['project_duration'])/365)
df_budget_expense['budget_diff'] = df_budget_expense['prorated_expense'] - df_budget_expense['budget']
df_over_budget = df_budget_expense[df_budget_expense["budget_diff"] > 0]
result = df_over_budget[['title','budget','prorated_expense']]
result = result.drop_duplicates().sort_values('title')
