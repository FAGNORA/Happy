import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os


# CSS pour réduire l'espace en haut de la page
st.markdown(
    """
    <style>
    /* Réduire l'espace vide au sommet de la page */
    .main .block-container {
        padding-top: 0rem;  /* Ajuster la valeur pour personnaliser */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Définition de variable
# 1- Images
# Définition de variable
# 1- Images
logo_WHR = Image.open('WHR.gif')
image_Panneau= Image.open('photo test.gif')
Logo_internet = Image.open('Internet.jpeg')
bonheur= Image.open('Bonheur.gif')
bandeau= Image.open('bandeau.jpeg')

#2 - Daframe

#df=pd.read_csv("world-happiness-report.csv")
#df_2021=pd.read_csv("world-happiness-report-2021.csv")
#df_global = pd.read_csv("C:/Users/fatim/Documents/df_global.csv")
# Charger les fichiers CSV depuis GitHub
# Charger les fichiers CSV depuis GitHub
df = pd.read_csv("https://raw.githubusercontent.com/FAGNORA/Hapiness_World_Report/main/world-happiness-report.csv")
df_2021 = pd.read_csv("https://raw.githubusercontent.com/FAGNORA/Hapiness_World_Report/main/world-happiness-report-2021.csv")
df_global = pd.read_csv("https://raw.githubusercontent.com/FAGNORA/Hapiness_World_Report/main/df_global.csv")
# **************************************************************Création des pages et des titres************************
pages=["Introduction","Exploration", "DataVisualization", "Pré Processing", "Modélisation", "Conclusion"]
#***************************************************************** Sidebar***********************************************

# CSS pour réduire l'espace vide en haut de la sidebar
st.markdown(
    """
    <style>
    /* Réduire l'espace vide en haut de la sidebar */
    .css-1d391kg {  /* Classe qui gère le conteneur de la sidebar */
        padding-top: 0rem;  /* Ajuster cette valeur pour changer l'espace */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    f"""
    <div style="
        #border: 2px solid #b80691; 
        #padding: 0px; 
        #border-radius: 50px;
        #background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:#262730;font-size:30px">Sommaire</h3>
    """, unsafe_allow_html=True)
st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)
                    
new_image = logo_WHR.resize((150, 150))
st.sidebar.image(new_image)

 #Ajouter un lien
st.sidebar.markdown('[Lien vers le site du World Happiness Report](https://www.worldhappiness.report)')

page=st.sidebar.radio("Aller vers", pages)
#Cette partie met en forme la barre du coté
st.markdown("""
       <style>
         section[data-testid="stSidebar"] 
              {background-color: #faca2b;}
       </style>""", unsafe_allow_html=True) 
#Cette partie met en forme la barre du coté


# Texte à afficher
text = """
<span style="color:purple;">**Promotion Data-Analyst - Février 2024**<span>

"""

# Injection de CSS pour créer un encadré autour du texte
st.sidebar.markdown(
    f"""
    <div style="
        border: 2px solid #b80691; 
        padding: 10px; 
        border-radius: 25px;
        background-color: #f5b74c;
        text-align:center;">
        {text}
    """,
    unsafe_allow_html=True)

# *********************************************************************************************Début de la page d'Introduction###########
if page == pages[0] : 
    new_image = bandeau.resize((1200, 600))
    st.image(new_image)

    st.markdown(
    f"""
    <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Analyse World Hapiness Report de 2005 à 2021</h3>
    """, unsafe_allow_html=True)

# Titre principal pour l'introduction
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Contexte</h3>', unsafe_allow_html=True)
    st.markdown("""
         <p style="text-align: justify;font-size:15px;">
         Le World Happiness Report est une publication annuelle élaborée par les Nations Unies, qui mesure et analyse le bonheur et le bien-être dans le monde entier.
         Ce rapport fournit une évaluation comparative du bonheur dans différents pays en s'appuyant sur des enquêtes menées auprès de populations diverses. 
         Les résultats du rapport sont basés sur des indicateurs clés tels que la satisfaction de vie, le soutien social, les libertés personnelles, 
         et la perception de la corruption, parmi d'autres facteurs.
         Le World Happiness Report a pour objectif principal de mieux comprendre les facteurs qui contribuent au bien-être des individus et des sociétés. 
         En évaluant les niveaux de bonheur à l'échelle mondiale, il permet d'identifier les tendances, les défis et les opportunités pour améliorer la qualité de vie. 
         Ce rapport est une ressource précieuse pour les décideurs politiques, les chercheurs, et les organisations internationales, 
         offrant des insights qui peuvent guider les politiques publiques et les initiatives en faveur du bien-être humain.
         </p>
     """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Objectifs </h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        À travers ce projet, nous visons à explorer et analyser les éléments factuels disponibles concernant le bien-être et le bonheur à l’échelle mondiale. 
        Sans nécessiter de connaissances préalables spécifiques en psychologie ou en sociologie, notre objectif est de rendre accessibles à un public curieux et non spécialisé des analyses basées sur des données fiables et librement accessibles.
        Nous répondrons aux problématiques suivantes :
        Les données disponibles permettent-elles de confirmer les variations dans les niveaux de bonheur à travers les pays ? Quels sont les indicateurs clés de ces variations ?
        Quel est le degré de corrélation entre les facteurs socio-économiques, culturels et les niveaux de bonheur reportés par les citoyens ?
        Quelles sont les tendances et les prédictions pour les niveaux de bonheur dans les décennies à venir ?
        </p>
    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Classification du problème </h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Ces questions de recherche nous amèneront à utiliser la plupart des compétences acquises au cours de notre formation :
        Grâce aux outils de Data Analyse et de Dataviz, nous allons déplacer, explorer, nettoyer, fusionner, visualiser et analyser les données disponibles.
        Les tests statistiques, ainsi que les régressions linéaires et polynomiales, nous permettront d’établir et d’analyser les corrélations entre les divers facteurs et les niveaux de bonheur.
        Grâce au machine learning, nous construirons un modèle prédictif des tendances futures du bonheur à travers les différentes régions.
        Enfin, un travail de recherche approfondi sera réalisé pour vérifier l’adéquation de nos résultats avec les études et les rapports existants.
        </p>
    """, unsafe_allow_html=True)


# Fin de la page d'Introduction#############

# zz redimensionnser une Image
#new_image = logo_WHR.resize((200, 200))
#st.image(new_image)
# zz

#****************************************************************************   Fin de la page d'Introduction  ***************


# ___________________________________________________________________________   Début de la page Exploration   ________________

if page == pages[1] : 
    st.markdown(
    f"""
    <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Analyse World Hapiness Report de 2005 à 2021</h3>

    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)
# traitement des données

    #st.markdown('<h3 style="color:blue;">LES DONNEES</h3>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Source de nos données</h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Les données sont accessibles sur Kaggle en accès libre,
        
        </p>
    """, unsafe_allow_html=True)

# Ajouter un lien
    st.markdown('[Accédez aux données du World Happiness Dataset sur Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness)')
    st.markdown('<h3 style="color:purple;">Présentation des données</h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        world-happiness-report.csv regroupant les données d’un panel d'années de (2005 – 
        2020). 
        Le fichier world-happiness-report-2021.csv, contenant des données collectées pour 
        le Happiness Report pour l’année 2021.
        </p>
    """, unsafe_allow_html=True)

    #compteurs de lignes des tableaux pour les inserer dans le descriptif
    Nb_lignes,Nb_colonnes = df.shape
    Nb_lignes2021,Nb_colonnes2021 = df_2021.shape

    Intro_tableau = 'Veuillez choisir le Dataframe pour afficher les détails : '

    Tableau_1 = 'Fichier contenant les données entre 2005 à 2020'
    Tableau_2 = 'Fichier contenant les données de 2021'
    Tableaux = st.radio( Intro_tableau, (Tableau_1,Tableau_2))

    if Tableaux == Tableau_1 : 
   
   
        st.markdown('<h3 style="color:purple;"></h3>', unsafe_allow_html=True)
        st.markdown('<h5 style="color:purple;text-align:center;">world-happiness-report.csv</h5>', unsafe_allow_html=True)

        st.markdown(
    """
    Détail des colonnes du fichier contenant les données collectées sur la **période 2005 à 2020**.
    """
    )
        st.markdown(f"Le fichier contient {Nb_lignes} lignes et {Nb_colonnes} colonnes")
          
        st.write(
    """    
    | Titre des colonnes                | Type         | Présence de valeurs nulles | Explication de la donnée                                                                 |
    |-----------------------------------|--------------|----------------------------|------------------------------------------------------------------------------------------|
    | Country name                      | Objet         | Aucune valeur vide          | Nom du pays où les mesures ont été relevées.                                             |
    | Year                              | Chiffre entier| Aucune valeur vide          | Année durant laquelle la mesure a été réalisée.                                          |
    | Life ladder                       | Numérique     | Aucune valeur vide          | Mesure du bonheur sur une échelle allant de 0 à 10, moyenne des réponses obtenues.       |
    | Log GDP per capita                | Numérique     | 36 valeurs vides            | Mesure de la richesse produite par habitant ou PIB/habitant.                             |
    | Social support                    | Numérique     | 13 valeurs vides            | Mesure de l'assistance sociale. Indicateur de soutien en cas de difficulté.              |
    | Healthy life expectancy           | Numérique     | 55 valeurs vides            | Mesure de l'espérance de vie d'une personne dès la naissance.                            |
    | Freedom to make life choices      | Numérique     | 32 valeurs vides            | Mesure de la capacité à faire ses propres choix de vie.                                   |
    | Generosity                        | Numérique     | 89 valeurs vides            | Mesure de la générosité, ex : don effectué à un organisme de bienfaisance.                |
    | Perceptions of corruption         | Numérique     | 110 valeurs vides           | Mesure de la manière dont la corruption est perçue.                                      |
    | Positive affect                   | Numérique     | 22 valeurs vides            | Impact positif.                                                                         |
    | Negative affect                   | Numérique     | 16 valeurs vides            | Impact négatif.                                                                         |
    """
    )

    elif Tableaux == Tableau_2 : 

        st.markdown('<h3 style="color:purple;"></h3>', unsafe_allow_html=True)
        st.markdown('<h5 style="color:purple;text-align:center;">world-happiness-report-2021.csv</h5>', unsafe_allow_html=True)

    # Description des fichiers CSV
    #st.header('Contenu des fichiers')
    #st.subheader('world-happiness-report.csv')
    #st.subheader('world-happiness-report-2021.csv')
        st.markdown(
    """
    Détail des colonnes du fichier contenant les données collectées sur **l'année 2021** :
        """
    )
        st.markdown(f"Le fichier contient {Nb_lignes2021} lignes et {Nb_colonnes2021} colonnes")
       
        st.write(
    """   
    | Titre des colonnes                | Type         | Présence de valeurs nulles | Explication de la donnée                                                                 |
    |---------------------------------- |--------------|----------------------------|------------------------------------------------------------------------------------------|
    | Country name                      | Objet         | Aucune valeur vide          | Nom du pays.                                                                            |
    | Regional indicator                | Objet         | Aucune valeur vide          | Indicateur régional, zone géographique.                                                 |
    | Ladder score                      | Numérique     | Aucune valeur vide          | Mesure du bonheur sur un score d'échelle de 0 à 10.                                      |
    | Standard error of ladder score    | Numérique     | Aucune valeur vide          | Mesure de l'erreur type du score d'échelle.                                              |
    | Upperwhisker                      | Numérique     | Aucune valeur vide          | Limites supérieures de la distribution des scores du bonheur.                            |
    | Lowerwhisker                      | Numérique     | Aucune valeur vide          | Limites inférieures de la distribution des scores du bonheur.                            |
    | Logged GDP per capita             | Numérique     | Aucune valeur vide          | Mesure de PIB enregistré par habitant.                                                   |
    | Social support                    | Numérique     | Aucune valeur vide          | Mesure de l'aide, l'assistance sociale.                                                 |
    | Healthy life expectancy           | Numérique     | Aucune valeur vide          | Mesure de l'espérance de vie en bonne santé.                                            |
    | Freedom to make life choices      | Numérique     | Aucune valeur vide          | Mesure de la liberté de faire des choix de vie.                                          |
    | Generosity                        | Numérique     | Aucune valeur vide          | Mesure de la générosité.                                                                 |
    | Perceptions of corruption         | Numérique     | Aucune valeur vide          | Mesure de la perception de la corruption.                                                |
    | Ladder score in Dystopia          | Numérique     | Aucune valeur vide          | Mesure du bonheur sur un score d'échelle dans la Dystopie.                               |
    | Explained by: Log GDP per capita  | Numérique     | Aucune valeur vide          | Score du bonheur expliqué par le PIB par habitant.                                       |
    | Explained by: Social support      | Numérique     | Aucune valeur vide          | Score du bonheur expliqué par l'aide sociale par habitant.                               |
    | Explained by: Healthy life expectancy | Numérique | Aucune valeur vide          | Score du bonheur expliqué par l'espérance de vie.                                        |
    | Explained by: Freedom to make life choices | Numérique | Aucune valeur vide       | Score du bonheur expliqué par la liberté de faire des choix de vie.                      |
    | Explained by: Generosity          | Numérique     | Aucune valeur vide          | Score du bonheur expliqué par la générosité.                                             |
    | Explained by: Perceptions of corruption | Numérique | Aucune valeur vide        | Score du bonheur expliqué par la perception de la corruption.                            |
    | Dystopia + residual               | Numérique     | Aucune valeur vide          | La perception du bonheur dans la Dystopie.                                               |
    """
    )

    st.text("")
    st.text("")
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Visualiser les données des deux DataFrame 
        </p>
    """, unsafe_allow_html=True)

    st.button("Reset", type="primary")
    if st.button("Données de 2005 à 2020"):
        st.dataframe(df)
    elif st.button("Données de 2021"): 
        st.dataframe(df_2021)
    else : st.text("Aucun dataframe de choisi")
# ___________________________________________________________________________   Fin de la page Exploration     __________________
# ===========================================================================  Début de la page DataVizualization  ===============
if page == pages[2] : 
    st.markdown(
        f"""
        <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Analyse World Hapiness Report de 2005 à 2021</h3>

    """, unsafe_allow_html=True)

    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: justify;font-size:15px;">
    Nous avons choisi de ne pas fusionner les deux fichiers lors de cette étape.
    Nous avons souhaité dans un premier temps effectuer une exploration sur les deux fichiers séparément, afin d’identifier les variables ayant une forte importance le sentiment de bonheur. 
        </p>
    """, unsafe_allow_html=True)

    moyenne_annee = df_global.groupby('year')['Life Ladder'].mean()
    reponse_annee = df_global.groupby('year')['Country name'].count()

    graphique1 = " Evolution du bonheur et du nombre de réponse à l'enquête WHR 2005 à 2020"
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)

    response_counts = df['year'].value_counts().reset_index()
    response_counts.columns = ['year', 'Number of Responses']  # Renommer les colonnes

    # Fusionner les occurrences avec le DataFrame d'origine pour la visualisation
    df = df.merge(response_counts, on='year')

    # Création de la figure
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Tracer le 1er graphique (Life Ladder)
    sns.lineplot(x='year', y='Life Ladder', data=df, ax=ax1, color='b', label='Life Ladder')
    ax1.set_ylabel("Indice de Vie (Life Ladder)", color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_title("Évolution de l'Indice de Vie et du Nombre de Réponses")

    # Création d'un deuxième axe Y pour le nombre de réponses

    ax2 = ax1.twinx()  # Créer un axe Y secondaire
    sns.lineplot(x='year', y='Number of Responses', data=df, ax=ax2, color='g', label='Nombre de Réponses')
    ax2.set_ylabel("Nombre de Réponses", color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    # Ajout d'une légende
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)


    st.markdown("""
    <p style="text-align: justify;font-size:15px;">
    L’observation du sentiment de bonheur de 2005 à 2020 permet de voir que globalement ce sentiment augmente sur la période. Les résultats des années 2005 et 2020 sont atypiques.
                
    </p>En effet, le 'Ladder Score' de 2005 est nettement supérieures aux autres années. Ce résultat peut s’expliquer par une faible participation à l’enquête. 
    </p>En 2020, on constate aussi une hausse soudaine du sentiment de bonheur, mais aussi une baisse significative des pays participants. (Environ 40% en moins). Le covid a impacté le taux de participation.
    
    </p>Pour effectuer ces analyses exploratoires, nous avons effectué une analyse de corrélation. 
                
    Cette eploration est appliquée sur la  partie des variables ayant une plus forte correlation avec le sentiment du bonheur.
    """, unsafe_allow_html=True)

    st.markdown('<h3 style="color:purple;">Analyse de la corrélation entre les différentes variables</h3>', unsafe_allow_html=True)

# @@@@@@     Matrice de Person
    st.markdown("""
    <p style="text-align: justify;font-size:15px;">

    Le heatmap sur le fichier contenant les données de 2005 à 2020 montre les corrélations les plus importante sur lequelle nous pouvons regarder les résultat plus en détails. 
    """, unsafe_allow_html=True)

    cor = df.iloc[:,2:10].corr() # sélection des variables quantitatives
    fig, ax = plt.subplots(figsize = (10,10))
    sns.heatmap(cor, annot = True, ax = ax, cmap = "flare")
    st.pyplot(fig)



# @@@@@@     Nuage de point par région

    #st.markdown("""
    #<p style="text-align: justify;font-size:15px;">
                
    #""", unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align: justify;font-size:15px;">
    La partie suivante reprend les principaux Item ayant le plus de coorelaction avec le score du Bonheur 'PIB par habitant', Social support, Generosity, expérence de vie, le sentiment de liberté.

    Les Nuages de point ci-desous reprennent les données par région, afin d'en facilité la lecture voici les pays de chaque groupe regionnal.                    
    """, unsafe_allow_html=True)

#****** Insersion du planisphere
    figure = px.choropleth(df_2021,
                    locations="Country name",
                    color="Regional indicator",
                    locationmode="country names",
                   )
    figure.update_layout(title="pays par zone régionale", showlegend=False)
    st.plotly_chart(figure)
#********* fin Insersion du planisphere


    st.markdown('<h3 style="color:purple;">Affichage des nuages de points : </h3>', unsafe_allow_html=True)

#***** Insersion nuage de point

    choix_1 = ['Choisir une variable','Ladder score','Logged GDP per capita','Social support','Generosity','Perceptions of corruption','Healthy life expectancy','Freedom to make life choices']
    choix = ['Choisir une variable','Logged GDP per capita','Social support','Generosity','Perceptions of corruption','Healthy life expectancy','Freedom to make life choices']
    option1 = st.selectbox('Choix de la variable 1 (axe x)', choix_1)
    option = st.selectbox('Choix de la variable 2 (axe y)', choix)
  

    if option == 'Choisir une variable'  or option1 == 'Choisir une variable' :
      st.write('**Veuillez choisir les données que vous souhaitez afficher**') 


      #fig = plt.figure()
    else :
     ""
     st.write(f"Vous avez choisi d afficher les variables :  **{option1}** et **{ option}**")

     fig = px.scatter(df_2021,x = option1,y = option, color = "Regional indicator",hover_name='Country name')
     plt.title('Sentiment de bonheur par PIB par Habitant',fontsize=9)
     fig.update_layout(xaxis = dict(range=[2,8],))
     if option == 'Logged GDP per capita' : 
        fig.update_layout(yaxis = dict(range=[6,12],))
     elif option == 'Social support' :
        fig.update_layout(yaxis = dict(range=[0.3,1],))
     elif option == 'Generosity':
        fig.update_layout(yaxis = dict(range=[-1,1],))
     elif option == 'Perceptions of corruption':
        fig.update_layout(yaxis = dict(range=[0,1],))
     elif option == 'Healthy life expectancy':
       fig.update_layout(yaxis = dict(range=[48,75],))
     elif option == 'Freedom to make life choices':
        fig.update_layout(yaxis = dict(range=[0.4,1],))
        
     st.plotly_chart(fig)
#***** Fin Insersion nuage de point


    ax =px.box(df_2021,y = 'Ladder score',x = "Regional indicator",color = "Regional indicator")
    st.plotly_chart(ax)
# Afficher le graphique dans Streamlit
st.pyplot(fig)

# Sauvegarder le graphique sous forme d'image
from io import BytesIO
buf = BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Bouton pour télécharger l'image
st.download_button(
    label="Télécharger le graphique",
    data=buf,
    file_name="evolution_bonheur.png",
    mime="image/png"
)



# =====================================================================================Fin de la page DataVizualization  =====================================
#
#
#  #####################################################################################   Début de la page Pré-processing  #####################################
if page == pages[3] : 
    st.markdown(
        f"""
        <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Analyse World Hapiness Report de 2005 à 2021</h3>

    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)

    # Ajout  des variables
    #st.markdown('<h3 style="color:Blue;"> PRE PROCESSING</h3>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;"> Ajout de variables</h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Year : ajout de l’année 2021, car celle-ci ne se trouve pas dans ce Dataframe alors que le
        second fichier (world-happiness-report.csv) contient les années. Il est nécessaire
        d’uniformiser cette variable. 
        </p>
    """, unsafe_allow_html=True)
#variable renommée
    st.markdown('<h3 style="color:purple;"> Variables renommées</h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Ladder score: car cette variable est nommée « Life Ladder » dans le fichier world-happinessreport-2021.csv. Il est nécessaire d’uniformiser cette variable.
        En effet, le score du bonheur a une dénomination différente entre les deux sources. Cela
        peut laisser supposer qu’elles peuvent être alimentées par des données dont les sources
        sont différentes. Etant donné que cette étude est accessible au grand public, une
        investigation a été poussée dans ce sens, afin de vérifier si celles-ci peuvent être
        exploitables. Nous en avons conclu que les deux valeurs sont semblables et représentent le
        même concept. La terminologie peut varier mais les valeurs numériques sont les mêmes.
        « Life Ladder » est un terme utilisé de manière informelle et « Ladder Score » est un terme
        plus technique et formel. 
        </p>
    """, unsafe_allow_html=True)
# Suppression des données

    st.markdown('<h3 style="color:purple;">Suppression des données</h3>', unsafe_allow_html=True)
    st.markdown(
    """
    <p style="text-align: justify; font-size: 15px;">
    Les suppressions de certaines variables dans notre analyse contribuent à la construction d'un modèle plus robuste. En évitant les problèmes associés à la colinéarité et à la redondance, nous pouvons nous concentrer sur les caractéristiques les plus pertinentes pour prédire les scores de bonheur. Cela permet une analyse plus précise et plus fiable des facteurs influençant le bonheur à travers différentes régions et pays du monde.
       """, unsafe_allow_html=True
         )
  #  Voici les variables supprimées et les raisons de leur suppression :
  #  </p>
  #  """, unsafe_allow_html=True
    #)

# Table des variables supprimées avec Markdown
    st.markdown(
    """
    | Variables                          | Type     | Présence de valeurs nulles | Explications                                                                                                                                 |
    |-----------------------------------|----------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
    | Healthy life expectancy at birth  | Float64  | 55 valeurs non-nulles       | Cette mesure représente la durée moyenne de vie en bonne santé qu'une personne peut s'attendre à avoir dès sa naissance. En revanche, dans le dataframe `df_2021`, la variable `Healthy life expectancy` mesure la durée moyenne de vie en bonne santé d'une population donnée à un moment donné. |
    | Positive effect                   | Float64  | 22 valeurs non-nulles       | La variable `Positive effect` est présente dans le premier dataframe mais absente du dataframe `df_2021`. Sa suppression est inévitable pour fusionner les deux dataframes. |
    | Negative effect                   | Float64  | 16 valeurs non-nulles       | De même, `Negative effect` est une variable dans le premier dataframe mais ne se trouve pas dans `df_2021`. Sa suppression est nécessaire pour la fusion des dataframes. |
    """, unsafe_allow_html=True
 )
# Traitement des données manquantes 
    st.markdown('<h3 style="color:purple;">Les données manquantes</h3>', unsafe_allow_html=True)
    st.markdown(
    """
    <p style="text-align: justify; font-size: 15px;">
    Par la moyenne de la donnée par pays; 
    Par la médiane ;
    Lorsque certaines données pour un pays étaient encore manquantes, remplacement par zéro, le proportion n'est pas significative.

    </p>
    """, unsafe_allow_html=True
    
    )
# le df global


# Présentation des variables avec Markdown
    st.markdown('<h3 style="color:purple;">Variables du Dataset</h3>', unsafe_allow_html=True)

# Description des variables
    st.markdown(
    """
    Voici les variables disponibles dans le dataset :

    | Variable                      | Type      | Présence de valeurs nulles | Explications                                                                                              |
    |-------------------------------|-----------|----------------------------|----------------------------------------------------------------------------------------------------------|
    | Country name                  | Object     | 2098 non-null               | Nom du pays où les mesures ont été relevées                                                               |
    | Year                          | Int64      | 2098 non-null               | Année durant laquelle la mesure a été réalisée                                                            |
    | Life Ladder                   | Float64    | 2098 non-null               | Mesure du bonheur sur un score d'échelle de 0 à 10                                                         |
    | Log GDP per capita            | Float64    | 2098 non-null               | Mesure de PIB enregistré par habitant                                                                     |
    | Social support                | Float64    | 2098 non-null               | Mesure l'aide, l'assistance sociale                                                                        |
    | Freedom to make life choices  | Float64    | 2098 non-null               | Mesure de la liberté de faire des choix de vie                                                             |
    | Generosity                    | Float64    | 2098 non-null               | Mesure de la générosité                                                                                   |
    | Perceptions of corruption     | Float64    | 2098 non-null               | Mesure de la perception de la corruption                                                                   |
    | Regional indicator            | Object     | 2098 non-null               | Indicateur régional, zone géographique                                                                     |
    """
)

# Ajouter des informations supplémentaires si nécessaire
    st.write(
    """
    Ces variables fournissent une vue d'ensemble des facteurs mesurés dans notre dataset, nous permettant d'analyser différents aspects du bonheur et du bien-être à travers les pays et les années.
    """
    )

    df_global=df_global.sort_values(by=["year"])
    fig = px.choropleth(df_global,
                    locations="Country name",
                    color="Life Ladder",
                    locationmode="country names",
                    animation_frame="year")
    fig.update_layout(title="Evolution du ladder score par pays par zone régionale (aprés pré-processing)")
    st.plotly_chart(fig)
# Afficher le graphique dans Streamlit
st.pyplot(fig)

# Sauvegarder le graphique sous forme d'image
from io import BytesIO
buf = BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Bouton pour télécharger l'image
st.download_button(
    label="Télécharger le graphique",
    data=buf,
    file_name="evolution_bonheur.png",
    mime="image/png"
)



#  #####################################################################################    Fin de la page Pré-processing   #####################################
#
#
#
# 
# ......................................................................................   Début de la page Modélisation   ...........................................

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import base64

# Vérification de la page
if page == pages[4]: 
    st.markdown(
        f"""
        <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Analyse World Happiness Report de 2005 à 2021</h3>
        </div>
        """, unsafe_allow_html=True)
    
    # Fonction pour générer un lien de téléchargement du fichier CSV
    def get_download_link(file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{file_path}">Télécharger le fichier CSV</a>'
        return href

    # Titre principal pour le volet modélisation
    st.markdown('<h3 style="color:purple;">Les modèles, Résultats et Analyse</h3>', unsafe_allow_html=True)

    # Spécifiez le chemin vers votre fichier CSV
    file_path = "C:/Users/fatim/Documents/results_df.csv"  # Assurez-vous que le chemin est correct et que le fichier existe

    # Vérifiez si le fichier existe
    if os.path.exists(file_path):
        # Charger les données à partir du fichier CSV
        results_df = pd.read_csv(file_path)

        # Afficher un aperçu des données
        st.markdown('<h3 style="color:purple;">Aperçu des données des métriques</h3>', unsafe_allow_html=True)
        st.write(results_df.head())
    else:
        st.error(f"Le fichier n'a pas été trouvé à l'emplacement spécifié : {file_path}")

    # Explication des modèles
    st.markdown('<h3 style="color:purple;">Choix du modèle et optimisation</h3>', unsafe_allow_html=True)
    st.markdown('<h5 style="color:Orange;">Gradient Boosting Regressor:</h5>', unsafe_allow_html=True)
    st.markdown("""<p style="text-align: justify;font-size:15px;">
        Le Gradient Boosting est souvent performant pour les problèmes de régression grâce à sa capacité à corriger les erreurs des modèles précédents en construisant des modèles séquentiels.
    </p>""", unsafe_allow_html=True)

    st.markdown('<h5 style="color:Orange;">Random Forest Regressor :</h5>', unsafe_allow_html=True)
    st.markdown("""<p style="text-align: justify;font-size:15px;">
        Il est robuste aux sur-ajustements (overfitting) et fonctionne bien avec une variété de types de données et de distributions.
    </p>""", unsafe_allow_html=True)

    st.markdown('<h5 style="color:Red;text-align:center;">La valeur cible est Le Life Ladder</h5>', unsafe_allow_html=True)
    st.markdown('<h5 style="color:Orange;">Techniques d\'optimisation des paramètres :</h5>', unsafe_allow_html=True)
    st.markdown("""<p style="text-align: justify;font-size:15px;">
        Contrairement au GridSearch, qui effectue une recherche exhaustive sur une grille d’hyperparamètres, le GridSearchCV utilise une validation croisée intégrée, offrant une méthode plus rigoureuse pour optimiser les hyperparamètres dans notre contexte.
    </p>""", unsafe_allow_html=True)

    # Filtrer les résultats pour chaque modèle
    rf_results = results_df[results_df['Model'] == 'Random Forest']
    gb_results = results_df[results_df['Model'] == 'Gradient Boosting']

    # Afficher les résultats pour Random Forest
    st.markdown('<h3 style="color:Purple;">Résultats pour le Random Forest :</h3>', unsafe_allow_html=True)
    if not rf_results.empty:
        st.dataframe(rf_results)

        # Graphiques pour Random Forest
        st.subheader("Graphiques des Métriques pour Random Forest")
        fig_rf = go.Figure()

        metrics = ['MSE', 'MAE', 'R2', 'RMSE']
        for metric in metrics:
            fig_rf.add_trace(go.Bar(
                x=rf_results['Best Parameters'],
                y=rf_results[metric],
                name=metric
            ))

        fig_rf.update_layout(
            title=dict(text='Métriques pour Random Forest', font=dict(size=38)),
            xaxis_title=dict(text='Meilleurs Hyperparamètres', font=dict(size=32)),
            yaxis_title=dict(text='Valeur', font=dict(size=22)),
            barmode='group',
            xaxis=dict(tickangle=-45),
            autosize=True,
            width=1000,
            height=600
        )
        st.plotly_chart(fig_rf, use_container_width=True)
    else:
        st.write("Aucun résultat trouvé pour Random Forest.")

    # Afficher les résultats pour Gradient Boosting
    st.markdown('<h3 style="color:Purple;">Résultats pour Gradient Boosting :</h3>', unsafe_allow_html=True)
    if not gb_results.empty:
        st.dataframe(gb_results)

        # Graphiques pour Gradient Boosting
        st.subheader("Graphiques des Métriques pour Gradient Boosting")
        fig_gb = go.Figure()

        metrics = ['MSE', 'MAE', 'R2', 'RMSE']
        for metric in metrics:
            fig_gb.add_trace(go.Bar(
                x=gb_results['Best Parameters'],
                y=gb_results[metric],
                name=metric
            ))

        fig_gb.update_layout(
            title=dict(text='Métriques pour Gradient Boosting', font=dict(size=38)),
            xaxis_title=dict(text='Meilleurs Hyperparamètres', font=dict(size=32)),
            yaxis_title=dict(text='Valeur', font=dict(size=22)),
            barmode='group',
            xaxis=dict(tickangle=-45),
            autosize=True,
            width=1000,
            height=600
        )
        st.plotly_chart(fig_gb, use_container_width=True)
    else:
        st.write("Aucun résultat trouvé pour Gradient Boosting.")

    # Télécharger le fichier CSV des résultats
    csv_file = 'model_results.csv'
    results_df.to_csv(csv_file, index=False)
    st.markdown(get_download_link(csv_file), unsafe_allow_html=True)

    # Conclusion des métriques
    st.markdown('<h3 style="color:Purple;">Analyse des métriques avec toutes les variables</h3>', unsafe_allow_html=True)
    st.markdown("""<p style="text-align: justify;font-size:15px;">
        Performance prédictive :
        Random Forest semble avoir une légère supériorité par rapport au Gradient Boosting en termes de MSE,
        MAE, RMSE, et R², il est légèrement plus performant pour cette tâche spécifique de régression.
        Temps de calcul :
        Le Gradient Boosting est beaucoup plus rapide à ajuster que le Random Forest, cela peut être un facteur
        important si la vitesse de calcul est une contrainte.
        Choix du modèle :
        Si la précision prédictive est la priorité et que le temps de calcul n'est pas une contrainte majeure, 
        le Random Forest est à prioriser.
    </p>""", unsafe_allow_html=True)

    # Données des métriques sans certaines variables
    st.markdown('<h3 style="color:Purple;">Analyse des erreurs des modèles sans les variables Country Name et Regional Indicator</h3>', unsafe_allow_html=True)
    st.markdown("""<p style="text-align: justify;font-size:15px;">
        Pour évaluer l'impact de l'optimisation des modèles, nous avons testé les modèles à la fois 
        avec et sans les variables "Country name" et "Regional indicator". 
        L'exclusion des deux variables a impacté les résultats des métriques : la MSE est passée de 0.121
        à 0.213, la MAE a également augmenté, de 0.261 à 0.348, et le R² a diminué""")

#  ....................................................................................  Fin de la page Modélisation  ..........................................
#                                                                                        Debut de la CONCLUSION
if page == pages[5] : 
    st.markdown(
        f"""
        <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Conclusion</h3>

    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)


    # Conclusion
    st.markdown('<h3 style="color:purple;">Peut-on prédire le bonheur ?</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: justify; font-size:15px;">
    L'exclusion des variables 'Country Name' et 'Regional Indicator' a conduit à une dégradation 
    des performances des deux modèles, suggérant que ces variables apportaient des informations 
    importantes pour prédire la variable cible. Il est donc recommandé de conserver les variables 
    'Country name' et 'Regional indicator' dans les modèles, sauf si une simplification est impérative 
    pour d'autres raisons (comme la réduction du temps de calcul ou la simplification du modèle).
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h3 style="color:purple;">Pour conclure sur cette partie</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: justify; font-size:15px;">
    En conclusion, bien que l'exclusion de variables puisse parfois simplifier le modèle, dans ce 
    cas particulier, ces variables semblent contenir des informations cruciales pour la 
    prédiction du bonheur. Il serait judicieux d'explorer davantage pourquoi ces variables sont 
    importantes et de considérer des techniques alternatives pour gérer leur impact sur le modèle tout 
    en maximisant la précision des prédictions. En ce qui concerne les métriques, la RMSE est recommandée 
    pour évaluer la précision des prédictions du bonheur. Le Modèle le Plus Performant est le Random Forest, 
    surtout lorsque les variables 'Country name' et 'Regional indicator' sont incluses. Il a des scores de 
    MSE, MAE, R², et RMSE meilleurs comparés à Gradient Boosting.
    </p>
    """, unsafe_allow_html=True)

    # Affichage de l'image
    new_image = bonheur.resize((1500, 1500))
    st.image(new_image, caption='Analyse du Bonheur', use_column_width=True)
