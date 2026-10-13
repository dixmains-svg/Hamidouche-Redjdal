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
# 3. SÉLECTION DE LA LANGUE
# ============================================================

langue_choisie = st.sidebar.selectbox("🌐 Langue / Language / Idioma", ["Français", "English", "Español"])

# ============================================================
# 4. BASE DE DONNÉES MULTILINGUE
# ============================================================

TEXTES = {
    "Français": {
        "fonction": "Responsable Section Port et Manutention",
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
            "keywords": ["🚚 Logistique & Transport", "📅 Planification", "👥 Supervision", "📈 Optimisation", "📊 Analyse des données", "⚓ Port & Manutention"],
            "poles": "Gestion Portuaire & Opérations de Manutention, Flotte Roulante, Entreposage & Fret",
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
                "poste": "Responsable Section Port et Manutention", "periode": "08/2026 - À ce jour", "entreprise": "SPA TMF Logistics",
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
                    "Anticipar les situations imprévues et prendre rapidement les décisions correctives.",
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
            {"annee": "2012", "titre": "Attestation de stage en gestion portuaire", "organisme": "Entreprise portuaire de Bejaia, Bejaia - Algérie"},
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
        "fonction": "Port and Handling Section Manager",
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
            "keywords": ["🚚 Logistics & Transport", "📅 Planning", "👥 Supervision", "📈 Optimization", "📊 Data Analysis", "⚓ Port & Handling"],
            "poles": "Port Management & Handling Operations, Rolling Fleet, Warehousing & Freight",
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
                "poste": "Port and Handling Section Manager", "periode": "08/2026 - Present", "entreprise": "SPA TMF Logistics",
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
            {"annee": "2012", "titre": "Port Management Internship Certificate", "organisme": "Bejaia Port Authority, Bejaia - Algeria"},
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
        "fonction": "Responsable de Sección Puerto y Manipulación",
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
            "keywords": ["🚚 Logística y Transporte", "📅 Planificación", "👥 Supervisión", "📈 Optimización", "📊 Análisis de Datos", "⚓ Puerto y Manipulación"],
            "poles": "Gestión Portuaria y Operaciones de Manipulación, Parque Móvil, Almacenamiento y Carga",
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
            ("🤝", "Coordinación", "Coordinación interdepartamental para asegurar la continuidad operativa."),
            ("⚙️", "Gestión de Recursos", "Preparación, asignación y uso óptimo de los recursos disponibles."),
        ],
        "experiences": [
            {
                "poste": "Responsable de Sección Puerto y Manipulación", "periode": "08/2026 - Presente", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Optimización y planificación de flujos de transporte.",
                    "Control y supervisión dinámica de la flota en tiempo real.",
                    "Supervisión de operaciones de transporte y manipulación.",
                    "Gestión de imprevistos, control de presencia y trazabilidad de la carga.",
                    "Gestión operativa y transmisión de directrices (Órdenes de Misión).",
                    "Gestión técnico-operativa del parque móvil.",
                    "Control y validación de tiempos de servicio.",
                    "Seguimiento de indicadores clave de rendimiento (KPI)."
                ],
            },
            {
                "poste": "Supervisor Técnico-Comercial", "periode": "01/2024 - 08/2026", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Analizar las necesidades de los clientes.",
                    "Elaborar informes de actividad diarios, mensuales y anuales.",
                    "Aportar soluciones logísticas pertinentes y adaptadas.",
                    "Supervisar el correcto desarrollo de la actividad.",
                    "Controlar los flujos de entrada y salida de las zonas de almacenamiento.",
                ],
            },
            {
                "poste": "Supervisor de Operaciones", "periode": "06/2022 - 01/2024", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Liderar y supervisar las operaciones de transporte.",
                    "Garantizar el correcto desarrollo de la actividad.",
                    "Controlar los flujos entrantes y salientes del almacén.",
                    "Planificar, organizar y controlar el trabajo del equipo.",
                    "Recibir pedidos de clientes y velar por su satisfacción.",
                    "Asegurar el cumplimiento del programa y adaptarlo a imprevistos.",
                ],
            },
            {
                "poste": "Responsable de Planificación", "periode": "02/2020 - 06/2022", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Preparar la disponibilidad de recursos humanos y materiales.",
                    "Planificar los pedidos de cada cliente.",
                    "Elaborar informes y KPIs relacionados con la actividad.",
                    "Recibir y procesar las solicitudes del departamento comercial.",
                    "Optimizar los recursos logísticos en términos de costes y plazos.",
                    "Emitir y gestionar las órdenes de misión.",
                    "Ajustar la programación operativa ante imprevistos.",
                ],
            },
            {
                "poste": "Coordinador Logístico", "periode": "02/2019 - 02/2020", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Mantener una coordinación fluida con los demás departamentos.",
                    "Diseñar e implementar indicadores de seguimiento del transporte.",
                    "Gestionar las alianzas con los proveedores de transporte.",
                    "Supervisar el rendimiento a corto, medio y largo plazo.",
                    "Garantizar el cumplimiento de los procedimientos y normativas.",
                ],
            },
            {
                "poste": "Responsable de Programación", "periode": "04/2016 - 10/2018", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Ejecutar y supervisar regularmente la programación y uso de recursos.",
                    "Establecer un planning óptimo equilibrando costes y plazos.",
                    "Anticipar situaciones imprevistas y tomar decisiones correctoras.",
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
            {"annee": "2012", "titre": "Licenciatura en Investigación Operativa", "organisme": "Opción: Sistemas de ayuda a la decisión. Universidad Abderrahmane Mira, Bejaia - Argelia"},
            {"annee": "2012", "titre": "Certificado de Prácticas en Gestión Portuaria", "organisme": "Autoridad Portuaria de Bejaia, Bejaia - Argelia"},
            {"annee": "2008", "titre": "Título de Bachillerato", "organisme": "Opción: Ciencias de la Naturaleza y de la Vida. Instituto Mohamed Boudiaf, Tazmalt - Argelia"},
        ],
        "competences": [
            "Dominio de Paquete Office: Excel, Word, PowerPoint y Outlook.",
            "Dominio de Matlab, LaTeX, Photoshop, Illustrator e InDesign.",
            "Lenguajes de programación: HTML, Java, Delphi y C++.",
            "Planificación y optimización de recursos.",
            "Gestión de operaciones de transporte.",
            "Supervisión de operaciones de transporte.",
            "Desarrollo e implementación de indicadores de transporte.",
            "Elaboración de informes y KPIs de actividad.",
            "Gestión de alianzas con proveedores de transporte.",
            "Coordinación interdepartamental.",
            "Gestión de recursos humanos y materiales.",
            "Gestión y emisión de órdenes de misión.",
        ],
        "langues": [
            ("Cabila", "Nativo / Excelente"),
            ("Árabe", "Nativo / Excelente"),
            ("Francés", "Fluido"),
            ("Inglés", "Intermedio"),
        ],
        "interets": [
            ("✈️", "Viajes"),
            ("⚽", "Pasión por el deporte"),
            ("🤝", "Actividades asociativas"),
            ("🎬", "Cine"),
            ("🎨", "Artes creativas"),
            ("💻", "Informática"),
        ]
    }
}

T = TEXTES[langue_choisie]

# ============================================================
# 5. GÉNÉRATEUR DE PDF (REPORTLAB)
# ============================================================

def generer_pdf():
    doc = SimpleDocTemplate(str(PDF_PATH), pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=22, textColor=colors.HexColor('#0F172A'), spaceAfter=4, fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Normal'], fontSize=12, textColor=colors.HexColor('#2563EB'), spaceAfter=15, fontName='Helvetica-Bold')
    section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#0F172A'), spaceBefore=12, spaceAfter=6, fontName='Helvetica-Bold')
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#334155'), spaceAfter=4, fontName='Helvetica')
    bold_style = ParagraphStyle('BoldStyle', parent=body_style, fontName='Helvetica-Bold')

    story.append(Paragraph(nom, title_style))
    story.append(Paragraph(f"{T['fonction']} | {telephone} | {email} | {adresse}", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563EB'), spaceAfter=10))

    # Profil
    story.append(Paragraph(T['sections']['profil'], section_style))
    story.append(Paragraph(T['profil'], body_style))
    story.append(Spacer(1, 8))

    # Expériences
    story.append(Paragraph(T['sections']['exp'], section_style))
    for exp in T['experiences']:
        story.append(Paragraph(f"<b>{exp['poste']}</b> — {exp['entreprise']} ({exp['periode']})", bold_style))
        for m in exp['missions']:
            story.append(Paragraph(f"• {m}", body_style))
        story.append(Spacer(1, 4))

    # Formations
    story.append(Paragraph(T['sections']['form'], section_style))
    for f in T['formations']:
        story.append(Paragraph(f"<b>{f['annee']}</b> : {f['titre']} — <font color='#64748B'>{f['organisme']}</font>", body_style))

    doc.build(story)

if not PDF_PATH.exists():
    try:
        generer_pdf()
    except Exception:
        pass

# ============================================================
# 6. INTERFACE GRAPHIQUE STREAMLIT
# ============================================================

with st.sidebar:
    st.markdown("---")
    if PDF_PATH.exists():
        with open(PDF_PATH, "rb") as f:
            st.download_button(label=T["download_btn"], data=f, file_name="cv_hamidouche_redjdal.pdf", mime="application/pdf")
    st.markdown("---")
    choix_menu = st.radio(T["nav_title"], T["nav"])
    st.markdown("---")
    st.markdown(T["sidebar_domains"])

# Accueil
if choix_menu == T["nav"][0]:
    col_header1, col_header2 = st.columns([1, 4])
    with col_header1:
        if PHOTO.exists():
            st.image(str(PHOTO), width=150)
        else:
            st.markdown('<div style="font-size:100px; text-align:center;">👨‍💼</div>', unsafe_allow_html=True)
    with col_header2:
        st.markdown(
            f"""
            <div class="cv-header">
                <div class="cv-name">{nom}</div>
                <div class="cv-title">{T['fonction']}</div>
                <div class="cv-subtitle">
                    📍 {adresse} &nbsp;&nbsp;|&nbsp;&nbsp; 📞 {telephone} &nbsp;&nbsp;|&nbsp;&nbsp; ✉️ {email}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="card"><div class="card-title">⏳ {T["labels"]["stat_exp"]}</div><div class="card-text"><b>9 ans</b></div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="card"><div class="card-title">💼 {T["labels"]["stat_postes"]}</div><div class="card-text"><b>6 postes</b></div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="card"><div class="card-title">🎓 {T["labels"]["stat_form"]}</div><div class="card-text" style="font-size:14px;"><b>{T["labels"]["degree_stat"]}</b></div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="card"><div class="card-title">🌐 {T["labels"]["stat_langues"]}</div><div class="card-text"><b>4 langues</b></div></div>', unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">{T["sections"]["profil"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card"><div class="card-text">{T["profil"]}</div></div>', unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">{T["sections"]["expertise"]}</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (icon, titre, desc) in enumerate(T["domaines"]):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="card">
                    <div style="font-size:24px; margin-bottom:8px;">{icon}</div>
                    <div class="card-title">{titre}</div>
                    <div class="card-text" style="font-size:13px; color:#64748B;">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Profil
elif choix_menu == T["nav"][1]:
    st.markdown(f'<div class="section-title">{T["sections"]["identite"]}</div>', unsafe_allow_html=True)
    c_photo, c_info1, c_info2 = st.columns([1, 2, 2])
    with c_photo:
        if PHOTO.exists():
            st.image(str(PHOTO), width=160)
        else:
            st.markdown('<div style="font-size:100px; text-align:center;">👨‍💼</div>', unsafe_allow_html=True)
    with c_info1:
        st.markdown(
            f"""
            <div class="card">
                <p><b>{T["labels"]["nom"]} :</b> {nom}</p>
                <p><b>{T["labels"]["nationalite"]} :</b> {T["nationalite"]}</p>
                <p><b>{T["labels"]["situation"]} :</b> {T["situation"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c_info2:
        st.markdown(
            f"""
            <div class="card">
                <p><b>{T["labels"]["fonction"]} :</b> {T["fonction"]}</p>
                <p><b>{T["labels"]["adresse"]} :</b> {adresse}</p>
                <p><b>{T["labels"]["service"]} :</b> {T["service_national"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(f'<div class="section-title">{T["sections"]["infos_pro"]}</div>', unsafe_allow_html=True)
    
    # Génération des Badges
    badges_html = "".join([f'<span class="badge-chip">{kw}</span>' for kw in T["labels"]["keywords"]])
    valeurs_html = "".join([f"<li style='margin-bottom:6px;'>{val}</li>" for val in T["labels"]["valeurs"]])

    st.markdown(
        f"""
        <div class="card">
            <div style="font-size:18px; font-weight:800; color:#0F172A; margin-bottom:10px;">
                <b>{T["labels"]["fonction"]}</b> chez <b>SPA TMF Logistics</b>
            </div>
            <div style="margin-bottom:15px;">
                {badges_html}
            </div>
            <div class="card-text" style="border-top: 1px solid #E2E8F0; padding-top:12px; margin-top:8px;">
                <p><b>📌 Pôles d'intervention :</b> {T["labels"]["poles"]}</p>
                <p style="margin-top:10px; margin-bottom:6px;"><b>🎯 Périmètre Opérationnel & Valeur Ajoutée :</b></p>
                <ul style="padding-left:20px; color:#334155;">
                    {valeurs_html}
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Expériences
elif choix_menu == T["nav"][2]:
    st.markdown(f'<div class="section-title">{T["sections"]["exp"]}</div>', unsafe_allow_html=True)
    for exp in T["experiences"]:
        missions_html = "".join([f"<div class='mission'>• {m}</div>" for m in exp["missions"]])
        st.markdown(
            f"""
            <div class="experience-card">
                <div class="experience-position">{exp['poste']}</div>
                <div class="experience-company">🏢 {exp['entreprise']}</div>
                <div class="experience-date">📅 {exp['periode']}</div>
                <div style="margin-top:10px; font-weight:700; color:#0F172A; font-size:14px;">{T["labels"]["missions"]} :</div>
                {missions_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Diplômes & Formations
elif choix_menu == T["nav"][3]:
    st.markdown(f'<div class="section-title">{T["sections"]["form"]}</div>', unsafe_allow_html=True)
    for form in T["formations"]:
        st.markdown(
            f"""
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div class="card-title" style="margin-bottom:0;">{form['titre']}</div>
                    <span style="background-color:#E0F2FE; color:#0369A1; padding:4px 10px; border-radius:20px; font-weight:700; font-size:13px;">{form['annee']}</span>
                </div>
                <div class="card-text" style="color:#64748B; margin-top:6px;">{form['organisme']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Compétences
elif choix_menu == T["nav"][4]:
    st.markdown(f'<div class="section-title">{T["sections"]["comp"]}</div>', unsafe_allow_html=True)
    for comp in T["competences"]:
        st.markdown(f'<div class="skill-card">✔️ {comp}</div>', unsafe_allow_html=True)

# Langues
elif choix_menu == T["nav"][5]:
    st.markdown(f'<div class="section-title">{T["sections"]["langues"]}</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (langue, niveau) in enumerate(T["langues"]):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">🌐 {langue}</div>
                    <div class="card-text" style="color:#2563EB; font-weight:700;">{niveau}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Centres d'intérêt
elif choix_menu == T["nav"][6]:
    st.markdown(f'<div class="section-title">{T["sections"]["interets"]}</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (icon, interet) in enumerate(T["interets"]):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <div style="font-size:32px; margin-bottom:8px;">{icon}</div>
                    <div class="card-title" style="font-size:16px;">{interet}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Contact
elif choix_menu == T["nav"][7]:
    st.markdown(f'<div class="section-title">{T["sections"]["contact"]}</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"""
            <div class="contact-card">
                <div class="contact-icon">📞</div>
                <div class="contact-title">{T["labels"]["tel"]}</div>
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
                <div class="contact-title">{T["labels"]["email"]}</div>
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
                <div class="contact-title">{T["labels"]["adresse_title"]}</div>
                <div class="contact-value">{adresse}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
