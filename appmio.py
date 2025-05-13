import streamlit as st
import time

st.text("""         
        Haha
        sto andando
        a capo
        """) 

st.text(":)") 



# RENDERIZZARE IMMAGINE CON PILLOW -> st.image()
from PIL import Image
image = Image.open('cat.png')
st.image(image, caption = 'Not impressed', width = 200)


st.header(':sparkles: :rainbow[INTERAZIONE] :sparkles:')  # :emoji: , :color[texto]


# BUTTON -> st.button()
st.subheader(':red[button]')   
if st.button('click me', help = 'clicca qui!!! :point_down:'):
    st.write(':sparkler: Hai cliccato')


# CHECK BOX -> st.checkbox()
st.subheader(':orange[**checkbox**]')  # **negrita**
if st.checkbox('check me'):
    st.write(':dart: Checked')


# RADIO BUTTON -> st.radio()

tri = Image.open('tri.jpg')
trex = Image.open('trex.jpg')
est  = Image.open('est.png')
vel = Image.open('vel.jpg')
bra = Image.open('bra.png')

st.subheader(':green[radio button]')

lang = st.radio('_Qual è il tuo dinosaurio preferito?_ :t-rex:', 
                ('Triceratops', 'T-rex', 'Estegosaurio', 'Velociraptor', 'Brachiosaurus'))
if st.button('Risposta definitiva?', help = 'cliccami ;) :point_down:'):
    st.toast('Runnando...')   # messaggio temporaneo
    if lang == 'Triceratops':
        st.image(tri, width = 300)
        st.audio('vel_sound.mp3')
    elif lang == 'T-rex':
        st.image(trex, width = 300)
        st.audio('vel_sound.mp3')
    elif lang == 'Estegosaurio':
        st.image(est, width = 300)
        st.audio('vel_sound.mp3')
    elif lang == 'Velociraptor':
        st.image(vel, width = 200)
        st.audio('vel_sound.mp3')
    elif lang == 'Brachiosaurus':
        st.image(bra, width = 200)
        st.audio('vel_sound.mp3')
    else:
        st.write('') 


# SLIDDER -> st.slider()
# st.subheader(':blue[slidder]') 
# st.write('**:abacus: Area di un rettangolo:**')
# lato_a = st.slider(':red-background[**Lato a**]', 1, 20)
# lato_b = st.slider(':red-background[**Lato b**]', 1, 20)

# if st.button('Vuoi sapere il risultato? :eyes:', help = 'Clicca qui!! :point_down:'):
#     st.write(lato_a * lato_b)

#st.text(f"Area: {lato_a * lato_b}")

# GRAFICO --> st.pyplot(fig):
# st.subheader(':violet[grafico]')

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 101)
# k = st.slider('k', 1, 4)
# y1 = x*k
# y2 = x**k
# y3 = x**(k+1)

# fig=  plt.figure(figsize = (8,6))
# plt.plot(x, y1, label = 'blue')
# plt.plot(x, y2, label = 'arancione')
# plt.plot(x, y3, label = 'verde')
# plt.legend()

# st.pyplot(fig)

# TEXT AND NUMBER INPUT -> st.text_input() , st.number_input()

st.subheader(':violet[Verifica comunicazione e dinamiche di gruppo]')

input1 = st.text_input("Qual è il tuo colore preferito?")
input2 = st.text_input("Qual è l'ultimo libro che hai letto?")
input3 = st.number_input("Quanti animali domestici hai?", min_value = 0, max_value = 10)
input4 = st.radio("Hai mai ucciso a qualcuno/a?", ('Si', 'No', 'Magari' , 'Si, con una lavatrice', 'Puoi ripetere la domanda?', 'Non ancora, ma non si sa mai', 'Lo volevo fare ma poi mi sono distratto/a', 'No, ma lo sarei se fosse giusto', 'Preferisco non rispondere'))


if st.button('Risultato'):
    with st.spinner('Sto pensando...'):
        time.sleep(3)
        if input4 == 'Si':
            st.success('Sei scorpione', icon = '🦂')
        elif input4 == 'Si, con una lavatrice':
            st.success('Sei pesce', icon = '🐟')
        elif input4 == 'No':
            st.success('Sei cancro', icon = '🦀')
        elif input4 == 'Magari':
            st.success('Sei aquario', icon = '🦈')
        elif input4 == 'Puoi ripetere la domanda?':
            st.success('Sei capricornio', icon = '🐐')
        elif input4 == 'Non ancora, ma non si sa mai':
            st.success('Sei ariete', icon = '🐏')
        elif input4 == 'Lo volevo fare ma poi mi sono distratto/a':
            st.success('Sei sagitario', icon = '🏹')
        elif input4 == 'No, ma lo sarei se fosse giusto':
            st.success('Sei vergine', icon = '...')
        else:
            st.success('Sei bilancia' , icon = '...')
    
    
    # st.success('Sei scorpione', icon = '⭐') # display a success message: (body, icon = "icon")


# https://emojipedia.org/