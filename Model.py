import streamlit as st
import plotly.graph_objects as go
import requests
import time
from streamlit_lottie import st_lottie

# ==========================================
# 1. 頁面基礎設定
# ==========================================
st.set_page_config(
    page_title="宥妤金牌業務",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="auto"
)

# 品牌色系
COLORS = {
    "primary": "#1A4D2E",    # 羅漢松綠
    "accent": "#D4AF37",     # 尊爵金
    "bg": "#FAFAFA",         # 乾淨白底
    "text": "#333333"
}

# ==========================================
# 2. CSS 優化 (修復跑版與字體)
# ==========================================
def load_css():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Noto Sans TC', sans-serif;
        color: {COLORS['text']};
    }}
    
    /* 隱藏圖片讀取錯誤時的預設圖示 */
    img:not([src]) {{ visibility: hidden; }}

    /* --- 標題樣式 --- */
    .hero-title {{
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, {COLORS['primary']}, {COLORS['accent']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }}
    .sub-title {{
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 40px;
    }}
    
    /* --- 區塊標題 --- */
    .section-header {{
        font-size: 1.8rem;
        font-weight: 700;
        color: {COLORS['primary']};
        border-left: 5px solid {COLORS['accent']};
        padding-left: 15px;
        margin-top: 50px;
        margin-bottom: 25px;
    }}

    /* --- 卡片優化 --- */
    .service-card {{
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #eee;
        height: 100%;
    }}
    
    /* --- 羅漢松專頁優化 --- */
    .tree-feature {{
        background-color: #f4f8f5;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #1A4D2E;
    }}

    /* --- 手機版適配 --- */
    @media (max-width: 600px) {{
        .hero-title {{ font-size: 2rem; }}
        .section-header {{ font-size: 1.5rem; }}
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. 功能函式 (Lottie & Google Form)
# ==========================================

@st.cache_data
def load_lottie_url(url: str):
    """讀取 Lottie 動畫，失敗回傳 None，避免破圖"""
    try:
        r = requests.get(url, timeout=3)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

@st.cache_data
def get_growth_data():
    years = list(range(2004, 2025, 2))
    clients = [1, 15, 40, 120, 300, 550, 800, 1200, 1800, 2500, 3200]
    assets = [0.1, 2, 5, 15, 30, 60, 100, 180, 300, 550, 800]
    return years, clients, assets

def send_to_google_form(name, phone, services, note):
    # 使用您提供的正確 ID
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc-RaTN1XIII1pg6TdgWKlb44lUtXJZTDG3MevZbl-qY_QjJQ/formResponse"
    data = {
        "entry.520939432": name,
        "entry.299821530": phone,
        "entry.1958493764": ", ".join(services),
        "entry.1312525539": note
    }
    try:
        requests.post(form_url, data=data)
        return True
    except:
        return False

# ==========================================
# 4. 頁面內容渲染
# ==========================================

def render_brand_story():
    # --- 1. 頂部 Hero Section (修復破圖與灰底) ---
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 嘗試讀取 Lottie，失敗則顯示乾淨的 Logo 或留白
        lottie_home = load_lottie_url("https://lottie.host/9e00b65f-4632-4752-9596-33924370258d/Q7yX6Q4S9s.json")
        if lottie_home:
            st_lottie(lottie_home, height=200, key="home_anim")
        else:
            # 備用方案：顯示文字 Emoji，確保不破圖
            st.markdown("<div style='font-size:100px; text-align:center;'>🏠</div>", unsafe_allow_html=True)
            
    with col2:
        st.markdown('<div class="hero-title" style="text-align: left; margin-top: 20px;">宥妤金牌業務<br>您的傳世資產守護者</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 1.1rem; color: #555; line-height: 1.8;">
        <b>「房子是容器，生活才是靈魂。」</b><br>
        20 年前，憑藉著一份把客戶當家人的初心起步。<br>
        如今，宥妤帶領團隊，整合<b>豪宅、園藝、人力</b>，成就您對家的最高想像。
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- 2. 形象大圖 (修復：直接使用 Unsplash 網址，不經過快取處理以避免灰塊) ---
    # 使用一張清晰的現代豪宅/團隊意象圖
    st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=2053&auto=format&fit=crop", 
             use_container_width=True, caption="專注細節，成就完美")

    # --- 3. 數據圖表 ---
    st.markdown('<div class="section-header">📈 成長見證</div>', unsafe_allow_html=True)
    years, clients, assets = get_growth_data()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=clients, mode='lines+markers', name='服務客戶(人)',
                             line=dict(color=COLORS['primary'], width=3), marker=dict(size=8, color=COLORS['accent'])))
    fig.add_trace(go.Scatter(x=years, y=assets, mode='lines', name='資產規模(億)',
                             line=dict(color=COLORS['accent'], width=3, dash='dot'), yaxis='y2'))
    fig.update_layout(
        xaxis=dict(showgrid=False),
        yaxis=dict(title="客戶數", showgrid=True, gridcolor='#f5f5f5'),
        yaxis2=dict(title="規模(億)", overlaying='y', side='right', showgrid=False),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=30, b=10),
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
    )
    st.plotly_chart(fig, use_container_width=True)

def render_trees():
    # --- 完全重做：羅漢松專頁 ---
    st.markdown('<div class="hero-title">傳世名樹・羅漢松</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">「家有羅漢松，世世不受窮」<br>不僅是園藝，更是傳承百年的資產</div>', unsafe_allow_html=True)

    # 1. 重點展示圖 (換成真正的羅漢松圖片)
    st.image("https://images.unsplash.com/photo-1599149791462-f76269666723?q=80&w=2000&auto=format&fit=crop", 
             caption="日本原裝進口・百年造型羅漢松", use_container_width=True)

    st.markdown('<div class="section-header">🌲 為什麼選擇羅漢松？</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="service-card">
            <h3 style="color:#1A4D2E;">🐢 長壽吉祥</h3>
            <p>象徵長壽與健康，四季常青，寓意家族基業長青，是豪宅庭院的必備鎮宅之樹。</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="service-card">
            <h3 style="color:#D4AF37;">💰 活的資產</h3>
            <p>羅漢松隨樹齡增長，價值逐年攀升。我們提供專業養護，確保您的資產持續增值。</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="service-card">
            <h3 style="color:#1A4D2E;">🎨 藝術樹形</h3>
            <p>每一棵都經過日本職人數十年修剪，姿態蒼勁高雅，為庭園注入禪意與氣勢。</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">🌿 嚴選樹種展示</div>', unsafe_allow_html=True)
    
    # 圖片畫廊
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://images.unsplash.com/photo-1696517454032-4d22168923a1?q=80&w=1000", caption="【皇室御用】黑松與羅漢松庭園造景", use_container_width=True)
        st.markdown("**適合位置**：主庭院、迎賓車道")
    with col_b:
        st.image("https://images.unsplash.com/photo-1583329068032-475356e72464?q=80&w=1000", caption="【禪意盆景】中型造型羅漢松", use_container_width=True)
        st.markdown("**適合位置**：玄關、露台、中庭")

    st.markdown("---")
    if st.button("📞 預約園區賞樹導覽", type="primary", use_container_width=True):
        st.session_state['page'] = '📞 預約諮詢'
        st.session_state['prefill_service'] = "羅漢松專人導覽"
        st.rerun()

def render_team():
    st.markdown('<div class="hero-title">金牌團隊・極致服務</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?q=80&w=2000", caption="專業管家與服務團隊", use_container_width=True)

    # --- 修復重點：使用 Streamlit 原生 Columns 取代 HTML Flexbox，確保不跑碼 ---
    st.markdown('<div class="section-header">✅ 宥妤嚴選標準</div>', unsafe_allow_html=True)
    
    # 使用 4 欄排版
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.info("✈️ **海外親選**")
        st.caption("親赴來源國面試，確認語言能力與工作態度。")
    
    with c2:
        st.info("🔍 **背景詳查**")
        st.caption("嚴格審核良民證，確保無不良嗜好與犯罪紀錄。")
        
    with c3:
        st.info("🎓 **專業培訓**")
        st.caption("豪宅禮儀、清潔技巧、長者照護專業訓練。")
        
    with c4:
        st.info("🏥 **健康把關**")
        st.caption("入境前與入境後完整健康檢查，讓您安心。")

    st.markdown("---")
    st.markdown("### 💡 服務項目細節")
    st.write("- **豪宅清潔**：定期大掃除、石材養護、地毯清潔。")
    st.write("- **貼身照護**：具備護理背景，專注長者陪伴與用藥管理。")
    st.write("- **園藝維護**：專業園丁定期修剪，維持庭園景觀。")

def render_luxury_homes():
    st.markdown('<div class="hero-title">宥妤嚴選・尊榮居所</div>', unsafe_allow_html=True)
    with st.expander("🔍 點擊展開搜尋條件"):
        s1, s2 = st.columns(2)
        s1.selectbox("地區", ["台北信義", "士林陽明", "新北板橋"])
        s2.slider("預算 (億)", 0.5, 10.0, (1.0, 3.0))

    st.markdown('<div class="section-header">🌟 精選物件</div>', unsafe_allow_html=True)

    def render_property(title, desc, price, img_url, key):
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.image(img_url, use_container_width=True)
        with c2:
            st.subheader(title)
            st.caption(desc)
            st.markdown(f"#### 總價：{price}")
            if st.button(f"預約賞屋 - {title}", key=key):
                st.session_state['page'] = '📞 預約諮詢'
                st.session_state['prefill_service'] = f"賞屋：{title}"
                st.rerun()
        st.markdown("---")

    render_property("信義首席公館", "SRC鋼骨 | 景觀露台 | 總裁級視野", "2.88 億", 
                    "https://images.unsplash.com/photo-1600596542815-6ad4c7213299?q=80&w=2000", "p1")
    render_property("陽明山隱世莊園", "千坪基地 | 私人泳池 | 極高隱私", "4.5 億", 
                    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2000", "p2")

def render_contact():
    st.markdown('<div class="hero-title">與宥妤聯繫</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(f"""
        <div class="service-card" style="text-align: left;">
            <h3 style="color:{COLORS['primary']}; margin-top:0;">📍 宥妤金牌服務處</h3>
            <p><b>專線</b>：0912-345-678</p>
            <p><b>LINE</b>：@yoyu_vip</p>
            <p style="color: #666; font-size: 0.9rem; margin-top: 20px;">
                我們將在 24 小時內與您聯繫。<br>
                您的資料將依個資法嚴格保密，請安心填寫。
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        with st.form("contact_form", clear_on_submit=True):
            st.write("📋 **預約單**")
            name = st.text_input("尊姓大名")
            phone = st.text_input("聯絡電話 (必填)")
            
            # 自動帶入服務
            default_services = []
            if 'prefill_service' in st.session_state:
                st.info(f"已自動選取：{st.session_state['prefill_service']}")
                if "賞屋" in st.session_state['prefill_service']: default_services.append("買賣豪宅")
                elif "羅漢松" in st.session_state['prefill_service']: default_services.append("羅漢松鑑賞")
                del st.session_state['prefill_service']

            services = st.multiselect("諮詢項目", ["買賣豪宅", "羅漢松鑑賞", "申請管家/外勞", "其他"], default=default_services)
            note = st.text_area("備註需求")
            
            submit = st.form_submit_button("送出預約", use_container_width=True)
            
            if submit:
                if not phone:
                    st.error("❗ 請填寫電話以便聯繫。")
                else:
                    with st.spinner("正在傳送資料..."):
                        if send_to_google_form(name, phone, services, note):
                            st.balloons()
                            st.success("✅ 預約成功！資料已傳送至後台。")
                        else:
                            st.error("⚠️ 傳送失敗，請直接撥打專線。")

# ==========================================
# 5. 主程式
# ==========================================
def main():
    load_css()
    
    if 'page' not in st.session_state:
        st.session_state['page'] = "📖 品牌故事"

    # 側邊欄
    with st.sidebar:
        st.markdown(f"<h1 style='text-align: center;'>👑</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: {COLORS['primary']};'>宥妤金牌業務</h3>", unsafe_allow_html=True)
        st.markdown("---")
        
        menu = st.radio(
            "選單",
            ["📖 品牌故事", "🏰 傳世豪宅", "🌲 頂級羅漢松", "👩‍💼 團隊與人力", "📞 預約諮詢"],
            index=["📖 品牌故事", "🏰 傳世豪宅", "🌲 頂級羅漢松", "👩‍💼 團隊與人力", "📞 預約諮詢"].index(st.session_state['page'])
        )
        if menu != st.session_state['page']:
            st.session_state['page'] = menu
            st.rerun()

        st.markdown("---")
        st.info("🏆 2024 年度銷售冠軍")

    # 頁面路由
    pg = st.session_state['page']
    if pg == "📖 品牌故事": render_brand_story()
    elif pg == "🏰 傳世豪宅": render_luxury_homes()
    elif pg == "🌲 頂級羅漢松": render_trees()
    elif pg == "👩‍💼 團隊與人力": render_team()
    elif pg == "📞 預約諮詢": render_contact()

if __name__ == "__main__":
    main()
