import streamlit as st
import utilities.TSP.perms as perms 
import utilities.RSA.rsa_tools as rsa
import utilities.RSA.text_tools as text_tools
import utilities.RSA.prime_tools as prime_tools
import utilities.RSA.decoding as decoding

st.set_page_config(page_title="Classroom Toolkit", layout="wide")

# --- Sidebar Main Menu ---
st.sidebar.title("🛠️ Toolkit")

category = st.sidebar.selectbox(
    "Choose a Category:", 
    ["Home", "TSP Tools", "Maths Functions"]
)

# --- Routing Logic ---
if category == "Home":
    st.title("Welcome to the Python Toolkit")
    st.write("Use the sidebar to select a category, then choose a specific tool to begin.")

elif category == "TSP Tools":
    tool = st.sidebar.selectbox("Select a TSP Tool:", ["Flight Router"]) 
    
    if tool == "Flight Router":
        st.header("Flight Routing Permutations")
        user_input = st.text_input("Enter IATA codes (comma separated):", "PNH, BKK, SIN", max_chars=40) 
        
        if st.button("Generate Routes"):
            result = perms.get_permutations(user_input) 
            st.success(f"Solved! Found {len(result)} possible routes.")
            with st.container(height=300):
                st.write(result[:100])

elif category == "Maths Functions":
    tool = st.sidebar.selectbox("Select a Maths Tool:", [
        "Text-to-Number Encoder", 
        "Number-to-Text Decoder",
        "Prime Number Finder",
        "Private Key Generator",
        "RSA Modular Exponentiation",
        "RSA Modulus Cracker"
    ])

    # Create a 2-column layout: Left (Tool), Right (Colab Export Panel)
    left_col, right_col = st.columns([1.5, 1])

    with right_col:
        st.markdown("### 📋 Colab Export Panel")
        st.markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MrEuclid/classroom_tools/)")
        
        st.markdown(
            """
            **How to use this:**
            1. Enter your variables below.
            2. Hover over the dark code block and click the **Copy icon** (top right corner).
            3. **Only after copying**, click the **Open in Colab** badge above.
            4. Paste the code into your first Colab cell!
            """
        )
        
        col1, col2 = st.columns(2)
        with col1:
            colab_p = st.text_input("p (Prime 1):", "")
            colab_e = st.text_input("e (Public Key):", "65537")
        with col2:
            colab_q = st.text_input("q (Prime 2):", "")
            colab_c = st.text_input("Plaintext (m):", "")
        
        n_val = str(int(colab_p) * int(colab_q)) if (colab_p.isdigit() and colab_q.isdigit()) else "None"
            
        colab_payload = (
            f"p = {colab_p if colab_p else 'None'}\n"
            f"q = {colab_q if colab_q else 'None'}\n"
            f"n = {n_val}\n"
            f"e = {colab_e if colab_e else 'None'}\n"
            f"m = {colab_c if colab_c else 'None'}\n"
        )
        st.code(colab_payload, language="python")

    with left_col:
        if tool == "Text-to-Number Encoder":
            st.header("Text Encoder")
            word = st.text_input("Enter a single word:")
            encoding = st.radio("Select Encoding:", ["ascii", "utf-8"])
            if st.button("Encode"):
                result = text_tools.text_to_number(word, encoding=encoding.split(" ")[0])
                st.success(f"**Value:** {result}")
                
        elif tool == "Number-to-Text Decoder":
            st.header("Number-to-Text Decoder")
            decrypted_input = st.text_input("Enter decrypted number ($m$):")
            if st.button("Decode", type="primary"):
                result = decoding.decode_rsa_number(int(decrypted_input.strip())) if decrypted_input.strip().isdigit() else "Invalid"
                st.success(f"**Result:** {result}")

        elif tool == "Prime Number Finder":
            st.header("Prime Generator")
            digits = st.number_input("Digits:", min_value=2, max_value=20, value=3)        
            if st.button("Generate", type="primary"):
                st.success(f"**Prime:** {prime_tools.generate_random_prime(digits)}")
            
        elif tool == "Private Key Generator":
            st.header("Private Key ($d$) Calculator")
            
            # Keep 'e' as a number input since it is usually just 65537
            e_val = st.number_input("e", value=65537)
            
            # Change phi(n) to a text input to bypass JavaScript's 15-digit limit
            phi_input = st.text_input("phi(n)", value="100")
            
            if st.button("Calculate", type="primary"):
                if phi_input.strip().isdigit():
                    phi_val = int(phi_input.strip())
                    result = rsa.calculate_private_key(e_val, phi_val)
                    st.success(f"**Private Key (d):** {result}\n\nSolved!")
                else:
                    st.error("Please enter a valid positive number for phi(n).")
        elif tool == "RSA Modular Exponentiation":
            st.header("Modular Exponentiation")
            b = st.number_input("Base", value=7)
            e = st.number_input("Exponent", value=13)
            n = st.number_input("Modulus", value=15)
            if st.button("Calculate", type="primary"):
                st.success(f"**Result:** {rsa.modular_exponentiation(b, e, n)}")

        elif tool == "RSA Modulus Cracker":
            st.header("RSA Modulus Cracker")
            n_input = st.text_input("Modulus (n):", "60987623363990694377")
            if st.button("Crack", type="primary"):
                p, q = prime_tools.crack_rsa_modulus(int(n_input.strip()))
                st.success(f"**p:** {p} | **q:** {q}")