import pandas as pd

df=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\AMIR\Shark Tank US.csv")
# print(df.head())
print(df.info())
# print(df.describe())


industry_average=df.groupby('Industry')['Total Deal Amount'].mean().sort_values(ascending=False)
print('Average Deal Amount Per Industry')
print(industry_average)

shark_amount_columns = [
    'Barbara Corcoran Investment Amount',
    'Mark Cuban Investment Amount',
    'Lori Greiner Investment Amount',
    'Robert Herjavec Investment Amount',
    'Daymond John Investment Amount',
    'Kevin O Leary Investment Amount'
]

sharks_contribution=df[shark_amount_columns].sum()
print("Total Contribution by Per Shark")
print(sharks_contribution.sort_values(ascending=False))


season_investment=df.groupby('Season Number')['Total Deal Amount'].sum()
print('Total Deal Amount Per Season')
print(season_investment)

print(df[['Pitchers City','Pitchers State']].head())
df['Pitchers Location']=df['Pitchers City'] + ',' + df['Pitchers State']

print(df[['Startup Name', 'Pitchers Location']].head())

state_count=df['Pitchers State'].value_counts()
print(state_count)


city_count=df['Pitchers City'].value_counts()
print(city_count)


top_location=df['Pitchers Location'].value_counts().head(10)
print(top_location)


df.to_csv('clean shark tank us.csv',index=False)