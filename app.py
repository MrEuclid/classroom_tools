import streamlit as st
import utilities.TSP.perms as perms 
import utilities.RSA.rsa_tools as rsa
import utilities.RSA.text_tools as text_tools
import utilities.RSA.prime_tools as prime_tools
import utilities.RSA.decoding as decoding

st.set_page_config(page_title="Classroom Toolkit", layout="wide")

# --- CSS FIX FOR CHROMEBOOKS ---
# --- UPGRADED CSS FIX FOR CHROMEBOOKS ---
st.markdown(
    """
    <style>
    /* 1. Force the master HTML/Body to take full physical screen height */
    html, body {
        height: 100% !important;
        margin: 0 !important;
    }
    
    /* 2. Force the sidebar shell to stretch perfectly to the bottom */
    [data-testid="stSidebar"] {
        height: 100vh !important;
        min-height: 100vh !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* 3. Ensure the internal content area expands and scrolls properly */
    [data-testid="stSidebarUserContent"] {
        flex-grow: 1 !important;
        height: 100% !important;
        overflow-y: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

    # --- COLAB EXPORT PANEL (SIDEBAR) ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("📋 Colab Export Panel")
    
    # Your specific GitHub Colab Notebook Link
    st.sidebar.markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MrEuclid/classroom_tools/blob/main/Copy_of_rsaCalculation.ipynb)")
    
    st.sidebar.write("Paste your generated values here to auto-build your Colab script.")
    
    # Interactive inputs acting as the new scratchpad
    colab_p = st.sidebar.text_input("p (Prime 1):", "")
    colab_q = st.sidebar.text_input("q (Prime 2):", "")
    colab_e = st.sidebar.text_input("e (Public Key):", "65537")
    colab_c = st.sidebar.text_input("Ciphertext (c):", "")
    
    # Auto-calculate n for the Colab payload if p and q are valid numbers
    n_val = "None"
    if colab_p.isdigit() and colab_q.isdigit():
        n_val = str(int(colab_p) * int(colab_q))
        
    # Construct the live-updating Python script safely without triple quotes
    colab_payload = (
        "# Pasted from Streamlit RSA Tools\n"
        f"p = {colab_p if colab_p else 'None'}\n"
        f"q = {colab_q if colab_q else 'None'}\n"
        f"n = {n_val}\n"
        f"e = {colab_e if colab_e else 'None'}\n"
        f"ciphertext = {colab_c if colab_c else 'None'}\n\n"
        "print('✅ Variables successfully loaded into Colab! Solved!')\n"
        "if n is not None:\n"
        "    print(f'Modulus n bits: {n.bit_length()}')\n"
    )

    # Render the code block
    st.sidebar.code(colab_payload, language="python")
    st.sidebar.markdown("---")

    # --- MAIN MATHS TOOLS ---
    if tool == "Text-to-Number Encoder":
        st.header("Text Encoder")
        word = st.text_input("Enter a single word:")
        encoding = st.radio("Select Encoding:", ["ascii (English)", "utf-8 (Khmer)"])
        
        if st.button("Encode"):
            enc = encoding.split(" ")[0] 
            result = text_tools.text_to_number(word, encoding=enc)
            
            st.success(f"**Integer Value ($m$):** {result}")
            st.info(f"Remember: Your RSA Modulus ($n$) MUST be larger than {result}!")
            
    elif tool == "Number-to-Text Decoder":
        st.header("Number-to-Text Decoder")
        st.write("Convert a decrypted integer back into a readable message.")
        
        decrypted_input = st.text_input("Enter the decrypted number ($m$):")
        
        if st.button("Decode Message", type="primary"):
            if decrypted_input.strip().isdigit():
                big_int = int(decrypted_input.strip())
                result = decoding.decode_rsa_number(big_int)
                
                if "[Error" in result:
                    st.error(result)
                else:
                    st.success(f"**Decoded Message:** {result} \n\n Well done! Solved!")
            else:
                st.warning("Please enter a valid, positive whole number.")

    elif tool == "Prime Number Finder":
        st.header("Prime Generator")
        st.write("Find a prime number ($p$ or $q$) of a specific length to build your RSA keys.")
        
        requested_digits = st.number_input("Enter the number of digits (2-20):", min_value=2, max_value=20, value=3, step=1)        
        if st.button("Generate Random Prime", type="primary"):
            result = prime_tools.generate_random_prime(requested_digits)
            st.success(f"**Found {requested_digits}-digit Prime:**\n\n{result}\n\nWell done!")
            
    elif tool == "Private Key Generator":
        st.header("Private Key ($d$) Calculator")
        st.write("Solves the equation: $(d \\times e) \\pmod{\\phi(n)} = 1$")
        
        col1, col2 = st.columns(2)
        with col1:
            e_val = st.number_input("Public Key (e)", min_value=3, value=65537, step=2)
        with col2:
            phi_val = st.number_input("Euler's Totient (phi(n))", min_value=2, value=100, step=1)
            
        if st.button("Generate Private Key", type="primary"):
            result = rsa.calculate_private_key(e_val, phi_val)
            
            if result is None:
                 st.error("Please enter valid numbers.")
            elif isinstance(result, str): 
                 st.error(result) 
            else:
                 st.success(f"**Your Private Key ($d$) is:**\n\n{result}")

    elif tool == "RSA Modular Exponentiation":
        st.header("RSA Cryptography Toolkit")
        st.write("Calculates: $a^b \\pmod n$")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            base = st.number_input("Base (a)", min_value=1, value=7, step=1)
        with col2:
            exp = st.number_input("Exponent (b)", min_value=-1, value=13, step=1)
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

    elif tool == "RSA Modulus Cracker":
        st.header("RSA Modulus Cracker")
        st.write("Factor a semi-prime modulus ($n$) back into its original primes ($p$ and $q$).")
        st.write("This demonstrates why modern RSA requires keys that are 600+ digits long!")
        
        n_input = st.text_input("Enter the Modulus (n):", "60987623363990694377")
        
        if st.button("Crack Modulus", type="primary"):
            if n_input.strip().isdigit():
                n_val = int(n_input.strip())
                
                with st.spinner(f"Attempting to factor {n_val}..."):
                    p, q = prime_tools.crack_rsa_modulus(n_val)
                
                if p and q:
                    st.success(f"**Cracked in milliseconds!**\n\n**Factor 1 (p):** {p}\n\n**Factor 2 (q):** {q}\n\nWell done! Solved!")
                else:
                    st.error("Failed to factor. The number might be prime, or it's too large for a quick script.")
            else:
                st.warning("Please enter a valid number.")