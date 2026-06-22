import streamlit as st
import utilities.TSP.perms as perms 
import utilities.RSA.rsa_tools as rsa
import utilities.RSA.text_tools as text_tools
import utilities.RSA.prime_tools as prime_tools
import utilities.RSA.decoding as decoding

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
            st.success(f"Solved! Found {len(result)} possible routes.")
            with st.container(height=300):
                st.write(result[:100])

elif category == "Maths Functions":
    tool = st.sidebar.selectbox("Select a Maths Tool:", [
        "Text-to-Number Encoder", 
        "Number-to-Text Decoder", # <-- ADD THIS LINE
        "Prime Number Finder",
        "Private Key Generator",
        "RSA Modular Exponentiation"
    ])

    if tool == "Text-to-Number Encoder":
        st.header("Text Encoder")
        word = st.text_input("Enter a single word:")
        encoding = st.radio("Select Encoding:", ["ascii (English)", "utf-8 (Khmer)"])
        
        if st.button("Encode"):
            # Strip the label to just pass 'ascii' or 'utf-8' to your function
            enc = encoding.split(" ")[0] 
            result = text_tools.text_to_number(word, encoding=enc)
            
            st.success(f"**Integer Value ($m$):** {result}")
            st.info(f"Remember: Your RSA Modulus ($n$) MUST be larger than {result}!")
    elif tool == "Number-to-Text Decoder":
        st.header("Number-to-Text Decoder")
        st.write("Convert a decrypted integer back into a readable message.")
        
        # Accept as text to prevent UI precision limits on massive numbers
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
        
        # Add the interactive UI constraints
        requested_digits = st.number_input("Enter the number of digits (2-20):", min_value=2, max_value=20, value=3)
        
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
                 st.error(result) # Catches the common factor error
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