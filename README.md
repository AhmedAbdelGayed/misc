#Defination: 
This Python function builds an item to item collaboration filering based recommendations engine based on a correlation matrix which is used basically for lookups.
The matrix values are correlation values between items. The values are calculated based on pandas corr function that can be called using multile correlation methods to calculate correlation values with minimum events.
#Input:
is a Pandas dataframe of users and Products/Services usage
#Application: 
The application of the function can be used to determine the correlation between the products/services based on customer usage. It is useful to determine how a specific product/service change can impact other products too.
