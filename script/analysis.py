# %%
import pandas as pd

# %%

df = pd.read_excel("../data/salary_survey.xlsx")
df

# %%

df.columns

# %%
df.columns = df.columns.str.replace('"', '')

# %%

df = df.rename(columns = {
                "Timestamp": "timestamp",
                "How old are you?": "age",
                "What industry do you work in?": "industry",
                "Job title": "job_title",
                "If your job title needs additional context, please clarify here:": "job_additional_context",
                "What is your annual salary? (You'll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)": "annual_salary",
                "How much additional monetary compensation do you get, if any (for example, bonuses or overtime in an average year)? Please only include monetary compensation here, not the value of benefits.": "additional_salary",
                "Please indicate the currency": "currency",
                "If Other, please indicate the currency here: ": "other_currency",
                "If your income needs additional context, please provide it here:": "income_additional_context",
                "What country do you work in?": "country",
                "If you're in the U.S., what state do you work in?": "us_state",
                "What city do you work in?": "city",
                "How many years of professional work experience do you have overall?": "years_of_experience_overall",
                "How many years of professional work experience do you have in your field?": "years_of_experience_field",
                "What is your highest level of education completed?": "level_of_education",
                "What is your gender?": "gender",
                "What is your race? (Choose all that apply.)": "race"

                }) 
df

# %%
df = df.drop(columns=['timestamp'])

# %%
df.isna().sum()

# %%

filter_columns = ["age",
                  "job_title",
                  "annual_salary",
                  "currency",
                  "country",
                  "years_of_experience_overall"]

df = df[filter_columns]
df

