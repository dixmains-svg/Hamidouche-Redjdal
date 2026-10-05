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
# 2. DESIGN CSS PROFESSIONNEL ET HAUT DE GAMME
# ============================================================
# ============================================================
# 2. DESIGN CSS : CHAMP SÉLECTIONNÉ EN NOIR FONCÉ ET ÉCRITURE GRASSE
# ============================================================
st.markdown(
    """
    <style>
    /* Import police Google */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Fond global de l'application */
    .stApp { background-color: #F8FAFC; }
    .block-container { max-width: 1200px; padding-top: 25px; padding-bottom: 50px; }

    /* Titre du champ (label au-dessus) */
    div[data-testid="stSidebar"] label p {
        color: #F8FAFC !important;
        font-weight: 800 !important;
        font-size: 14px !important;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    /* 1. CHAMP DE SÉLECTION FERMÉ (Fond Noir + Écriture Blanche Grasse) */
    div[data-baseweb="select"] > div {
        background-color: #000000 !important;
        border: 2px solid #475569 !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2) !important;
    }

    /* Force le texte sélectionné en BLANC PUR et TRÈS GRAS */
    div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    /* Flèche du menu déroulant (Blanc pur) */
    div[data-baseweb="select"] svg {
        fill: #FFFFFF !important;
    }

    /* 2. MENU DÉROULANT OUVERT (Fond Blanc + Écriture Noire Grasse) */
    ul[data-baseweb="menu"] {
        background-color: #FFFFFF !important;
        border: 2px solid #CBD5E1 !important;
        border-radius: 8px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.15) !important;
    }

    /* Options dans la liste déroulante */
    ul[data-baseweb="menu"] li div,
    ul[data-baseweb="menu"] li span,
    ul[data-baseweb="menu"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        font-weight: 800 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Effet au survol de la souris dans la liste (Gris clair) */
    ul[data-baseweb="menu"] li:hover,
    ul[data-baseweb="menu"] li:hover * {
        background-color: #F1F5F9 !important;
        color: #2563EB !important;
        -webkit-text-fill-color: #2563EB !important;
    }

    /* Styles généraux de la Sidebar */
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

    /* Bouton Télécharger PDF */
    [data-testid="stSidebar"] button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        padding: 10px 16px !important;
    }

    /* Style En-tête CV */
    .cv-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        color: #FFFFFF;
        padding: 35px 40px;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
        border: 1px solid #334155;
    }
    .cv-name { font-size: 38px; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 8px; color: #FFFFFF; }
    .cv-title { font-size: 22px; font-weight: 600; margin-bottom: 16px; color: #38BDF8; }
    .cv-subtitle { font-size: 15px; line-height: 1.7; color: #94A3B8; }

    /* Titres de section */
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

    /* Cartes principales */
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

    /* Cartes d'expérience */
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

    /* Cartes compétences & contact */
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
        "experiences": [
            {
                "poste": "Superviseur techno-commercial", "periode": "01/2024 - À ce jour", "entreprise": "SPA TMF Logistics",
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
        "fonction": "Logistics Planner & Supervisor",
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
            "degree_subtitle": "Master 2 in Operational Research",
            "sub_keywords": "Logistics • Transport • Planning • Supervision • Optimization",
            "photo_missing": "Photo not found"
        },
        "domaines": [
            ("🚚", "Transport", "Organization, tracking, and supervision of transport operations."),
            ("📦", "Logistics", "Flow management, logistics operations, and resource allocation."),
            ("📅", "Planning", "Scheduling operations and planning human and material resources."),
            ("👥", "Supervision", "Team management and operational control."),
            ("📈", "Optimization", "Cost reduction, lead time improvement, and optimal resource usage."),
            ("📊", "Reporting", "Developing and tracking activity reports for management."),
            ("🎯", "KPI", "Implementation and monitoring of activity performance indicators."),
            ("🤝", "Coordination", "Inter-departmental coordination ensuring seamless operations."),
            ("⚙️", "Resource Management", "Preparation, assignment, and optimal allocation of resources."),
        ],
        "experiences": [
            {
                "poste": "Technical & Commercial Supervisor", "periode": "01/2024 - Present", "entreprise": "SPA TMF Logistics",
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
        "fonction": "Planificador y Supervisor Logístico",
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
            "degree_subtitle": "Máster 2 en Investigación Operativa",
            "sub_keywords": "Logística • Transporte • Planificación • Supervisión • Optimización",
            "photo_missing": "Foto no encontrada"
        },
        "domaines": [
            ("🚚", "Transporte", "Organización, seguimiento y supervisión de operaciones de transporte."),
            ("📦", "Logística", "Gestión de flujos, operaciones logísticas y recursos."),
            ("📅", "Planificación", "Programación de operaciones y planificación de recursos humanos y materiales."),
            ("👥", "Supervisión", "Gestión de equipos y control del desarrollo de las operaciones."),
            ("📈", "Optimización", "Búsqueda de soluciones para optimizar costes, plazos y recursos."),
            ("📊", "Reportes", "Elaboración y seguimiento de informes de actividad para la dirección."),
            ("🎯", "KPI", "Implementación y seguimiento de indicadores de rendimiento."),
            ("🤝", "Coordinación", "Coordinación interdepartamental para asegurar la continuidad operativa."),
            ("⚙️", "Gestión de Recursos", "Preparación, asignación y uso óptimo de los recursos disponibles."),
        ],
        "experiences": [
            {
                "poste": "Supervisor Técnico-Comercial", "periode": "01/2024 - Presente", "entreprise": "SPA TMF Logistics",
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
                    "Controlar el rendimiento operativo a corto, medio y largo plazo.",
                    "Garantizar el cumplimiento de los procedimientos y normativas.",
                ],
            },
            {
                "poste": "Responsable de Programación", "periode": "04/2016 - 10/2018", "entreprise": "SPA TMF Logistics",
                "missions": [
                    "Ejecutar y supervisar la programación y el uso de recursos.",
                    "Establecer una planificación óptima equilibrando costes y plazos.",
                    "Anticipar imprevistos y tomar decisiones correctivas con rapidez.",
                    "Estudiar la viabilidad de las misiones antes de asignar recursos.",
                ],
            },
        ],
        "formations": [
            {"annee": "2021", "titre": "Curso de Transporte Internacional de Mercancías", "organisme": "Cámara Argelina de Comercio e Industria, Argel - Argelia"},
            {"annee": "2020", "titre": "Curso de Planificación y Optimización Logística", "organisme": "Instituto Internacional de Management, Bejaia - Argelia"},
            {"annee": "2019", "titre": "Curso de Logística y Transporte", "organisme": "Instituto Internacional de Management, Bejaia - Argelia"},
            {"annee": "2019", "titre": "Curso de Gestión del Tiempo y Prioridades", "organisme": "Instituto Internacional de Management, Bejaia - Argelia"},
            {"annee": "2018", "titre": "Curso de Gestión de Operaciones de Transporte", "organisme": "Instituto Internacional de Management, Bejaia - Argelia"},
            {"annee": "2015", "titre": "Máster 2 en Investigación Operativa", "organisme": "Especialidad: Fiabilidad y Evaluación de Rendimiento de Redes. Universidad Abderrahmane Mira, Bejaia - Argelia"},
            {"annee": "2012", "titre": "Grado / Licenciatura en Investigación Operativa", "organisme": "Especialidad: Sistemas de Apoyo a la Toma de Decisiones. Universidad Abderrahmane Mira, Bejaia - Argelia"},
            {"annee": "2012", "titre": "Certificado de Prácticas en Gestión Portuaria", "organisme": "Autoridad Portuaria de Bejaia, Bejaia - Argelia"},
            {"annee": "2008", "titre": "Título de Bachillerato", "organisme": "Especialidad: Ciencias de la Naturaleza y de la Vida. Instituto Mohamed Boudiaf, Tazmalt - Argelia"},
        ],
        "competences": [
            "Dominio de MS Office: Excel, Word, PowerPoint y Outlook.",
            "Dominio de Matlab, LaTeX, Photoshop, Illustrator e InDesign.",
            "Lenguajes de programación: HTML, Java, Delphi y C++.",
            "Planificación y optimización de recursos.",
            "Gestión de operaciones de transporte.",
            "Supervisión de operaciones de transporte.",
            "Diseño e implementación de indicadores de seguimiento.",
            "Elaboración de informes y KPIs de actividad.",
            "Gestión de acuerdos con proveedores de transporte.",
            "Coordinación interdepartamental.",
            "Gestión de recursos humanos y materiales.",
            "Administración y emisión de órdenes de misión.",
        ],
        "langues": [
            ("Cabilio (Kabyle)", "Nativo / Excelente"),
            ("Árabe", "Nativo / Excelente"),
            ("Francés", "Avanzado / Fluido"),
            ("Inglés", "Intermedio"),
        ],
        "interets": [
            ("✈️", "Viajes"),
            ("⚽", "Pasión por el Deporte"),
            ("🤝", "Actividades Comunitarias"),
            ("🎬", "Cine"),
            ("🎨", "Artes Creativas"),
            ("💻", "Informática y Tecnología"),
        ]
    }
}

t = TEXTES[langue_choisie]

# ============================================================
# 4. GÉNÉRATION DU PDF
# ============================================================

def generer_pdf(filepath, data_langue):
    doc = SimpleDocTemplate(
        str(filepath),
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontSize=20, leading=24, textColor=colors.HexColor('#0F172A'), spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle', parent=styles['Normal'],
        fontSize=12, leading=16, textColor=colors.HexColor('#2563EB'), spaceAfter=12
    )
    section_heading = ParagraphStyle(
        'SectionHeading', parent=styles['Heading2'],
        fontSize=13, leading=16, textColor=colors.HexColor('#0F172A'), spaceBefore=10, spaceAfter=6
    )
    body_style = ParagraphStyle(
        'BodyTextCustom', parent=styles['Normal'],
        fontSize=9, leading=13, textColor=colors.HexColor('#334155')
    )

    story = []
    story.append(Paragraph(f"<b>{nom}</b>", title_style))
    story.append(Paragraph(f"<b>{data_langue['fonction']}</b>", subtitle_style))
    story.append(Paragraph(f"📞 {telephone} &nbsp;|&nbsp; ✉️ {email} &nbsp;|&nbsp; 📍 {adresse}", body_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563EB'), spaceAfter=12))

    story.append(Paragraph(data_langue['sections']['profil'].upper(), section_heading))
    story.append(Paragraph(data_langue['profil'], body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph(data_langue['sections']['exp'].upper(), section_heading))
    for exp in data_langue['experiences']:
        story.append(Paragraph(f"<b>{exp['poste']}</b> — <i>{exp['entreprise']}</i> ({exp['periode']})", body_style))
        for mission in exp['missions']:
            story.append(Paragraph(f"• {mission}", body_style))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 6))

    story.append(Paragraph(data_langue['sections']['form'].upper(), section_heading))
    for form in data_langue['formations']:
        story.append(Paragraph(f"<b>{form['annee']}</b> : {form['titre']} — <i>{form['organisme']}</i>", body_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 6))

    story.append(Paragraph(data_langue['sections']['comp'].upper(), section_heading))
    comp_text = ", ".join(data_langue['competences'])
    story.append(Paragraph(f"<b>{data_langue['sections']['comp']} :</b> {comp_text}", body_style))
    
    langues_text = ", ".join([f"{l} ({n})" for l, n in data_langue['langues']])
    story.append(Paragraph(f"<b>{data_langue['sections']['langues']} :</b> {langues_text}", body_style))

    doc.build(story)

generer_pdf(PDF_PATH, t)

# ============================================================
# 5. EN-TÊTE DU CV
# ============================================================

col_photo, col_header = st.columns([1, 4])

with col_photo:
    st.markdown('<div style="background: linear-gradient(135deg, #0F172A, #1E293B); padding: 20px; border-radius: 16px; height: 100%; text-align: center; border: 1px solid #334155;">', unsafe_allow_html=True)
    if PHOTO.exists():
        st.image(str(PHOTO), width=180)
    else:
        st.markdown('<div style="font-size:90px; padding:20px;">👤</div>', unsafe_allow_html=True)
        st.warning(t["labels"]["photo_missing"])
    st.markdown("</div>", unsafe_allow_html=True)

with col_header:
    st.markdown(
        f"""
        <div class="cv-header">
            <div class="cv-name">{nom}</div>
            <div class="cv-title">👨‍💼 {t['fonction']}</div>
            <div class="cv-subtitle">
                {t['labels']['degree_subtitle']}
                <br><br>
                {t['labels']['sub_keywords']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# 6. SIDEBAR ET NAVIGATION
# ============================================================

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"""
    <div style="text-align:center; padding:10px 0px;">
        <div style="font-size:35px;">👨‍💼</div>
        <div style="font-size:18px; font-weight:800; color:white;">{nom}</div>
        <div style="font-size:12px; color:#94A3B8;">CURRICULUM VITAE</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if PDF_PATH.exists():
    with open(PDF_PATH, "rb") as f:
        pdf_bytes = f.read()

    st.sidebar.download_button(
        label=t["download_btn"],
        data=pdf_bytes,
        file_name="CV_HAMIDOUCHE_REDJDAL.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

st.sidebar.markdown("---")
page = st.sidebar.radio(t["nav_title"], t["nav"])
st.sidebar.markdown("---")
st.sidebar.markdown(t["sidebar_domains"])

# ============================================================
# 7. CONTENU PRINCIPAL
# ============================================================

if page in ["🏠 Accueil", "🏠 Home", "🏠 Inicio"]:
    st.markdown(f"<div class='section-title'>{t['sections']['profil']}</div>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><p class="card-text">{t["profil"]}</p></div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    experience_value = "09 Ans" if langue_choisie == "Français" else ("09 Años" if langue_choisie == "Español" else "09 Yrs")
    with col1: st.metric(t["labels"]["stat_exp"], experience_value)
    with col2: st.metric(t["labels"]["stat_postes"], len(t["experiences"]))
    with col3: st.metric(t["labels"]["stat_form"], len(t["formations"]))
    with col4: st.metric(t["labels"]["stat_langues"], len(t["langues"]))

    st.markdown(f"<div class='section-title'>{t['sections']['expertise']}</div>", unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, (icon, title, desc) in enumerate(t["domaines"]):
        with cols[idx % 3]:
            st.markdown(f'<div class="card"><div class="card-title">{icon} {title}</div><p class="card-text">{desc}</p></div>', unsafe_allow_html=True)

elif page in ["👤 Profil", "👤 Profile", "👤 Perfil"]:
    st.markdown(f"<div class='section-title'>{t['sections']['identite']}</div>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f'<div class="card"><div class="card-title">{t["labels"]["nom"]}</div><p class="card-text">{nom}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><div class="card-title">{t["labels"]["nationalite"]}</div><p class="card-text">{t["nationalite"]}</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown(f'<div class="card"><div class="card-title">{t["labels"]["situation"]}</div><p class="card-text">{t["situation"]}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><div class="card-title">{t["labels"]["service"]}</div><p class="card-text">{t["service_national"]}</p></div>', unsafe_allow_html=True)

elif page in ["💼 Expériences", "💼 Experience", "💼 Experiencia"]:
    st.markdown(f"<div class='section-title'>{t['sections']['exp']}</div>", unsafe_allow_html=True)
    for exp in t["experiences"]:
        missions_html = "".join([f"<div class='mission'>• {m}</div>" for m in exp["missions"]])
        st.markdown(
            f"""
            <div class="experience-card">
                <div class="experience-position">{exp['poste']}</div>
                <div class="experience-company">🏢 {exp['entreprise']}</div>
                <div class="experience-date">📅 {exp['periode']}</div>
                <div style="font-weight:700; color:#0F172A; margin-top:10px;">{t['labels']['missions']} :</div>
                {missions_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

elif page in ["🎓 Diplômes & Formations", "🎓 Education & Training", "🎓 Educación y Formación"]:
    st.markdown(f"<div class='section-title'>{t['sections']['form']}</div>", unsafe_allow_html=True)
    for form in t["formations"]:
        st.markdown(
            f"""
            <div class="card">
                <span style="background-color:#0F172A; color:#FFFFFF; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700;">{form['annee']}</span>
                <div class="card-title" style="margin-top:10px;">{form['titre']}</div>
                <div style="color:#64748B; font-size:14px; font-weight:600;">📍 {form['organisme']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif page in ["🛠️ Compétences", "🛠️ Skills", "🛠️ Habilidades"]:
    st.markdown(f"<div class='section-title'>{t['sections']['comp']}</div>", unsafe_allow_html=True)
    cols = st.columns(2)
    for idx, comp in enumerate(t["competences"]):
        with cols[idx % 2]:
            st.markdown(f'<div class="skill-card">✔ {comp}</div>', unsafe_allow_html=True)

elif page in ["🌐 Langues", "🌐 Languages", "🌐 Idiomas"]:
    st.markdown(f"<div class='section-title'>{t['sections']['langues']}</div>", unsafe_allow_html=True)
    cols = st.columns(2)
    for idx, (langue, niveau) in enumerate(t["langues"]):
        with cols[idx % 2]:
            st.markdown(f'<div class="card"><div class="card-title">🗣️ {langue}</div><p class="card-text">{niveau}</p></div>', unsafe_allow_html=True)

elif page in ["⭐ Centres d'intérêt", "⭐ Interests", "⭐ Intereses"]:
    st.markdown(f"<div class='section-title'>{t['sections']['interets']}</div>", unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, (icon, interet) in enumerate(t["interets"]):
        with cols[idx % 3]:
            st.markdown(f'<div class="card" style="text-align:center;"><div style="font-size:35px;">{icon}</div><div class="card-title" style="margin-top:10px; font-size:18px;">{interet}</div></div>', unsafe_allow_html=True)

elif page in ["📞 Contact", "📞 Contacto"]:
    st.markdown(f"<div class='section-title'>{t['sections']['contact']}</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="contact-card"><div class="contact-icon">📞</div><div class="contact-title">{t["labels"]["tel"]}</div><div class="contact-value">{telephone}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="contact-card"><div class="contact-icon">✉️</div><div class="contact-title">{t["labels"]["email"]}</div><div class="contact-value">{email}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="contact-card"><div class="contact-icon">📍</div><div class="contact-title">{t["labels"]["adresse_title"]}</div><div class="contact-value">{adresse}</div></div>', unsafe_allow_html=True)
