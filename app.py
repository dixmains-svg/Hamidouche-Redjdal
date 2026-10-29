import streamlit as st
from pathlib import Path
import base64

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

# Convertir la photo en base64 pour l'intégrer proprement dans le CSS/HTML
def get_image_base64(path):
    if path.exists():
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return None

photo_b64 = get_image_base64(PHOTO)

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
        display: flex;
        align-items: center;
        gap: 25px;
    }
    .cv-header-content { flex: 1; }
    .cv-avatar {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #38BDF8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
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
# 3. SÉLECTION DE LA LANGUE
# ============================================================

langue_choisie = st.sidebar.selectbox("🌐 Langue / Language / Idioma / Tutlayt", ["Français", "English", "Español", "Tamazight"])

# ============================================================
# 4. BASE DE DONNÉES MULTILINGUE
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
👥 Supervision  
📈 Optimization  
📊 Data Analysis  
""",
        "profil": (
            "Dynamic, reliable, and possessing strong interpersonal skills, "
            "with 9 years of experience in the field of logistics. "
            "Highly proficient with IT tools, I aim to apply "
            "my skills and motivation to serve a growing company "
            "and take on new professional challenges."
        ),
        "sections": {
            "profil": "Professional Profile", "expertise": "Fields of Expertise",
            "actuel": "Current Position", "identite": "👤 Identity",
            "infos_pro": "📋 Professional Information", "exp": "Work Experience",
            "form": "Education & Training", "comp": "Professional Skills",
            "langues": "Languages", "interets": "Interests", "contact": "Contact"
        },
        "labels": {
            "nom": "Name", "nationalite": "Nationality", "situation": "Marital Status",
            "fonction": "Position", "adresse": "Address", "service": "Military Service",
            "stat_exp": "Experience", "stat_postes": "Positions", "stat_form": "Training",
            "stat_langues": "Languages", "missions": "Key Responsibilities", "tel": "Phone",
            "email": "Email", "adresse_title": "Address",
            "degree_stat": "Master 2 in Operational Research",
            "keywords": ["🚚 Logistics & Transport", "📅 Planning", "👥 Supervision", "📈 Optimization", "📊 Data Analysis", "🏗️ Operations & Handling"],
            "poles": "Transport Management, Handling Operations, Rolling Fleet, Warehousing & Freight",
            "valeurs": [
                "Real-time dynamic fleet supervision and vehicle rotation optimization.",
                "Digital tracking of Mission Orders (MO) and operational cost control.",
                "Multi-site coordination (Akbou, Algiers, Setif, Oran) and handling service quality monitoring.",
                "Operational data processing for modeling and strategic decision support."
            ]
        },
        "domaines": [
            ("🚚", "Transport", "Organization, tracking, and supervision of transport operations."),
            ("📦", "Logistics", "Flow management, logistics operations, and resource allocation."),
            ("📅", "Planning", "Scheduling operations and planning human and material resources."),
            ("👥", "Supervision", "Team management and operational control."),
            ("📈", "Optimization", "Cost reduction, lead time improvement, and optimal resource usage."),
            ("📊", "Data Analysis", "Processing, analyzing, and leveraging operational data for decision support."),
            ("📋", "Reporting", "Developing and tracking activity reports for management."),
            ("🎯", "KPI", "Implementation and monitoring of activity performance indicators."),
            ("🤝", "Coordination", "Inter-departmental coordination ensuring seamless operations."),
            ("⚙️", "Resource Management", "Preparation, assignment, and optimal allocation of resources."),
        ],
        "experiences": [
            {
                "poste": "Transport and Handling Section Manager", "periode": "08/2026 - Present", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Transport Flow Optimization & Planning.",
                    "Real-Time Dynamic Fleet Management & Supervision.",
                    "Supervision of Transport & Handling Operations.",
                    "Contingency Management, Attendance & Freight Traceability.",
                    "Operational Management & Transmission of Directives (Mission Orders).",
                    "Technical & Operational Management of the Rolling Fleet.",
                    "Control & Validation of Service Hours.",
                    "Monitoring Key Performance Indicators (KPIs)."
                ],
            },
            {
                "poste": "Technical & Commercial Supervisor", "periode": "01/2024 - 08/2026", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Analyze customer requirements and needs.",
                    "Establish daily, monthly, and annual activity reports.",
                    "Provide relevant and adapted logistics solutions.",
                    "Monitor ongoing operational activities.",
                    "Control inbound and outbound flows within storage areas.",
                ],
            },
            {
                "poste": "Operations Supervisor", "periode": "06/2022 - 01/2024", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Lead and supervise transport operations.",
                    "Monitor operational smooth execution.",
                    "Control inbound and outbound warehouse flows.",
                    "Plan, organize, and control team tasks.",
                    "Receive customer orders and ensure customer satisfaction.",
                    "Ensure program delivery and adapt to contingencies.",
                ],
            },
            {
                "poste": "Planning Officer", "periode": "02/2020 - 06/2022", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Prepare human and material resource availability.",
                    "Schedule order execution per customer.",
                    "Develop activity-related reporting and KPIs.",
                    "Receive and process commercial requests.",
                    "Optimize logistics resources regarding cost and lead times.",
                    "Issue and manage mission orders.",
                    "Adjust operational schedules in case of unforeseen events.",
                ],
            },
            {
                "poste": "Logistics Coordinator", "periode": "02/2019 - 02/2020", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Develop and maintain seamless coordination with other departments.",
                    "Design and deploy transport monitoring indicators.",
                    "Manage partnerships with transport service providers.",
                    "Monitor short, medium, and long-term activity performance.",
                    "Ensure compliance with work procedures and safety regulations.",
                ],
            },
            {
                "poste": "Scheduling Officer", "periode": "04/2016 - 10/2018", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Execute and regularly monitor resource scheduling and usage.",
                    "Establish optimal schedules balancing cost and delivery times.",
                    "Anticipate unexpected situations and take prompt corrective decisions.",
                    "Analyze mission feasibility prior to assigning resources.",
                ],
            },
        ],
        "formations": [
            {"annee": "2021", "titre": "Training in International Freight Transport", "organisme": "Algerian Chamber of Commerce and Industry, Algiers - Algeria"},
            {"annee": "2020", "titre": "Training in Logistics Planning & Optimization", "organisme": "International Management Institute, Bejaia - Algeria"},
            {"annee": "2019", "titre": "Training in Logistics & Transport", "organisme": "International Management Institute, Bejaia - Algeria"},
            {"annee": "2019", "titre": "Training in Time & Priority Management", "organisme": "International Management Institute, Bejaia - Algeria"},
            {"annee": "2018", "titre": "Training in Transport Operations Management", "organisme": "International Management Institute, Bejaia - Algeria"},
            {"annee": "2015", "titre": "Master's Degree (M2) in Operational Research", "organisme": "Option: Network Reliability and Performance Evaluation. Abderrahmane Mira University, Bejaia - Algeria"},
            {"annee": "2012", "titre": "Bachelor's Degree in Operational Research", "organisme": "Option: Decision Support Systems. Abderrahmane Mira University, Bejaia - Algeria"},
            {"annee": "2012", "titre": "Transport Operations Management Internship Certificate", "organisme": "EPB, Bejaia - Algeria"},
            {"annee": "2008", "titre": "High School Diploma (Baccalaureate)", "organisme": "Option: Natural Sciences and Life. Mohamed Boudiaf High School, Tazmalt - Algeria"},
        ],
        "competences": [
            "Proficient in MS Office: Excel, Word, PowerPoint, and Outlook.",
            "Proficient in Matlab, LaTeX, Photoshop, Illustrator, and InDesign.",
            "Programming Languages: HTML, Java, Delphi, and C++.",
            "Resource planning and optimization.",
            "Management of transport operations.",
            "Supervision of transport operations.",
            "Development and implementation of transport tracking indicators.",
            "Development of activity-related reports and KPIs.",
            "Partnership management with transport providers.",
            "Inter-departmental coordination.",
            "Management of human and material resources.",
            "Administration and generation of mission orders.",
        ],
        "langues": [
            ("Kabyle", "Native / Excellent"),
            ("Arabic", "Native / Excellent"),
            ("French", "Fluent"),
            ("English", "Intermediate"),
        ],
        "interets": [
            ("✈️", "Travel"),
            ("⚽", "Sports Passion"),
            ("🤝", "Community Activities"),
            ("🎬", "Cinema"),
            ("🎨", "Creative Arts"),
            ("💻", "IT & Technology"),
        ]
    },
    "Español": {
        "fonction": "Responsable de Sección Transporte y Manipulación",
        "nationalite": "Argelina",
        "situation": "Casado",
        "service_national": "Eximido",
        "nav_title": "NAVEGACIÓN",
        "download_btn": "📄 Descargar CV (PDF)",
        "nav": [
            "🏠 Inicio", "👤 Perfil", "💼 Experiencia", "🎓 Educación y Formación",
            "🛠️ Habilidades", "🌐 Idiomas", "⭐ Intereses", "📞 Contacto"
        ],
        "sidebar_domains": """
**CAMPOS PROFESIONALES**

🚚 Transporte  
📦 Logística  
📊 Planificación  
👥 Supervisión  
📈 Optimización  
📊 Análisis de Datos  
""",
        "profil": (
            "Dinámico, serio y con excelentes habilidades interpersonales, "
            "con 9 años de experiencia en el sector de la logística. "
            "Muy hábil con las herramientas informáticas, deseo aportar "
            "mis competencias y motivación al servicio de una empresa "
            "y asumir nuevos retos profesionales."
        ),
        "sections": {
            "profil": "Perfil Profesional", "expertise": "Áreas de Experiencia",
            "actuel": "Puesto Actual", "identite": "👤 Identidad",
            "infos_pro": "📋 Información Profesional", "exp": "Experiencia Laboral",
            "form": "Educación y Formación", "comp": "Habilidades Profesionales",
            "langues": "Idiomas", "interets": "Intereses", "contact": "Contacto"
        },
        "labels": {
            "nom": "Nombre", "nationalite": "Nacionalidad", "situation": "Estado Civil",
            "fonction": "Puesto", "adresse": "Dirección", "service": "Servicio Militar",
            "stat_exp": "Experiencia", "stat_postes": "Puestos", "stat_form": "Formación",
            "stat_langues": "Idiomas", "missions": "Principales Responsabilidades", "tel": "Teléfono",
            "email": "Correo electrónico", "adresse_title": "Dirección",
            "degree_stat": "Máster 2 en Investigación Operativa",
            "keywords": ["🚚 Logística y Transporte", "📅 Planificación", "👥 Supervisión", "📈 Optimización", "📊 Análisis de Datos", "🏗️ Operaciones y Manipulación"],
            "poles": "Gestión del Transporte, Operaciones de Manipulación, Parque Móvil, Almacenamiento y Carga",
            "valeurs": [
                "Control dinámico de la flota en tiempo real y optimización del tiempo de rotación.",
                "Digitalización de Órdenes de Misión (OM) y gestión analítica de costes operativos.",
                "Coordinación entre centros (Akbou, Argel, Sétif, Orán) y seguimiento de calidad de operaciones.",
                "Procesamiento de datos operativos para la toma de decisiones estratégicas."
            ]
        },
        "domaines": [
            ("🚚", "Transporte", "Organización, seguimiento y supervisión de operaciones de transporte."),
            ("📦", "Logística", "Gestión de flujos, operaciones logísticas y recursos."),
            ("📅", "Planificación", "Programación de operaciones y planificación de recursos humanos y materiales."),
            ("👥", "Supervisión", "Gestión de equipos y control del desarrollo de las operaciones."),
            ("📈", "Optimización", "Búsqueda de soluciones para optimizar costes, plazos y recursos."),
            ("📊", "Análisis de Datos", "Procesamiento, análisis y aprovechamiento de datos operativos para la toma de decisiones."),
            ("📋", "Reportes", "Elaboración y seguimiento de informes de actividad para la dirección."),
            ("🎯", "KPI", "Implementación y seguimiento de indicadores de rendimiento."),
            ("🤝", "Coordinación", "Coordinación interdepartamental para garantizar operaciones fluidas."),
            ("⚙️", "Gestión de Recursos", "Preparación, asignación y optimización de los recursos disponibles."),
        ],
        "experiences": [
            {
                "poste": "Responsable de Sección Transporte y Manipulación", "periode": "08/2026 - Presente", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Optimización y planificación de flujos de transporte.",
                    "Gestión y supervisión dinámica de la flota en tiempo real.",
                    "Supervisión de operaciones de transporte y manipulación.",
                    "Gestión de incidencias, control de presencia y trazabilidad de carga.",
                    "Gestión operativa y transmisión de directivas (Órdenes de Misión).",
                    "Gestión técnica y operativa de la flota rodante.",
                    "Control y validación de tiempos de servicio.",
                    "Seguimiento de indicadores clave de rendimiento (KPI)."
                ],
            },
            {
                "poste": "Supervisor Técnico y Comercial", "periode": "01/2024 - 08/2026", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Analizar las necesidades de los clientes.",
                    "Elaborar informes de actividad diarios, mensuales y anuales.",
                    "Aportar soluciones pertinentes y adaptadas.",
                    "Supervisar el desarrollo de la actividad.",
                    "Controlar los flujos de entrada y salida en la zona de almacenamiento.",
                ],
            },
            {
                "poste": "Supervisor de Explotación", "periode": "06/2022 - 01/2024", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Dirigir y supervisar las operaciones de transporte.",
                    "Garantizar el buen desarrollo de la actividad.",
                    "Controlar los flujos de entrada y salida del almacén.",
                    "Planificar, organizar y controlar el trabajo del equipo.",
                    "Recepción de pedidos de clientes y garantía de su satisfacción.",
                    "Asegurar la ejecución del programa adaptándose a imprevistos.",
                ],
            },
            {
                "poste": "Responsable de Planificación", "periode": "02/2020 - 06/2022", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Preparar la disponibilidad de recursos humanos y materiales.",
                    "Planificar los pedidos de cada cliente.",
                    "Elaborar informes y KPI relacionados con la actividad.",
                    "Recibir y procesar las solicitudes del departamento comercial.",
                    "Optimizar los recursos logísticos en términos de costes y plazos.",
                    "Administrar y emitir órdenes de misión.",
                    "Ajustar los programas operativos ante imprevistos.",
                ],
            },
            {
                "poste": "Coordinador Logístico", "periode": "02/2019 - 02/2020", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Desarrollar y mantener una perfecta coordinación con los demás departamentos.",
                    "Diseñar e implantar indicadores de seguimiento del transporte.",
                    "Gestionar alianzas con proveedores de servicios de transporte.",
                    "Supervisar el rendimiento de las actividades a corto, medio y largo plazo.",
                    "Velar por el cumplimiento de los procedimientos de trabajo y normativas.",
                ],
            },
            {
                "poste": "Responsable de Programación", "periode": "04/2016 - 10/2018", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Ejecutar y supervisar regularmente la programación y uso de recursos.",
                    "Establecer una planificación óptima minimizando costes y plazos.",
                    "Anticipar situaciones imprevistas y tomar decisiones correctivas rápidas.",
                    "Estudiar la viabilidad de las misiones antes de asignar recursos.",
                ],
            },
        ],
        "formations": [
            {"annee": "2021", "titre": "Formación en Transporte Internacional de Mercancías", "organisme": "Cámara Argelina de Comercio e Industria, Argel - Argelia"},
            {"annee": "2020", "titre": "Formación en Planificación y Optimización Logística", "organisme": "Instituto Internacional de Gestión, Bejaia - Argelia"},
            {"annee": "2019", "titre": "Formación en Logística y Transporte", "organisme": "Instituto Internacional de Gestión, Bejaia - Argelia"},
            {"annee": "2019", "titre": "Formación en Gestión del Tiempo y Prioridades", "organisme": "Instituto Internacional de Gestión, Bejaia - Argelia"},
            {"annee": "2018", "titre": "Formación en Gestión de Operaciones de Transporte", "organisme": "Instituto Internacional de Gestión, Bejaia - Argelia"},
            {"annee": "2015", "titre": "Máster 2 en Investigación Operativa", "organisme": "Opción: Fiabilidad y evaluación de rendimiento de redes. Universidad Abderrahmane Mira, Bejaia - Argelia"},
            {"annee": "2012", "titre": "Licenciatura en Investigación Operativa", "organisme": "Opción: Ayuda a la decisión. Universidad Abderrahmane Mira, Bejaia - Argelia"},
            {"annee": "2012", "titre": "Certificado de Prácticas en Gestión de Operaciones de Transporte", "organisme": "EPB, Bejaia - Argelia"},
            {"annee": "2008", "titre": "Título de Bachillerato", "organisme": "Opción: Ciencias de la Naturaleza y de la Vida. Instituto Mohamed Boudiaf, Tazmalt - Argelia"},
        ],
        "competences": [
            "Dominio de MS Office: Excel, Word, PowerPoint y Outlook.",
            "Dominio de Matlab, LaTeX, Photoshop, Illustrator e InDesign.",
            "Lenguajes de programación: HTML, Java, Delphi y C++.",
            "Planificación y optimización de recursos.",
            "Gestión de operaciones de transporte.",
            "Supervisión de operaciones de transporte.",
            "Desarrollo e implantación de indicadores de seguimiento de transporte.",
            "Elaboración de informes y KPI de actividad.",
            "Gestión de colaboraciones con proveedores de transporte.",
            "Coordinación interdepartamental.",
            "Gestión de recursos humanos y materiales.",
            "Gestión y emisión de órdenes de misión.",
        ],
        "langues": [
            ("Cabiliño / Kabyle", "Nativo / Excelente"),
            ("Árabe", "Nativo / Excelente"),
            ("Francés", "Fluido"),
            ("Inglés", "Intermedio"),
        ],
        "interets": [
            ("✈️", "Viajes"),
            ("⚽", "Pasión por el Deporte"),
            ("🤝", "Actividades Associativas"),
            ("🎬", "Cine"),
            ("🎨", "Artes Creativas"),
            ("💻", "Informática"),
        ]
    },
    "Tamazight": {
        "fonction": "Amasay n Temnaḍt n Uɣennǧu d Usali (Responsable Section Transport et Manutention)",
        "nationalite": "Azzayri",
        "situation": "Yejji (Amecta)",
        "service_national": "Yeffeɣ (Dégagé)",
        "nav_title": "ASENAW",
        "download_btn": "📄 Sider CV (PDF)",
        "nav": [
            "🏠 Asnaseb", "👤 Aglam", "💼 Timmuzɣiwin (Expériences)", "🎓 Timsirin & Taseddayin (Formations)",
            "🛠️ Tirmitin (Compétences)", "🌐 Tutlayin", "⭐ Isenfaren / Ihulfan", "📞 Assaɣ (Contact)"
        ],
        "sidebar_domains": """
**ISWIWEN N TMELLALTEFT**

🚚 Aɣennǧu (Transport)  
📦 Tallunt (Logistics)  
📊 Asenqed (Planning)  
👥 Anekkaz (Supervision)  
📈 Asnerni (Optimization)  
📊 Asileɣ n Isefka (Data Analysis)  
""",
        "profil": (
            "D ameskar, d unṣib yernu ɣur-i lǧehd deg tallelt d wawal, "
            "s 9 iseggasen n tirmit deg unnar n tallunt (logistique). "
            "Ssnen-iyi imenza nniḍen n tfulka, bɣiɣ ad ssedduɣ "
            "tizemmar-iw d lɣerc-iw i wakken ad ḥbuɣ tamurt "
            "yernu ad qedceɣ tiɣawsiwin timaynutin."
        ),
        "sections": {
            "profil": "Aglam Unṣib", "expertise": "Isragen n Tirmit",
            "actuel": "Tirmit tamezwarut", "identite": "👤 Tasnefrayt",
            "infos_pro": "📋 Talɣut Tunṣibt", "exp": "Timmuzɣiwin n Uqedcic",
            "form": "Taseddayin d Timsirin", "comp": "Tizemmaren Tunṣibin",
            "langues": "Tutlayin", "interets": "Isenfaren", "contact": "Assaɣ"
        },
        "labels": {
            "nom": "Isem", "nationalite": "Tamazɣa / Tagduda", "situation": "Tawacult",
            "fonction": "Tawuri", "adresse": "Tansa", "service": "Amsaraj Awanak",
            "stat_exp": "Tirmit", "stat_postes": "Tawuriwin", "stat_form": "Timsirin",
            "stat_langues": "Tutlayin", "missions": "Tiɣawsiwin Timezwura", "tel": "Tiliɣri",
            "email": "Imayl", "adresse_title": "Tansa",
            "degree_stat": "Master 2 deg Usefrek d Usenqed",
            "keywords": ["🚚 Tallunt d Uɣennǧu", "📅 Asenqed", "👥 Anekkaz", "📈 Asnerni", "📊 Asileɣ n Isefka", "🏗️ Tigawin d Usali"],
            "poles": "Asileɣ n Uɣennǧu, Tigawin n Usali, Iɣerruba, Taɣzut d Wezzay",
            "valeurs": [
                "Asefrek alemmas n tɣerruft s tizi n wussan d usnerni n wuzzel n ikamyunen.",
                "Asileɣ n Tira n Tikli (OM) d usefrek n lexsaṣ n tmacin.",
                "Asdukel n tama (At Bu Yebdran, Bgayet, Setif, Wehran) d usefrek n tallelt.",
                "Asefrek n isefka n twwuri i usefti d tallelt n ufran."
            ]
        },
        "domaines": [
            ("🚚", "Aɣennǧu", "Asefrek d usenqed n tiɣawsiwin n uɣennǧu."),
            ("📦", "Tallunt", "Assefrek n isragen d tiɣawsiwin n tallunt."),
            ("📅", "Asenqed", "Asidef n wahilen d usenqed n medden d tmacin."),
            ("👥", "Anekkaz", "Asenqed n trebbuyaɛ d usdukel n twwuri."),
            ("📈", "Asnerni", "Anadi n tifrat i usemɣer n lexsaṣ, akud d tmarayt."),
            ("📊", "Asileɣ n Isefka", "Asileɣ d usenqed n isefka n twwuri i wakken ad fken afud."),
            ("📋", "Azenzi", "Asnulfu d usenqed n isenfaren n twwuri."),
            ("🎯", "KPI", "Asbeddi d usenqed n ismal n tmazɣa."),
            ("🤝", "Asdukel", "Asdukel gar iɣlifen yemgaraden i wakken ad kemlen twwuriwin."),
            ("⚙️", "Asefrek n Isragen", "Aheggi d useqdec n isragen yellan."),
        ],
        "experiences": [
            {
                "poste": "Amasay n Temnaḍt n Uɣennǧu d Usali", "periode": "08/2026 - Ar ass-a", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Asnerni d usenqed n ubrid n uɣennǧu.",
                    "Asefrek d unekkaz alemmas n tɣerruft s tizi n wussan.",
                    "Anekkaz n tiɣawsiwin n uɣennǧu d usali.",
                    "Asefrek n wuguren, asenqed n ubrid.",
                    "Asenqed n twuri d usuter n tɣawsiwin (OM).",
                    "Asefrek unṣib n tɣerruft.",
                    "Asenqed n wakud n twwuri.",
                    "Asenqed n ismal n tmazɣa (KPI)."
                ],
            },
            {
                "poste": "Anekkaz Unṣib d Uzniɣ", "periode": "01/2024 - 08/2026", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Asenqed n isuturen n yemsuzaɣ.",
                    "Asnulfu n isenfaren n wass, n waggur d useggas.",
                    "Aseɣersi n tifrat yessefkun.",
                    "Asenqed n twuri n ussefrek.",
                    "Asenqed n isragen n unekcum d tuffɣa deg taɣzut.",
                ],
            },
            {
                "poste": "Anekkaz n Tiɣawsiwin", "periode": "06/2022 - 01/2024", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Aselway d unekkaz n tiɣawsiwin n uɣennǧu.",
                    "Asenqed n ubrid n twwuri.",
                    "Asenqed n isragen n unekcum d tuffɣa.",
                    "Asenqed d usefrek n tarbaɛt.",
                    "Asefrek n isuturen n yemsuzaɣ d taceqquft.",
                    "Asdukel n wahil d usenqed-is s wawalen.",
                ],
            },
            {
                "poste": "Amasay n Usenqed", "periode": "02/2020 - 06/2022", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Aheggi n tmarayt n medden d tmacin.",
                    "Asenqed n isuturen n yal amsuzaɣ.",
                    "Asnulfu n isenfaren d KPI.",
                    "Asefrek n isuturen n usali.",
                    "Asnerni n isragen n tallunt s lexsaṣ.",
                    "Asenqed d usuffeɣ n twuriwin.",
                    "Asenqed n wahil s wuguren.",
                ],
            },
            {
                "poste": "Amhaz n Tallunt", "periode": "02/2019 - 02/2020", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Asnulfu n usdukel s wawal d iɣlifen nniḍen.",
                    "Asnulfu n ismal n usenqed n uɣennǧu.",
                    "Asefrek n wassaɣen d iɛessasen n uɣennǧu.",
                    "Aselway d usenqed n twwuri i lebɛiḍ.",
                    "Asenqed n leqwanen n twwuri.",
                ],
            },
            {
                "poste": "Amasay n Usenqed n Wahil", "periode": "04/2016 - 10/2018", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Asnulfu d usenqed n wahil d useqdec.",
                    "Asbeddi n usenqed s lexsaṣ d wakud.",
                    "Asenqed n wuguren d ufran n tifrat.",
                    "Asileɣ n tixutert n twuriqin.",
                ],
            },
        ],
        "formations": [
            {"annee": "2021", "titre": "Tamsirit deg Uɣennǧu Agraɣlan", "organisme": "Taseqqamut n Lezzayer n Usali d Tizuzu, Lezzayer - Lezzayer"},
            {"annee": "2020", "titre": "Tamsirit deg Asenqed d Usnerni n Tallunt", "organisme": "Tasdawit n Usefrek, Bgayet - Lezzayer"},
            {"annee": "2019", "titre": "Tamsirit deg Tallunt d Uɣennǧu", "organisme": "Tasdawit n Usefrek, Bgayet - Lezzayer"},
            {"annee": "2019", "titre": "Tamsirit deg Usefrek n Wakud d Tezwura", "organisme": "Tasdawit n Usefrek, Bgayet - Lezzayer"},
            {"annee": "2018", "titre": "Tamsirit deg Usefrek n Tiɣawsiwin n Uɣennǧu", "organisme": "Tasdawit n Usefrek, Bgayet - Lezzayer"},
            {"annee": "2015", "titre": "Master 2 deg Usefrek d Usenqed", "organisme": "Tasdawit Abderrahmane Mira, Bgayet - Lezzayer"},
            {"annee": "2012", "titre": "Licence deg Usefrek d Usenqed", "organisme": "Tasdawit Abderrahmane Mira, Bgayet - Lezzayer"},
            {"annee": "2012", "titre": "Takadit n Usileɣ deg Usefrek n Uɣennǧu", "organisme": "EPB, Bgayet - Lezzayer"},
            {"annee": "2008", "titre": "Baccalauréat (Akat n Tasdawit)", "organisme": "Aɣbaz Mohamed Boudiaf, Tazmalt - Lezzayer"},
        ],
        "competences": [
            "Assefrek n Pack Office : Excel, Word, PowerPoint d Outlook.",
            "Assefrek n Matlab, LaTeX, Photoshop, Illustrator d InDesign.",
            "Tabbayin n Tira : HTML, Java, Delphi d C++.",
            "Asenqed d usnerni n isragen.",
            "Asefrek n tiɣawsiwin n uɣennǧu.",
            "Anekkaz n tiɣawsiwin n uɣennǧu.",
            "Asbeddi n ismal n usenqed n uɣennǧu.",
            "Asnulfu n isenfaren d KPI.",
            "Asefrek n wassaɣen d yimsenɛa.",
            "Asdukel s iɣlifen nniḍen.",
            "Asefrek n medden d tmacin.",
            "Asefrek d usuffeɣ n twuriwin.",
        ],
        "langues": [
            ("Taqbaylit", "Ssen-tt mliḥa"),
            ("Taɛrabt", "Ssen-tt mliḥa"),
            ("Tafransist", "Ssen-tt"),
            ("Taglizit", "Tilawt"),
        ],
        "interets": [
            ("✈️", "Ibriden (Voyage)"),
            ("⚽", "Uurar (Sport)"),
            ("🤝", "Tawwuri n Tmetti"),
            ("🎬", "Sinima"),
            ("🎨", "Tawuri n Tfulka"),
            ("💻", "Taseddawit (IT)"),
        ]
    }
}

t = TEXTES[langue_choisie]

# ============================================================
# 5. BARRE LATÉRALE (SIDEBAR)
# ============================================================

st.sidebar.markdown(f"### {t['nav_title']}")
menu_choisi = st.sidebar.radio("", t["nav"], label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.markdown(t["sidebar_domains"])
st.sidebar.markdown("---")

# ============================================================
# 6. FONCTION DE GÉNÉRATION DU PDF
# ============================================================

def generer_pdf():
    doc = SimpleDocTemplate(str(PDF_PATH), pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#0F172A'), spaceAfter=4, fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#2563EB'), spaceAfter=12, fontName='Helvetica-Bold')
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#334155'), leading=13, spaceAfter=8)
    section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#0F172A'), spaceBefore=14, spaceAfter=6, fontName='Helvetica-Bold')
    
    story = []
    story.append(Paragraph(nom, title_style))
    story.append(Paragraph(t["fonction"], subtitle_style))
    story.append(Paragraph(f"<b>{t['labels']['tel']} :</b> {telephone} | <b>{t['labels']['email']} :</b> {email} | <b>{t['labels']['adresse_title']} :</b> {adresse}", body_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563EB'), spaceBefore=8, spaceAfter=12))
    
    story.append(Paragraph(t["sections"]["profil"], section_style))
    story.append(Paragraph(t["profil"], body_style))
    
    story.append(Paragraph(t["sections"]["exp"], section_style))
    for exp in t["experiences"]:
        story.append(Paragraph(f"<b>{exp['poste']}</b> - <font color='#2563EB'>{exp['entreprise']}</font>", ParagraphStyle('ExpTitle', parent=body_style, fontName='Helvetica-Bold', fontSize=10)))
        story.append(Paragraph(f"<i>{exp['periode']}</i>", ParagraphStyle('ExpDate', parent=body_style, textColor=colors.HexColor('#64748B'), fontSize=8, spaceAfter=4)))
        for m in exp["missions"]:
            story.append(Paragraph(f"• {m}", body_style))
        story.append(Spacer(1, 4))
        
    story.append(Paragraph(t["sections"]["form"], section_style))
    for f in t["formations"]:
        story.append(Paragraph(f"• <b>{f['annee']}</b> : {f['titre']} - <i>{f['organisme']}</i>", body_style))
        
    doc.build(story)

if PDF_PATH.exists():
    with open(PDF_PATH, "rb") as pdf_file:
        st.sidebar.download_button(
            label=t["download_btn"],
            data=pdf_file,
            file_name="cv_hamidouche_redjdal.pdf",
            mime="application/pdf",
        )

# ============================================================
# 7. CORPS DE LA PAGE (AFFICHAGE AVEC PHOTO)
# ============================================================

# Code HTML pour l'en-tête avec condition sur l'existence de la photo
avatar_html = f'<img src="data:image/jpeg;base64,{photo_b64}" class="cv-avatar">' if photo_b64 else '<div style="font-size: 60px;">👨‍💼</div>'

st.markdown(
    f"""
    <div class="cv-header">
        {avatar_html}
        <div class="cv-header-content">
            <div class="cv-name">{nom}</div>
            <div class="cv-title">{t["fonction"]}</div>
            <div class="cv-subtitle">
                📍 {adresse}   |   📞 {telephone}   |   ✉️ {email}
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Génération automatique du PDF
try:
    generer_pdf()
except Exception:
    pass

# Navigation interactive par onglets / sections conditionnelles
if menu_choisi.startswith("🏠") or "Accueil" in menu_choisi or "Home" in menu_choisi or "Inicio" in menu_choisi or "Asnaseb" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["profil"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card"><div class="card-text">{t["profil"]}</div></div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="section-title">{t["sections"]["expertise"]}</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (ic, title, desc) in enumerate(t["domaines"]):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">{ic} {title}</div>
                    <div class="card-text">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif menu_choisi.startswith("👤") or "Profil" in menu_choisi or "Profile" in menu_choisi or "Perfil" in menu_choisi or "Aglam" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["identite"]}</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="contact-card"><div class="contact-title">{t["labels"]["nationalite"]}</div><div class="contact-value">{t["nationalite"]}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="contact-card"><div class="contact-title">{t["labels"]["situation"]}</div><div class="contact-value">{t["situation"]}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="contact-card"><div class="contact-title">{t["labels"]["service"]}</div><div class="contact-value">{t["service_national"]}</div></div>', unsafe_allow_html=True)
        
    st.markdown(f'<div class="section-title">{t["sections"]["infos_pro"]}</div>', unsafe_allow_html=True)
    for val in t["labels"]["valeurs"]:
        st.markdown(f'<div class="skill-card">💡 {val}</div>', unsafe_allow_html=True)

elif menu_choisi.startswith("💼") or "Expérience" in menu_choisi or "Experience" in menu_choisi or "Experiencia" in menu_choisi or "Timmuzɣiwin" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["exp"]}</div>', unsafe_allow_html=True)
    for exp in t["experiences"]:
        missions_html = "".join([f"<li class='mission'>{m}</li>" for m in exp["missions"]])
        st.markdown(
            f"""
            <div class="experience-card">
                <div class="experience-position">{exp["poste"]}</div>
                <div class="experience-company">{exp["entreprise"]}</div>
                <div class="experience-date">📅 {exp["periode"]}</div>
                <ul>{missions_html}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif menu_choisi.startswith("🎓") or "Diplômes" in menu_choisi or "Education" in menu_choisi or "Educación" in menu_choisi or "Timsirin" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["form"]}</div>', unsafe_allow_html=True)
    for form in t["formations"]:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">🎓 {form["titre"]} ({form["annee"]})</div>
                <div class="card-text">🏛️ <b>{form["organisme"]}</b></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif menu_choisi.startswith("🛠️") or "Compétences" in menu_choisi or "Skills" in menu_choisi or "Habilidades" in menu_choisi or "Tirmitin" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["comp"]}</div>', unsafe_allow_html=True)
    for comp in t["competences"]:
        st.markdown(f'<div class="skill-card">✔️ {comp}</div>', unsafe_allow_html=True)

elif menu_choisi.startswith("🌐") or "Langues" in menu_choisi or "Languages" in menu_choisi or "Idiomas" in menu_choisi or "Tutlayin" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["langues"]}</div>', unsafe_allow_html=True)
    for lang, niveau in t["langues"]:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">🗣️ {lang}</div>
                <div class="card-text"><b>{niveau}</b></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif menu_choisi.startswith("⭐") or "Centres" in menu_choisi or "Interests" in menu_choisi or "Intereses" in menu_choisi or "Isenfaren" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["interets"]}</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (ic, nom_interet) in enumerate(t["interets"]):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="contact-card">
                    <div class="contact-icon">{ic}</div>
                    <div class="contact-title">{nom_interet}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif menu_choisi.startswith("📞") or "Contact" in menu_choisi or "Assaɣ" in menu_choisi:
    st.markdown(f'<div class="section-title">{t["sections"]["contact"]}</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"""
            <div class="contact-card">
                <div class="contact-icon">📞</div>
                <div class="contact-title">{t["labels"]["tel"]}</div>
                <div class="contact-value">{telephone}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""
            <div class="contact-card">
                <div class="contact-icon">✉️</div>
                <div class="contact-title">{t["labels"]["email"]}</div>
                <div class="contact-value">{email}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f"""
            <div class="contact-card">
                <div class="contact-icon">📍</div>
                <div class="contact-title">{t["labels"]["adresse_title"]}</div>
                <div class="contact-value">{adresse}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
