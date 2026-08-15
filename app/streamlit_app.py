
import streamlit as st
import pandas as pd
import numpy as np

# Page settings
st.set_page_config(page_title="Marketing Performance Predictor", page_icon="📊", layout="centered")

st.title("📊 Marketing Content Performance Predictor")
st.write("Predict the performance score of a social media post before publishing.")

# Inputs
industry = st.selectbox(
    "Industry",
    ["Fashion", "Food", "Education", "Technology", "Healthcare", "Real Estate"]
)

platform = st.selectbox(
    "Platform",
    ["Instagram", "YouTube Shorts", "Facebook"]
)

content_type = st.selectbox(
    "Content Type",
    ["Reel", "Carousel", "Static Post"]
)

topic = st.selectbox(
    "Topic",
    ["Product Education", "Behind the Scenes", "Offer/Discount", "Customer Story", "Trending Topic"]
)

posting_time = st.slider("Posting Time (24-hour)", 0, 23, 19)

ad_spend = st.number_input("Ad Spend (₹)", min_value=0, value=1500, step=100)

# Simple scoring logic (demo prototype)
score = 50

# Platform effect
if platform == "Instagram":
    score += 12
elif platform == "YouTube Shorts":
    score += 8
else:
    score += 4

# Content type effect
if content_type == "Reel":
    score += 15
elif content_type == "Carousel":
    score += 8
else:
    score += 3

# Topic effect
if topic == "Product Education":
    score += 10
elif topic == "Customer Story":
    score += 7
elif topic == "Trending Topic":
    score += 8
else:
    score += 5

# Posting time effect
if 18 <= posting_time <= 20:
    score += 10
elif 12 <= posting_time <= 14:
    score += 5
else:
    score += 2

# Industry effect
if industry in ["Fashion", "Food"]:
    score += 5

# Ad spend effect
score += min(ad_spend / 1000, 5)

# Keep score between 0 and 100
score = max(0, min(100, round(score, 1)))

# Engagement estimate
engagement = round(score * 0.065, 2)

# Predict button
if st.button("Predict Performance"):

    st.success(f"Predicted Performance Score: {score} / 100")

    st.metric("Expected Engagement Rate", f"{engagement}%")

    st.subheader("Top Factors")

    factors = []

    if content_type == "Reel":
        factors.append("Reel format historically performs best")

    if platform == "Instagram":
        factors.append("Instagram has higher engagement")

    if topic == "Product Education":
        factors.append("Educational content gets more saves and shares")

    if 18 <= posting_time <= 20:
        factors.append("Evening posting time is strong")

    if not factors:
        factors.append("Balanced content setup")

    for f in factors:
        st.write("• " + f)

    st.subheader("Recommendation")

    if score >= 80:
        st.info("Prioritize this post and publish between 6 PM and 8 PM.")
    elif score >= 65:
        st.info("Good post. Consider adding a stronger hook or CTA.")
    else:
        st.warning("Improve content type or posting time before publishing.")

st.divider()

st.caption("Demo prototype for assignment submission (simplified prediction logic).")
