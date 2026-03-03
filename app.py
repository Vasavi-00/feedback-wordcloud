# ============================================================
# Live Feedback Word Cloud - Streamlit Application
# ============================================================
# This app collects anonymous user responses and visualizes
# them as a live-updating word cloud.
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import os

# ── Configuration ────────────────────────────────────────────
CSV_FILE = "responses.csv"          # File where responses are stored
QUESTION = "What comes to your mind when you hear Artificial Intelligence?"
MAX_CHARS = 100                     # Maximum allowed response length


# ── Helper: Load responses from CSV ─────────────────────────
def load_responses() -> pd.DataFrame:
    """
    Read stored responses from the CSV file.
    Returns an empty DataFrame if the file does not exist yet.
    """
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    # Create an empty DataFrame with the expected column
    return pd.DataFrame(columns=["response"])


# ── Helper: Save a new response to CSV ──────────────────────
def save_response(text: str) -> None:
    """
    Append a single response to the CSV file.
    Only the response text is stored — no names, emails, or IPs.
    """
    df = load_responses()
    new_row = pd.DataFrame({"response": [text]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)


# ── Helper: Generate word cloud figure ──────────────────────
def generate_wordcloud(df: pd.DataFrame) -> plt.Figure | None:
    """
    Combine all responses into one string and render a WordCloud.
    Returns None when there is no text to display.
    """
    if df.empty:
        return None

    # Join every response into a single large block of text
    all_text = " ".join(df["response"].dropna().astype(str).tolist())

    if not all_text.strip():
        return None
l
    # Build a custom stopword set (STOPWORDS comes from the wordcloud library)
    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update(["the", "is", "and", "a", "an", "of", "to", "in",
                              "it", "that", "this", "with", "for", "on", "are",
                              "was", "be", "as", "at", "by", "we", "or", "from"])

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        stopwords=custom_stopwords,
        max_words=200,
        colormap="viridis",        # Colour scheme — change freely
        collocations=False,        # Avoid repeating two-word pairs
    ).generate(all_text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    plt.tight_layout(pad=0)
    return fig


# ── Page setup ───────────────────────────────────────────────
st.set_page_config(
    page_title="Live Feedback Word Cloud",
    page_icon="☁️",
    layout="centered",
)

# ── Title ────────────────────────────────────────────────────
st.title("☁️ Live Feedback Word Cloud")
st.markdown("---")

# ── Section 1 · Question ─────────────────────────────────────
st.subheader("💬 Question")
st.markdown(f"**{QUESTION}**")
st.markdown("---")

# ── Section 2 · Input box ────────────────────────────────────
st.subheader("✏️ Your Response")
user_input = st.text_input(
    label="Type your response below:",
    max_chars=MAX_CHARS,
    placeholder="e.g. automation, robots, ChatGPT …",
)

# Character counter shown beneath the box
remaining = MAX_CHARS - len(user_input)
st.caption(f"{remaining} characters remaining  |  🔒 Responses are fully anonymous — no personal data is collected.")

# ── Section 3 · Submit button ────────────────────────────────
st.subheader("📨 Submit")
if st.button("Submit Response", type="primary"):
    cleaned = user_input.strip()

    if not cleaned:
        st.warning("⚠️ Please type a response before submitting.")
    else:
        save_response(cleaned)
        st.success("✅ Your response has been recorded — thank you!")
        # Rerun so the word cloud below refreshes immediately
        st.rerun()

st.markdown("---")

# ── Section 4 · Live word cloud ──────────────────────────────
st.subheader("🌐 Live Word Cloud")

df = load_responses()
total = len(df)

if total == 0:
    st.info("No responses yet. Be the first to submit one above!")
else:
    st.caption(f"Generated from **{total}** response(s) collected so far.")
    fig = generate_wordcloud(df)
    if fig:
        st.pyplot(fig)
    else:
        st.info("Not enough text to build a word cloud yet.")

# ── Footer ───────────────────────────────────────────────────
st.markdown("---")
st.caption("Built with ❤️ using Streamlit · WordCloud · Matplotlib · Pandas")