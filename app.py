import streamlit as st

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Hamidouche Redjdal | CV",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fa;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ================= HEADER ================= */

.cv-header {
    background: linear-gradient(135deg, #102a43, #1f5f8b);
    border-radius: 24px;
    padding: 45px 50px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 12px 35px rgba(16,42,67,0.20);
}

.header-name {
    font-size: 43px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.header-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 18px;
}

.header-subtitle {
    font-size: 15px;
    line-height: 1.9;
    opacity: 0.95;
}

/* ================= SECTION ================= */

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #102a43;
    margin-top: 25px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 3px solid #1f5f8b;
}

/* ================= CARDS ================= */

.card {
    background: white;
    border-radius: 17px;
    padding: 25px;
    margin-bottom: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.card-title {
    color: #102a43;
    font-size: 19px;
    font-weight: 800;
}

.card-text {
    color: #52606d;
    line-height: 1.8;
}

/* ================= EXPERIENCE ================= */

.experience-card {
    background: white;
    border-radius: 17px;
    padding: 25px;
    margin-bottom: 20px;
    border-left: 5px solid #1f5f8b;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.experience-position {
    color: #102a43;
    font-size: 20px;
    font-weight: 800;
}

.experience-company {
    color: #1f5f8b;
    font-weight: 700;
    margin-top: 5px;
}

.experience-date {
    color: #829ab1;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 15px;
}

.mission {
    color: #52606d;
    margin: 7px 0;
    line-height: 1.6;
}

/* ================= FORMATION ================= */

.education-card {
    background: white;
    border-radius: 17px;
    padding: 22px;
    margin-bottom: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.year {
    display: inline-block;
    background: #102a43;
    color: white;
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
}

.education-title {
    color: #102a43;
    font-weight: 800;
    font-size: 17px;
}

.education-school {
    color: #627d98;
    margin-top: 7px;
    font-size: 14px;
}

/* ================= TAGS ================= */

.tag {
    display: inline-block;
    padding: 9px 15px;
    margin: 4px;
    border-radius: 25px;
    background: #e9f2f9;
    color: #102a43;
    font-size: 14px;
    font-weight: 600;
}

/* ================= SKILLS ================= */

.skill-card {
    background: white;
    border-radius: 14px;
    padding: 17px;
    margin-bottom: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    color: #334e68;
}

/* ================= CONTACT ================= */

.contact-card {
    background: white;
    border-radius: 17px;
    padding: 25px;
    text-align: center;
    min-height: 150px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.contact-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.contact-title {
    color: #102a43;
    font-weight: 800;
    margin-bottom: 8px;
}

.contact-value {
    color: #52606d;
    font-size: 14px;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #829ab1;
    padding-top: 40px;
    font-size: 13px;
}

/* ================= SIDEBAR ================= */

[data-testid="stSidebar"] {
    background: #102a43;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* ================= MOBILE ================= */

@media (max-width: 768px) {

    .cv-header {
        padding: 30px 25px;
    }

    .header-name {
        font-size: 31px;
    }

    .header-title {
        font-size: 18px;
    }

    .section-title {
        font-size: 23px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DONNEES DU CV
# ============================================================

nom = "HAMIDOUCHE REDJDAL"

fonction = "Planificateur & Superviseur Logistique"

telephone = "00213775 73 79 30"

email = "hamidoucheredjdal@yahoo.fr"

adresse = "Tazmalt 06039, wilaya de Bejaia"

nationalite = "Algérienne"

situation = "Marié"

service_national = "Dégagé"


# ============================================================
# PROFIL
# ============================================================

profil = """
Dynamique, sérieux et ayant de bonnes compétences relationnelles,
avec 9 ans d'expérience dans le domaine de la logistique.

Très à l'aise avec les outils informatiques, je souhaite mettre
mes compétences et ma motivation au service d'une entreprise
et relever de nouveaux défis professionnels.
"""


# ============================================================
# EXPERIENCES
# ============================================================

experiences = [

    {
        "poste": "Superviseur techno-commercial",
        "date": "01/2024 - À ce jour",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Analyser les besoins des clients.",
            "Établir des reportings d'activité quotidiens, mensuels et annuels.",
            "Apporter des solutions pertinentes et adaptées.",
            "Suivre le bon déroulement de l'activité.",
            "Contrôler les flux entrants et sortants de la zone d'entreposage."
        ]
    },

    {
        "poste": "Superviseur exploitation",
        "date": "06/2022 - 01/2024",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Piloter et superviser les opérations de transport.",
            "Suivre le bon déroulement de l'activité.",
            "Contrôler les flux entrants et sortants de la zone d'entreposage.",
            "Planifier, organiser et contrôler l'activité d'une équipe.",
            "Réceptionner les commandes des clients et veiller à leur satisfaction.",
            "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus."
        ]
    },

    {
        "poste": "Chargé de la planification",
        "date": "02/2020 - 06/2022",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Préparer la disponibilité des ressources humaines et matérielles.",
            "Planifier les commandes de chaque client.",
            "Élaborer les reportings et les KPI liés à l'activité.",
            "Réceptionner et traiter les demandes de service commercial.",
            "Optimiser les ressources logistiques en termes de coûts et de délais.",
            "Administrer et générer les ordres de mission.",
            "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus."
        ]
    },

    {
        "poste": "Coordinateur logistique",
        "date": "02/2019 - 02/2020",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Élaborer et maintenir une parfaite coordination avec les autres services.",
            "Élaborer et mettre en place des indicateurs de suivi de transport.",
            "Gérer les partenariats avec les prestataires de transport.",
            "Piloter et contrôler les performances des activités à court, moyen et long terme.",
            "Veiller au respect des procédures de travail et à la réglementation."
        ]
    },

    {
        "poste": "Chargé de la programmation",
        "date": "04/2016 - 10/2018",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Exécuter et suivre régulièrement la programmation et l'utilisation des ressources.",
            "Établir un planning optimal en optimisant les coûts et les délais.",
            "Anticiper les situations imprévues et prendre rapidement les décisions correctives.",
            "Étudier la faisabilité d'une mission avant d'affecter les ressources."
        ]
    }
]


# ============================================================
# FORMATIONS
# ============================================================

formations = [

    (
        "2021",
        "Formation en Transport international des marchandises",
        "Chambre algérienne de commerce et d'industrie, Alger - Algérie"
    ),

    (
        "2020",
        "Formation en Planification et optimisation logistique",
        "Institut international de Management, Bejaia - Algérie"
    ),

    (
        "2019",
        "Formation en Logistique et transport",
        "Institut international de management, Bejaia - Algérie"
    ),

    (
        "2019",
        "Formation en Gestion des temps et des priorités",
        "Institut international de management, Bejaia - Algérie"
    ),

    (
        "2018",
        "Formation en Gestion des opérations de transport",
        "Institut international de management, Bejaia - Algérie"
    ),

    (
        "2015",
        "Master 2 en Recherche opérationnelle",
        "Option : fiabilité et évaluation des Performances des Réseaux — Université Abderrahmane Mira, Bejaia - Algérie"
    ),

    (
        "2012",
        "Licence en Recherche Opérationnelle",
        "Option : Aide à la décision — Université Abderrahmane Mira, Bejaia - Algérie"
    ),

    (
        "2012",
        "Attestation de stage en gestion portuaire",
        "Entreprise portuaire de Bejaia, Bejaia - Algérie"
    ),

    (
        "2008",
        "Diplôme Baccalauréat",
        "Option : Science de la nature et de la vie — Lycée Mohamed Boudiaf, Tazmalt - Algérie"
    )
]


# ============================================================
# COMPETENCES
# ============================================================

competences = [

    "Maîtrise du Pack Office : Excel, Word, PowerPoint, Outlook",

    "Maîtrise de Matlab, LaTeX, Photoshop, Illustrator et InDesign",

    "Langages de programmation : HTML, Java, Delphi, C++",

    "Planification des ressources",

    "Optimisation des coûts et des délais",

    "Gestion des opérations de transport",

    "Supervision des opérations de transport",

    "Élaboration des indicateurs de suivi",

    "Reporting d'activité",

    "Gestion des partenariats avec les prestataires",

    "Coordination entre les services",

    "Gestion des ordres de mission"
]


# ============================================================
# LANGUES
# ============================================================

langues = [
    "Kabyle",
    "Arabe",
    "Français",
    "Anglais"
]


# ============================================================
# CENTRES D'INTERET
# ============================================================

interets = [
    ("✈️", "Voyage"),
    ("⚽", "Passion pour le sport"),
    ("🤝", "Activités associatives"),
    ("🎬", "Cinéma"),
    ("🎨", "Arts créatifs"),
    ("💻", "Informatique")
]


# ============================================================
# HEADER PRINCIPAL
# ============================================================

st.markdown("""
<div class="cv-header">

    <div class="header-name">
        HAMIDOUCHE REDJDAL
    </div>

    <div class="header-title">
        🚚 Planificateur & Superviseur Logistique
    </div>

    <div class="header-subtitle">

        Master 2 en Recherche Opérationnelle
        <br><br>

        Logistique &nbsp; • &nbsp;
        Transport &nbsp; • &nbsp;
        Planification &nbsp; • &nbsp;
        Supervision &nbsp; • &nbsp;
        Optimisation

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding:10px 0 20px 0;
    ">
        <div style="font-size:45px;">🚚</div>

        <div style="
            font-size:20px;
            font-weight:800;
        ">
            HAMIDOUCHE REDJDAL
        </div>

        <div style="
            font-size:13px;
            margin-top:5px;
        ">
            CV PROFESSIONNEL
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "MENU",
    [
        "🏠 Accueil",
        "👤 Profil",
        "💼 Expériences",
        "🎓 Diplômes & Formations",
        "🛠️ Compétences",
        "🌐 Langues",
        "⭐ Centres d'intérêt",
        "📞 Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **DOMAINES**

    🚚 Transport

    📦 Logistique

    📊 Planification

    👥 Supervision

    📈 Optimisation
    """
)

# ============================================================
# ACCUEIL
# ============================================================

if page == "🏠 Accueil":

    st.markdown(
        "<div class='section-title'>Profil professionnel</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">

            <p class="card-text" style="font-size:17px;">
                {profil}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # INDICATEURS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Expérience", "9 ans")

    with col2:
        st.metric("Postes", "5")

    with col3:
        st.metric("Formations", "9")

    with col4:
        st.metric("Langues", "4")

    # --------------------------------------------------------
    # DOMAINES D'EXPERTISE
    # --------------------------------------------------------

    st.markdown(
        "<div class='section-title'>Domaines d'expertise</div>",
        unsafe_allow_html=True
    )

    domaines = [
        "Logistique",
        "Transport",
        "Planification",
        "Supervision",
        "Optimisation",
        "Reporting",
        "KPI",
        "Coordination",
        "Gestion des ressources"
    ]

    for domaine in domaines:
        st.markdown(
            f"<span class='tag'>✓ {domaine}</span>",
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # EXPERIENCE ACTUELLE
    # --------------------------------------------------------

    st.markdown(
        "<div class='section-title'>Expérience actuelle</div>",
        unsafe_allow_html=True
    )

    current = experiences[0]

    st.markdown(
        f"""
        <div class="experience-card">

            <div class="experience-position">
                {current["poste"]}
            </div>

            <div class="experience-company">
                🏢 {current["entreprise"]}
            </div>

            <div class="experience-date">
                📅 {current["date"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
    # --------------------------------------------------------
    # INDICATEURS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Expérience", "9 ans")

    with col2:
        st.metric("Postes", "5")

    with col3:
        st.metric("Formations", "9")

    with col4:
        st.metric("Langues", "4")

    # --------------------------------------------------------
    # EXPERTISE
    # --------------------------------------------------------


    # --------------------------------------------------------
    # POSTE ACTUEL
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Expérience actuelle</div>',
        unsafe_allow_html=True
    )

    current = experiences[0]

    st.markdown(
        f"""
        <div class="experience-card">

            <div class="experience-position">
                {current["poste"]}
            </div>

            <div class="experience-company">
                {current["entreprise"]}
            </div>

            <div class="experience-date">
                📅 {current["date"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PROFIL
# ============================================================

elif page == "👤 Profil":

    st.markdown(
        '<div class="section-title">👤 Profil professionnel</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">

            <p class="card-text" style="font-size:18px;">
                {profil}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Informations personnelles</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    👤 Identité
                </div>

                <br>

                <b>Nom</b>
                <p>{nom}</p>

                <b>Nationalité</b>
                <p>{nationalite}</p>

                <b>Situation familiale</b>
                <p>{situation}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    📋 Informations
                </div>

                <br>

                <b>Adresse</b>
                <p>{adresse}</p>

                <b>Service national</b>
                <p>{service_national}</p>

                <b>Fonction</b>
                <p>{fonction}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# EXPERIENCES
# ============================================================

elif page == "💼 Expériences":

    st.markdown(
        '<div class="section-title">💼 Expériences professionnelles</div>',
        unsafe_allow_html=True
    )

    for exp in experiences:

        st.markdown(
            f"""
            <div class="experience-card">

                <div class="experience-position">
                    {exp["poste"]}
                </div>

                <div class="experience-company">
                    🏢 {exp["entreprise"]}
                </div>

                <div class="experience-date">
                    📅 {exp["date"]}
                </div>

                <strong>Principales missions</strong>

                <div style="margin-top:12px;">
            """,
            unsafe_allow_html=True
        )

        for mission in exp["missions"]:

            st.markdown(
                f"""
                <div class="mission">
                    ✓ {mission}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FORMATIONS
# ============================================================

elif page == "🎓 Diplômes & Formations":

    st.markdown(
        '<div class="section-title">🎓 Diplômes & Formations</div>',
        unsafe_allow_html=True
    )

    for annee, titre, organisme in formations:

        st.markdown(
            f"""
            <div class="education-card">

                <div class="year">
                    {annee}
                </div>

                <div class="education-title">
                    {titre}
                </div>

                <div class="education-school">
                    🏫 {organisme}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# COMPETENCES
# ============================================================

elif page == "🛠️ Compétences":

    st.markdown(
        '<div class="section-title">🛠️ Compétences</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    for i, competence in enumerate(competences):

        target = col1 if i % 2 == 0 else col2

        with target:

            st.markdown(
                f"""
                <div class="skill-card">
                    <strong>✓</strong> {competence}
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# LANGUES
# ============================================================

elif page == "🌐 Langues":

    st.markdown(
        '<div class="section-title">🌐 Langues</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    for i, langue in enumerate(langues):

        with cols[i]:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">

                    <div style="font-size:35px;">
                        🌐
                    </div>

                    <div class="card-title">
                        {langue}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        "Le CV fourni indique les langues Kabyle, Arabe, "
        "Français et Anglais, mais ne précise pas le niveau "
        "de maîtrise de chacune."
    )


# ============================================================
# CENTRES D'INTERET
# ============================================================

elif page == "⭐ Centres d'intérêt":

    st.markdown(
        '<div class="section-title">⭐ Centres d'intérêt</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    for i, (icone, interet) in enumerate(interets):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">

                    <div style="font-size:40px;">
                        {icone}
                    </div>

                    <div class="card-title">
                        {interet}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# CONTACT
# ============================================================

elif page == "📞 Contact":

    st.markdown(
        '<div class="section-title">📞 Contact</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="contact-card">

                <div class="contact-icon">
                    📱
                </div>

                <div class="contact-title">
                    Téléphone
                </div>

                <div class="contact-value">
                    {telephone}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="contact-card">

                <div class="contact-icon">
                    📧
                </div>

                <div class="contact-title">
                    Email
                </div>

                <div class="contact-value">
                    {email}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="contact-card">

                <div class="contact-icon">
                    📍
                </div>

                <div class="contact-title">
                    Adresse
                </div>

                <div class="contact-value">
                    {adresse}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🚚 Disponibilité professionnelle
            </div>

            <p class="card-text">
                Profil orienté logistique, transport, planification,
                supervision et optimisation des opérations.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <strong>HAMIDOUCHE REDJDAL</strong>

        <br>

        Planificateur & Superviseur Logistique

        <br><br>

        Curriculum Vitae professionnel

    </div>
    """,
    unsafe_allow_html=True
)
