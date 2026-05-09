import streamlit as st


st.set_page_config(page_title="E-Bike Kit Marketing App", page_icon="🚲", layout="centered")

st.title("🚲 E-Bike Kit from E-Waste")
st.subheader("A concept showcase built with Streamlit")

st.write(
    "Explore a simple concept of how an e-bike kit made from recovered e-waste "
    "components could be presented to customers."
)

with st.container():
    st.markdown("### Why this kit?")
    st.markdown(
        """
        - ♻️ Reuses recoverable materials from e-waste
        - ⚡ Supports low-emission mobility
        - 🧩 Designed for retrofit compatibility
        """
    )

with st.container():
    st.markdown("### Example package")
    st.markdown(
        """
        - Motor unit
        - Battery pack
        - Controller
        - Installation accessories
        """
    )

st.success("This app is ready to be extended with pricing, visuals, and lead capture.")
