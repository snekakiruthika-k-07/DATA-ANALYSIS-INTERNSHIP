# -*- coding: utf-8 -*-
"""cognifyz technology

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mmamWjYurJayujpMAxAG2ia7G07fnh5w
"""

import pandas as pd
df = pd.read_csv("/content/Dataset .csv")
df

df.columns

#TASK 1
# Assuming the column containing cuisine information is named 'Cuisine'
cuisine_counts = df['Cuisines'].value_counts()
# Get the top three cuisines
top_three_cuisines = cuisine_counts.head(3)
print("ALL CUISINES",cuisine_counts)
print("Top three cuisines:")
print(top_three_cuisines)
import matplotlib.pyplot as plt
plt.pie(top_three_cuisines, labels=top_three_cuisines.index, autopct='%1.1f%%', startangle=140)
plt.title('Top Three Cuisines')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#TASK 2
# Assuming the column containing city information is named 'City'
city_counts = df['City'].value_counts()

# Get the city with the highest number of restaurants
city_with_most_restaurants = city_counts.idxmax()

# Group by city and calculate the average rating for each city
average_ratings_by_city = df.groupby('City')['Aggregate rating'].mean()

# Find the city with the highest average rating
city_with_highest_average_rating = average_ratings_by_city.idxmax()
highest_average_rating = average_ratings_by_city.max()

print("City with the highest average rating:", city_with_highest_average_rating)
print("Average rating:", average_ratings_by_city)
print("City with the highest number of restaurants:", city_with_most_restaurants)

#TASK 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming the columns containing restaurant names and price range information are named 'Restaurant Name' and 'Price Range'
restaurant_names = df['Restaurant Name']
price_ranges = df['Price range']

# Create a bar chart with default colors
plt.figure(figsize=(10, 6))
plt.bar(restaurant_names, price_ranges, color='skyblue')
plt.xlabel('Restaurant Name')
plt.ylabel('Price Range')
plt.title('Restaurant Price Range with Default Colors')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Assuming the column containing price range information is named 'Price Range'
price_range_counts = df['Price range'].value_counts()

# Calculate the total number of restaurants
total_restaurants = len(df)

# Calculate the percentage of restaurants in each price range category
percentage_restaurants_by_price_range = (price_range_counts / total_restaurants) * 100

print("Percentage of restaurants in each price range category:")
print(percentage_restaurants_by_price_range)

# Convert string values to boolean
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': True, 'No': False})

# Count the number of restaurants that offer online delivery
online_delivery_count = df['Has Online delivery'].sum()

# Calculate the total number of restaurants
total_restaurants = len(df)

# Calculate the percentage of restaurants that offer online delivery
percentage_restaurants_with_delivery = (online_delivery_count / total_restaurants) * 100

print("Percentage of restaurants that offer online delivery:", percentage_restaurants_with_delivery)

with_delivery = df[df['Has Online delivery'] == 'Yes']
without_delivery = df[df['Has Online delivery'] == 'No']

# Step 2: Calculate the average ratings for each dataset
avg_rating_with_delivery = with_delivery['Aggregate rating'].mean()
avg_rating_without_delivery = without_delivery['Aggregate rating'].mean()

# Step 3: Compare the average ratings
print("Average rating with online delivery:", avg_rating_with_delivery)
print("Average rating without online delivery:", avg_rating_without_delivery)

#task 1
# Step 1: Bin the aggregate ratings into ranges
rating_ranges = pd.cut(df['Aggregate rating'], bins=[0, 1, 2, 3, 4, 5])

# Step 2: Count the number of ratings in each range
rating_counts = rating_ranges.value_counts()

# Step 3: Determine the range with the highest count
most_common_range = rating_counts.idxmax()

# Display the results
print("Distribution of Aggregate Ratings:")
print(rating_counts)
print("\nMost common rating range:", most_common_range)

# Calculate the average number of votes received by restaurants
average_votes = df['Votes'].mean()

# Display the result
print("Average number of votes received by restaurants:", average_votes)

#task 2
# Step 1: Split the 'Cuisines' column to extract individual cuisines
cuisine_counts = df['Cuisines'].str.split(', ', expand=True)

# Step 2: Reshape the DataFrame to have cuisines in a single column
cuisine_counts = cuisine_counts.melt(value_name='Cuisine').dropna()

# Step 3: Count the occurrences of each unique combination of cuisines
common_cuisine_combinations = cuisine_counts.groupby(cuisine_counts.columns.tolist()).size().reset_index(name='Count')

# Step 4: Sort by count to find the most common combinations
most_common_combinations = common_cuisine_combinations.sort_values(by='Count', ascending=False)

# Display the top 10 most common combinations
print("Top 10 most common combinations of cuisines:")
print(most_common_combinations.head(10))

# Step 1: Split the 'Cuisines' column to extract individual cuisines
cuisine_counts = df['Cuisines'].str.split(', ', expand=True)

# Step 2: Reshape the DataFrame to have cuisines in a single column
cuisine_counts = cuisine_counts.melt(value_name='Cuisine').dropna()

# Step 3: Merge the cuisine information back to the original dataset
merged_data = pd.merge(df, cuisine_counts, left_index=True, right_index=True)

# Step 4: Calculate the average rating for each unique combination of cuisines
avg_rating_by_cuisine = merged_data.groupby('Cuisine')['Aggregate rating'].mean().reset_index(name='Average Rating')

# Step 5: Sort the combinations by average rating to find the highest-rated cuisines
sorted_avg_ratings = avg_rating_by_cuisine.sort_values(by='Average Rating', ascending=False)

# Display the top 10 highest-rated cuisine combinations
print("Top 10 highest-rated cuisine combinations:")
print(sorted_avg_ratings.head(10))

#task 3
import folium
# Create a map centered on the mean latitude and longitude
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
mymap = folium.Map(location=map_center, zoom_start=10)

# Add markers for each restaurant
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(mymap)

# Save the map to an HTML file
mymap.save("restaurant_locations.html")
mymap
from google.colab import files
files.download("restaurant_locations.html")

import pandas as pd
import folium
from sklearn.cluster import KMeans


# Extract latitude and longitude coordinates
coordinates = df[['Latitude', 'Longitude']]

# Perform K-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # You can adjust the number of clusters as needed
clusters = kmeans.fit_predict(coordinates)

# Add cluster labels to the dataset
df['Cluster'] = clusters

# Create a map centered on the mean latitude and longitude
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
mymap = folium.Map(location=map_center, zoom_start=10)

# Define colors for clusters
cluster_colors = ['red', 'blue', 'green', 'purple', 'orange']

# Add markers for each restaurant with cluster color
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color=cluster_colors[row['Cluster']],
        fill=True,
        fill_color=cluster_colors[row['Cluster']],
        fill_opacity=0.7,
        popup=row['Restaurant Name']
    ).add_to(mymap)

# Save the map to an HTML file
mymap.save("restaurant_clusters.html")
mymap

#task 4
# Group the dataset by 'Restaurant Name' and count occurrences
restaurant_counts = df.groupby('Restaurant Name').size()

# Filter out restaurant names that occur more than once
restaurant_chains = restaurant_counts[restaurant_counts > 1]

# Display the identified restaurant chains
print("Restaurant chains present in the dataset:")
print(restaurant_chains)

# Step 1: Identify restaurant chains
restaurant_chains = df.groupby('Restaurant Name').size()
restaurant_chains = restaurant_chains[restaurant_chains > 1].index.tolist()

# Step 2: Calculate the average rating for each restaurant chain
chain_ratings = {}
for chain in restaurant_chains:
    chain_data = df[df['Restaurant Name'] == chain]
    avg_rating = chain_data['Aggregate rating'].mean()
    chain_ratings[chain] = avg_rating

# Step 3: Analyze the popularity of each restaurant chain based on the number of votes
chain_popularity = {}
for chain in restaurant_chains:
    chain_data = df[df['Restaurant Name'] == chain]
    total_votes = chain_data['Votes'].sum()
    chain_popularity[chain] = total_votes

# Convert dictionaries to pandas Series for easier analysis
chain_ratings = pd.Series(chain_ratings)
chain_popularity = pd.Series(chain_popularity)

# Combine ratings and popularity into a DataFrame
chain_data = pd.DataFrame({'Average Rating': chain_ratings, 'Total Votes': chain_popularity})

# Display the DataFrame sorted by average rating
print("Restaurant chains sorted by average rating:")
print(chain_data.sort_values(by='Average Rating', ascending=False))

# Display the DataFrame sorted by total votes
print("\nRestaurant chains sorted by total votes:")
print(chain_data.sort_values(by='Total Votes', ascending=False))

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Assuming the text reviews are in a column named 'Rating text'
reviews = df['Rating text']

# Step 1: Preprocessing
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Apply preprocessing to each review
preprocessed_reviews = reviews.apply(preprocess_text)

# Step 2: Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'positive'
    elif score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis to each review
sentiments = preprocessed_reviews.apply(get_sentiment)

# Step 3: Keyword Extraction
positive_reviews = preprocessed_reviews[sentiments == 'positive']
negative_reviews = preprocessed_reviews[sentiments == 'negative']

# Step 4: Counting
vectorizer = CountVectorizer()

# Fit and transform positive reviews
positive_counts = vectorizer.fit_transform(positive_reviews)

# Fit and transform negative reviews
negative_counts = vectorizer.fit_transform(negative_reviews)

# Step 5: Analysis
positive_keywords = vectorizer.get_feature_names_out()
negative_keywords = vectorizer.get_feature_names_out()

# Display the most common positive and negative keywords
print("Most common positive keywords:", positive_keywords)
print("Most common negative keywords:", negative_keywords)

import nltk
nltk.download('stopwords')