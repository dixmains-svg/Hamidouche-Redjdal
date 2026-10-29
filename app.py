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
# 2. DESIGN CSS
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp { background-color: #F8FAFC; }
    .block-container { max-width: 1200px; padding-top: 25px; padding-bottom: 50px; }

    div[data-testid="stSidebar"] label p {
        color: #F8FAFC !important;
        font-weight: 800 !important;
        font-size: 14px !important;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    div[data-baseweb="select"] > div {
        background-color: #000000 !important;
        border: 2px solid #475569 !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2) !important;
    }

    div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    div[data-baseweb="select"] svg { fill: #FFFFFF !important; }

    ul[data-baseweb="menu"] {
        background-color: #FFFFFF !important;
        border: 2px solid #CBD5E1 !important;
        border-radius: 8px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.15) !important;
    }

    ul[data-baseweb="menu"] li div,
    ul[data-baseweb="menu"] li span,
    ul[data-baseweb="menu"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        font-weight: 800 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    ul[data-baseweb="menu"] li:hover,
    ul[data-baseweb="menu"] li:hover * {
        background-color: #F1F5F9 !important;
        color: #2563EB !important;
        -webkit-text-fill-color: #2563EB !important;
    }

    [data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #1E293B;
    }

    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span {
        color: #E2E8F0 !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label span {
        color: #38BDF8 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }

    [data-testid="stSidebar"] button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        padding: 10px 16px !important;
    }

    .cv-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        color: #FFFFFF;
        padding: 30px 35px;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
        border: 1px solid #334155;
    }
    .cv-name { font-size: 36px; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 8px; color: #FFFFFF; }
    .cv-title { font-size: 20px; font-weight: 600; margin-bottom: 14px; color: #38BDF8; }
    .cv-subtitle { font-size: 14px; line-height: 1.7; color: #94A3B8; }

    .section-title {
        color: #0F172A;
        font-size: 24px;
        font-weight: 800;
        margin-top: 30px;
        margin-bottom: 18px;
        padding-bottom: 8px;
        border-bottom: 3px solid #2563EB;
        display: inline-block;
    }

    .card { 
        background-color: #FFFFFF; 
        border-radius: 12px; 
        padding: 22px; 
        margin-bottom: 16px; 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); 
        border: 1px solid #E2E8F0;
    }
    .card-title { color: #0F172A; font-size: 18px; font-weight: 700; margin-bottom: 8px; }
    .card-text { color: #334155; font-size: 15px; line-height: 1.7; }

    .badge-chip {
        display: inline-block;
        background-color: #E0F2FE;
        color: #0369A1;
        padding: 5px 12px;
        border-radius: 18px;
        font-size: 13px;
        font-weight: 700;
        margin-right: 6px;
        margin-bottom: 8px;
    }

    .experience-card {
        background-color: #FFFFFF; 
        border-left: 5px solid #2563EB; 
        border-radius: 10px;
        padding: 22px; 
        margin-bottom: 18px; 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border-top: 1px solid #E2E8F0;
        border-right: 1px solid #E2E8F0;
        border-bottom: 1px solid #E2E8F0;
    }
    .experience-position { color: #0F172A; font-size: 20px; font-weight: 800; }
    .experience-company { color: #2563EB; font-size: 15px; font-weight: 700; margin-top: 4px; }
    .experience-date { color: #64748B; font-size: 13px; margin-top: 4px; margin-bottom: 12px; font-weight: 600; }
    .mission { color: #334155; line-height: 1.6; margin-top: 6px; font-size: 14px; }

    .skill-card { 
        background-color: #FFFFFF; 
        border-radius: 10px; 
        padding: 16px; 
        margin-bottom: 12px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.04); 
        color: #0F172A; 
        font-weight: 600;
        border: 1px solid #E2E8F0;
    }
    .contact-card { 
        background-color: #FFFFFF; 
        border-radius: 12px; 
        padding: 22px; 
        text-align: center; 
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); 
        border: 1px solid #E2E8F0;
    }
    .contact-icon { font-size: 30px; margin-bottom: 6px; }
    .contact-title { color: #0F172A; font-weight: 800; margin-bottom: 6px; }
    .contact-value { color: #475569; font-size: 14px; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 3. SÉLECTION DE LA LANGUE (Ajout de Tamazight)
# ============================================================

langue_choisie = st.sidebar.selectbox("🌐 Langue / Language / Idioma / Tutlayt", ["Français", "English", "Español", "Tamazight"])

# ============================================================
# 4. BASE DE DONNÉES MULTILINGUE (Avec Tamazight)
# ============================================================

TEXTES = {
    "Français": {
        "fonction": "Responsable Section Transport et Manutention",
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
📊 Analyse des données  
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
            "degree_stat": "Master 2 en Recherche Opérationnelle",
            "keywords": ["🚚 Logistique & Transport", "📅 Planification", "👥 Supervision", "📈 Optimisation", "📊 Analyse des données", "🏗️ Opérations & Manutention"],
            "poles": "Gestion du Transport, Opérations de Manutention, Flotte Roulante, Entreposage & Fret",
            "valeurs": [
                "Pilotage dynamique de la flotte en temps réel et optimisation de la rotation des camions.",
                "Digitalisation et suivi analytique des Ordres de Mission (OM) et maîtrise des coûts d'exploitation.",
                "Coordination multi-sites (Akbou, Alger, Sétif, Oran) et suivi rigoureux des prestations de manutention.",
                "Traitement de données opérationnelles pour la modélisation et l'aide à la décision stratégique."
            ]
        },
        "domaines": [
            ("🚚", "Transport", "Organisation, suivi et supervision des opérations de transport."),
            ("📦", "Logistique", "Gestion des flux, des opérations logistiques et des ressources."),
            ("📅", "Planification", "Élaboration des programmes et planification des ressources humaines et matérielles."),
            ("👥", "Supervision", "Suivi des équipes et contrôle du bon déroulement des opérations."),
            ("📈", "Optimisation", "Recherche de solutions permettant d'améliorer les coûts, les délais et l'utilisation des ressources."),
            ("📊", "Analyse des données", "Exploitation, traitement et analyse des données opérationnelles pour l'aide à la décision."),
            ("📋", "Reporting", "Élaboration et suivi des reportings d'activité pour faciliter le pilotage."),
            ("🎯", "KPI", "Mise en place et suivi des indicateurs de performance liés à l'activité."),
            ("🤝", "Coordination", "Coordination entre les différents services et intervenants afin d'assurer la continuité des opérations."),
            ("⚙️", "Gestion des ressources", "Préparation, affectation et utilisation optimale des ressources disponibles."),
        ],
        "experiences": [
            {
                "poste": "Responsable Section Transport et Manutention", "periode": "08/2026 - À ce jour", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Optimisation & Planification des Flux de Transport.",
                    "Pilotage & Supervision Dynamique de la Flotte en Temps Réel.",
                    "Supervision des Opérations de Transport & Manutention.",
                    "Gestion des Imprévus, Pointage & Traçabilité du Fret.",
                    "Management Opérationnel & Transmission des Directives (OM).",
                    "Gestion Technico-Opérationnelle du Parc Roulant.",
                    "Contrôle & Validation des Temps de Service.",
                    "Suivi des Indicateurs Clés de Performance (KPI)."
                ],
            },
            {
                "poste": "Superviseur techno-commercial", "periode": "01/2024 - 08/2026", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Analyser les besoins des clients.",
                    "Établir des reportings d'activité quotidiens, mensuels et annuels.",
                    "Apporter des solutions pertinentes et adaptées.",
                    "Suivre le bon déroulement de l'activité.",
                    "Contrôler les flux entrants et sortants de la zone d'entreposage.",
                ],
            },
            {
                "poste": "Superviseur exploitation", "periode": "06/2022 - 01/2024", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Piloter et superviser les opérations de transport.",
                    "Suivre le bon déroulement de l'activité.",
                    "Contrôler les flux entrants et sortants de la zone d'entreposage.",
                    "Planifier, organiser et contrôler l'activité d'une équipe.",
                    "Réceptionner les commandes des clients et veiller à leur satisfaction.",
                    "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus.",
                ],
            },
            {
                "poste": "Chargé de la planification", "periode": "02/2020 - 06/2022", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Préparer la disponibilité des ressources humaines et matérielles.",
                    "Planifier les commandes de chaque client.",
                    "Élaborer les reportings et les KPI liés à l'activité.",
                    "Réceptionner et traiter les demandes du service commercial.",
                    "Optimiser les ressources logistiques en termes de coûts et de délais.",
                    "Administrer et générer les ordres de mission.",
                    "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus.",
                ],
            },
            {
                "poste": "Coordinateur logistique", "periode": "02/2019 - 02/2020", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Élaborer et maintenir une parfaite coordination avec les autres services.",
                    "Élaborer et mettre en place des indicateurs de suivi de transport.",
                    "Gérer les partenariats avec les prestataires de transport.",
                    "Piloter et contrôler les performances des activités à court, moyen et long terme.",
                    "Veiller au respect des procédures de travail et de la réglementation.",
                ],
            },
            {
                "poste": "Chargé de la programmation", "periode": "04/2016 - 10/2018", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Exécuter et suivre régulièrement la programmation et l'utilisation des ressources.",
                    "Établir un planning optimal en optimisant les coûts et les délais.",
                    "Anticiper les situations imprévues et prendre rapidement les décisions correctives.",
                    "Étudier la faisabilité d'une mission avant d'affecter les ressources.",
                ],
            },
        ],
        "formations": [
            {"annee": "2021", "titre": "Formation en Transport international des marchandises", "organisme": "Chambre algérienne de commerce et d'industrie, Alger - Algérie"},
            {"annee": "2020", "titre": "Formation en Planification et optimisation logistique", "organisme": "Institut international de Management, Bejaia - Algérie"},
            {"annee": "2019", "titre": "Formation en Logistique et transport", "organisme": "Institut international de management, Bejaia - Algérie"},
            {"annee": "2019", "titre": "Formation en Gestion des temps et des priorités", "organisme": "Institut international de management, Bejaia - Algérie"},
            {"annee": "2018", "titre": "Formation en Gestion des opérations de transport", "organisme": "Institut international de management, Bejaia - Algérie"},
            {"annee": "2015", "titre": "Master 2 en Recherche opérationnelle", "organisme": "Option : Fiabilité et évaluation des performances des réseaux. Université Abderrahmane Mira, Bejaia - Algérie"},
            {"annee": "2012", "titre": "Licence en Recherche opérationnelle", "organisme": "Option : Aide à la décision. Université Abderrahmane Mira, Bejaia - Algérie"},
            {"annee": "2012", "titre": "Attestation de stage en gestion des opérations de transport", "organisme": "EPB, Bejaia - Algérie"},
            {"annee": "2008", "titre": "Diplôme Baccalauréat", "organisme": "Option : Science de la nature et de la vie. Lycée Mohamed Boudiaf, Tazmalt - Algérie"},
        ],
        "competences": [
            "Maîtrise du Pack Office : Excel, Word, PowerPoint et Outlook.",
            "Maîtrise de Matlab, LaTeX, Photoshop, Illustrator et InDesign.",
            "Langages de programmation : HTML, Java, Delphi et C++.",
            "Planification et optimisation des ressources.",
            "Gestion des opérations de transport.",
            "Supervision des opérations de transport.",
            "Élaboration et mise en place des indicateurs de suivi de transport.",
            "Élaboration des reportings et KPI liés à l'activité.",
            "Gestion des partenariats avec les prestataires de transport.",
            "Coordination avec les autres services.",
            "Gestion des ressources humaines et matérielles.",
            "Gestion et génération des ordres de mission.",
        ],
        "langues": [
            ("Kabyle", "Maîtrise très bien"),
            ("Arabe", "Maîtrise très bien"),
            ("Français", "Maîtrise bien"),
            ("Anglais", "Maîtrise moyenne"),
        ],
        "interets": [
            ("✈️", "Voyage"),
            ("⚽", "Passion pour le sport"),
            ("🤝", "Activités associatives"),
            ("🎬", "Cinéma"),
            ("🎨", "Arts créatifs"),
            ("💻", "Informatique"),
        ]
    },
    "English": {
        "fonction": "Transport and Handling Section Manager",
        "nationalite": "Algerian",
        "situation": "Married",
        "service_national": "Exempted",
        "nav_title": "NAVIGATION",
        "download_btn": "📄 Download CV (PDF)",
        "nav": [
            "🏠 Home", "👤 Profile", "💼 Experience", "🎓 Education & Training",
            "🛠️ Skills", "🌐 Languages", "⭐ Interests", "📞 Contact"
        ],
        "sidebar_domains": """
**PROFESSIONAL FIELDS**

🚚 Transport  
📦 Logistics  
📊 Planning
