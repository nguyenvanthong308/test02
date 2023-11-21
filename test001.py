import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

session = st.session_state
if not session:
    session = {}
st.set_page_config(layout= "wide") 
if "add_hari" not in session:
    session["add_hari"] = False
if "edit_hari" not in session:
    session["edit_hari"] = False
if "zen_danmen" not in session:     ######################
    session["zen_danmen"] = False   ######################
if "HARI" not in session:   ######################
    session["HARI"] = ""    ######################
if "click" not in session:   ######################
    session["click"] = 0    ######################
if "off_button" not in session:
    session["off_button"] = False
if "LIST_KAI" not in session:
    session["LIST_KAI"] = []
######################################################################################################################
def draw_square(size, position_top, position_left, text):
    square_html = f'<div style="width: {size}px; height: {size}px; background-color: #A2A1A2; position: absolute; top: {position_top - 10}px; left: {position_left}px;">' \
                  f'<div style="position: absolute; top: 50%; left: 50%; transform: translate(-40%, -370%); color: red; font-size: 20px;">{text}</div>'
    st.markdown(square_html, unsafe_allow_html=True)

def draw_square1(size, position_top, position_left):
    square_html = f'<div style="width: {size}px; height: {size}px; background-color: #D4D6CA; position: absolute; top: {position_top - 10}px; left: {position_left}px;"></div>'
    st.markdown(square_html, unsafe_allow_html=True)

def draw_square2(size, position_top, position_left,text1):
    square_html1 = f'<div style="width: {size+80}px; height: {size}px; background-color: gray; position: absolute; top: {position_top}px; left: {position_left}px;">' \
                   f'<div style="position: absolute; top: 50%; left: 50%; transform: translate(-40%, -330%); color: black; font-size: 20px;">{text1}</div>'
    st.markdown(square_html1, unsafe_allow_html=True)

def draw_square3(size, position_top, position_left,text1, text2,text_G1, text_XY, text_0):
    square_html1 = f'<div style="width: {size+80}px; height: {size}px; background-color: gray; position: absolute; top: {position_top}px; left: {position_left}px;">' \
                   f'<div style="position: absolute; top: 50%; left: 60%; transform: translate(-40%, -130%); color: yellow; font-size: 20px;">{text1}</div>'\
                   f'<div style="position: absolute; top: 50%; left: 60%; transform: translate(-40%, 30%); color: blue; font-size: 20px;">{text2}</div>'\
                   f'<div style="position: absolute; top: 50%; left: 15%; transform: translate(-40%, -80%); color: black; font-size: 30px;">{text_G1}</div>'\
                   f'<div style="position: absolute; top: 50%; left: -85%; transform: translate(-40%, -80%); color: blue; font-size: 20px;">{text_XY}</div>'\
                   f'<div style="position: absolute; top: 50%; left: 20%; transform: translate(-40%, -240%); color: blue; font-size: 20px;">{text_0}</div>'
    st.markdown(square_html1, unsafe_allow_html=True)
 ###########
def draw_square4(size, position_top, position_left, TEXT_左, TEXT_下, Y_F, X_F, TEXT_右, TEXT_上):
    square_html1 = f'<div style="width: {size}px; height: {size}px; background-color: gray; position: absolute; top: {position_top}px; left: {position_left}px;">' \
                   f'<div style="position: absolute; top: -7%; left: 25%; transform: translate(-40%, -130%); color: red; font-size: 20px;">{TEXT_左}</div>'\
                   f'<div style="position: absolute; top: 35%; left: -25%; transform: translate(-40%, 200%); color: red; font-size: 20px;">{TEXT_下}</div>'\
                   f'<div style="position: absolute; top: 50%; left: -50%; transform: translate(-40%, -70%); color: black; font-size: 25px;">{Y_F}</div>'\
                   f'<div style="position: absolute; top: 50%; left: 50%; transform: translate(-40%, -500%); color: black; font-size: 25px;">{X_F}</div>'\
                   f'<div style="position: absolute; top: -15%; left: 75%; transform: translate(-40%, -80%); color: red; font-size: 20px;">{TEXT_右}</div>'\
                   f'<div style="position: absolute; top: 55%; left: -25%; transform: translate(-40%, -250%); color: red; font-size: 20px;">{TEXT_上}</div>'   
    
    st.markdown(square_html1, unsafe_allow_html=True)
def draw_square5(size, position_top, position_left, TEXT_C0):
    square_html = f'<div style="width: {size}px; height: {size}px; background-color: #D4D6CA; position: absolute; top: {position_top - 10}px; left: {position_left}px;">' \
                  f'<div style="position: absolute; top: 50%; left: 45%; transform: translate(-40%, -50%); black: yellow; font-size: 40px;">{TEXT_C0}</div>'
    st.markdown(square_html, unsafe_allow_html=True)
###########
def draw_horizontal_line(length, position_top, position_left):
    line_html = f'<hr style="border: 1px dashed red; width: {length}px; position: absolute; top: {position_top}px; left: {position_left}px;">'
    st.markdown(line_html, unsafe_allow_html=True)

def draw_horizontal_line1(length, position_top, position_left): #solid
    line_html = f'<hr style="border: 1px solid blue; width: {length}px; position: absolute; top: {position_top}px; left: {position_left}px;">'
    st.markdown(line_html, unsafe_allow_html=True)

def draw_vertical_line2(length, position_top, position_left):
    line_html = f'<div style="border: 1px solid blue; height: {length}px; position: absolute; top: {position_top}px; left: {position_left}px;"></div>'
    st.markdown(line_html, unsafe_allow_html=True)

def draw_vertical_line(length, position_top, position_left):
    line_html = f'<div style="border: 1px dashed blue; height: {length}px; position: absolute; top: {position_top}px; left: {position_left}px;"></div>'
    st.markdown(line_html, unsafe_allow_html=True)

def number_callback():
    if "new_number" not in session:
        session["new_number"] = 0
    session["selected_number"] = session.new_number
    #session["selected_number"] = session["new_number"]
######################################################################################################################

def STEEL_callback():
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"new"]

def steel_callback():
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"new"]
def Steel_callback():
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"new"]
def shape_callback():
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"new"]
    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"new"]
def add_hari():
    session["add_hari"] = True
    session["click"] += 1

def edit_hari(hari_data, ):
    session["edit_hari"] = True
    session[session["selected_kai"]+"梁符号"] = hari_data
    session["HARI"] = hari_data

def OK_add(hari_data,hari_collection):
    hari_collection.append(hari_data)
    session["add_hari"] = False

def cancel_add():
    session["add_hari"] = False

def OK_edit():
    session["edit_hari"] = False

def remove_hari(hari_data,hari_collection):
    hari_collection.remove(str(hari_data))
    session['_'+session["selected_kai"]+"梁符号"] = ""
    
def keeper(key):
    # Copy from widget key to placeholder
    session['_'+key] = session[key]
############################################## 通りの数量・通りの符号、スパンの間隔、階の数量・階の符号、柱符号、柱のズレ寸法、梁符号、梁の段差、梁のズレ寸法を入力##############################################
def main():
    ########### BUTTON #############
    if session["off_button"] == False:
    #################################
        col1, col2 = st.columns([1,1])
        with col1:
            numberY = st.number_input('水平方向の通りの数量', min_value=1, max_value=50, value=2, step=1)
            for y in range(1,numberY+1):
                session["Y"+str(y)] = st.text_input("水平方向の通りの名称 No."+str(y),"Y"+str(y))
        with col2:
            numberX = st.number_input('鉛直方向の通りの数量', min_value=1, max_value=20, value=2, step=1)
            for x in range(1,numberX+1):
                session["X"+str(x)] = st.text_input("鉛直方向の通りの名称 No."+str(x),"X"+str(x))
    ###################################################################################################
        Y_A1 = None   # ,Y_A1, Y_B1 , X_A1 , X_B1 ,
        Y_B1 = None
        number_Y = None

        X_A1 = None
        X_B1 = None
        number_X = None

        TEXT_C0 = None
        TEXT_左 = None
        TEXT_下 = None 
        TEXT_右 = None 
        TEXT_上 = None
        Y_F = None
        X_F = None

        text_段差_Y = None
        text_ズレ上_Y = None
        text_ズレ下_Y = None 
        text_梁名_Y = None
        Y1_F1 = None
        Y2_F1 = None
        X_F1 = None

        text_段差_X = None
        text_ズレ上_X = None
        text_ズレ下_X = None 
        text_梁名_X = None
        X1_F2 = None
        X2_F2 = None
        Y_F2 = None
    ###################################################### ,number_Y, number_X,
        st.write("各通りの間隔を入力")
        with st.expander("Y"):
            for y in range(1,numberY):
                colY3, colY, colY1, colY2 = st.columns([1,1,2,1])
                with colY:
                    st.markdown("<br>" * 2, unsafe_allow_html=True)
                    session["Y"+str(y)+"-"+"Y"+str(y+1)] = st.text_input(session["Y"+str(y)]+"-"+session["Y"+str(y+1)], str(y+11199))
                    Y_A1 = "Y"+str(y)
                    Y_B1 = "Y"+str(y+1)
                    number_Y = session["Y"+str(y)+"-"+"Y"+str(y+1)]
                    st.markdown("<br>" * 3, unsafe_allow_html=True)
                    with colY1:
                        #fig = create_grid(numberX, numberY,number_Y,'',Y_F,X_F,Y1_F1, Y2_F1, X_F1, X1_F2, X2_F2, Y_F2,TEXT_左,TEXT_下,TEXT_右,TEXT_上,'',text_段差_Y,text_ズレ上_Y,text_ズレ下_Y,text_梁名_Y,'','','','',Y_A1,Y_B1,'','',) #,texts1, texts2, texts3, texts4
                        #st.pyplot(fig)
                        draw_square(size= 120, position_top= 60, position_left= 150, text= Y_A1)
                        draw_square(size= 120, position_top= 44, position_left= 450, text= Y_B1)

                        draw_square2(size= 100, position_top= 30, position_left= 270, text1 = number_Y) #black

                        draw_square1(size= 45, position_top= 52, position_left= 488)
                        draw_square1(size= 45, position_top= 35, position_left= 188)

                        draw_horizontal_line(length= 500, position_top= 0, position_left= 110) #red
                        
                        draw_horizontal_line1(length= 320, position_top= -95, position_left= 200) #black
                        draw_vertical_line(length= 180, position_top= -90, position_left= 210) #blue
                        draw_vertical_line(length= 180, position_top= -105, position_left= 510) #blue  
        with st.expander("X"):
            for x in range(1,numberX):
                colX2, colX, colX1, colX3 = st.columns([1,1,2,1])
                with colX:
                    st.markdown("<br>" * 2, unsafe_allow_html=True)
                    session["X"+str(x)+"-"+"X"+str(x+1)] = st.text_input(session["X"+str(x)]+"-"+session["X"+str(x+1)],str(x+6499))
                    X_A1 = "X"+str(x)
                    X_B1 = "X"+str(x+1)
                    number_X = session["X"+str(x)+"-"+"X"+str(x+1)]
                    st.markdown("<br>" * 3, unsafe_allow_html=True)
                    with colX1:
                        #fig = create_grid(numberX, numberY,'', number_X,Y_F,X_F,Y1_F1, Y2_F1, X_F1, X1_F2, X2_F2, Y_F2,TEXT_左,TEXT_下,TEXT_右,TEXT_上,'',text_段差_Y,text_ズレ上_Y,text_ズレ下_Y,text_梁名_Y,'','','','','','',X_A1,X_B1,) #,texts1, texts2, texts3, texts4
                        #st.pyplot(fig)
                        draw_square(size= 120, position_top= 60, position_left= 150, text= X_A1)
                        draw_square(size= 120, position_top= 44, position_left= 450, text= X_B1)

                        draw_square2(size= 100, position_top= 30, position_left= 270, text1 = number_X) #black

                        draw_square1(size= 45, position_top= 52, position_left= 488)
                        draw_square1(size= 45, position_top= 35, position_left= 188)

                        draw_horizontal_line(length= 500, position_top= 0, position_left= 110) #red
                        draw_horizontal_line1(length= 320, position_top= -95, position_left= 200) #black
                        draw_vertical_line(length= 180, position_top= -90, position_left= 210) #blue
                        draw_vertical_line(length= 180, position_top= -105, position_left= 510) #blue 
    #########################################################################################################
        kai = st.number_input('階数を入力', min_value=1, max_value=50, value=1, step=1)  # value 2
        list_kai = list()
        for k in range(1,kai+1):
                session[str(k)+"F"] = st.text_input("階の符号 No."+str(k),str(k)+"F")
                list_kai.append(session[str(k)+"F"])
        session["LIST_KAI"] = list_kai
        st.write("階・通りに対して柱の「符号・ズレ寸法」を入力")
        
        for k in range(1,kai+1):  
            for a,b in ((y,x) for y in range(1,numberY+1) for x in range(1,numberX+1)):
                with st.expander(session[str(k)+"F"] + " " + "Y"+str(a)+"-"+"X"+str(b)): 
                    colA4, colA1, colA2, colA3= st.columns([1,1,1,1])
                    with colA1:
                        session[str(0)+"F"] = "0F" ##
                        session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"柱名"] = "C0" ##

                        session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の柱の符号は", session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"])
                        Y_F = session["Y"+str(a)]
                        X_F = session["X"+str(b)]
                        session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"左"] = 500 ##
                        session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"下"] = 500 ##
                        session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"左"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の左側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"左"])
                        TEXT_左 = session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"左"] ### TEXT_左
                        session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"下"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の下側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"下"])
                        TEXT_下 = session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"下"] ### TEXT_下
                        session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"右"] = 500 ##
                        session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"上"] = 500 ##
                        session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"右"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の右側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"右"])
                        TEXT_右 = session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"右"] ### TEXT_右
                        session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"上"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の上側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"上"])
                        TEXT_上 = session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"上"] #TEXT_上 
                        TEXT_C0 = session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"] ### TEXT_C0, TEXT_左, TEXT_下, TEXT_右, TEXT_上
                    with colA2:
                            #fig = create_grid(numberX - numberX + 1, numberY - numberY + 1,number_Y, number_X,Y_F,X_F,Y1_F1, Y2_F1, X_F1, X1_F2, X2_F2, Y_F2,TEXT_左, TEXT_下, TEXT_右, TEXT_上 ,TEXT_C0,text_段差_Y, text_ズレ上_Y , text_ズレ下_Y, text_梁名_Y,'', '' , '', '','', '' , '', '',)
                            #st.pyplot(fig)
                            st.markdown("<br>" * 3, unsafe_allow_html=True)
                            draw_square4(size= 200, position_top= 30, position_left= 150, TEXT_左 = TEXT_左, TEXT_下 = TEXT_下, Y_F = Y_F, X_F = X_F, TEXT_右 = TEXT_右, TEXT_上 = TEXT_上 ) #black
                            draw_square5(size= 70, position_top= 85, position_left= 215, TEXT_C0 = TEXT_C0)

                            draw_horizontal_line(length= 310, position_top= 60, position_left= 80) #red horizontal
                            draw_vertical_line(length= 310, position_top= -85, position_left= 250) #blue vertical

                            draw_horizontal_line1(length= 40, position_top= -66, position_left= 105) # line horizontal
                            draw_horizontal_line1(length= 40, position_top= 116, position_left= 105) # line vertical
                            draw_horizontal_line1(length= 210, position_top= -125, position_left= 145) # line horizontal

                            draw_vertical_line2(length= 40, position_top= -128, position_left= 150) # line vertical
                            draw_vertical_line2(length= 40, position_top= -144, position_left= 349) # line vertical
                            draw_vertical_line2(length= 210, position_top= -120, position_left= 125) # line vertical blue
            st.write("---")
            
    ###############################################################################################################################

        st.write("階・通りに対して梁の「符号・段差・ズレ寸法」を入力")
        list_hari = list()
        for k in range(1,kai+1):
            
            for x in range(1,numberX+1):
                for y in range(1,numberY): 
                    with st.expander(session[str(k)+"F"] + " " +"X"+str(x)+"通り "+ "Y"+str(y)+"-"+"Y"+str(y+1)+"間"):
                        colB4, colB1, colB2,colB3 = st.columns([1,1,1,1])
                        with colB1:
                            session["0F" +"X"+str(x)+"通り "+ "Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"上"] = 300 ##
                            session["0F" +"X"+str(x)+"通り "+ "Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"下"] = 300 ##
                            Y1_F1 = session["Y"+str(y)]
                            Y2_F1 = session["Y"+str(y+1)] # ,Y1_F1, Y2_F1, X_F1,
                            X_F1 = session["X"+str(x)]
                            
                            session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"梁名"]=st.text_input(session[str(k)+"F"]+" "+"X"+str(x)+"通り "+session["Y"+str(y)]+"-"+session["Y"+str(y+1)]+"間"+"の梁の符号は","G1")
                            text_梁名_Y = session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"梁名"] # text_梁名_Y
                            session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"段差"]=st.text_input(session[str(k)+"F"]+" "+"X"+str(x)+"通り "+session["Y"+str(y)]+"-"+session["Y"+str(y+1)]+"間"+" = "+session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"梁名"]+"の梁の段差は",0)
                            text_段差_Y = session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"段差"] #text_段差_Y
                            session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"上"] = st.text_input(session[str(k)+"F"]+" "+"X"+str(x)+"通り "+session["Y"+str(y)]+"-"+session["Y"+str(y+1)]+"間"+"の上側、"+session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"梁名"]+"がズレ ",session[session[str(k-1)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"上"])
                            text_ズレ上_Y = session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"上"] #text_ズレ上_Y
                            session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"下"] = st.text_input(session[str(k)+"F"]+" "+"X"+str(x)+"通り "+session["Y"+str(y)]+"-"+session["Y"+str(y+1)]+"間"+"の下側、"+session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"梁名"]+"がズレ ",session[session[str(k-1)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"下"])
                            text_ズレ下_Y = session[session[str(k)+"F"]+"X"+str(x)+"通り "+"Y"+str(y)+"-"+"Y"+str(y+1)+"間"+"下"] #text_ズレ下_Y # text_段差_Y, text_ズレ上_Y , text_ズレ下_Y, text_梁名_Y
                        with colB2:
                            #if numberX > 0 or numberY > 0:
                                #fig = create_grid(numberX - numberX + 2, numberY - numberY + 2,number_Y, number_X,Y_F,X_F,Y1_F1, Y2_F1, X_F1, '', '', '','','','','','',text_段差_Y, text_ズレ上_Y , text_ズレ下_Y, text_梁名_Y,'', '' , '', '','', '' , '', '',)
                                #st.pyplot(fig) 
                            st.markdown("<br>" * 2, unsafe_allow_html=True)
                            draw_square(size= 120, position_top= 60, position_left= 50, text= Y1_F1)
                            draw_square(size= 120, position_top= 44, position_left= 350, text= Y2_F1)
                            draw_square3(size= 100, position_top= 30, position_left= 170, text1 = text_ズレ上_Y, text2 = text_ズレ下_Y, text_G1 = text_梁名_Y, text_XY = X_F1, text_0 = text_段差_Y) #black
                                                                            #,text1, text2,text_G1, text_XY, text_0
                            draw_square1(size= 45, position_top= 52, position_left= 388)
                            draw_square1(size= 45, position_top= 35, position_left= 88)

                            draw_horizontal_line(length= 500, position_top= 0, position_left= 10) #red
                            draw_vertical_line(length= 180, position_top= -75, position_left= 110) #blue
                            draw_vertical_line(length= 180, position_top= -90, position_left= 410) #blue  
            for y in range(1,numberY+1):
                for x in range(1,numberX):
                    with st.expander(session[str(k)+"F"] + " " +"Y"+str(y)+"通り "+ "X"+str(x)+"-"+"X"+str(x+1)+"間"):
                        colB4, colB1,colB2, colB3 = st.columns([1,1,1,1])
                        with colB1:
                            session["0F" +"Y"+str(y)+"通り "+ "X"+str(x)+"-"+"X"+str(x+1)+"間"+"上"] = 300 ##
                            session["0F" +"Y"+str(y)+"通り "+ "X"+str(x)+"-"+"X"+str(x+1)+"間"+"下"] = 300 ##
                            X1_F2 = session["X"+str(x)]
                            X2_F2 = session["X"+str(x+1)] # ,X1_F2, X2_F2, Y_F2,
                            Y_F2 = session["Y"+str(y)]

                            session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"梁名"]=st.text_input(session[str(k)+"F"]+" "+"Y"+str(y)+"通り "+session["X"+str(x)]+"-"+session["X"+str(x+1)]+"間"+"の梁の符号は","G1")
                            text_梁名_X = session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"梁名"] # # text_段差_X, text_ズレ上_X , text_ズレ下_X, text_梁名_X
                            session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"段差"]=st.text_input(session[str(k)+"F"]+" "+"Y"+str(y)+"通り "+session["X"+str(x)]+"-"+session["X"+str(x+1)]+"間"+" = "+session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"梁名"]+"の梁の段差は",0)
                            text_段差_X = session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"段差"] # text_梁名_X
                            session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"上"] = st.text_input(session[str(k)+"F"]+" "+"Y"+str(y)+"通り "+session["X"+str(x)]+"-"+session["X"+str(x+1)]+"間"+"の上側、"+session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"梁名"]+"がズレ ",session[session[str(k-1)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"上"])
                            text_ズレ上_X = session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"上"] # text_ズレ上_X
                            session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"下"] = st.text_input(session[str(k)+"F"]+" "+"Y"+str(y)+"通り "+session["X"+str(x)]+"-"+session["X"+str(x+1)]+"間"+"の下側、"+session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"梁名"]+"がズレ ",session[session[str(k-1)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"下"])
                            text_ズレ下_X = session[session[str(k)+"F"]+"Y"+str(y)+"通り "+"X"+str(x)+"-"+"X"+str(x+1)+"間"+"下"] # text_ズレ下_X
                        with colB2: 
                                #fig = create_grid(numberX - numberX + 2, numberY - numberY + 2,number_Y, number_X,Y_F,X_F,X1_F2, X2_F2, Y_F2,'', '', '','','','','','',text_段差_X, text_ズレ上_X , text_ズレ下_X, text_梁名_X,'', '' , '', '','', '' , '', '',)
                                #st.pyplot(fig)
                                st.markdown("<br>" * 2, unsafe_allow_html=True)
                                draw_square(size= 120, position_top= 60, position_left= 50, text= X1_F2)
                                draw_square(size= 120, position_top= 44, position_left= 350, text= X2_F2)
                                draw_square3(size= 100, position_top= 30, position_left= 170, text1 = text_ズレ上_X, text2 = text_ズレ下_X, text_G1 = text_梁名_X, text_XY = Y_F2, text_0 = text_段差_X) #black
                                                                                #,text1, text2,text_G1, text_XY, text_0
                                draw_square1(size= 45, position_top= 52, position_left= 388)
                                draw_square1(size= 45, position_top= 35, position_left= 88)

                                draw_horizontal_line(length= 500, position_top= 0, position_left= 10) #red
                                draw_vertical_line(length= 180, position_top= -75, position_left= 110) #blue
                                draw_vertical_line(length= 180, position_top= -90, position_left= 410) #blue 
        st.write("---")

###############################################################################################################################
    ############################################## 梁リストを入力##############################################

########### BUTTON #############
    button = st.checkbox("OFF")
    if button:
        session["off_button"] = True  
    else:
        session["off_button"] = False
###################################
    st.write("梁リストを入力")
    list_steel = ["SD295","SD345","SD390","SD490","ウルボン"]
    list_shape = ["1","2","3","4","5"]
    if (session["add_hari"] == False) & (session["edit_hari"] == False):
        if "selected_number" not in session:
            session['selected_number'] = session["LIST_KAI"][0]
        session["selected_kai"] = st.selectbox("階を選択",session["LIST_KAI"],index=session["LIST_KAI"].index(session["selected_number"]),key = 'new_number',on_change = number_callback)
        st.button("梁を追加", on_click=add_hari)
    selected_kai = session["selected_kai"]
    if (selected_kai + "hari_collection") not in session:
        session[selected_kai + "hari_collection"] = []
    hari_collection = session[selected_kai + "hari_collection"]
    if session["add_hari"] == True:
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col4:
            #################################################### 梁符号 #####################################################
            if str('_'+session["selected_kai"]+"梁符号"+str(session["click"])) not in session:
                session['_'+session["selected_kai"]+"梁符号"+str(session["click"])]=''
            session[session["selected_kai"]+"梁符号"+str(session["click"])] = session['_'+session["selected_kai"]+"梁符号"+str(session["click"])]
            session[session["selected_kai"]+"_"+"梁符号"] = st.text_input("梁符号",key=session["selected_kai"]+"梁符号"+str(session["click"]),on_change=keeper,args=[session["selected_kai"]+"梁符号"+str(session["click"])])
            hari_data = session[session["selected_kai"]+"_"+"梁符号"]
        if (hari_data == ""):       ######################
                st.warning("梁符号を入力してください。")
        if (hari_data in hari_collection):
                st.error("入力された梁符号は既に存在します。別の符号を入力してください。")
        if (hari_data != "") & (hari_data not in hari_collection):      ######################
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns(15)
            with col14:
                add = st.button("追加", on_click=OK_add,args=(hari_data,hari_collection))
            with col15:
                cancle = st.button("キャンセル", on_click=cancel_add)

    if (session["add_hari"] == False) & (session["edit_hari"] == False):
        st.write("登録済梁の一覧") 
        for hari_data in hari_collection:
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
            with col4:
                    st.write(hari_data)
            with col6:
                    st.button(":pencil: 編集", key=f"edit_{hari_data}", on_click=edit_hari, args=(hari_data, ))
            with col8:
                    st.button("🗑️ 削除", key=f"del_{hari_data}", on_click=remove_hari, args=(hari_data,hari_collection))

    if session["edit_hari"] == True:
        session[session["selected_kai"]+"梁符号"] = session["HARI"]     ######################
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"] = list_steel[2]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"] = list_steel[2]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"] = list_steel[2]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"] = list_steel[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"] = list_steel[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"] = list_steel[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"] = list_steel[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"] = list_steel[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"] = list_steel[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"] = list_shape[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"] = list_shape[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"] = list_shape[0]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"] = list_shape[1]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"] = list_shape[1]
        if (session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected") not in session:
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"] = list_shape[1]
        col1, col2, col3, col4 = st.columns(4)
        with col4:
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"全断面") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"全断面"]=False
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"全断面"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"全断面"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"全断面"] = st.toggle('全断面',key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"全断面",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"全断面"])
            on = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"全断面"]
            if on: 
                session["zen_danmen"] = True
            else: 
                session["zen_danmen"] = False

        with col2:
            if on:
                st.subheader("全断面")
            else:
                st.subheader("中央") 
            #################################################### 中央 幅 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"幅"]=st.text_input("梁幅",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"])
            #################################################### 中央 成 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"成"]=st.text_input("梁成",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"])
            #################################################### 中央 主筋径 #####################################################
            Col1, Col2 = st.columns(2)
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"主筋径"]=st.text_input("主筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"])
            #################################################### 中央 主筋材質 #####################################################
            with Col2:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"主筋材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"new",on_change = STEEL_callback)
            #################################################### 中央 上筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"上筋本数"]=st.text_input("上筋本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"])
            #################################################### 中央 上宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"上宙1"]=st.text_input("上宙1",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"])
            #################################################### 中央 上宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"上宙2"]=st.text_input("上宙2",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"])
            #################################################### 中央 下宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"下宙2"]=st.text_input("下宙2",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"])
            #################################################### 中央 下宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"下宙1"]=st.text_input("下宙1",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"])
            #################################################### 中央 下筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"下筋本数"]=st.text_input("下筋本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 中央 スタラップ径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"スタラップ径"]=st.text_input("ｽﾀﾗｯﾌﾟ径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"])
            #################################################### 中央 スタラップ ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"ピッチ"]=st.text_input("ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"])
            #################################################### 中央 スタラップ 材質 #####################################################
            with Col3:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"スタラップ材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"new",on_change = steel_callback)
            Col1, Col2 = st.columns(2)
            #################################################### 中央 スタラップ 形 #####################################################
            with Col1:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"スタラップ形"] = st.selectbox("ｽﾀﾗｯﾌﾟ形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"new",on_change = shape_callback)
            #################################################### 中央 CAP径 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"CAP径"]=st.text_input("CAP径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 中央 中子径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子径"]=st.text_input("中子筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"])
            #################################################### 中央 中子ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子ピッチ"]=st.text_input("ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"])
            #################################################### 中央 中子材質 #####################################################
            with Col3:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"new",on_change = Steel_callback)
            Col1, Col2 = st.columns(2)
            #################################################### 中央 中子形 #####################################################
            with Col1:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子形"] = st.selectbox("中子筋形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"new",on_change = shape_callback)
            #################################################### 中央 中子本数 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子本数"]=st.text_input("本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"])
        with col1:
            st.subheader("端部1",) 
            #################################################### 端部1 幅 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"幅"]=st.text_input("梁幅",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"],disabled=session["zen_danmen"])
            #################################################### 端部1 成 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]
            else:    
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"成"]=st.text_input("梁成",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"],disabled=session["zen_danmen"])
            #################################################### 端部1 主筋径 #####################################################
            Col1, Col2 = st.columns(2)
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"主筋径"]=st.text_input("主筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"],disabled=session["zen_danmen"])
            #################################################### 端部1 主筋材質 #####################################################
            with Col2:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"主筋材質"] = st.selectbox("主筋材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"主筋材質"] = st.selectbox("主筋材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
            #################################################### 端部1 上筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"上筋本数"]=st.text_input("上筋本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"],disabled=session["zen_danmen"])
            #################################################### 端部1 上宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"上宙1"]=st.text_input("上宙1",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"],disabled=session["zen_danmen"])
            #################################################### 端部1 上宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"上宙2"]=st.text_input("上宙2",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"],disabled=session["zen_danmen"])
            #################################################### 端部1 下宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"下宙2"]=st.text_input("下宙2",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"],disabled=session["zen_danmen"])
            #################################################### 端部1 下宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"下宙1"]=st.text_input("下宙1",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"],disabled=session["zen_danmen"])
            #################################################### 端部1 下筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"下筋本数"]=st.text_input("下筋本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部1 スタラップ 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ径"]=st.text_input("ｽﾀﾗｯﾌﾟ径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"],disabled=session["zen_danmen"])
            #################################################### 端部1 スタラップ ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"ピッチ"]=st.text_input("ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部1 スタラップ 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部1 スタラップ 形 #####################################################
            with Col1:
                if on :
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ形"] = st.selectbox("ｽﾀﾗｯﾌﾟ形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ形"] = st.selectbox("ｽﾀﾗｯﾌﾟ形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部1 CAP 径 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"CAP径"]=st.text_input("CAP径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部1 中子 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子径"]=st.text_input("中子筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"],disabled=session["zen_danmen"])
            #################################################### 端部1 中子 ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子ピッチ"]=st.text_input("ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部1 中子 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部1 中子 形 #####################################################
            with Col1:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子形"] = st.selectbox("中子筋形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子形"] = st.selectbox("中子筋形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部1 中子 本数 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子本数"]=st.text_input("本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"],disabled=session["zen_danmen"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"腹筋径"]=st.text_input("腹筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"腹筋本数"]=st.text_input("腹筋本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"幅止筋径"]=st.text_input("幅止筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"幅止筋ﾋﾟｯﾁ"]=st.text_input("幅止筋ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"])
        with col3:
            st.subheader("端部2",) 
            #################################################### 端部2 幅 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"幅"]=st.text_input("梁幅",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"],disabled=session["zen_danmen"])
            #################################################### 端部2 成 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]
            else:    
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"成"]=st.text_input("梁成",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"],disabled=session["zen_danmen"])
            #################################################### 端部2 主筋径 #####################################################
            Col1, Col2 = st.columns(2)
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"主筋径"]=st.text_input("主筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"],disabled=session["zen_danmen"])
            #################################################### 端部2 主筋材質 #####################################################
            with Col2:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"主筋材質"] = st.selectbox("主筋材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"主筋材質"] = st.selectbox("主筋材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
            #################################################### 端部2 上筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"上筋本数"]=st.text_input("上筋本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"],disabled=session["zen_danmen"])
            #################################################### 端部2 上宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"上宙1"]=st.text_input("上宙1",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"],disabled=session["zen_danmen"])
            #################################################### 端部2 上宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"上宙2"]=st.text_input("上宙2",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"],disabled=session["zen_danmen"])
            #################################################### 端部2 下宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"下宙2"]=st.text_input("下宙2",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"],disabled=session["zen_danmen"])
            #################################################### 端部2 下宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"下宙1"]=st.text_input("下宙1",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"],disabled=session["zen_danmen"])
            #################################################### 端部2 下筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"下筋本数"]=st.text_input("下筋本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部2 スタラップ 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ径"]=st.text_input("ｽﾀﾗｯﾌﾟ径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"],disabled=session["zen_danmen"])
            #################################################### 端部2 スタラップ ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"ピッチ"]=st.text_input("ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部2 スタラップ 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部2 スタラップ 形 #####################################################
            with Col1:
                if on :
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ形"] = st.selectbox("ｽﾀﾗｯﾌﾟ形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ形"] = st.selectbox("ｽﾀﾗｯﾌﾟ形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部2 CAP 径 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"CAP径"]=st.text_input("CAP径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部2 中子 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子径"]=st.text_input("中子筋径",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"],disabled=session["zen_danmen"])
            #################################################### 端部2 中子 ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子ピッチ"]=st.text_input("ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部2 中子 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子材質"] = st.selectbox("材質",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部2 中子 形 #####################################################
            with Col1:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子形"] = st.selectbox("中子筋形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子形"] = st.selectbox("中子筋形",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部2 中子 本数 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子本数"]=st.text_input("本数",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"],disabled=session["zen_danmen"])   
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns(15)
        with col14:
            ok = st.button("更新", on_click=OK_edit)
###############################################################################################################################

if __name__ == "__main__":
    main()

