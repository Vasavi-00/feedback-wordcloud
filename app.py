# ============================================================
# Live Feedback Word Cloud - Streamlit Application
# Collects anonymous responses and visualizes them as a word cloud
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import os

# ── Configuration ────────────────────────────────────────────
CSV_FILE = "responses.csv"
QUESTION = "What comes to your mind when you hear Artificial Intelligence?"
MAX_CHARS = 100


# ── Helper: Load responses ───────────────────────────────────
def load_responses():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=["response"])
        df.to_csv(CSV_FILE, index=False)
        return df


# ── Helper: Save response ────────────────────────────────────
def save_response(text):
    df = load_responses()
    new_row = pd.DataFrame({"response": [text]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)


# ── Helper: Generate word cloud ──────────────────────────────
def generate_wordcloud(df):

    if df.empty:
        return None

    all_text = " ".join(df["response"].dropna().astype(str).tolist())

    if not all_text.strip():
        return None

    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update([
        "the","is","and","a","an","of","to","in","it",
        "that","this","with","for","on","are","was",
        "be","as","at","by","we","or","from"
    ])

    wc = WordCloud(
        width=900,
        height=450,
        background_color="white",
        stopwords=custom_stopwords,
        max_words=200,
        colormap="viridis",
        collocations=False
    ).generate(all_text)

    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    plt.tight_layout()

    return fig


# ── Page Setup ───────────────────────────────────────────────
st.set_page_config(
    page_title="Live Feedback Word Cloud",
    page_icon="☁️",
    layout="centered"
)

# ── Title ────────────────────────────────────────────────────
st.title("☁️ Live Feedback Word Cloud")
st.write("Submit a word or short phrase. Responses are **anonymous**.")

st.divider()

# ── Question ─────────────────────────────────────────────────
st.subheader("💬 Question")
st.write(f"**{QUESTION}**")

st.divider()

# ── Input Section ────────────────────────────────────────────
st.subheader("✏️ Your Response")

user_input = st.text_input(
    "Type your response below:",
    max_chars=MAX_CHARS,
    placeholder="Example: automation, robots, future..."
)

remaining = MAX_CHARS - len(user_input)
st.caption(f"{remaining} characters remaining")

# ── Submit ───────────────────────────────────────────────────
if st.button("Submit Response", type="primary"):

    cleaned = user_input.strip()

    if cleaned == "":
        st.warning("Please enter a response before submitting.")

    else:
        save_response(cleaned)
        st.success("Your response has been recorded!")

        st.rerun()

st.divider()

# ── Word Cloud Section ───────────────────────────────────────
st.subheader("🌐 Live Word Cloud")

df = load_responses()
total = len(df)

if total == 0:
    st.info("No responses yet. Be the first to submit one!")

else:

    st.caption(f"Generated from {total} responses")

    fig = generate_wordcloud(df)

    if fig:
        st.pyplot(fig)


# ── Optional: Show Raw Responses ─────────────────────────────
with st.expander("View collected responses"):
    st.dataframe(df)


# ── Optional: Download Data ──────────────────────────────────
st.download_button(
    label="Download responses CSV",
    data=df.to_csv(index=False),
    file_name="responses.csv",
    mime="text/csv"
)

st.divider()

# ── Footer ───────────────────────────────────────────────────
st.caption("Built with ❤️ using Streamlit, WordCloud, Pandas, and Matplotlib")