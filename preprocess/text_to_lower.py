text=['This is introduction to NLP','It is likely to be useful',
'to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage',
'I like this book','I want more books like this']
#convert list to data frame
import pandas as pd
df = pd.DataFrame({'tweet':text})
# print(df)

#When you want to perform lowercasing on a data frame, use the apply
#a function as shown below:

df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))
# print(df)
df['tweet'] = df['tweet'].str.replace('[^\w\s]','')
print(df)