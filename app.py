import streamlit as st

st.set_page_config(
    page_title="HAMIDOUCHE REDJDAL | CV",
    page_icon="🚚",
    layout="wide"
)

# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
<style>
.stApp {
    background-color: #f4f7fb;
}

.cv-header {
    background: linear-gradient(135deg, #102a43, #1f5f8b);
    color: white;
    padding: 45px 50px;
    border-radius: 22px;
    margin-bottom: 30px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

.cv-name {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 12px;
}

.cv-title {
    font-size: 23px;
    font-weight: 600;
    margin-bottom: 20px;
}

.cv-subtitle {
    font-size: 16px;
    line-height: 1.8;
}
</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
<div class="cv-header">
<div class="cv-name">HAMIDOUCHE REDJDAL</div>
<div class="cv-title">🚚 Planificateur &amp; Superviseur Logistique</div>
<div class="cv-subtitle">
Master 2 en Recherche Opérationnelle
<br><br>
Logistique &nbsp; • &nbsp;
Transport &nbsp; • &nbsp;
Planification &nbsp; • &nbsp;
Supervision &nbsp; • &nbsp;
Optimisation
</div>
</div>
""",
    unsafe_allow_html=True
)

# ============================================================
# TEST
# ============================================================

st.success("✅ Le fichier app.py fonctionne correctement.")

st.write("Bienvenue sur le CV professionnel de HAMIDOUCHE REDJDAL.")
