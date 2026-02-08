# ============================================
# Streamlit App: PDF → WordCloud (FAST & FIXED)
# NO MODEL TRAINING
# ============================================

import streamlit as st
import numpy as np
import re
import matplotlib.pyplot as plt

from PyPDF2 import PdfReader
from wordcloud import WordCloud
from PIL import Image


# ---------- UI ----------
st.set_page_config(page_title="PDF → WordCloud", layout="centered")

st.title("📄 PDF → WordCloud Generator")
st.write("Upload a PDF and a mask image (India map / any shape)")

pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])
mask_file = st.file_uploader("Upload Mask Image (PNG/JPG)", type=["png", "jpg", "jpeg"])

generate = st.button("Generate WordCloud")


# ---------- MAIN ----------
if generate and pdf_file and mask_file:

    # ----- 1. Read PDF -----
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    if len(text) < 50:
        st.error("❌ PDF text extraction failed")
        st.stop()

    # ----- 2. Clean text -----
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    st.success("✅ PDF text extracted")

    # ----- 3. Load & FIX mask -----
    mask = Image.open(mask_file).convert("L")
    mask = np.array(mask)

    # Binary mask
    mask = np.where(mask > 200, 255, 0)

    # IMPORTANT: invert mask so shape is black
    mask = 255 - mask

    st.subheader("Mask Preview (Corrected)")
    st.image(mask, clamp=True)
    st.write("Mask values:", np.unique(mask))

    # ----- 4. Generate WordCloud -----
    wc = WordCloud(
        background_color="white",
        mask=mask,
        max_words=300,
        contour_width=2,
        contour_color="black"
    )

    wc.generate(text)

    # ----- 5. Display -----
    st.subheader("✅ Generated WordCloud")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

else:
    st.info("📌 Upload PDF + Mask image, then click Generate")
