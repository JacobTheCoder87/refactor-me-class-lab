import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?

# OLD CODE BELOW
#s1 = df['Purchase Amount (USD)'].mean()
#s2 = df['Purchase Amount (USD)'].median()
#s3 = df['Purchase Amount (USD)'].max()
#s4 = df['Purchase Amount (USD)'].min()
#s5 = df['Purchase Amount (USD)'].std()

#print("Summary statistics on Purchase Amount (USD)")
#print("Mean", s1)
#print("Median", s2)
#print("Max", s3)
#print("Min", s4)
#print("Standard Dev", s5)
#print()


# NEW CODE: We can just use the describe function to print out the summary statistics on the Purchase Amount (USD) column.
PASummaryStat = df["Purchase Amount (USD)"].describe()
print("Summary statistics on Purchase Amount (USD)")
print(PASummaryStat)
print()

# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?

# OLD CODE BELOW
#s1 = df['Age'].mean()
#s2 = df['Age'].median()
#s3 = df['Age'].max()
#s4 = df['Age'].min()
#s5 = df['Age'].std()

#print("Summary statistics on Age")
#print("Mean", s1)
#print("Median", s2)
#print("Max", s3)
#print("Min", s4)
#print("Standard Dev", s5)
#print()

#Same as what was done above. We could use the describe function to help us print out the summary statistics with less
#and more concise code
AgeSummaryStat = df["Age"].describe()
print("Summary statistics on Age")
print(AgeSummaryStat)
print()

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?

# OLD CODE BELOW
#winter = df[df.Season == "Winter"]
#summer = df[df.Season == "Summer"]
#spring = df[df.Season == "Spring"]
#fall = df[df.Season == "Fall"]

#s1 = winter['Purchase Amount (USD)'].mean()
#s2 = winter['Purchase Amount (USD)'].median()
#s3 = winter['Purchase Amount (USD)'].max()
#s4 = winter['Purchase Amount (USD)'].min()
#s5 = winter['Purchase Amount (USD)'].std()

#print("Winter summary statistics on Purchase Amount (USD)")
#print("Mean", s1)
#print("Median", s2)
#print("Max", s3)
#print("Min", s4)
#print("Standard Dev", s5)
#print()

#s1 = summer['Purchase Amount (USD)'].mean()
#s2 = summer['Purchase Amount (USD)'].median()
#s3 = summer['Purchase Amount (USD)'].max()
#s4 = summer['Purchase Amount (USD)'].min()
#s5 = summer['Purchase Amount (USD)'].std()

#print("Summer summary statistics on Purchase Amount (USD)")
#print("Mean", s1)
#print("Median", s2)
#print("Max", s3)
#print("Min", s4)
#print("Standard Dev", s5)
#print()

#s1 = spring['Purchase Amount (USD)'].mean()
#s2 = spring['Purchase Amount (USD)'].median()
#s3 = spring['Purchase Amount (USD)'].max()
#s4 = spring['Purchase Amount (USD)'].min()
#s5 = spring['Purchase Amount (USD)'].std()

#print("Spring summary statistics on Purchase Amount (USD)")
#print("Mean", s1)
#print("Median", s2)
#print("Max", s3)
#print("Min", s4)
#print("Standard Dev", s5)
#print()

#s1 = fall['Purchase Amount (USD)'].mean()
#s2 = fall['Purchase Amount (USD)'].median()
#s3 = fall['Purchase Amount (USD)'].max()
#s4 = fall['Purchase Amount (USD)'].min()
#s5 = fall['Purchase Amount (USD)'].std()

#print("Fall summary statistics on Purchase Amount (USD)")
#print("Mean", s1)
#print("Median", s2)
#print("Max", s3)
#print("Min", s4)
#print("Standard Dev", s5)
#print()


# NEW CODE: We could just use the function groupby to group the data in Seasons and selecting only the Purchase Amount (USD) from the 
# Season category and then use the describe function to help us get the summary statistics of all the seasons in a much more concise code.
print("Seasons summary statistics on Purchase Amount (USD)")
SeasonsSummary = df.groupby("Season")["Purchase Amount (USD)"].describe()
print(SeasonsSummary)
print()

# keep all columns except for "Customer", & "Discount Applied"
# TODO: is there a more efficient way to exclude columns in your dataset?

# OLD CODE
#df = df[[
    #"Customer ID",
    #"Age",
    #"Gender",
    #"Item Purchased",
    #"Category",
    #"Purchase Amount (USD)",
    #"Location",
    #"Size",
    #"Color",
    #"Season",
    #"Review Rating",
    #"Subscription Status",
    #"Shipping Type",
    #"Promo Code Used",
    #"Previous Purchases",
    #"Payment Method",
    #"Frequency of Purchases"
#]]

#New code: Just use the drop method to drop the two columns.

drop_column_on_data = df.drop(columns=["Customer ID", "Discount Applied"])

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)

#OLD CODE
#payment_methods = df['Payment Method'].unique()
#ny = df[df.Location == "New York"]

#most_frequent_method = {}

#for method in payment_methods:
    #most_frequent_method[method] = len(ny[ny['Payment Method'] == method])

#print(most_frequent_method)

#NEW CODE: We could use the groupby method again to filter out specifically for the payment method and the location. Then we can use
#value_counts to help us count the value of that filtered data.

payment_methods = df.groupby("Payment Method")['Location'].value_counts()
print(payment_methods)

# Write this updated data out to csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
