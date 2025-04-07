import pandas as pd

df = pd.read_csv(r"C:\Users\m8cg2\OneDrive\Desktop\elevate lab data analyst intern\day-1 task\corrected_marketing_campaign.csv")  # remove sep="\t"

print(df.columns)
df.head()
df.columns = df.columns.str.strip()  # Clean column names
df['Education'] = df['Education'].str.strip().str.lower()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.lower()

print(df.isnull().sum())

df = df.dropna()
df = df.drop_duplicates()
df['Education'] = df['Education'].str.strip().str.lower()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.lower()
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df['income'] = df['income'].astype(float)
df['kidhome'] = df['kidhome'].astype(int)
df['teenhome'] = df['teenhome'].astype(int)
df.to_csv("cleaned_customer_personality.csv", index=False)
