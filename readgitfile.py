import pandas as pd

#########Reads Data from GIT##########

url_github = 'https://raw.githubusercontent.com/kiranvandavasi2915/raw/main/Customers.csv?raw=true'
pd.set_option('display.max_columns', None)
pd_df = pd.read_csv(url_github, index_col=0)


pdf = pd.DataFrame(pd_df)

print(pdf.head(5))



