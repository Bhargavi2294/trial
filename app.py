import streamlit as st
from utils.quality_utils import check_image_quality
from utils.cert_utils import required_certifications

st.set_page_config(page_title="PCB Check & Certification", layout="centered")
st.title(" PCB Quality & Certification Assistant")

option = st.selectbox(
    "Choose what you'd like to do:",
    ["Select", "1. Quality + Certification", "2. Quality Check Only", "3. Certification Required Only"]
)

uploaded = st.file_uploader("Upload PCB Image (PNG/JPG)", type=["png", "jpg", "jpeg"])
pcb_name = st.text_input("Enter PCB Name")

if option != "Select":
    if not pcb_name:
        st.warning("Please enter the PCB Name.")
        st.stop()
    if (option != "3. Certification Required Only") and not uploaded:
        st.warning("Please upload a PCB image for quality checks.")
        st.stop()

    # Do quality check if needed
    quality_results = None
    if option in ["1. Quality + Certification", "2. Quality Check Only"]:
        img, quality_results = check_image_quality(uploaded)
        st.image(img, caption="PCB Image Preview", use_column_width=True)
        st.markdown("### 🛠 Quality Check Results:")
        st.write(f"- **Format:** {quality_results['format']}")
        st.write(f"- **Resolution:** {quality_results['width']}×{quality_results['height']}")
        st.write(f"- **Aspect Ratio:** {quality_results['aspect_ratio']}")
        st.write(f"- **File Size:** {quality_results['size_kb']} KB")
        if quality_results['warnings']:
            st.warning("⚠️ Warnings:\n" + "\n".join(["• " + w for w in quality_results['warnings']]))
        else:
            st.success("✅ Basic quality checks passed.")

    # Do certification if needed
    if option in ["1. Quality + Certification", "3. Certification Required Only"]:
        certs = required_certifications(pcb_name)
        st.markdown("### 📋 Required Certifications:")
        for c in certs:
            st.write(f"- {c}")

    # Summary
    st.markdown("---")
    st.markdown("### 🔍 Summary")
    if quality_results:
        st.write(f"Quality: {'PASS' if not quality_results['warnings'] else 'ISSUES'}")
    st.write(f"Certifications Needed: {', '.join(certs)}")
