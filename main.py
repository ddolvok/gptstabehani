import streamlit as st
import os

# 페이지 설정
st.set_page_config(page_title="메인 메뉴", page_icon="🚀")

# 페이지 메뉴 설정
page_menu = {
    "App1": {"url": "app1", "img": "https://www.hanion.co.kr/news/photo/202107/23434_67333_2940.jpg", "description": "진짜 사진작가가 찍은 것 같은 '실사 사진' 만들 수 있어요."},
    "App2": {"url": "app2", "img": "https://blog.artmusee.com/_images/artwork/320/20180128004347_1517067827142822.jpg", "description": "안드레아스 아헨바흐 등 유명인 작풍을 따라할 수 있어요."},
    "App3": {"url": "app3", "img": "https://s3.ap-northeast-2.amazonaws.com/icunow.co.kr/2021/07/23150530/Khagwal-3D-Illustration-Library3-1024x609.jpg", "description": "3D 일러스트레이션을 빠르게 만들어요."},
    "App4": {"url": "app4", "img": "https://a-static.besthdwallpaper.com/electric-power-anime-scenery-wallpaper-2560x1600-106282_7.jpg", "description": "애니메이션 느낌이 나는 그림을 그릴 수 있어요."},
}

# 이미지 버튼 생성 함수
def create_image_button(app_name, img_url, description):
    img = st.image(img_url, use_column_width=True, output_format="PNG")
    btn = st.button(f"Open {app_name}", key=img_url)
    st.write(description)
    st.write("")  # 간격을 조금 더 벌리기 위해 추가
    return btn

# 메인 로직 실행
def main():
    st.title("GPT Stable Diffusion (랩)")

    # 예쁜 박스로 텍스트 꾸미기
    st.markdown(
        """
        <div style="background-color:#eee; padding:20px 30px; border-radius:10px; margin-bottom:20px;">
            <h3 style="text-align:center;">🎨 원하는 이미지 스타일로 들어가서 '키워드'만 넣어보세요. 🌟</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 각 버튼 분리
    btn_app1 = create_image_button("App1", page_menu['App1']['img'], page_menu['App1']['description'])
    btn_app2 = create_image_button("App2", page_menu['App2']['img'], page_menu['App2']['description'])
    btn_app3 = create_image_button("App3", page_menu['App3']['img'], page_menu['App3']['description'])
    btn_app4 = create_image_button("App4", page_menu['App4']['img'], page_menu['App4']['description'])

    if btn_app1:
        open_app('App1')
    elif btn_app2:
        open_app('App2')
    elif btn_app3:
        open_app('App3')
    elif btn_app4:
        open_app('App4')

# 선택된 앱 실행 함수
def open_app(app_key):
    file_name = page_menu[app_key]["url"]
    os.system(f"streamlit run {file_name}.py")

if __name__ == "__main__":
    main()
