import streamlit as st
import joblib
from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="SalesIQ | Sales Prediction",
   
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. PROJECT PATHS AND MODEL
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "outputs" / "sales_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file not found. Check outputs/sales_model.pkl")
    st.stop()

# ==========================================
# 3. CUSTOM DARK ROSE GOLD THEME
# ==========================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #160D13 0%, #24121D 55%, #301722 100%);
    color: #F8EDF0;
}

/* Hide default header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1C1018;
    border-right: 1px solid #51303E;
}

/* General text */
.stApp, .stApp p, .stApp label {
    color: #EADDE2;
}

/* Headings */
h1, h2, h3 {
    color: #F4D6C5 !important;
}

/* Main title */
.hero-title {
    font-size: 44px;
    font-weight: 800;
    color: #F4D6C5;
    letter-spacing: -1px;
    margin-bottom: 4px;
}

.hero-subtitle {
    color: #C5A5B2;
    font-size: 16px;
    margin-bottom: 25px;
}

/* Section headings */
.section-heading {
    color: #E7B9A0;
    font-size: 21px;
    font-weight: 700;
    margin-top: 12px;
    margin-bottom: 12px;
}

/* Cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #321C29, #25151F);
    border: 1px solid #77505D;
    border-radius: 16px;
    padding: 22px;
}

/* Metric labels and values */
[data-testid="stMetricLabel"] {
    color: #CDAEBA !important;
}

[data-testid="stMetricValue"] {
    color: #F4D6C5 !important;
}

/* Inputs */
div[data-baseweb="input"] {
    background-color: #2A1923;
    border: 1px solid #77505D;
    border-radius: 10px;
}

div[data-baseweb="input"] input {
    color: #FFF4F0 !important;
}

/* Form container */
[data-testid="stForm"] {
    background-color: #241620;
    border: 1px solid #654351;
    padding: 25px;
    border-radius: 18px;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #A65D72, #C18A70);
    color: white !important;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 45px;
    transition: 0.3s;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: linear-gradient(90deg, #C18A70, #D9AD91);
    border: none;
    transform: translateY(-2px);
}

/* Alerts */
[data-testid="stAlert"] {
    background-color: #34202B;
    border-radius: 12px;
}

/* Divider */
hr {
    border-color: #563542;
}

/* Footer */
.footer {
    color: #A98A98;
    text-align: center;
    padding: 25px;
    font-size: 13px;
}

/* Sidebar text */
[data-testid="stSidebar"] p {
    color: #D9C3CC;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("#  SalesIQ")

    st.markdown("### SALES ANALYTICS")
    st.caption("Machine Learning Dashboard")

    st.markdown("---")

    st.markdown("#### PROJECT OVERVIEW")

    st.write(
        "SalesIQ predicts product sales using "
        "advertising expenditure and a trained "
        "Machine Learning model."
    )

    st.markdown("---")

    st.markdown("#### TECHNOLOGY STACK")

    st.write(" Python")
    st.write(" Pandas")
    st.write(" Scikit-learn")
    st.write(" Streamlit")

    st.markdown("---")

    st.markdown("#### MODEL INFORMATION")
    st.caption("Algorithm: Linear Regression")
    st.caption("Dataset: Advertising.csv")

    st.markdown("---")
    st.caption("Version 1.0 | 2026")

# ==========================================
# 5. MAIN DASHBOARD HEADER
# ==========================================

st.markdown(
    '<div class="hero-title">Sales Prediction Studio</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Intelligent sales forecasting powered by Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================
# 6. INTRODUCTION
# ==========================================

st.markdown(
    '<div class="section-heading"> Advertising Analytics</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter your advertising expenditure across "
    "different channels to estimate your expected sales."
)

# ==========================================
# 7. INPUT FORM
# ==========================================

st.markdown(
    '<div class="section-heading"> Enter Your Budget</div>',
    unsafe_allow_html=True
)

with st.form("prediction_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        tv = st.number_input(
            " TV Advertising",
            min_value=0.0,
            value=150.0,
            step=1.0
        )

    with col2:
        radio = st.number_input(
            " Radio Advertising",
            min_value=0.0,
            value=25.0,
            step=1.0
        )

    with col3:
        newspaper = st.number_input(
            " Newspaper Advertising",
            min_value=0.0,
            value=20.0,
            step=1.0
        )

    submitted = st.form_submit_button(
        " GENERATE SALES PREDICTION",
        use_container_width=True
    )
# ==========================================
# 8. PREDICTION RESULT
# ==========================================

if submitted:

    input_data = [[tv, radio, newspaper]]

    prediction = model.predict(input_data)[0]

    total_budget = tv + radio + newspaper

    st.markdown("---")

    st.markdown(
        '<div class="section-heading"> Prediction Results</div>',
        unsafe_allow_html=True
    )

    result1, result2 = st.columns(2)

    with result1:
        st.metric(
            label="PREDICTED SALES",
            value=f"{prediction:.2f}"
        )

    with result2:
        st.metric(
            label="TOTAL ADVERTISING BUDGET",
            value=f"{total_budget:.2f}"
        )

    st.success(
        f"Prediction generated successfully! "
        f"Estimated sales: {prediction:.2f}"
    )

    st.balloons()

# ==========================================
# 9. FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    'SALESIQ • Built with Python & Machine Learning'
    '<br>Turning advertising data into business insights.'
    '</div>',
    unsafe_allow_html=True
)