import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv')
    df = df.dropna(subset=['title', 'publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

st.title("📘 CORD-19 Data Explorer")
st.write("Explore COVID-19 research trends from the CORD-19 dataset.")

# Year range filter
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Visualization 1: Publications by Year
st.subheader("📈 Publications per Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Visualization 2: Top Journals
st.subheader("🏛️ Top 10 Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
ax.set_xlabel("Publications")
st.pyplot(fig)

# Visualization 3: Word Cloud
st.subheader("☁️ Common Words in Titles")
text = " ".join(filtered['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# Display data sample
st.subheader("📋 Sample Data")
st.dataframe(filtered.head(10))
