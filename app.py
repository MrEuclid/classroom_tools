import streamlit as st
import utilities.perms as perms # Import your module

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
    st.header("Permutation Generator")
    user_input = st.text_input("Enter letters:", "ABCD")
    
    if st.button("Generate"):
        result = perms.get_permutations(user_input) # Calling function from your file
        st.write(result)
    
    if show_code:
        st.subheader("Code for this utility:")
        # You can read the file directly
        with open("utilities/combsTSP.py", "r") as f:
            st.code(f.read(), language='python')

elif page == "Calculator":
    st.title("Calculator")
    # ... logic here
