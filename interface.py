import streamlit as st
import pickle

# ---------------- Load Model ----------------
# Ensure 'model.pkl' and 'vectorizer.pkl' are in the same directory
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    model_loaded = True
except Exception as e:
    model_loaded = False
    error_message = str(e)

# ---------------- Page Config ----------------
st.set_page_config(page_title="Fake News Detection System", page_icon="🔍", layout="wide")

# ---------------- Global CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f8f9fa, white);
    font-family: "Google Sans", Arial, sans-serif;
}
section[data-testid="stSidebar"] {
    background: white;
    border-right: 1px solid #e0e0e0;
}
.card {
    border-radius: 12px;
    padding: 15px;
    margin: 8px 0;
    color: white;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 14px rgba(0,0,0,0.3);
}

/* --- Category Buttons (Pills) --- */
/* Target all buttons within the category selection columns (horizontal block) */
[data-testid^="stHorizontalBlock"] button {
    /* General Pill Styling */
    width: 100%;
    height: 48px;
    border-radius: 24px; 
    color: white !important; 
    border: none !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    transition: all 0.2s ease;
    font-weight: bold;
}

/* Category Button Hover Effect */
[data-testid^="stHorizontalBlock"] button:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
    transform: translateY(-2px);
}

/* --- Headline Buttons (Cards) --- */
/* Target all buttons within the headlines vertical block */
[data-testid="stVerticalBlock"] > div:nth-child(2) [data-testid^="stButton"] button {
    /* General Card Styling */
    width: 100%;
    text-align: left;
    color: #333 !important;
    background-color: #f0f0f0 !important;
    border-radius: 8px !important;
    border: none !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    margin: 5px 0;
    padding-left: 20px;
    padding-top: 15px;
    padding-bottom: 15px;
    line-height: 1.2;
}

/* Headline Button Hover Effect */
[data-testid="stVerticalBlock"] > div:nth-child(2) [data-testid^="stButton"] button:hover {
    background-color: #e8e8e8 !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
    transform: none;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Google-style Title ----------------
def google_style_title():
    st.markdown("""<h1 style='text-align: center; font-family: "Google Sans", Arial, sans-serif; 
    font-size: 48px; font-weight: bold; letter-spacing: -1px;'>
<span style='color:blue'>F</span><span style='color:red'>a</span><span style='color:orange'>k</span><span style='color:blue'>e </span>
<span style='color:green'>N</span><span style='color:red'>e</span><span style='color:orange'>w</span><span style='color:blue'>s </span>
<span style='color:green'>D</span><span style='color:red'>e</span><span style='color:blue'>t</span><span style='color:orange'>e</span><span style='color:green'>c</span><span style='color:red'>t</span><span style='color:blue'>i</span><span style='color:orange'>o</span><span style='color:green'>n </span>
<span style='color:red'>S</span><span style='color:blue'>y</span><span style='color:green'>s</span><span style='color:orange'>t</span><span style='color:red'>e</span><span style='color:blue'>m</span>
</h1>""", unsafe_allow_html=True)

# ---------------- Prediction Function ----------------
def predict_news(text):
    # Confidence calculation removed as requested
    if not model_loaded:
        return f"⚠ Model not loaded: {error_message}"
        
    vectorized = vectorizer.transform([text])
    prediction = model.predict(vectorized)[0]
    
    # NOTE: Check your model's class mapping (1=Real or 1=Fake) 
    # Current assumption: 1 = Real News
    if prediction == 1 or prediction == "real":
        return "✅ Real News"
    else:
        return "❌ Fake News"

# ---------------- Sidebar ----------------
st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Navigation Options", # FIXED: Added label for accessibility
    ["🏠 Home", "📂 Category", "ℹ About"],
    index=0,
    key="nav_radio",
    label_visibility="hidden" # Hides label since title is sufficient
)

# ---------------- Home Page ----------------
if page == "🏠 Home":
    google_style_title()
    st.subheader("Enter News Article below 👇")

    if not model_loaded:
        st.error(f"⚠ Model not loaded: {error_message}")
    else:
        news_text = st.text_area("Paste news article here:", height=200)
        if st.button("🔎 Predict"):
            if news_text.strip() == "":
                st.warning("Please enter some news article.")
            else:
                result = predict_news(news_text) # Confidence removed
                
                st.markdown("### 📝 Prediction Result")
                color = "#28A745" if "Real" in result else "#DC3545"
                st.markdown(
                    f"<div style='background-color:{color}; color:white; "
                    f"padding:15px; border-radius:12px; font-size:18px; font-weight:bold; "
                    f"text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.3);'>"
                    f"{result}</div>",
                    unsafe_allow_html=True,
                )

# ---------------- Category Page ----------------
elif page == "📂 Category":
    google_style_title()
    st.markdown("<h2 style='text-align: center; color:#4285F4; margin-top:10px;'>Select a Category 👇</h2>", unsafe_allow_html=True)

    categories = {
        "Politics": ["Government announces new election reforms", "Politician caught in corruption scandal", "Opposition claims economy is failing",],
        "Sports": ["Team wins FIFA World Cup", "Player breaks 100m sprint record", "Fake report: Superstar retires at age 25",],
        "Technology": ["Apple launches revolutionary hologram iPhone", "Scientists develop AI that writes novels", "Fake: Facebook shutting down permanently",],
        "Health": ["New vaccine shows 95% success in trials", "Study finds junk food causes health issues", "Fake: Drinking coffee cures cancer",],
        "Entertainment": ["Actor wins Oscar for best performance", "A TV series won multiple awards at an international ceremony.", "Netflix releases most-watched series ever",]
    }

    # Define Google-themed colors for categories
    category_colors = {
        "Politics": "#4285F4",    # Google Blue
        "Sports": "#DB4437",      # Google Red
        "Technology": "#F4B400",  # Google Yellow/Orange
        "Health": "#0F9D58",      # Google Green
        "Entertainment": "#673AB7" # Google Purple
    }

    if "selected_category" not in st.session_state:
        st.session_state.selected_category = None
    if "selected_headline" not in st.session_state:
        st.session_state.selected_headline = None

    # --- Category Buttons (Pills) ---
    cols = st.columns(len(categories))

    for i, cat in enumerate(categories.keys()):
        color = category_colors[cat]
        
        button_key = f"cat_{cat}"

        # Inject custom background color for this specific button using CSS
        # Targets the button container within the columns based on index
        st.markdown(
            f"""
            <style>
            [data-testid="stVerticalBlock"] [data-testid="stHorizontalBlock"] > div:nth-child({i+1}) button {{
                background-color: {color} !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # Use st.button. If clicked, update state (No duplicates)
        if cols[i].button(cat, key=button_key, help=f"Select {cat} category", use_container_width=True):
            st.session_state.selected_category = cat
            st.session_state.selected_headline = None
            st.rerun() 

    # --- Headline Buttons (Cards) ---
    if st.session_state.selected_category:
        cat = st.session_state.selected_category
        color = category_colors[cat]

        st.markdown(
            f"<h3 style='color:{color}; margin-top:25px;'>Sample {cat} Headlines</h3>",
            unsafe_allow_html=True,
        )
        
        # Inject CSS to style the left border of the headline cards
        st.markdown(
            f"""
            <style>
            [data-testid="stVerticalBlock"] > div:nth-child(2) [data-testid^="stButton"] button {{
                border-left: 5px solid {color} !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        for hl in categories[cat]:
            # Use st.button. If clicked, update state (No duplicates)
            if st.button(hl, key=f"hl_{hl}", help="Analyze this headline", use_container_width=True):
                st.session_state.selected_headline = hl
                st.rerun()

    # --- Prediction Result ---
    if st.session_state.selected_headline:
        hl = st.session_state.selected_headline
        result = predict_news(hl) # Confidence removed

        st.markdown("<h3 style='margin-top:25px;'>📝 Analysis Result</h3>", unsafe_allow_html=True)

        # Use Google-style alert colors
        if "Real" in result:
            color = "#0F9D58" # Green (Success)
            bg_color = "#E6F6E6"
        else:
            color = "#DB4437" # Red (Error/Warning)
            bg_color = "#FBE6E6"

        st.markdown(
            f"""
            <div style='background-color:{bg_color}; color:{color}; 
            padding:20px; border-radius:12px; font-size:24px; font-weight:bold; 
            text-align:center; border: 1px solid {color};
            box-shadow:0 2px 4px rgba(0,0,0,0.1); margin-top:15px;'>
            {result}</div>
            """, 
            unsafe_allow_html=True,
        )


# ---------------- About Page ----------------
elif page == "ℹ About":
    google_style_title()
    st.subheader("About 📖")

    st.markdown("""
    <div style='text-align: justify; font-size:18px; line-height:1.8; margin-top:22px; font-family:"Google Sans", Arial, sans-serif;'>
        Welcome to the <b>Fake News Detection System</b> — a <span style="color:blue;">smart</span> and 
        <span style="color:green;">reliable</span> tool powered by <b>Machine Learning</b>.  
        <br><br>
        Just paste any news article and instantly check whether it appears 
        <b style="color:green;">Real</b> ✅ or <b style="color:red;">Fake</b> ❌.  
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display: flex; gap: 20px; margin-top: 30px; font-family:'Google Sans', Arial, sans-serif;">
        <div style="flex:1; background:#f0f8ff; padding:18px; border-radius:20px; text-align:center;">
            <h4 style="color:blue;">🔹 User-Friendly</h4>
            <p>Clean and minimal interface, easy for anyone to use.</p>
        </div>
        <div style="flex:1; background:#f5fff5; padding:18px; border-radius:20px; text-align:center;">
            <h4 style="color:green;">🔹 Versatile</h4>
            <p>Works across Politics, Sports, Technology, Health, and Entertainment.</p>
        </div>
        <div style="flex:1; background:#fff8dc; padding:18px; border-radius:20px; text-align:center;">
            <h4 style="color:orange;">🔹 Fast & Accurate</h4>
            <p>Instant predictions with trained ML models.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='margin: 50px 0; text-align:center;'>
        <hr style='border: none; height: 4px; width:70%; 
        background: linear-gradient(to right, blue, green, orange, red); 
        border-radius: 50px;'>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: justify; font-size:16px; line-height:1.8; font-family:"Google Sans", Arial, sans-serif;'>
        <b>Why use this system?</b><br><br>
        ✅ Protect yourself from <b style="color:red;">fake news</b> and misinformation. <br>
        ✅ Build awareness and promote <b style="color:blue;">responsible news sharing</b>. <br>
        ✅ Enhance trust in <b style="color:green;">online information</b>.  
        <br><br>
        <b style="color:orange;">Note:</b> Predictions depend on the dataset used for training 
        and may not always be 100% accurate.  
        <br><br>
        👨‍💻 <b>Developed by:</b> <span style='color:blue;'>Suzan Ajmeri</span><br>
        📧 <b>Email:</b> <a href="mailto:suzanajmeri986@gmail.com" style="color:green; text-decoration:none;">suzanajmeri986@gmail.com</a>
    </div>
    """, unsafe_allow_html=True)