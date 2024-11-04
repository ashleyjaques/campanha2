import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Título da campanha
st.title('Campanha de Doação de Sangue')

# Adicionando uma imagem
st.image("Campanha.png")

# Descrição da campanha
st.markdown("""
## Junte-se a nós para salvar vidas!

A doação de sangue é um ato de solidariedade que pode salvar até três vidas. 
Participe da nossa campanha e ajude a promover a doação de sangue na sua comunidade.
""")

# Formulário de doação
st.subheader('Formulário de Doação')

with st.form('Formulário de Doador', clear_on_submit=True):
    col1, col2 = st.columns(2)

    nome = col1.text_input('Nome:')
    sobrenome = col2.text_input('Sobrenome:')
    email = col1.text_input('E-mail:')
    telefone = col2.text_input('Telefone:')
    
    idade = col1.number_input('Idade:', min_value=18, max_value=120)
    tipo_sanguineo = col2.selectbox('Tipo Sanguíneo:', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    
    submitted = st.form_submit_button("Enviar")

# Botão de envio
if submitted:
    if nome and sobrenome and email:
        st.success('Obrigado por se registrar como doador!')

        # Criação do DataFrame com os dados do formulário
        dados = {
            "Nome": [nome],
            "Sobrenome": [sobrenome],
            "Email": [email],
            "Telefone": [telefone],
            "Idade": [idade],
            "Tipo Sanguíneo": [tipo_sanguineo],
            "Data de Inscrição": [datetime.now().strftime(format="DD/MM/YYYY")]
        }
        df = pd.DataFrame(dados)

        # Definindo o caminho do arquivo
        pasta = "dados_doadores"
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        arquivo_csv = os.path.join(pasta, f'doador_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')

        # Salvando o DataFrame em um arquivo CSV
        df.to_csv(arquivo_csv, index=False)

        st.write(f'Dados salvos em: {arquivo_csv}')

# Sidebar para contato
st.markdown('---')
st.subheader('Entre em contato conosco')
st.write('Se você tiver alguma dúvida ou quiser mais informações, entre em contato:')
st.write('📧 Email: contato.sjr.captacao@hemominas.mg.gov.br')
st.write('📞 Telefone: (32) 3322-2900')
st.write('[🌐 Facebook](https://m.facebook.com/hemominas/photos/)')
st.write('[🐦 Twitter](https://twitter.com/hemominas)')
st.write('[📸 Instagram](https://www.instagram.com/hemominas/)')