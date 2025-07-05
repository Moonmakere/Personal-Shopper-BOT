import streamlit as st

# Page configuration
st.set_page_config(page_title="Personalized E-Commerce Recommender Bot", layout="wide")

# App Title
st.title("🛍️ Personalized E-Commerce Recommender Bot")

# Tabs for navigation
tabs = st.tabs(["🏠 Home", "🤖 Bot"])

# Home Tab
with tabs[0]:
    st.header("Welcome to Your Personal Shopping Assistant!")
    st.markdown("""
    This AI-powered assistant helps you discover **hyper-personalized product recommendations** for Indian D2C food and fashion brands.

    ### 🔍 Key Features:
    - Understands your **natural language queries** (e.g., "vegan snacks under ₹300")
    - Recommends products with **confidence scores** and **clear justifications**
    - Considers your **diet, style, budget, and seasonal preferences**
    - Tailored specifically for the **Indian market**
    
    ---
    
    #### 🧠 Sample Queries You Can Try:
    - `I need vegan snacks under ₹300`
    - `Trendy ethnic wear for festive season`
    - `Casual shoes for men under ₹2000`
    - `High-protein breakfast options`

    ---
    """)
    st.success("Switch to the **Bot tab** to start chatting!")

# Bot Tab
with tabs[1]:
    st.header("🤖 Chat with Your Shopping Assistant")

    # Input from user
    user_input = st.text_input("What are you looking for today?", placeholder="e.g. I need vegan snacks under ₹300")

    # Simulate bot response (Placeholder for integration)
    if user_input:
        st.subheader("🛒 Top Recommendations for You:")
        with st.container():
            st.markdown("### 1. **Plant-Based Protein Cookies** - ₹299")
            st.progress(0.95)
            st.info("Why it's perfect: These gluten-free cookies fit your vegan diet and budget perfectly. With 12g plant protein per serving, they're both healthy and delicious!")

        with st.container():
            st.markdown("### 2. **Quinoa Energy Bites** - ₹249")
            st.progress(0.87)
            st.info("Why it's perfect: Vegan superfood snacks under your budget with natural sweetness from dates and coconut.")

    else:
        st.warning("Enter a query above to get recommendations!")

