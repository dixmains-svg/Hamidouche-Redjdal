import streamlit as st

st.set_page_config(
    page_title="HAMIDOUCHE REDJDAL | CV",
    page_icon="🚚",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f7fb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #102a43, #1f5f8b);
        color: white;
        padding: 45px 50px;
        border-radius: 22px;
        margin-bottom: 30px;
        text-align: left;
    ">

        <div style="
            font-size: 44px;
            font-weight: 800;
            margin-bottom: 10px;
        ">
            HAMIDOUCHE REDJDAL
        </div>

        <div style="
            font-size: 23px;
            font-weight: 600;
            margin-bottom: 20px;
        ">
            🚚 Planificateur &amp; Superviseur Logistique
        </div>

        <div style="
            font-size: 16px;
            line-height: 1.8;
        ">
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

st.success("✅ Le fichier app.py fonctionne correctement.")
