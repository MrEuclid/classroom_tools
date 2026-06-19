import streamlit as st
import utilities.perms as perms 
import utilities.rsa_tools as rsa  # Import your new module

st.set_page_config(page_title="Classroom Toolkit", layout="wide")

# --- Sidebar ---
st.sidebar.title("🛠️ Toolkit")
page = st.sidebar.selectbox("Choose a tool:", ["Home", "Permutations", "Calculator"])
show_code = st.sidebar.checkbox("Show Source Code", value=False)

# --- Main App ---
if page == "Home":
    st.title("Welcome to the Python Toolkit")
    st.write("Use the sidebar to explore different utilities.")

elif page == "Permutations":
    # ... (Your existing permutations code stays exactly the same) ...
    pass

elif page == "Modular Exponentiation":
    st.title("RSA Cryptography Toolkit")
    
    st.subheader("Modular Exponentiation")
    st.write("Calculates: $a^b \\pmod n$")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        base = st.number_input("Base (a)", min_value=1, value=7, step=1)
    with col2:
        exp = st.number_input("Exponent (b)", min_value=1, value=13, step=1)
    with col3:
        mod = st.number_input("Modulus (n)", min_value=2, value=15, step=1)
        
    if st.button("Calculate", type="primary"):
        # Call the logic from your utilities folder!
        result = rsa.modular_exponentiation(base, exp, mod)
        
        # Handle the UI based on what the utility file returns
        if result is None:
             st.error("Please enter valid numbers.")
        elif isinstance(result, str): # Catch the ZeroDivisionError message
             st.error(result)
        else:
             st.success(f"**Result:** {result}")