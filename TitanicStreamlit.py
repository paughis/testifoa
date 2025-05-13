# streamlit run TitanicStreamlit.py
# dataset url = https://frenzy86.s3.eu-west-2.amazonaws.com/fav/tecno/titanic.csv

# from PIL import Image

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import io

# @st.cache  # guarda el file en cache, asi no lo carga cada vez y va mas rapido
# def load_data():
#     pass
#....

# TERMINAR ESTO!!!!
@st.cache_resource
def load_models():
    models = {}    
    model_configs = {
                    'titanic': 'models/titanic_pipe.pkl',       # 'titan_pipe.pkl'
                    #'iris': 'models/iris_pipe.pkl'  
                    }
    for model_name, model_path in model_configs.items():
        if os.path.exists(model_path):
            models[model_name] = joblib.load(model_path)
        else:
            st.error(f"File modello non trovato: {model_path}")
    return models
######


# def load_clean_data():
#     uploaded_file = st.file_uploader("Choose a file",type={"csv"})
#     df = pd.read_csv(uploaded_file, sep='\t')
#     df1 = df.copy()
#     features_to_remove = ['Name', 'PassengerId', 'Ticket', 'Cabin']
#     df1 = df1.drop(features_to_remove, axis=1)
#     st.dataframe(df1)

def convert_to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="data",index=False)
    # see: https://xlsxwriter.readthedocs.io/working_with_pandas.html
    writer.close()
    return output.getvalue()

st.set_page_config(page_icon="random")

def main():
    
    st.title(" 🌹 Rose o Jack? 💀" )
    st.subheader("🚢 Vuoi sapere se avresti sopravvissuto al Titanic o meno?")
    
    uploaded_file = st.file_uploader("Per iniziare, carica il Titanic Dataset: :point_down:",type={"csv"})
    df = pd.read_csv(uploaded_file, sep='\t')
    df1 = df.copy()
    
    features_to_remove = ['Name', 'PassengerId', 'Ticket', 'Cabin']
    df1 = df1.drop(features_to_remove, axis=1)

    if st.button('Go'):
        st.dataframe(df1)


    tab1, tab2, tab3 = st.tabs(["EDA", "Pred", "Batch"])

    with tab1:
        st.header(":abacus: Statistica")
        st.dataframe(df1.describe())

        st.header(":chart_with_upwards_trend: Pairplot")
        
        fig = plt.figure(figsize=(12,12))
        fig = sns.pairplot(df1, hue='Survived',  height=1.5, palette="viridis")
        st.pyplot(fig)

        st.header(":star: Correlazione")
        
        df_numeric = df1.select_dtypes(include = ['float', 'int'])
        corr = df_numeric.corr()

        fig2,ax = plt.subplots(figsize = (8,6))
        sns.heatmap(corr, annot=True, cmap = 'Blues', ax=ax)
        st.pyplot(fig2)
    
    with tab2:

    # target / features, test_train_split, numerical / categorical????

        st.header(":crystal_ball: :rainbow[Prediction]")

        Pclass = st.radio('Passenger class', (1, 2, 3))
        Age = st.number_input('Age', 0 , 80)
        SibSp = st.number_input('Number of siblings / spouses', 0, 10)
        Fare = st.number_input('Passenger fare', 6, 300)
        Sex = st.radio('Sex', ('female', 'male'))
        Parch = st.number_input('Number of parents / children', 0, 10)
        Embarked = st.radio('Port of Embarkation', ('C', 'Q', 'S'))

        data = {
            "Pclass": [Pclass],
            "Age": [Age],
            "SibSp": [SibSp],
            "Fare" : [Fare],
            "Sex" : [Sex],
            "Parch": [Parch],
            "Embarked": [Embarked]
            }
        
        pred_data = pd.DataFrame(data)

        titan_pipe = joblib.load('titan_pipe.pkl')

        if st.button(':mage: Fare predizione'):
            pred = titan_pipe.predict(pred_data)[0]          # con [0] me da solo el elemento, la stringa. Si no, me daria el array!
            if pred == 1:
                st.success("😎 Ce l'hai fatta! 😎")
            else:
                st.warning("💀 Sei cibo per i pesci 💀")

        with tab3:

            st.header(":magic_wand: :rainbow[Batch Processing]")
            uploaded_file = st.file_uploader("Carica un file Excel :point_down:")

            if uploaded_file is not None:
                # Verifica l'estensione del file
                if uploaded_file.name.endswith('.xlsx'):
                    df = pd.read_excel(uploaded_file)
                    st.success(":tada: File caricato con successo!")
                else:
                    st.error("Formato file non supportato!")

            df_pred = df.copy()
            titan_pipe = joblib.load('titan_pipe.pkl')
            predict_column = titan_pipe.predict(df_pred)
            df_pred['Sopravvisuto'] = predict_column
            
            st.subheader("Preview :eyes:")
            st.dataframe(df_pred)

            st.subheader("Scarica il file qui!! :point_down:")
            st.download_button(
                                label="Download as Excel-file",
                                data=convert_to_excel(df_pred),     # convierte el dataframe df_pred a formato Excel y lo pasa a "data"
                                file_name="titanic_pred.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", # identifica el contenido como archivo excel, ayuda al navegador a manejar correctamente el archivo (no obligatorio)
                                key="excel_download",
                                )


if __name__ =='__main__':
    main()


    # if uploaded_file is not None:
    #     if st.button('Go'):

    # url = st.text_input('Incolla dataset URL:', "https://frenzy86.s3.eu-west-2.amazonaws.com/fav/tecno/titanic.csv")
    # df = None  # Esto y la linea siguiente son para que no aparezca error con el input vacio

    # if url != '':
    #     df = pd.read_csv(url, sep='\t')