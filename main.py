import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("📈 구글 드라이브 CSV 데이터 시각화")

# 구글 드라이브 CSV 파일 다운로드 URL
csv_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# 데이터 불러오기
@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류 발생: {e}")
        return None

df = load_data(csv_url)

if df is not None:
    st.subheader("🔍 데이터 미리보기")
    st.dataframe(df.head())

    # 사용자에게 X, Y 축 컬럼 선택하게 하기
    st.subheader("🛠️ 시각화 설정")
    x_col = st.selectbox("X축 컬럼 선택", df.columns)
    y_col = st.selectbox("Y축 컬럼 선택", df.columns)

    # 그래프 그리기
    fig = px.line(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("데이터를 불러올 수 없습니다.")
