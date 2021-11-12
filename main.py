import time

import streamlit as st

from data_creator import movement, latency_count

# movement = []
#
#
# @st.cache
# def create_data():
#     for x in range(50):
#         moves = ['left', 'right', 'up', 'down', 'shoot', 'duck', 'aim']
#         movement.append(random.choice(moves))
#         return movement


cols1, cols2, cols3 = st.columns([1, 2, 1])

with cols1:
    st.write("")

with cols2:
    st.title(""":video_game: Singularity :video_game:""")

with cols3:
    st.write("")

st.markdown('----------------')

# cloud_choice = st.selectbox('Choose platforms', ['Normal online gaming', 'Singularity Cloud'])

col4, col5 = st.columns(2)

with col4:
    normal_cloud = st.button('Test cloud speeds')

with col5:
    sing_cloud = st.button('Test Singularity speeds')

if normal_cloud:
    st.header('Player 1 has the advantage because of better internet and equipment')
    time.sleep(2)
    
    st.subheader('Data flowing loading....')
    time.sleep(1)
    # if cloud_choice == 'Normal online gaming':
    for x in range(len(movement)):
        # st.write(f'Move number {x}')
        if x in latency_count:
            st.success(f'Player 2: {movement[x]}')
        else:
            st.info(f'Player 1: {movement[x]}')
            time.sleep(0.5)

if sing_cloud:
    st.header('On Singularity, both players latency is matched for a better gaming experience')
    time.sleep(2)

    st.subheader('Data flowing loading....')
    time.sleep(1)

    for x in range(len(movement)):
        if x % 2 == 0:
            st.info(f'Player 1: {movement[x]}')
            time.sleep(1)
        else:
            st.success(f'Player 2: {movement[x]}')
            time.sleep(1)
