import streamlit as st
import utilities.TSP.perms as perms 
import utilities.RSA.rsa_tools as rsa

st.set_page_config(page_title="Classroom Toolkit", layout="wide")

# --- Sidebar Main Menu ---
st.sidebar.title("🛠️ Toolkit")

# First Dropdown: The Folder / Category
category = st.sidebar.selectbox(
    "Choose a Category:", 
    ["Home", "TSP Tools", "Maths Functions"]
)

# --- Routing Logic ---
if category == "Home":
    st.title("Welcome to the Python Toolkit")
    st.write("Use the sidebar to select a category, then choose a specific tool to begin.")

elif category == "TSP Tools":
    # Updated the tool name to be more relevant
    tool = st.sidebar.selectbox("Select a TSP Tool:", ["Flight Router"]) 
    
    if tool == "Flight Router":
        st.header("Flight Routing Permutations")
        
        # Increased max_chars to 40 (allows for about 7-8 airport codes safely)
        # Updated the placeholder text to guide the students
        user_input = st.text_input("Enter IATA codes (comma separated):", "PNH, BKK, SIN", max_chars=40) 
        
        if st.button("Generate Routes"):
            result = perms.get_permutations(user_input) 
            st.success(f"Success! Found {len(result)} possible routes.")
            with st.container(height=300):
                st.write(result[:100])
elif category == "Maths Functions":
    # Second Dropdown: Appears only when Maths is selected
    tool = st.sidebar.selectbox("Select a Maths Tool:", ["RSA Modular Exponentiation"])
    
    if tool == "RSA Modular Exponentiation":
        st.header("RSA Cryptography Toolkit")
        st.write("Calculates: $a^b \\pmod n$")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            base = st.number_input("Base (a)", min_value=1, value=7, step=1)
        with col2:
            exp = st.number_input("Exponent (b)", min_value=1, value=13, step=1)
        with col3:
            mod = st.number_input("Modulus (n)", min_value=2, value=15, step=1)
            
        if st.button("Calculate", type="primary"):
            result = rsa.modular_exponentiation(base, exp, mod)
            
            if result is None:
                 st.error("Please enter valid numbers.")
            elif isinstance(result, str): 
                 st.error(result)
            else:
                 st.success(f"**Result:** {result}")