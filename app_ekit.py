import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="RE-VOLT E-Bike Kit", page_icon="🚲")

# --- CUSTOM CSS FOR GREEN THEME ---
st.markdown("""
    <style>
    /* Full page background - Soft Mint Green Gradient */
    .stApp {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    }

    /* Styling the Sidebar - Forest Green */
    [data-testid="stSidebar"] {
        background-color: #2e7d32 !important;
    }

    /* Making sidebar text white for contrast */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Custom styling for headers */
    h1, h2, h3 {
        color: #1b5e20 !important;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Green buttons */
    .stButton>button {
        background-color: #4caf50;
        color: white;
        border-radius: 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #388e3c;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Title and New Motto ---
st.title("🚲 RE-VOLT: The Circular E-Bike Kit")
st.markdown("### :green[Move Smarter. Waste Less.]")

# --- Sidebar Navigation ---
page = st.sidebar.selectbox("Go to:",
                            ["Security & Control", "AI Smart Matching", "DIY Guides", "Kids' Explorer Edition"])

# --- 1. Security & Control (Bluetooth Simulation) ---
if page == "Security & Control":
    st.header("🔒 Security & Phone Link")
    st.info("Syncing with your bike's second-life battery system via Bluetooth.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔗 Connect to Bike"):
            with st.spinner("Searching for RE-VOLT Hub..."):
                time.sleep(2)
                st.success("Connected to Bike #RV-2026")

    with col2:
        lock_status = st.toggle("Remote Digital Lock", value=True)
        st.write(f"Bike Status: {'🔒 LOCKED' if lock_status else '🔓 UNLOCKED'}")

    st.divider()
    st.subheader("🚨 Anti-Theft Alerts")
    if st.checkbox("Enable 'Movement Alert' (Push Notification)"):
        st.warning("Alerts enabled. You will be notified if your bike moves while locked.")

# --- 2. AI Powered Smart Matching ---
elif page == "AI Smart Matching":
    st.header("🧠 AI Compatibility Check")
    st.write("Upload a photo of your bike front fork or wheel to check for a perfect fit.")

    kit_type = st.radio("Select Kit Category:", ["Adult Kit", "Kids' Kit"])
    uploaded_file = st.file_uploader("Take/Upload a picture of your bike", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        with st.spinner("AI analyzing frame geometry..."):
            time.sleep(3)
            st.success("Analysis Complete!")
            st.metric(label="Compatibility Score", value="98%")
            st.write("✅ **Fit Confirmed:** This fork matches our standard hub motor.")
    else:
        st.write("Waiting for photo upload...")

# --- 3. DIY Guides (No Video Uploads) ---
elif page == "DIY Guides":
    st.header("🛠️ Step-by-Step DIY Installation")
    st.write("Follow these simple steps to install your kit in under 20 minutes.")

    tabs = st.tabs(["1. Front Wheel", "2. Wireless Sensor", "3. Battery Mount"])

    with tabs[0]:
        st.subheader("Step 1: Swapping the Wheel")
        st.write("1. Flip your bike upside down or put it on a stand.")
        st.write("2. Open the quick-release lever on your front wheel and remove it.")
        st.write("3. Slide the RE-VOLT Hub Motor wheel into the fork.")
        st.write("4. Tighten the motor bolts and ensure the cable points toward the fork leg.")

    with tabs[1]:
        st.subheader("Step 2: Setting up Bluetooth Pedaling")
        st.write("1. Take the wireless coin-sensor from your kit.")
        st.write("2. Snap it onto the inside of your left pedal arm (crank).")
        st.write("3. Rotate the pedals once to wake up the Bluetooth signal.")

    with tabs[2]:
        st.subheader("Step 3: Mounting the Second-Life Bottle")
        st.write("1. Place the RE-VOLT Bottle Battery into your standard water bottle cage.")
        st.write("2. Use the safety strap to click it into place.")
        st.write("3. Connect the single cable from the bottle to the front wheel motor.")

# --- 4. Kids' Section (Updated Sign & Features) ---
elif page == "Kids' Explorer Edition":
    st.header("🚀 RE-VOLT Explorer Edition")
    st.write("Small bikes, big impact. The smartest way for kids to keep up with the family.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🛡️ Guardian Mode")
        st.write("Parents can set a hard speed limit (e.g., 12 km/h) through the app.")

        st.markdown("### 🎨 Digital Style-Kit")
        st.write("Change the LED light colors on the battery pack via the app!")

    with col2:
        st.markdown("### 🎵 Sound-Box")
        st.write("Choose between 'Electric Racer' or 'Friendly Robot' sounds while pedaling.")

        st.markdown("### 🗺️ Geo-Fencing")
        st.write("Get a buzz on your phone if the bike leaves your pre-set safe zone.")