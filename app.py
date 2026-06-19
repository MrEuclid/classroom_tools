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
    
    # Safety limit: Restrict to 7 characters (max 5,040 permutations)
    user_input = st.text_input("Enter letters:", "ABCD", max_chars=7) 
    
    if st.button("Generate"):
        result = perms.get_permutations(user_input) 
        
        # Display the math!
        st.success(f"Success! Found {len(result)} possible permutations.")
        
        # Only render the first 100 items to the screen to keep it fast
        st.write("Here is a preview of the first 100:")
        
        # Display in a clean, scrollable box rather than dumping onto the page
        with st.container(height=300):
            st.write(result[:100])
    
    if show_code:
        st.subheader("Code for this utility:")
        # You can read the file directly
        with open("utilities/perms.py", "r") as f:
            st.code(f.read(), language='python')

elif page == "Calculator":
    st.title("Calculator")
    # ... logic here
