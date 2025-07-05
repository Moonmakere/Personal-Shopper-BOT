import streamlit as st

# Page configuration
st.set_page_config(page_title="Fashion Recommender Bot", layout="wide")

# App Title
st.title("👗 Personalized Fashion Recommender Bot")

# Tabs for navigation
tabs = st.tabs(["🏠 Home", "🧵 Bot"])

# Home Tab
with tabs[0]:
    st.header("Welcome to Your AI Fashion Assistant!")
    st.markdown("""
    This intelligent assistant helps you find **stylish, budget-friendly fashion** from top Indian D2C brands based on your preferences.

    ### ✨ Key Features:
    - Understands your **fashion style, budget, season, and occasion**
    - Offers **highly personalized outfit suggestions** using AI
    - Considers **Indian trends**, festivals, and local pricing (₹)
    - Delivers clear **justifications** for each recommendation
    
    ---
    
    #### 🧠 Sample Queries You Can Try:
    - `Light ethnic wear for summer`
    - `Trendy casual wear under ₹1000`
    - `Traditional outfit for Diwali under ₹2500`
    - `Formal wear for office meetings`
    
    ---
    """)
    st.success("Switch to the **Bot tab** to get your outfit recommendations!")

# Bot Tab
with tabs[1]:
    st.header("🧵 Talk to Your Fashion Stylist")

    # Input from user
    user_input = st.text_input("Describe your fashion need:", placeholder="e.g. Trendy casual wear under ₹1000")

    # Simulate bot response (Placeholder for integration)
    if user_input:
        st.subheader("👚 Recommended Outfits for You:")
        
        with st.container():
            st.markdown("### 1. **Oversized Cotton Tee** – ₹799")
            st.progress(0.85)
            st.info("Why it's perfect: On-trend oversized fit in breathable cotton – stylish and comfortable for casual outings within your budget.")

        with st.container():
            st.markdown("### 2. **Handblock Print Kurta** – ₹1499")
            st.progress(0.92)
            st.info("Why it's perfect: 100% cotton kurta keeps you cool and elegant – ideal for summer events or small traditional functions.")

    else:
        st.warning("Enter your outfit preference above to get recommendations!")
