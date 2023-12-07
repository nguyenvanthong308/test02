import streamlit as st
from qsketchmetric.renderer import Renderer
from ezdxf import new
from ezdxf import units
from ezdxf.addons import Importer
from ezdxf.addons.drawing import Frontend, RenderContext, pymupdf, layout, config
from PIL import Image
import plotly.express as px
import io
session = st.session_state
st.set_page_config(
    layout= "wide",
    )
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
if "span_before_Y" not in session: 
    session["span_before_Y"] = 0
if "span_before_X" not in session: 
    session["span_before_X"] = 0    


def tsugite_callback():
    session["継手 上筋"] = session.new_継手_上筋
    session["継手 下筋"] = session.new_継手_下筋

def number_callback():
    session["selected_number"] = session.new_number
    session["selected_NUMBER"] = session.new_NUMBER
    session["selected_DOORI"] = session.new_DOORI
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

def generate_image(output_dxf_1):
    msp = output_dxf_1.modelspace()
    # 1. create the render context
    context = RenderContext(output_dxf_1)
    # 2. create the backend
    backend = pymupdf.PyMuPdfBackend()
    # 3. create and configure the frontend
    cfg = config.Configuration(background_policy=config.BackgroundPolicy.WHITE)
    frontend = Frontend(context, backend, config=cfg)
    # 4. draw the modelspace
    frontend.draw_layout(msp)
    # 5. create an A4 page layout
    page = layout.Page(297, 210, layout.Units.mm, margins=layout.Margins.all(20))
    # 6. get the PNG rendering as bytes
    png_bytes = backend.get_pixmap_bytes(page, fmt="png", dpi=1000)

    # Tạo hình ảnh với Pillow
    image = Image.open(io.BytesIO(png_bytes))

    # Thay thế st.image bằng biểu đồ Plotly
    fig = px.imshow(image)
    fig.update_layout(title='Sample image', width=1000, height=800)  # Điều chỉnh kích thước ở đây
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    st.plotly_chart(fig)

def download_pdf(output_dxf_1):
    msp = output_dxf_1.modelspace()
    # 1. create the render context
    context = RenderContext(output_dxf_1)
    # 2. create the backend
    backend = pymupdf.PyMuPdfBackend()
    # 3. create and configure the frontend
    cfg = config.Configuration(background_policy=config.BackgroundPolicy.WHITE)
    frontend = Frontend(context, backend, config=cfg)
    # 4. draw the modelspace
    frontend.draw_layout(msp)
    # 5. create an A4 page layout
    page = layout.Page(297, 210, layout.Units.mm, margins=layout.Margins.all(2))
    # 6. get the PDF rendering as bytes
    pdf_bytes = backend.get_pdf_bytes(page)
    btn_pdf = st.download_button(
    label="Download PDF",
    data=pdf_bytes,
    file_name="output_01.pdf")
 
def download_dxf(output_dxf_1):
    output_dxf_1.saveas("output_02.dxf")
    with open("output_02.dxf") as file:
        btn_dxf = st.download_button(
        label="Download DXF",
        data=file,
        file_name="Output_02.dxf",
        )


def main():
    #################################### INPUT #######################################
    list_doori = list()
    list_dooriY = list()
    list_dooriX = list()
    numberY = st.number_input('水平方向の通りの数量', min_value=1, max_value=50, value=2, step=1)
    for y in range(1,numberY+1):
        session["Y"+str(y)] = st.text_input("水平方向の通りの名称 No."+str(y),"Y"+str(y))
        list_dooriY.append(session["Y"+str(y)])
        list_doori.append(session["Y"+str(y)])

    numberX = st.number_input('鉛直方向の通りの数量', min_value=1, max_value=20, value=3, step=1)
    for x in range(1,numberX+1):
        session["X"+str(x)] = st.text_input("鉛直方向の通りの名称 No."+str(x),"X"+str(x))
        list_dooriX.append(session["X"+str(x)])
        list_doori.append(session["X"+str(x)])

    for y in range(1,numberY):
        session["Y"+str(y)+"-"+"Y"+str(y+1)]=st.text_input(session["Y"+str(y)]+"-"+session["Y"+str(y+1)],"11200")

    for x in range(1,numberX):
        session["X"+str(x)+"-"+"X"+str(x+1)]=st.text_input(session["X"+str(x)]+"-"+session["X"+str(x+1)],"6500")
    kai = st.number_input('階数を入力', min_value=1, max_value=50, value=2, step=1)
    list_kai = list()
    for k in range(1,kai+1):
            session[str(k)+"F"] = st.text_input("階の符号 No."+str(k),str(k)+"F")
            list_kai.append(session[str(k)+"F"])
    st.write(":blue[階・通りに対して柱の「符号・ズレ寸法」を入力]")
    input_variables =list()
    session["Y"+str(0)+"-"+"Y"+str(1)]= 0 #khai bao span Y0-Y1 dau tien = 0
    session["X"+str(0)+"-"+"X"+str(1)] = 0 #khai bao span X0-x1 dau tien = 0
    for k in range(1,kai+1):
        for a,b in ((y,x) for y in range(1,numberY+1) for x in range(1,numberX+1)):
            with st.expander(session[str(k)+"F"] + " " + "Y"+str(a)+"-"+"X"+str(b)):
                session[str(0)+"F"] = "0F" ##
                session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"柱名"] = "C0" ##
                session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の柱の符号は", session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"])
                col1, col2 = st.columns(2)
                session["input_variables_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)]= {'h': 15000}
                session["input_variables_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)]= {'h': 15000}
                with col1:
                    session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"左"] = 500 ##
                    session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"下"] = 500 ##
                    session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(0)+"左"] = 0
                    session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(0)+"下"] = 0
                    session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"左"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の左側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"左"])
                    session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"下"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の下側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"下"])

                with col2:
                    session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"右"] = 500 ##
                    session["0F" + "Y"+str(a)+"-"+"X"+str(b)+"上"] = 500 ##
                    session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"右"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の右側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"右"])
                    session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"上"] = st.text_input(session[str(k)+"F"] + " " + session["Y"+str(a)]+"-"+session["X"+str(b)] + "の上側、"+session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"柱名"]+"がズレ ",session[session[str(k-1)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"上"])
                
                session["input_variables_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)]["trai"] = int(session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"左"])  # cho truc Y
                session["input_variables_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)]["trai"] = int(session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"下"])  # cho truc X

                session["input_variables_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)]["trai_before"] = int(session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(1)+"左"]) # cho truc Y ###### trai dau tien o X1
                session["input_variables_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)]["trai_before"] = int(session[session[str(k)+"F"] + "Y"+str(1)+"-"+"X"+str(b)+"下"]) # cho truc X ###### trai dau tien o Y1

                session["span_before_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(0)] = 0 #khai bao span before cho truc X0 dau tien = 0 # cho truc Y
                session["input_variables_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)]["span_before"] = int(session["X"+str(b-1)+"-"+"X"+str(b)]) + int(session["span_before_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b-1)]) # cho truc Y
                session["span_before_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)] = session["input_variables_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)]["span_before"] # cho truc Y
                
                session["span_before_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(0)] = 0 #khai bao span before cho truc Y0 dau tien = 0 # cho truc X
                session["input_variables_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)]["span_before"] = int(session["Y"+str(a-1)+"-"+"Y"+str(a)]) + int(session["span_before_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a-1)]) # cho truc X
                session["span_before_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)] = session["input_variables_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)]["span_before"] # cho truc X

                session["input_variables_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)]["phai"] = int(session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"右"]) # cho truc Y
                session["input_variables_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)]["phai"] = int(session[session[str(k)+"F"] + "Y"+str(a)+"-"+"X"+str(b)+"上"]) # cho truc X

                session["input_variables_"+session[str(k)+"F"]+"Y"+str(a)+"X"+str(b)]["doori"] = session["X"+str(b)] # cho truc Y
                session["input_variables_"+session[str(k)+"F"]+"X"+str(b)+"Y"+str(a)]["doori"] = session["Y"+str(a)] # cho truc X

        for y in range(1,numberY+1):  # tat ca cho truc Y 
            for x in range(1,numberX):
                session["input_variables_"+session[str(k)+"F"]+"Y"+str(y)+"X"+str(x)]["TRAI"] = int(session[session[str(k)+"F"] + "Y"+str(y)+"-"+"X"+str(x)+"右"]) #trai cua nhip X1-X2 la phai cua X1, nen cong thuc la (x)+"右"

                session["input_variables_"+session[str(k)+"F"]+"Y"+str(y)+"X"+str(x)]["PHAI"] = int(session[session[str(k)+"F"] + "Y"+str(y)+"-"+"X"+str(x+1)+"左"])  #phai cua nhip X1-X2 la trai cua X2, nen cong thuc la (x+1)+"左"
                
                session["input_variables_"+session[str(k)+"F"]+"Y"+str(y)+"X"+str(x)]["SPAN"] = int(session["X"+str(x)+"-"+"X"+str(x+1)]) #co 2 nhip thi tinh tu truc X1,X2
        for x in range(1,numberX+1): # tat ca cho truc X 
            for y in range(1,numberY):
                session["input_variables_"+session[str(k)+"F"]+"X"+str(x)+"Y"+str(y)]["TRAI"] = int(session[session[str(k)+"F"] + "Y"+str(y)+"-"+"X"+str(x)+"上"]) #trai cua nhip Y1-Y2 la phai cua Y1, nen cong thuc la (y)..."上"

                session["input_variables_"+session[str(k)+"F"]+"X"+str(x)+"Y"+str(y)]["PHAI"] = int(session[session[str(k)+"F"] + "Y"+str(y+1)+"-"+"X"+str(x)+"下"]) #phai cua nhip Y1-Y2 la trai cua Y2, nen cong thuc la (y+1)..."下"

                session["input_variables_"+session[str(k)+"F"]+"X"+str(x)+"Y"+str(y)]["SPAN"] = int(session["Y"+str(y)+"-"+"Y"+str(y+1)]) #co 1 nhip thi tinh tu truc Y1

    st.write("---")

    ############################################## 梁リストを入力##############################################
    st.write(":blue[梁リストを入力]")
    list_steel = ["SD295","SD345","SD390","SD490","ウルボン"]
    list_shape = ["1","2","3","4","5"]
    if (session["add_hari"] == False) & (session["edit_hari"] == False):
        if "selected_number" not in session:
            session['selected_number'] = list_kai[0]
        session["selected_kai"] = st.selectbox("階を選択",list_kai,index=list_kai.index(session["selected_number"]),key = 'new_number',on_change = number_callback)
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
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"幅"]=st.text_input(":green[梁幅]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"])
            #################################################### 中央 成 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"成"]=st.text_input(":green[梁成]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"])
            #################################################### 中央 主筋径 #####################################################
            Col1, Col2 = st.columns(2)
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"主筋径"]=st.text_input(":green[主筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"])
            #################################################### 中央 主筋材質 #####################################################
            with Col2:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"主筋材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"new",on_change = STEEL_callback)
            #################################################### 中央 上筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"上筋本数"]=st.text_input(":green[上筋本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"])
            #################################################### 中央 上宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"上宙1"]=st.text_input(":green[上宙1]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"])
            #################################################### 中央 上宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"上宙2"]=st.text_input(":green[上宙2]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"])
            #################################################### 中央 下宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"下宙2"]=st.text_input(":green[下宙2]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"])
            #################################################### 中央 下宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"下宙1"]=st.text_input(":green[下宙1]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"])
            #################################################### 中央 下筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"下筋本数"]=st.text_input(":green[下筋本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 中央 スタラップ径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"スタラップ径"]=st.text_input(":green[ｽﾀﾗｯﾌﾟ径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"])
            #################################################### 中央 スタラップ ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"ピッチ"]=st.text_input("ﾋﾟｯﾁ",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"])
            #################################################### 中央 スタラップ 材質 #####################################################
            with Col3:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"スタラップ材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"new",on_change = steel_callback)
            Col1, Col2 = st.columns(2)
            #################################################### 中央 スタラップ 形 #####################################################
            with Col1:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"スタラップ形"] = st.selectbox(":green[ｽﾀﾗｯﾌﾟ形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"new",on_change = shape_callback)
            #################################################### 中央 CAP径 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"CAP径"]=st.text_input(":green[CAP径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 中央 中子径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子径"]=st.text_input(":green[中子筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"])
            #################################################### 中央 中子ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子ピッチ"]=st.text_input(":green[ﾋﾟｯﾁ]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"])
            #################################################### 中央 中子材質 #####################################################
            with Col3:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"new",on_change = Steel_callback)
            Col1, Col2 = st.columns(2)
            #################################################### 中央 中子形 #####################################################
            with Col1:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子形"] = st.selectbox(":green[中子筋形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"new",on_change = shape_callback)
            #################################################### 中央 中子本数 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]=''
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+"_"+"中子本数"]=st.text_input(":green[本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"])
        with col1:
            st.subheader("端部1",) 
            #################################################### 端部1 幅 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"幅"]=st.text_input(":green[梁幅]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"幅"],disabled=session["zen_danmen"])
            #################################################### 端部1 成 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]
            else:    
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"成"]=st.text_input(":green[梁成]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"成"],disabled=session["zen_danmen"])
            #################################################### 端部1 主筋径 #####################################################
            Col1, Col2 = st.columns(2)
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"主筋径"]=st.text_input(":green[主筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋径"],disabled=session["zen_danmen"])
            #################################################### 端部1 主筋材質 #####################################################
            with Col2:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"主筋材質"] = st.selectbox(":green[主筋材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"主筋材質"] = st.selectbox(":green[主筋材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
            #################################################### 端部1 上筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"上筋本数"]=st.text_input(":green[上筋本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上筋本数"],disabled=session["zen_danmen"])
            #################################################### 端部1 上宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"上宙1"]=st.text_input(":green[上宙1]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙1"],disabled=session["zen_danmen"])
            #################################################### 端部1 上宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"上宙2"]=st.text_input(":green[上宙2]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"上宙2"],disabled=session["zen_danmen"])
            #################################################### 端部1 下宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"下宙2"]=st.text_input(":green[下宙2]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙2"],disabled=session["zen_danmen"])
            #################################################### 端部1 下宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"下宙1"]=st.text_input(":green[下宙1]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下宙1"],disabled=session["zen_danmen"])
            #################################################### 端部1 下筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"下筋本数"]=st.text_input(":green[下筋本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"下筋本数"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部1 スタラップ 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ径"]=st.text_input(":green[ｽﾀﾗｯﾌﾟ径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ径"],disabled=session["zen_danmen"])
            #################################################### 端部1 スタラップ ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"ピッチ"]=st.text_input(":green[ﾋﾟｯﾁ]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部1 スタラップ 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部1 スタラップ 形 #####################################################
            with Col1:
                if on :
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ形"] = st.selectbox(":green[ｽﾀﾗｯﾌﾟ形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"スタラップ形"] = st.selectbox(":green[ｽﾀﾗｯﾌﾟ形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部1 CAP 径 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"CAP径"]=st.text_input(":green[CAP径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"CAP径"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部1 中子 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子径"]=st.text_input(":green[中子筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子径"],disabled=session["zen_danmen"])
            #################################################### 端部1 中子 ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子ピッチ"]=st.text_input(":green[ﾋﾟｯﾁ]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部1 中子 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部1 中子 形 #####################################################
            with Col1:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子形"] = st.selectbox(":green[中子筋形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子形"] = st.selectbox(":green[中子筋形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部1 中子 本数 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+"_"+"中子本数"]=st.text_input(":green[本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部1"+" "+"中子本数"],disabled=session["zen_danmen"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"腹筋径"]=st.text_input(":green[腹筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋径"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"腹筋本数"]=st.text_input(":green[腹筋本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"腹筋本数"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"幅止筋径"]=st.text_input(":green[幅止筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋径"])
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"]=''
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+"_"+"幅止筋ﾋﾟｯﾁ"]=st.text_input(":green[幅止筋ﾋﾟｯﾁ]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"幅止筋ﾋﾟｯﾁ"])
        with col3:
            st.subheader("端部2",) 
            #################################################### 端部2 幅 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"幅"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"幅"]=st.text_input(":green[梁幅]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"幅"],disabled=session["zen_danmen"])
            #################################################### 端部2 成 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"成"]
            else:    
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"成"]=st.text_input(":green[梁成]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"成"],disabled=session["zen_danmen"])
            #################################################### 端部2 主筋径 #####################################################
            Col1, Col2 = st.columns(2)
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"主筋径"]=st.text_input(":green[主筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋径"],disabled=session["zen_danmen"])
            #################################################### 端部2 主筋材質 #####################################################
            with Col2:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"主筋材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"主筋材質"] = st.selectbox(":green[主筋材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"主筋材質"] = st.selectbox(":green[主筋材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"主筋材質"+"new",on_change = STEEL_callback,disabled=session["zen_danmen"])
            #################################################### 端部2 上筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"上筋本数"]=st.text_input(":green[上筋本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上筋本数"],disabled=session["zen_danmen"])
            #################################################### 端部2 上宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"上宙1"]=st.text_input(":green[上宙1]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙1"],disabled=session["zen_danmen"])
            #################################################### 端部2 上宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"上宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"上宙2"]=st.text_input(":green[上宙2]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"上宙2"],disabled=session["zen_danmen"])
            #################################################### 端部2 下宙2 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙2"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"下宙2"]=st.text_input(":green[下宙2]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙2"],disabled=session["zen_danmen"])
            #################################################### 端部2 下宙1 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下宙1"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"下宙1"]=st.text_input(":green[下宙1]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下宙1"],disabled=session["zen_danmen"])
            #################################################### 端部2 下筋本数 #####################################################
            if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数") not in session:
                session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"]=''
            if on:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"下筋本数"]
            else:
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"]
            session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"下筋本数"]=st.text_input(":green[下筋本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"下筋本数"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部2 スタラップ 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ径"]=st.text_input(":green[ｽﾀﾗｯﾌﾟ径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ径"],disabled=session["zen_danmen"])
            #################################################### 端部2 スタラップ ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"ピッチ"]=st.text_input(":green[ﾋﾟｯﾁ]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部2 スタラップ 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ材質"+"new",on_change = steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部2 スタラップ 形 #####################################################
            with Col1:
                if on :
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"スタラップ形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ形"] = st.selectbox(":green[ｽﾀﾗｯﾌﾟ形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"スタラップ形"] = st.selectbox(":green[ｽﾀﾗｯﾌﾟ形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"スタラップ形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部2 CAP 径 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"CAP径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"CAP径"]=st.text_input(":green[CAP径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"CAP径"],disabled=session["zen_danmen"])
            Col1, Col2, Col3 = st.columns(3)
            #################################################### 端部2 中子 径 #####################################################
            with Col1:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子径"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子径"]=st.text_input(":green[中子筋径]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子径"],disabled=session["zen_danmen"])
            #################################################### 端部2 中子 ピッチ #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子ピッチ"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子ピッチ"]=st.text_input(":green[ﾋﾟｯﾁ]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子ピッチ"],disabled=session["zen_danmen"])
            #################################################### 端部2 中子 材質 #####################################################
            with Col3:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子材質"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子材質"] = st.selectbox(":green[材質]",list_steel,index=list_steel.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子材質"+"new",on_change = Steel_callback,disabled=session["zen_danmen"])
            Col1, Col2 = st.columns(2)
            #################################################### 端部2 中子 形 #####################################################
            with Col1:
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子形"+"selected"]
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子形"] = st.selectbox(":green[中子筋形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子形"] = st.selectbox(":green[中子筋形]",list_shape,index=list_shape.index(session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"selected"]),key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子形"+"new",on_change = shape_callback,disabled=session["zen_danmen"])
            #################################################### 端部2 中子 本数 #####################################################
            with Col2:
                if str('_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数") not in session:
                    session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"]=''
                if on:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"] = session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"中央"+" "+"中子本数"]
                else:
                    session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"] = session['_'+session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"]
                session[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+"_"+"中子本数"]=st.text_input(":green[本数]",key=session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数",on_change=keeper,args=[session["selected_kai"]+" "+session[session["selected_kai"]+"梁符号"]+" "+"端部2"+" "+"中子本数"],disabled=session["zen_danmen"])   
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns(15)
        with col14:
            ok = st.button("更新", on_click=OK_edit)
    ############################################## 梁計算値設定 ##############################################
    st.write("---")
    st.write(":blue[施工図を作成]")
    if (session["add_hari"] == False) & (session["edit_hari"] == False):
        if "selected_NUMBER" not in session:
            session['selected_NUMBER'] = list_kai[0]
        if "selected_DOORI" not in session:
            session['selected_DOORI'] = list_doori[0]
        col1, col2 = st.columns(2)
        with col1:
            session["selected_KAI"] = st.selectbox("階を選択",list_kai,index=list_kai.index(session["selected_NUMBER"]),key = 'new_NUMBER',on_change = number_callback)
    
        with col2:
            session["selected_DOORI"] = st.selectbox("通を選択",list_doori,index=list_doori.index(session["selected_DOORI"]),key = 'new_DOORI',on_change = number_callback)
    selected_KAI = session["selected_KAI"]
    st.write(selected_KAI)
    selected_DOORI = session["selected_DOORI"]
    st.write(selected_DOORI)
    if selected_DOORI in list_dooriY:
        for x in range(1,numberX+1):
            input_variables.append(session["input_variables_"+selected_KAI+selected_DOORI+"X"+str(x)])
    else: 
        for y in range(1,numberY+1):
            input_variables.append(session["input_variables_"+selected_KAI+selected_DOORI+"Y"+str(y)])
    st.write(input_variables)
    _input_variables = input_variables[:-1]
    st.write(_input_variables)
    output_dxf_1 = new()
    output_dxf_1.units = units.MM
    output_dxf_1.header['$INSUNITS'] = units.MM
    # create target layout
    tblock = output_dxf_1.blocks.new('SOURCE_ENTS')
    for input in input_variables:
    #################################### DXF_2 ##############################################################################
        output_dxf_2 = new()
        output_dxf_2.units = units.MM
        # which is a shortcut (including validation) for
        output_dxf_2.header['$INSUNITS'] = units.MM
        renderer = Renderer('DXFmoi3.dxf', output_dxf_2, input)
        renderer.render()
        msp_2 = output_dxf_2.modelspace()

        #################################### trai #######################################
        # Collect all anonymous block references starting with '-trai_dim'
        trai_dim = msp_2.query('INSERT[name ? "^\-trai_dim.+"]')
        # Collect the references of the 'trai_dim' block
        for trai_dim_block_ref in trai_dim:
            # Get the block layout of the anonymous block
            trai_dim_attdef_block = output_dxf_2.blocks.get(trai_dim_block_ref.dxf.name)
            # Find all block references to 'trai_dim_attdef' in the anonymous block
            trai_dim_attdef = trai_dim_attdef_block.query('INSERT[name=="-trai_dim_attdef"]')
            if len(trai_dim_attdef):
                trai_dim_attdef_entity = trai_dim_attdef[0]
                for trai_dim_attdef_attrib in trai_dim_attdef_entity.attribs:
                    if trai_dim_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        trai_dim_attdef_attrib.dxf.text = input['trai']  # change attribute content

        #################################### phai #######################################
        # Collect all anonymous block references starting with '-phai_dim'
        phai_dim = msp_2.query('INSERT[name ? "^\-phai_dim.+"]')
        # Collect the references of the 'phai_dim' block
        for phai_dim_block_ref in phai_dim:
            # Get the block layout of the anonymous block
            phai_dim_attdef_block = output_dxf_2.blocks.get(phai_dim_block_ref.dxf.name)
            # Find all block references to 'phai_dim_attdef' in the anonymous block
            phai_dim_attdef = phai_dim_attdef_block.query('INSERT[name=="-phai_dim_attdef"]')
            if len(phai_dim_attdef):
                phai_dim_attdef_entity = phai_dim_attdef[0]
                for phai_dim_attdef_attrib in phai_dim_attdef_entity.attribs:
                    if phai_dim_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        phai_dim_attdef_attrib.dxf.text = input['phai']  # change attribute content

            #################################### doori #######################################
        # Collect all anonymous block references starting with '-doori'
        doori_text = msp_2.query('INSERT[name ? "^\-doori.+"]')
        # Collect the references of the 'doori' block
        for doori_block_ref in doori_text:
            # Get the block layout of the anonymous block
            doori_attdef_block = output_dxf_2.blocks.get(doori_block_ref.dxf.name)
            # Find all block references to 'doori_attdef' in the anonymous block
            doori_attdef = doori_attdef_block.query('INSERT[name=="-doori_attdef"]')
            if len(doori_attdef):
                doori_attdef_entity = doori_attdef[0]
                for doori_attdef_attrib in doori_attdef_entity.attribs:
                    if doori_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        doori_attdef_attrib.dxf.text = input['doori']  # change attribute content

        #################################### IMPORT ##############################################################################

        importer = Importer(output_dxf_2, output_dxf_1)

        # import all entities from source modelspace into modelspace of the target drawing
        importer.import_modelspace()

        # import all CIRCLE and LINE entities from source modelspace into an arbitrary target layout.
        # query source entities
        ents = output_dxf_2.modelspace().query('CIRCLE LINE')
        # import source entities into target block
        importer.import_entities(ents, tblock)

        # This is ALWAYS the last & required step, without finalizing the target drawing is maybe invalid!
        # This step imports all additional required table entries and block definitions.
        importer.finalize()

    for _input in _input_variables:
    #################################### DXF_3 ##############################################################################
        output_dxf_3 = new()
        output_dxf_3.units = units.MM
        # which is a shortcut (including validation) for
        output_dxf_3.header['$INSUNITS'] = units.MM
        renderer = Renderer('DXFmoi4.dxf', output_dxf_3, _input)
        renderer.render()
        msp_3 = output_dxf_3.modelspace()

        #################################### span #######################################
        # Collect all anonymous block references starting with '-span_dim'
        span_dim = msp_3.query('INSERT[name ? "^\-span_dim.+"]')
        # Collect the references of the 'span_dim' block
        for span_dim_block_ref in span_dim:
            # Get the block layout of the anonymous block
            span_dim_attdef_block = output_dxf_3.blocks.get(span_dim_block_ref.dxf.name)
            # Find all block references to 'span_dim_attdef' in the anonymous block
            span_dim_attdef = span_dim_attdef_block.query('INSERT[name=="-span_dim_attdef"]')
            if len(span_dim_attdef):
                span_dim_attdef_entity = span_dim_attdef[0]
                for span_dim_attdef_attrib in span_dim_attdef_entity.attribs:
                    if span_dim_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_dim_attdef_attrib.dxf.text = _input['SPAN']  # change attribute content

        #################################### span_tong #######################################
        # Collect all anonymous block references starting with '-span_tong'
        span_tong = msp_3.query('INSERT[name ? "^\-span_tong.+"]')
        # Collect the references of the 'span_tong' block
        for span_tong_block_ref in span_tong:
            # Get the block layout of the anonymous block
            span_tong_attdef_block = output_dxf_3.blocks.get(span_tong_block_ref.dxf.name)
            # Find all block references to 'span_tong_attdef' in the anonymous block
            span_tong_attdef = span_tong_attdef_block.query('INSERT[name=="-span_tong_attdef"]')
            if len(span_tong_attdef):
                span_tong_attdef_entity = span_tong_attdef[0]
                for span_tong_attdef_attrib in span_tong_attdef_entity.attribs:
                    if span_tong_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_tong_attdef_attrib.dxf.text = (_input['SPAN']-_input['TRAI']-_input['PHAI'])  # change attribute content

            #################################### span_nhip1_dim #######################################
        # Collect all anonymous block references starting with '-span_nhip1_dim'
        span_nhip1_dim_text = msp_3.query('INSERT[name ? "^\-span_nhip1_dim.+"]')
        # Collect the references of the 'span_nhip1_dim' block
        for span_nhip1_dim_block_ref in span_nhip1_dim_text:
            # Get the block layout of the anonymous block
            span_nhip1_dim_attdef_block = output_dxf_3.blocks.get(span_nhip1_dim_block_ref.dxf.name)
            # Find all block references to 'span_nhip1_dim_attdef' in the anonymous block
            span_nhip1_dim_attdef = span_nhip1_dim_attdef_block.query('INSERT[name=="-span_nhip1_dim_attdef"]')
            if len(span_nhip1_dim_attdef):
                span_nhip1_dim_attdef_entity = span_nhip1_dim_attdef[0]
                for span_nhip1_dim_attdef_attrib in span_nhip1_dim_attdef_entity.attribs:
                    if span_nhip1_dim_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip1_dim_attdef_attrib.dxf.text = round((_input['SPAN']-_input['TRAI']-_input['PHAI'])/4)  # change attribute content

            #################################### span_nhip2_dim #######################################
        # Collect all anonymous block references starting with '-span_nhip2_dim'
        span_nhip2_dim_text = msp_3.query('INSERT[name ? "^\-span_nhip2_dim.+"]')
        # Collect the references of the 'span_nhip2_dim' block
        for span_nhip2_dim_block_ref in span_nhip2_dim_text:
            # Get the block layout of the anonymous block
            span_nhip2_dim_attdef_block = output_dxf_3.blocks.get(span_nhip2_dim_block_ref.dxf.name)
            # Find all block references to 'span_nhip2_dim_attdef' in the anonymous block
            span_nhip2_dim_attdef = span_nhip2_dim_attdef_block.query('INSERT[name=="-span_nhip2_dim_attdef"]')
            if len(span_nhip2_dim_attdef):
                span_nhip2_dim_attdef_entity = span_nhip2_dim_attdef[0]
                for span_nhip2_dim_attdef_attrib in span_nhip2_dim_attdef_entity.attribs:
                    if span_nhip2_dim_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip2_dim_attdef_attrib.dxf.text = round((_input['SPAN']-_input['TRAI']-_input['PHAI'])/2)  # change attribute content

                    #################################### span_nhip3_dim #######################################
        # Collect all anonymous block references starting with '-span_nhip3_dim'
        span_nhip3_dim_text = msp_3.query('INSERT[name ? "^\-span_nhip3_dim.+"]')
        # Collect the references of the 'span_nhip3_dim' block
        for span_nhip3_dim_block_ref in span_nhip3_dim_text:
            # Get the block layout of the anonymous block
            span_nhip3_dim_attdef_block = output_dxf_3.blocks.get(span_nhip3_dim_block_ref.dxf.name)
            # Find all block references to 'span_nhip3_dim_attdef' in the anonymous block
            span_nhip3_dim_attdef = span_nhip3_dim_attdef_block.query('INSERT[name=="-span_nhip3_dim_attdef"]')
            if len(span_nhip3_dim_attdef):
                span_nhip3_dim_attdef_entity = span_nhip3_dim_attdef[0]
                for span_nhip3_dim_attdef_attrib in span_nhip3_dim_attdef_entity.attribs:
                    if span_nhip3_dim_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip3_dim_attdef_attrib.dxf.text = round((_input['SPAN']-_input['TRAI']-_input['PHAI'])/4)  # change attribute content

        #################################### span_hari #######################################
        # Collect all anonymous block references starting with '-span_hari'
        span_hari = msp_3.query('INSERT[name ? "^\-span_hari.+"]')
        # Collect the references of the 'span_hari' block
        for span_hari_block_ref in span_hari:
            # Get the block layout of the anonymous block
            span_hari_attdef_block = output_dxf_3.blocks.get(span_hari_block_ref.dxf.name)
            # Find all block references to 'span_hari_attdef' in the anonymous block
            span_hari_attdef = span_hari_attdef_block.query('INSERT[name=="-span_hari_attdef"]')
            if len(span_hari_attdef):
                span_hari_attdef_entity = span_hari_attdef[0]
                for span_hari_attdef_attrib in span_hari_attdef_entity.attribs:
                    if span_hari_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_hari_attdef_attrib.dxf.text = "_input['hari']"  # change attribute content

        #################################### span_dansa #######################################
        # Collect all anonymous block references starting with '-span_dansa'
        span_dansa = msp_3.query('INSERT[name ? "^\-span_dansa.+"]')
        # Collect the references of the 'span_dansa' block
        for span_dansa_block_ref in span_dansa:
            # Get the block layout of the anonymous block
            span_dansa_attdef_block = output_dxf_3.blocks.get(span_dansa_block_ref.dxf.name)
            # Find all block references to 'span_dansa_attdef' in the anonymous block
            span_dansa_attdef = span_dansa_attdef_block.query('INSERT[name=="-span_dansa_attdef"]')
            if len(span_dansa_attdef):
                span_dansa_attdef_entity = span_dansa_attdef[0]
                for span_dansa_attdef_attrib in span_dansa_attdef_entity.attribs:
                    if span_dansa_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_dansa_attdef_attrib.dxf.text = "_input['dansa']"  # change attribute content

        #################################### span_WxH #######################################
        # Collect all anonymous block references starting with '-span_WxH'
        span_WxH = msp_3.query('INSERT[name ? "^\-span_WxH.+"]')
        # Collect the references of the 'span_WxH' block
        for span_WxH_block_ref in span_WxH:
            # Get the block layout of the anonymous block
            span_WxH_attdef_block = output_dxf_3.blocks.get(span_WxH_block_ref.dxf.name)
            # Find all block references to 'span_WxH_attdef' in the anonymous block
            span_WxH_attdef = span_WxH_attdef_block.query('INSERT[name=="-span_WxH_attdef"]')
            if len(span_WxH_attdef):
                span_WxH_attdef_entity = span_WxH_attdef[0]
                for span_WxH_attdef_attrib in span_WxH_attdef_entity.attribs:
                    if span_WxH_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_WxH_attdef_attrib.dxf.text = "_input['WxH']"  # change attribute content

        #################################### span_nhip1_top1 #######################################
        # Collect all anonymous block references starting with '-span_nhip1_top1'
        span_nhip1_top1 = msp_3.query('INSERT[name ? "^\-span_nhip1_top1.+"]')
        # Collect the references of the 'span_nhip1_top1' block
        for span_nhip1_top1_block_ref in span_nhip1_top1:
            # Get the block layout of the anonymous block
            span_nhip1_top1_attdef_block = output_dxf_3.blocks.get(span_nhip1_top1_block_ref.dxf.name)
            # Find all block references to 'span_nhip1_top1_attdef' in the anonymous block
            span_nhip1_top1_attdef = span_nhip1_top1_attdef_block.query('INSERT[name=="-span_nhip1_top1_attdef"]')
            if len(span_nhip1_top1_attdef):
                span_nhip1_top1_attdef_entity = span_nhip1_top1_attdef[0]
                for span_nhip1_top1_attdef_attrib in span_nhip1_top1_attdef_entity.attribs:
                    if span_nhip1_top1_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip1_top1_attdef_attrib.dxf.text = "_input['nhip1_top1']"  # change attribute content

        #################################### span_nhip1_top2 #######################################
        # Collect all anonymous block references starting with '-span_nhip1_top2'
        span_nhip1_top2 = msp_3.query('INSERT[name ? "^\-span_nhip1_top2.+"]')
        # Collect the references of the 'span_nhip1_top2' block
        for span_nhip1_top2_block_ref in span_nhip1_top2:
            # Get the block layout of the anonymous block
            span_nhip1_top2_attdef_block = output_dxf_3.blocks.get(span_nhip1_top2_block_ref.dxf.name)
            # Find all block references to 'span_nhip1_top2_attdef' in the anonymous block
            span_nhip1_top2_attdef = span_nhip1_top2_attdef_block.query('INSERT[name=="-span_nhip1_top2_attdef"]')
            if len(span_nhip1_top2_attdef):
                span_nhip1_top2_attdef_entity = span_nhip1_top2_attdef[0]
                for span_nhip1_top2_attdef_attrib in span_nhip1_top2_attdef_entity.attribs:
                    if span_nhip1_top2_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip1_top2_attdef_attrib.dxf.text = "_input['nhip1_top2']"  # change attribute content

        #################################### span_nhip1_top3 #######################################
        # Collect all anonymous block references starting with '-span_nhip1_top3'
        span_nhip1_top3 = msp_3.query('INSERT[name ? "^\-span_nhip1_top3.+"]')
        # Collect the references of the 'span_nhip1_top3' block
        for span_nhip1_top3_block_ref in span_nhip1_top3:
            # Get the block layout of the anonymous block
            span_nhip1_top3_attdef_block = output_dxf_3.blocks.get(span_nhip1_top3_block_ref.dxf.name)
            # Find all block references to 'span_nhip1_top3_attdef' in the anonymous block
            span_nhip1_top3_attdef = span_nhip1_top3_attdef_block.query('INSERT[name=="-span_nhip1_top3_attdef"]')
            if len(span_nhip1_top3_attdef):
                span_nhip1_top3_attdef_entity = span_nhip1_top3_attdef[0]
                for span_nhip1_top3_attdef_attrib in span_nhip1_top3_attdef_entity.attribs:
                    if span_nhip1_top3_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip1_top3_attdef_attrib.dxf.text = "_input['nhip1_top3']"  # change attribute content

        #################################### span_nhip2_top1 #######################################
        # Collect all anonymous block references starting with '-span_nhip2_top1'
        span_nhip2_top1 = msp_3.query('INSERT[name ? "^\-span_nhip2_top1.+"]')
        # Collect the references of the 'span_nhip2_top1' block
        for span_nhip2_top1_block_ref in span_nhip2_top1:
            # Get the block layout of the anonymous block
            span_nhip2_top1_attdef_block = output_dxf_3.blocks.get(span_nhip2_top1_block_ref.dxf.name)
            # Find all block references to 'span_nhip2_top1_attdef' in the anonymous block
            span_nhip2_top1_attdef = span_nhip2_top1_attdef_block.query('INSERT[name=="-span_nhip2_top1_attdef"]')
            if len(span_nhip2_top1_attdef):
                span_nhip2_top1_attdef_entity = span_nhip2_top1_attdef[0]
                for span_nhip2_top1_attdef_attrib in span_nhip2_top1_attdef_entity.attribs:
                    if span_nhip2_top1_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip2_top1_attdef_attrib.dxf.text = "_input['nhip2_top1']"  # change attribute content

        #################################### span_nhip2_top2 #######################################
        # Collect all anonymous block references starting with '-span_nhip2_top2'
        span_nhip2_top2 = msp_3.query('INSERT[name ? "^\-span_nhip2_top2.+"]')
        # Collect the references of the 'span_nhip2_top2' block
        for span_nhip2_top2_block_ref in span_nhip2_top2:
            # Get the block layout of the anonymous block
            span_nhip2_top2_attdef_block = output_dxf_3.blocks.get(span_nhip2_top2_block_ref.dxf.name)
            # Find all block references to 'span_nhip2_top2_attdef' in the anonymous block
            span_nhip2_top2_attdef = span_nhip2_top2_attdef_block.query('INSERT[name=="-span_nhip2_top2_attdef"]')
            if len(span_nhip2_top2_attdef):
                span_nhip2_top2_attdef_entity = span_nhip2_top2_attdef[0]
                for span_nhip2_top2_attdef_attrib in span_nhip2_top2_attdef_entity.attribs:
                    if span_nhip2_top2_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip2_top2_attdef_attrib.dxf.text = "_input['nhip2_top2']"  # change attribute content

        #################################### span_nhip2_top3 #######################################
        # Collect all anonymous block references starting with '-span_nhip2_top3'
        span_nhip2_top3 = msp_3.query('INSERT[name ? "^\-span_nhip2_top3.+"]')
        # Collect the references of the 'span_nhip2_top3' block
        for span_nhip2_top3_block_ref in span_nhip2_top3:
            # Get the block layout of the anonymous block
            span_nhip2_top3_attdef_block = output_dxf_3.blocks.get(span_nhip2_top3_block_ref.dxf.name)
            # Find all block references to 'span_nhip2_top3_attdef' in the anonymous block
            span_nhip2_top3_attdef = span_nhip2_top3_attdef_block.query('INSERT[name=="-span_nhip2_top3_attdef"]')
            if len(span_nhip2_top3_attdef):
                span_nhip2_top3_attdef_entity = span_nhip2_top3_attdef[0]
                for span_nhip2_top3_attdef_attrib in span_nhip2_top3_attdef_entity.attribs:
                    if span_nhip2_top3_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip2_top3_attdef_attrib.dxf.text = "_input['nhip2_top3']"  # change attribute content

        #################################### span_nhip3_top1 #######################################
        # Collect all anonymous block references starting with '-span_nhip3_top1'
        span_nhip3_top1 = msp_3.query('INSERT[name ? "^\-span_nhip3_top1.+"]')
        # Collect the references of the 'span_nhip3_top1' block
        for span_nhip3_top1_block_ref in span_nhip3_top1:
            # Get the block layout of the anonymous block
            span_nhip3_top1_attdef_block = output_dxf_3.blocks.get(span_nhip3_top1_block_ref.dxf.name)
            # Find all block references to 'span_nhip3_top1_attdef' in the anonymous block
            span_nhip3_top1_attdef = span_nhip3_top1_attdef_block.query('INSERT[name=="-span_nhip3_top1_attdef"]')
            if len(span_nhip3_top1_attdef):
                span_nhip3_top1_attdef_entity = span_nhip3_top1_attdef[0]
                for span_nhip3_top1_attdef_attrib in span_nhip3_top1_attdef_entity.attribs:
                    if span_nhip3_top1_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip3_top1_attdef_attrib.dxf.text = "_input['nhip3_top1']"  # change attribute content

        #################################### span_nhip3_top2 #######################################
        # Collect all anonymous block references starting with '-span_nhip3_top2'
        span_nhip3_top2 = msp_3.query('INSERT[name ? "^\-span_nhip3_top2.+"]')
        # Collect the references of the 'span_nhip3_top2' block
        for span_nhip3_top2_block_ref in span_nhip3_top2:
            # Get the block layout of the anonymous block
            span_nhip3_top2_attdef_block = output_dxf_3.blocks.get(span_nhip3_top2_block_ref.dxf.name)
            # Find all block references to 'span_nhip3_top2_attdef' in the anonymous block
            span_nhip3_top2_attdef = span_nhip3_top2_attdef_block.query('INSERT[name=="-span_nhip3_top2_attdef"]')
            if len(span_nhip3_top2_attdef):
                span_nhip3_top2_attdef_entity = span_nhip3_top2_attdef[0]
                for span_nhip3_top2_attdef_attrib in span_nhip3_top2_attdef_entity.attribs:
                    if span_nhip3_top2_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip3_top2_attdef_attrib.dxf.text = "_input['nhip3_top2']"  # change attribute content

        #################################### span_nhip3_top3 #######################################
        # Collect all anonymous block references starting with '-span_nhip3_top3'
        span_nhip3_top3 = msp_3.query('INSERT[name ? "^\-span_nhip3_top3.+"]')
        # Collect the references of the 'span_nhip3_top3' block
        for span_nhip3_top3_block_ref in span_nhip3_top3:
            # Get the block layout of the anonymous block
            span_nhip3_top3_attdef_block = output_dxf_3.blocks.get(span_nhip3_top3_block_ref.dxf.name)
            # Find all block references to 'span_nhip3_top3_attdef' in the anonymous block
            span_nhip3_top3_attdef = span_nhip3_top3_attdef_block.query('INSERT[name=="-span_nhip3_top3_attdef"]')
            if len(span_nhip3_top3_attdef):
                span_nhip3_top3_attdef_entity = span_nhip3_top3_attdef[0]
                for span_nhip3_top3_attdef_attrib in span_nhip3_top3_attdef_entity.attribs:
                    if span_nhip3_top3_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip3_top3_attdef_attrib.dxf.text = "_input['nhip3_top3']"  # change attribute content

        #################################### span_nhip1_bot1 #######################################content
        # Collect all anonymous block references starting with '-span_nhip1_bot1'
        span_nhip1_bot1 = msp_3.query('INSERT[name ? "^\-span_nhip1_bot1.+"]')
        # Collect the references of the 'span_nhip1_bot1' block
        for span_nhip1_bot1_block_ref in span_nhip1_bot1:
            # Get the block layout of the anonymous block
            span_nhip1_bot1_attdef_block = output_dxf_3.blocks.get(span_nhip1_bot1_block_ref.dxf.name)
            # Find all block references to 'span_nhip1_bot1_attdef' in the anonymous block
            span_nhip1_bot1_attdef = span_nhip1_bot1_attdef_block.query('INSERT[name=="-span_nhip1_bot1_attdef"]')
            if len(span_nhip1_bot1_attdef):
                span_nhip1_bot1_attdef_entity = span_nhip1_bot1_attdef[0]
                for span_nhip1_bot1_attdef_attrib in span_nhip1_bot1_attdef_entity.attribs:
                    if span_nhip1_bot1_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip1_bot1_attdef_attrib.dxf.text = "_input['nhip1_bot1']"  # change attribute content

        #################################### span_nhip1_bot2 #######################################
        # Collect all anonymous block references starting with '-span_nhip1_bot2'
        span_nhip1_bot2 = msp_3.query('INSERT[name ? "^\-span_nhip1_bot2.+"]')
        # Collect the references of the 'span_nhip1_bot2' block
        for span_nhip1_bot2_block_ref in span_nhip1_bot2:
            # Get the block layout of the anonymous block
            span_nhip1_bot2_attdef_block = output_dxf_3.blocks.get(span_nhip1_bot2_block_ref.dxf.name)
            # Find all block references to 'span_nhip1_bot2_attdef' in the anonymous block
            span_nhip1_bot2_attdef = span_nhip1_bot2_attdef_block.query('INSERT[name=="-span_nhip1_bot2_attdef"]')
            if len(span_nhip1_bot2_attdef):
                span_nhip1_bot2_attdef_entity = span_nhip1_bot2_attdef[0]
                for span_nhip1_bot2_attdef_attrib in span_nhip1_bot2_attdef_entity.attribs:
                    if span_nhip1_bot2_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip1_bot2_attdef_attrib.dxf.text = "_input['nhip1_bot2']"  # change attribute content

        #################################### span_nhip1_bot3 #######################################
        # Collect all anonymous block references starting with '-span_nhip1_bot3'
        span_nhip1_bot3 = msp_3.query('INSERT[name ? "^\-span_nhip1_bot3.+"]')
        # Collect the references of the 'span_nhip1_bot3' block
        for span_nhip1_bot3_block_ref in span_nhip1_bot3:
            # Get the block layout of the anonymous block
            span_nhip1_bot3_attdef_block = output_dxf_3.blocks.get(span_nhip1_bot3_block_ref.dxf.name)
            # Find all block references to 'span_nhip1_bot3_attdef' in the anonymous block
            span_nhip1_bot3_attdef = span_nhip1_bot3_attdef_block.query('INSERT[name=="-span_nhip1_bot3_attdef"]')
            if len(span_nhip1_bot3_attdef):
                span_nhip1_bot3_attdef_entity = span_nhip1_bot3_attdef[0]
                for span_nhip1_bot3_attdef_attrib in span_nhip1_bot3_attdef_entity.attribs:
                    if span_nhip1_bot3_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip1_bot3_attdef_attrib.dxf.text = "_input['nhip1_bot3']"  # change attribute content

        #################################### span_nhip2_bot1 #######################################
        # Collect all anonymous block references starting with '-span_nhip2_bot1'
        span_nhip2_bot1 = msp_3.query('INSERT[name ? "^\-span_nhip2_bot1.+"]')
        # Collect the references of the 'span_nhip2_bot1' block
        for span_nhip2_bot1_block_ref in span_nhip2_bot1:
            # Get the block layout of the anonymous block
            span_nhip2_bot1_attdef_block = output_dxf_3.blocks.get(span_nhip2_bot1_block_ref.dxf.name)
            # Find all block references to 'span_nhip2_bot1_attdef' in the anonymous block
            span_nhip2_bot1_attdef = span_nhip2_bot1_attdef_block.query('INSERT[name=="-span_nhip2_bot1_attdef"]')
            if len(span_nhip2_bot1_attdef):
                span_nhip2_bot1_attdef_entity = span_nhip2_bot1_attdef[0]
                for span_nhip2_bot1_attdef_attrib in span_nhip2_bot1_attdef_entity.attribs:
                    if span_nhip2_bot1_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip2_bot1_attdef_attrib.dxf.text = "_input['nhip2_bot1']"  # change attribute content

        #################################### span_nhip2_bot2 #######################################
        # Collect all anonymous block references starting with '-span_nhip2_bot2'
        span_nhip2_bot2 = msp_3.query('INSERT[name ? "^\-span_nhip2_bot2.+"]')
        # Collect the references of the 'span_nhip2_bot2' block
        for span_nhip2_bot2_block_ref in span_nhip2_bot2:
            # Get the block layout of the anonymous block
            span_nhip2_bot2_attdef_block = output_dxf_3.blocks.get(span_nhip2_bot2_block_ref.dxf.name)
            # Find all block references to 'span_nhip2_bot2_attdef' in the anonymous block
            span_nhip2_bot2_attdef = span_nhip2_bot2_attdef_block.query('INSERT[name=="-span_nhip2_bot2_attdef"]')
            if len(span_nhip2_bot2_attdef):
                span_nhip2_bot2_attdef_entity = span_nhip2_bot2_attdef[0]
                for span_nhip2_bot2_attdef_attrib in span_nhip2_bot2_attdef_entity.attribs:
                    if span_nhip2_bot2_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip2_bot2_attdef_attrib.dxf.text = "_input['nhip2_bot2']"  # change attribute content

        #################################### span_nhip2_bot3 #######################################
        # Collect all anonymous block references starting with '-span_nhip2_bot3'
        span_nhip2_bot3 = msp_3.query('INSERT[name ? "^\-span_nhip2_bot3.+"]')
        # Collect the references of the 'span_nhip2_bot3' block
        for span_nhip2_bot3_block_ref in span_nhip2_bot3:
            # Get the block layout of the anonymous block
            span_nhip2_bot3_attdef_block = output_dxf_3.blocks.get(span_nhip2_bot3_block_ref.dxf.name)
            # Find all block references to 'span_nhip2_bot3_attdef' in the anonymous block
            span_nhip2_bot3_attdef = span_nhip2_bot3_attdef_block.query('INSERT[name=="-span_nhip2_bot3_attdef"]')
            if len(span_nhip2_bot3_attdef):
                span_nhip2_bot3_attdef_entity = span_nhip2_bot3_attdef[0]
                for span_nhip2_bot3_attdef_attrib in span_nhip2_bot3_attdef_entity.attribs:
                    if span_nhip2_bot3_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip2_bot3_attdef_attrib.dxf.text = "_input['nhip2_bot3']"  # change attribute content

        #################################### span_nhip3_bot1 #######################################
        # Collect all anonymous block references starting with '-span_nhip3_bot1'
        span_nhip3_bot1 = msp_3.query('INSERT[name ? "^\-span_nhip3_bot1.+"]')
        # Collect the references of the 'span_nhip3_bot1' block
        for span_nhip3_bot1_block_ref in span_nhip3_bot1:
            # Get the block layout of the anonymous block
            span_nhip3_bot1_attdef_block = output_dxf_3.blocks.get(span_nhip3_bot1_block_ref.dxf.name)
            # Find all block references to 'span_nhip3_bot1_attdef' in the anonymous block
            span_nhip3_bot1_attdef = span_nhip3_bot1_attdef_block.query('INSERT[name=="-span_nhip3_bot1_attdef"]')
            if len(span_nhip3_bot1_attdef):
                span_nhip3_bot1_attdef_entity = span_nhip3_bot1_attdef[0]
                for span_nhip3_bot1_attdef_attrib in span_nhip3_bot1_attdef_entity.attribs:
                    if span_nhip3_bot1_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip3_bot1_attdef_attrib.dxf.text = "_input['nhip3_bot1']"  # change attribute content

        #################################### span_nhip3_bot2 #######################################
        # Collect all anonymous block references starting with '-span_nhip3_bot2'
        span_nhip3_bot2 = msp_3.query('INSERT[name ? "^\-span_nhip3_bot2.+"]')
        # Collect the references of the 'span_nhip3_bot2' block
        for span_nhip3_bot2_block_ref in span_nhip3_bot2:
            # Get the block layout of the anonymous block
            span_nhip3_bot2_attdef_block = output_dxf_3.blocks.get(span_nhip3_bot2_block_ref.dxf.name)
            # Find all block references to 'span_nhip3_bot2_attdef' in the anonymous block
            span_nhip3_bot2_attdef = span_nhip3_bot2_attdef_block.query('INSERT[name=="-span_nhip3_bot2_attdef"]')
            if len(span_nhip3_bot2_attdef):
                span_nhip3_bot2_attdef_entity = span_nhip3_bot2_attdef[0]
                for span_nhip3_bot2_attdef_attrib in span_nhip3_bot2_attdef_entity.attribs:
                    if span_nhip3_bot2_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip3_bot2_attdef_attrib.dxf.text = "_input['nhip3_bot2']"  # change attribute content

        #################################### span_nhip3_bot3 #######################################
        # Collect all anonymous block references starting with '-span_nhip3_bot3'
        span_nhip3_bot3 = msp_3.query('INSERT[name ? "^\-span_nhip3_bot3.+"]')
        # Collect the references of the 'span_nhip3_bot3' block
        for span_nhip3_bot3_block_ref in span_nhip3_bot3:
            # Get the block layout of the anonymous block
            span_nhip3_bot3_attdef_block = output_dxf_3.blocks.get(span_nhip3_bot3_block_ref.dxf.name)
            # Find all block references to 'span_nhip3_bot3_attdef' in the anonymous block
            span_nhip3_bot3_attdef = span_nhip3_bot3_attdef_block.query('INSERT[name=="-span_nhip3_bot3_attdef"]')
            if len(span_nhip3_bot3_attdef):
                span_nhip3_bot3_attdef_entity = span_nhip3_bot3_attdef[0]
                for span_nhip3_bot3_attdef_attrib in span_nhip3_bot3_attdef_entity.attribs:
                    if span_nhip3_bot3_attdef_attrib.dxf.tag == "noidung":  # identify attribute by tag
                        span_nhip3_bot3_attdef_attrib.dxf.text = "_input['nhip3_bot3']"  # change attribute content

        #################################### IMPORT ##############################################################################

        importer = Importer(output_dxf_3, output_dxf_1)

        # import all entities from source modelspace into modelspace of the target drawing
        importer.import_modelspace()

        # import all CIRCLE and LINE entities from source modelspace into an arbitrary target layout.
        # query source entities
        ents = output_dxf_3.modelspace().query('CIRCLE LINE')
        # import source entities into target block
        importer.import_entities(ents, tblock)

        # This is ALWAYS the last & required step, without finalizing the target drawing is maybe invalid!
        # This step imports all additional required table entries and block definitions.
        importer.finalize()
    
    # delete entities from the layer
    key_func = output_dxf_1.layers.key
    layer_key = key_func("delete_1")
    with output_dxf_1.entitydb.trashcan() as trash:
        for entity in output_dxf_1.entitydb.values():
            if not entity.dxf.hasattr("layer"):
                continue
            if layer_key == key_func(entity.dxf.layer):
                trash.add(entity.dxf.handle)

    generate_image(output_dxf_1)
    download_dxf(output_dxf_1)
    download_pdf(output_dxf_1)

if __name__ == "__main__":
    main()
