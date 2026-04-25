import pandas as pd 

df = pd.read_csv(r"C:Windows\path", encoding='latin1')


print(df.head()) #Display first 5 rows of each column 
print(df.info()) #Display number of lines, column's type and not null value
print(df.describe()) #Display basics statistics of numeric columns
print(df.isnull().sum()) #Calcul and display the number of missing values in each column 


df.drop(columns=["Postal Code"],inplace=True) #Remove the column Postal Code without creating copy

#Conversion of columns order date and ship date to date format
df["Order Date"]= pd.to_datetime(df["Order Date"],dayfirst=True) 
df["Ship Date"]= pd.to_datetime(df["Ship Date"], dayfirst=True)

#Verification that the columns has been transformed
print(f"\nDates après conversion :")
print(df[["Order Date", "Ship Date"]].dtypes)
#Display an example 
print(f"\nExemple :")
print(df[["Order Date", "Ship Date"]].head(30))

# Export
df.to_csv("Global_Superstore_clean.csv", index=False, encoding="utf-8")
print(f"\nExport terminé")
