import streamlit as st
import feedparser
import pandas as pd

st.title("Apple Mentions in News (RSS)")

keywords = ["apple", "iphone", "aapl", "tim cook"]

# Working RSS feed
url = "https://news.google.com/rss/search?q=Apple&hl=en-GB&gl=GB&ceid=GB:en"

if st.button("Fetch and Count"):
    feed = feedparser.parse(url)

    matches = []

    for entry in feed.entries:
        title = (entry.get("title") or "").lower()
        link = entry.get("link") or ""

        if any(word in title for word in keywords):
            matches.append({"headline": entry.get("title"), "link": link})

    df = pd.DataFrame(matches)

    st.metric("Apple mentions", len(df))
    st.dataframe(df)