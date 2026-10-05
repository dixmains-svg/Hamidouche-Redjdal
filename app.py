import streamlit as st
from pathlib import Path

# Bibliothèques pour la génération du PDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ============================================================
# 1. CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="HAMIDOUCHE REDJDAL | CV",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

PHOTO = Path("photo.jpg")
PDF_PATH = Path("cv_hamidouche_redjdal.pdf")

nom = "HAMIDOUCHE REDJDAL"
telephone = "00213775 73 79 30"
email = "hamidoucheredjdal@yahoo.fr"
adresse = "Tazmalt 06039, wilaya de Bejaia"

# ============================================================
# 2. SÉLECTION DE LA LANGUE DANS LA SIDEBAR (FOND BLANC / TEXTE NOIR)
# ============================================================
st.markdown(
    """
    <style>
    /* 1. Titre du champ (label au-dessus) */
    div[data-testid="stSidebar"] label p {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 15px !important;
    }

    /* 2. Boîte du champ sélectionné (Fond Blanc + Bordure Grise) */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 2px solid #cccccc !important;
        border-radius: 8px !important;
    }

    /* 3. Écriture noire dans la boîte sélectionnée */
    div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        color: #000000 !important;
        font-weight: bold !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 4. Flèche du menu déroulant (Noire) */
    div[data-baseweb="select"] svg {
        fill: #000000 !important;
    }

    /* 5. Menu déroulant ouvert (Fond Blanc) */
    ul[data-baseweb="menu"] {
        background-color: #ffffff !important;
        border: 2px solid #cccccc !important;
    }

    /* 6. Écriture noire dans la liste des options */
    ul[data-baseweb="menu"] li div,
    ul[data-baseweb="menu"] li span,
    ul[data-baseweb="menu"] li {
        color: #000000 !important;
        background-color: #ffffff !important;
        font-weight: bold !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 7. Passage de la souris (Survol / Hover) */
    ul[data-baseweb="menu"] li:hover,
    ul[data-baseweb="menu"] li:hover * {
        background-color: #e0e0e0 !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Selection de la langue (Français, English, Español)
langue_choisie = st.sidebar.selectbox("🌐 Langue / Language / Idioma", ["Français", "English", "Español"])

# ============================================================
# 3. BASE DE DONNÉES MULTILINGUE
# ============================================================

TEXTES = {
    "Français": {
        "fonction": "Planificateur et Superviseur Logistique",
        "nationalite": "Algérienne",
        "situation": "Marié",
        "service_national": "Dégagé",
        "nav_title": "NAVIGATION",
        "download_btn": "📄 Télécharger le CV (PDF)",
        "nav": [
            "🏠 Accueil", "👤 Profil", "💼 Expériences", "🎓 Diplômes & Formations",
            "🛠️ Compétences", "🌐 Langues", "⭐ Centres d'intérêt", "📞 Contact"
        ],
        "sidebar_domains": """
**DOMAINES PROFESSIONNELS**

🚚 Transport  
📦 Logistique  
📊 Planification  
👥 Supervision  
📈 Optimisation  
""",
        "profil": (
            "Dynamique, sérieux et ayant de bonnes compétences relationnelles, "
            "avec 9 ans d'expérience dans le domaine de la logistique. "
            "Très à l'aise avec les outils informatiques, je souhaite mettre "
            "mes compétences et ma motivation au service d'une entreprise "
            "et relever de nouveaux défis professionnels."
        ),
        "sections": {
            "profil": "Profil professionnel", "expertise": "Domaines d'expertise",
            "actuel": "Expérience actuelle", "identite": "👤 Identité",
            "infos_pro": "📋 Informations professionnelles", "exp": "Expériences professionnelles",
            "form": "Diplômes & Formations", "comp": "Compétences professionnelles",
            "langues": "Langues", "interets": "Centres d'intérêt", "contact": "Contact"
        },
        "labels": {
            "nom": "Nom", "nationalite": "Nationalité", "situation": "Situation familiale",
            "fonction": "Fonction", "adresse": "Adresse", "service": "Service national",
            "stat_exp": "Expérience", "stat_postes": "Postes", "stat_form": "Formations",
            "stat_langues": "Langues", "missions": "Principales missions", "tel": "Téléphone",
            "email": "Email", "adresse_title": "Adresse",
            "degree_subtitle": "Master 2 en Recherche Opérationnelle",
            "sub_keywords": "Logistique • Transport • Planification • Supervision • Optimisation",
            "photo_missing": "Photo non trouvée"
        },
        "domaines": [
            ("🚚", "Transport", "Organisation, suivi et supervision des opérations de transport."),
            ("📦", "Logistique", "Gestion des flux, des opérations logistiques et des ressources."),
            ("📅", "Planification", "Élaboration des programmes et planification des ressources humaines et matérielles."),
            ("👥", "Supervision", "Suivi des équipes et contrôle du bon déroulement des opérations."),
            ("📈", "Optimisation", "Recherche de solutions permettant d'améliorer les coûts, les délais et l'utilisation des ressources."),
            ("📊", "Reporting", "Élaboration et suivi des reportings d'activité pour faciliter le pilotage."),
            ("🎯", "KPI", "Mise en place et suivi des indicateurs de performance liés à l'activité."),
            ("🤝", "Coordination", "Coordination entre les différents services et intervenants afin d'assurer la continuité des opérations."),
            ("⚙️", "Gestion des ressources", "Préparation, affectation et utilisation optimale des ressources disponibles."),
        ],
