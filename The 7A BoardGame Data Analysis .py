#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Importing the Necessary packages
import pandas as pd
from sklearn.model_selection import train_test_split


# In[30]:


# Question 1
games = pd.read_csv("C:\\Users\\n\\Downloads\\board_games (1).csv")
train_sample, test_sample = train_test_split(games, test_size=0.3, random_state=1031)
mean_rating_train = train_sample['rating'].mean()
print(f"Mean rating in the train sample: {mean_rating_train}")


# In[37]:


# Question 2
# Calculate the correlation coefficients
correlations = games[['min_age', 'age_of_game', 'max_players', 'min_players', 'playtime', 'rating']].corr()

# Find the variable with the highest absolute correlation coefficient
correlations = correlations.drop('rating')
strongest_correlation = correlations['rating'].abs().idxmax()

# Map the variable to the corresponding option
variable_options = {
    'min_age': 'a',
    'age_of_game': 'b',
    'max_players': 'c',
    'min_players': 'd',
    'playtime': 'e'
}

strongest_variable = variable_options[strongest_correlation]
print("Variable with the strongest correlation with game 'rating':", strongest_variable)


# In[38]:


#Question 3
# Count the number of games in each category
category_counts = games[['Fantasy', 'Economic', 'Wargame', 'CardGame', 'Fighting']].apply(pd.Series.value_counts).loc['Yes']

# Find the category with the highest count
most_popular_category = category_counts.idxmax()

print("Most popular game category:", most_popular_category)


# In[45]:


# Question 4
# Calculate the average rating for each category
# This code uses the groupby() function to group the games by the category columns 
# ('Economic', 'Fighting', 'CardGame', 'Fantasy', 'Wargame'), and then calculates the average rating 
# for each category using the mean() function on the 'rating' column.

category_ratings = games.groupby(['Economic', 'Fighting', 'CardGame', 'Fantasy', 'Wargame'])['rating'].mean()

# Find the category with the highest average rating
highest_rating_category = category_ratings.idxmax()

print("Game category with the highest rating:", highest_rating_category)


# In[44]:


#This is the End

