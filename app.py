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

# Ajout de Español dans la liste déroulante
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
            ("📊", "Reportes", "El
