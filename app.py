import streamlit as st
from datetime import datetime
from io import BytesIO

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CV - Hamidouche Redjdal",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>
    .stApp {
        background: #f4f7fb;
    }

    .hero {
        background: linear-gradient(135deg, #0f2747, #1e5a91);
        color: white;
        padding: 35px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(15,39,71,.15);
    }

    .hero h1 {
        font-size: 42px;
        margin: 0 0 8px 0;
        font-weight: 800;
    }

    .hero h3 {
        margin: 0;
        font-weight: 400;
        opacity: .95;
    }

    .contact-card {
        background: white;
        padding: 18px;
        border-radius: 15px;
        border-left: 5px solid #1e5a91;
        box-shadow: 0 4px 15px rgba(0,0,0,.06);
        margin-bottom: 15px;
    }

    .section-title {
        color: #0f2747;
        font-size: 26px;
        font-weight: 800;
        border-bottom: 3px solid #1e5a91;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    .timeline {
        background: white;
        border-radius: 15px;
        padding: 20px 25px;
        margin-bottom: 15px;
        border-left: 5px solid #1e5a91;
        box-shadow: 0 4px 15px rgba(0,0,0,.06);
    }

    .job-title {
        color: #0f2747;
        font-size: 20px;
        font-weight: 800;
    }

    .company {
        color: #1e5a91;
        font-weight: 700;
    }

    .period {
        color: #666;
        font-size: 14px;
        font-weight: 600;
    }

    .skill {
        background: white;
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 10px;
        box-shadow: 0 3px 12px rgba(0,0,0,.05);
    }

    .education {
        background: white;
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,.06);
    }

    .education-year {
        display: inline-block;
        background: #0f2747;
        color: white;
        border-radius: 20px;
        padding: 5px 12px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .tag {
        display: inline-block;
        background: #e8f1fa;
        color: #0f2747;
        border-radius: 20px;
        padding: 7px 13px;
        margin: 4px;
        font-weight: 600;
        font-size: 14px;
    }

    .footer {
        text-align: center;
        color: #777;
        padding: 30px 0 10px 0;
        font-size: 13px;
    }

    @media print {
        .stSidebar, [data-testid="stSidebar"], .stButton {
            display: none !important;
        }

        .stApp {
            background: white;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DONNEES DU CV
# Source: CV_redjdal.docx fourni par l'utilisateur
# ============================================================

CV = {
    "nom": "HAMIDOUCHE REDJDAL",
    "titre": "Planificateur et Superviseur Logistique",
    "profil": (
        "Dynamique, sérieux et ayant de bonnes compétences relationnelles, "
        "avec 9 ans d'expérience dans le domaine de la logistique. "
        "Je suis très à l'aise avec les outils informatiques et j'aimerais "
        "mettre mes compétences et ma motivation au service de votre entreprise. "
        "Je suis prêt à relever le défi."
    ),
    "telephone": "00213775 73 79 30",
    "email": "hamidoucheredjdal@yahoo.fr",
    "adresse": "Tazmalt 06039, wilaya de Bejaia",
    "nationalite": "Algérienne",
    "situation": "Marié",
    "service_national": "Dégagé",
    "experiences": [
        {
            "poste": "Superviseur techno-commercial",
            "periode": "01/2024 - à ce jour",
            "entreprise": "SPA TMF Logistics",
            "missions": [
                "Analyser les besoins des clients.",
                "Établir des reporting d'activité quotidiens, mensuels et annuels.",
                "Apporter des solutions pertinentes et adaptées.",
                "Suivi le bon déroulement de l'activité.",
                "Contrôler les flux entrants et sortants de la zone d'entreposage.",
            ],
        },
        {
            "poste": "Superviseur exploitation",
            "periode": "06/2022 - 01/2024",
            "entreprise": "SPA TMF Logistics",
            "missions": [
                "Piloter et superviser les opérations de transport.",
                "Suivi le bon déroulement de l’activité.",
                "Contrôler les flux entrants et sortants de la zone d'entreposage.",
                "Planifier, organiser et contrôler l'activité d'une équipe.",
                "Réceptionner les commandes des clients et veiller à leur satisfaction.",
                "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus.",
            ],
        },
        {
            "poste": "Chargé de la planification",
            "periode": "02/2020 - 06/2022",
            "entreprise": "SPA TMF Logistics",
            "missions": [
                "Préparer la disponibilité des ressources humaines et matérielles.",
                "Planifier les commandes de chaque client.",
                "Élaborer les reportings et les KPI's liés à l'activité.",
                "Réceptionner et traiter les demandes de service commercial.",
                "Optimiser les ressources logistiques en termes des coûts et des délais.",
                "Administrer et générer les ordres de mission.",
                "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus et de l'environnement externe.",
            ],
        },
        {
            "poste": "Coordinateur logistique",
            "periode": "02/2019 - 02/2020",
            "entreprise": "SPA TMF Logistics",
            "missions": [
                "Élaborer et maintenir une parfaite coordination avec d'autres services.",
                "Élaborer et mettre en place des indicateurs de suivi de transport.",
                "Gérer les partenariats avec les prestataires de transport.",
                "Piloter et contrôler les performances des activités à court, moyen et long terme.",
                "Veiller au respect des procédures de travail et à la réglementation.",
            ],
        },
        {
            "poste": "Chargé de la programmation",
            "periode": "04/2016 - 10/2018",
            "entreprise": "SPA TMF Logistics",
            "missions": [
                "Exécuter et suivre régulièrement la programmation et l'utilisation des ressources.",
                "Établir un planning optimal, en optimisant les coûts et les délais.",
                "Anticiper les situations imprévues et prendre rapidement les décisions correctives.",
                "Étudier la faisabilité d'une mission avant d'affecter les ressources.",
            ],
        },
    ],
    "formations": [
        ("2021", "Formation en Transport international des marchandises", "Chambre algérienne de commerce et d'industrie, Alger - Algérie"),
        ("2020", "Formation en Planification et optimisation logistique", "Institut international de Management, Bejaia - Algérie"),
        ("2019", "Formation en Logistique et transport", "Institut international de management, Bejaia - Algérie"),
        ("2019", "Formation en Gestion des temps et des priorités", "Institut international de management, Bejaia - Algérie"),
        ("2018", "Formation en Gestion des opérations de transport", "Institut international de management, Bejaia - Algérie"),
        ("2015", "Master 2 en Recherche opérationnel - Option : fiabilité et évaluation des Performances des Réseaux", "Université Abderrahmane Mira, Bejaia - Algérie"),
        ("2012", "Licence en Recherche Opérationnel - Option : Aide à la décision", "Université Abderrahmane Mira, Bejaia - Algérie"),
        ("2012", "Attestation de stage en gestion portuaire", "Entreprise portuaire de Bejaia, Bejaia - Algérie"),
        ("2008", "Diplôme Baccalauréat - Option : Science de la nature et de la vie", "Lycée Mohamed Boudiaf, Tazmalt - Algérie"),
    ],
    "competences": [
        "Maîtrise du Pack Office : Excel, Word, PowerPoint, Outlook",
        "Maîtrise de Matlab",
        "Maîtrise de LaTeX",
        "Photoshop",
        "Illustrator",
        "InDesign",
        "Langages de programmation : HTML, Java, Delphi, C++",
        "Planification et optimisation logistique",
        "Gestion des opérations de transport",
        "Reporting et KPI",
        "Gestion des ressources logistiques",
        "Supervision des opérations de transport",
    ],
    "langues": ["Kabyle", "Arabe", "Français", "Anglais"],
    "interets": [
        "Voyage",
        "Passion pour le sport",
        "Activités associatives",
        "Cinéma",
        "Arts créatifs",
        "Informatique",
    ],
}

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## 📄 Mon CV")
    st.markdown("---")

    section = st.radio(
        "Navigation",
        [
            "🏠 Accueil",
            "👤 Profil",
            "💼 Expériences",
            "🎓 Formations",
            "🛠️ Compétences",
            "🌐 Langues",
            "⭐ Centres d'intérêt",
            "📞 Contact",
        ],
    )

    st.markdown("---")
    st.markdown("### 📌 Informations")
    st.write("**Nom :**", CV["nom"])
    st.write("**Fonction :**", CV["titre"])
    st.write("**Domaine :** Logistique & Transport")

# ============================================================
# HEADER
# ============================================================

st.markdown(
    f"""
    <div class="hero">
        <h1>{CV["nom"]}</h1>
        <h3>🚚 {CV["titre"]}</h3>
        <p style="margin-top:15px; font-size:17px;">
            Logistique • Transport • Planification • Supervision • Optimisation
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# ACCUEIL
# ============================================================

if section == "🏠 Accueil":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Expérience indiquée dans le CV", "9 ans")

    with col2:
        st.metric("Expériences professionnelles", "5")

    with col3:
        st.metric("Formations & diplômes", "9")

    st.markdown('<div class="section-title">👤 Profil professionnel</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="contact-card">
            <p style="font-size:17px; line-height:1.8;">
                {CV["profil"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">🎯 Domaines d’expertise</div>', unsafe_allow_html=True)

    tags = [
        "Planification logistique",
        "Transport",
        "Supervision",
        "Optimisation",
        "KPI & Reporting",
        "Gestion des ressources",
        "Ordres de mission",
        "Relation client",
    ]

    st.markdown(
        "".join([f'<span class="tag">{tag}</span>' for tag in tags]),
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">💼 Parcours professionnel</div>', unsafe_allow_html=True)

    for exp in CV["experiences"]:
        st.markdown(
            f"""
            <div class="timeline">
                <div class="job-title">{exp["poste"]}</div>
                <div class="company">{exp["entreprise"]}</div>
                <div class="period">📅 {exp["periode"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# PROFIL
# ============================================================

elif section == "👤 Profil":

    st.markdown('<div class="section-title">👤 Profil professionnel</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="contact-card">
            <p style="font-size:18px; line-height:1.9;">
                {CV["profil"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">📌 Informations personnelles</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.write("**Nom et prénom :**", CV["nom"])
        st.write("**Nationalité :**", CV["nationalite"])
        st.write("**Situation familiale :**", CV["situation"])

    with c2:
        st.write("**Adresse :**", CV["adresse"])
        st.write("**Situation vis-à-vis du service national :**", CV["service_national"])
        st.write("**Fonction :**", CV["titre"])

# ============================================================
# EXPERIENCES
# ============================================================

elif section == "💼 Expériences":

    st.markdown('<div class="section-title">💼 Expériences professionnelles</div>', unsafe_allow_html=True)

    for i, exp in enumerate(CV["experiences"], start=1):

        with st.container():
            st.markdown(
                f"""
                <div class="timeline">
                    <div class="job-title">{i}. {exp["poste"]}</div>
                    <div class="company">🏢 {exp["entreprise"]}</div>
                    <div class="period">📅 {exp["periode"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("**Principales missions :**")

            for mission in exp["missions"]:
                st.markdown(f"- {mission}")

            st.markdown("---")

# ============================================================
# FORMATIONS
# ============================================================

elif section == "🎓 Formations":

    st.markdown('<div class="section-title">🎓 Diplômes et formations</div>', unsafe_allow_html=True)

    for annee, diplome, organisme in CV["formations"]:
        st.markdown(
            f"""
            <div class="education">
                <div class="education-year">{annee}</div>
                <div style="font-size:18px;font-weight:800;color:#0f2747;">
                    {diplome}
                </div>
                <div style="margin-top:8px;color:#555;">
                    🏫 {organisme}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# COMPETENCES
# ============================================================

elif section == "🛠️ Compétences":

    st.markdown('<div class="section-title">🛠️ Compétences professionnelles et informatiques</div>', unsafe_allow_html=True)

    for competence in CV["competences"]:
        st.markdown(
            f"""
            <div class="skill">
                ✅ {competence}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# LANGUES
# ============================================================

elif section == "🌐 Langues":

    st.markdown('<div class="section-title">🌐 Langues</div>', unsafe_allow_html=True)

    cols = st.columns(4)

    for col, langue in zip(cols, CV["langues"]):
        with col:
            st.markdown(
                f"""
                <div class="contact-card" style="text-align:center;">
                    <div style="font-size:35px;">🌐</div>
                    <strong>{langue}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.info(
        "Le CV fourni mentionne les langues Kabyle, Arabe, Français et Anglais, "
        "sans préciser les niveaux de maîtrise."
    )

# ============================================================
# CENTRES D'INTERET
# ============================================================

elif section == "⭐ Centres d'intérêt":

    st.markdown('<div class="section-title">⭐ Centres d’intérêt</div>', unsafe_allow_html=True)

    cols = st.columns(3)

    icons = ["✈️", "⚽", "🤝", "🎬", "🎨", "💻"]

    for i, interet in enumerate(CV["interets"]):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="contact-card" style="text-align:center;">
                    <div style="font-size:35px;">{icons[i]}</div>
                    <strong>{interet}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ============================================================
# CONTACT
# ============================================================

elif section == "📞 Contact":

    st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="contact-card">
            <h3>📱 Téléphone</h3>
            <p>{CV["telephone"]}</p>
        </div>

        <div class="contact-card">
            <h3>📧 Email</h3>
            <p>{CV["email"]}</p>
        </div>

        <div class="contact-card">
            <h3>📍 Adresse</h3>
            <p>{CV["adresse"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Curriculum Vitae • Hamidouche Redjdal<br>
        Planification • Logistique • Transport • Supervision
    </div>
    """,
    unsafe_allow_html=True,
)
