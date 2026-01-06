import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ---------------------------------
# Load environment variables
# ---------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("Gemini_API"))

# ---------------------------------
# Initialize Gemini model (safe)
# ---------------------------------
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------------------------
# App UI
# ---------------------------------
st.title("🎧 Song Recommend System")
st.markdown("### 🎶 Discover songs that match your mood")
st.markdown("---")

st.subheader("😊 Mood Input")
user_input = st.text_input("💭 How are you feeling right now?")

st.markdown("---")

submit_button = st.button("🎵 Recommend My Songs")

# ---------------------------------
# Recommendation Logic
# ---------------------------------
if submit_button:
    if user_input:
        st.markdown("## 🎼 Recommended Songs")
        st.markdown("_Here are some songs that match your vibe:_ 🎧")

        with st.spinner("🔍 Finding the perfect tracks for you..."):
            response = model.generate_content(
                f"""
Recommend 5 Indian songs that match the mood '{user_input}'.

Rules:
- Songs must be Indian (Hindi or regional Indian languages only)
- Do NOT include any international / non-Indian songs
- Output ONLY a markdown table
- Columns must be exactly:
  Song Name | Artist
"""

            )

        st.markdown(response.text)

        st.markdown("---")
        st.markdown("✨ _Enjoy your music and have a great day!_ ✨")

    else:
        st.warning("⚠️ Please enter your mood before clicking the button.")
