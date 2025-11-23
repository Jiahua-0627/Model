import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import os

# ==========================================
# 1. 頁面設定 (品牌核心確立)
# ==========================================
st.set_page_config(
    page_title="宥妤金牌業務 - 傳世資產守護者",
    page_icon="👑", # 改用皇冠圖標
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 極致奢華優化
# ==========================================
st.markdown("""
    <style>
    /* --- 全域字體引入 --- */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans TC', sans-serif;
        color: #2C3E50; /* 深灰字體 */
    }
    
    /* --- 背景與容器 --- */
    .stApp {
        background-color: #FAFAFA; /* 更乾淨的米白背景 */
    }

    /* --- 側邊欄優化 --- */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #F0F0F0;
        box-shadow: 2px 0 10px rgba(0,0,0,0.05);
    }
    section[data-testid="stSidebar"] h1 {
        color: #1A4D2E !important; /* 品牌深綠 */
        font-weight: 700;
    }
    section[data-testid="stSidebar"] .stRadio label {
        color: #333333 !important;
        font-weight: 500;
        font-size: 1.05rem;
        padding: 10px 0;
    }

    /* --- 卡片設計 (更具立體感) --- */
    div.css-1r6slb0, div.stMetric {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 25px; /* 增加內部間距 */
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* 更柔和的陰影 */
        transition: all 0.3s ease;
        border: 1px solid rgba(0,0,0,0.05);
    }
    div.css-1r6slb0:hover, div.stMetric:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.15); /* 金色光暈陰影 */
        border-color: #D4AF37;
    }

    /* --- 標題特效 (更霸氣) --- */
    .hero-title {
        font-size: 3rem; /* 加大字體 */
        font-weight: 700;
        background: linear-gradient(135deg, #1A4D2E 0%, #D4AF37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        text-align: center; /* 置中對齊 */
    }
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1A4D2E;
        margin-top: 40px;
        margin-bottom: 20px;
        border-left: 5px solid #D4AF37;
        padding-left: 15px;
    }

    /* --- 關鍵字標籤 --- */
    .tag {
        display: inline-block;
        background-color: #F4F9F4;
        color: #1A4D2E;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        border: 1px solid #E0E0E0;
    }

    /* --- 圖片優化 --- */
    [data-testid="stImage"] img {
        border-radius: 12px; /* 圖片圓角 */
    }

    /* --- 動畫類 --- */
    .animate-box { animation: fadeInUp 1s ease-out; }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* 手機版微調 */
    @media only screen and (max-width: 600px) {
        .hero-title { font-size: 2rem; text-align: left; }
        .section-title { font-size: 1.5rem; }
        div.css-1r6slb0, div.stMetric { padding: 15px; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 圖片讀取功能 (使用相對路徑)
# ==========================================
# 重要說明：請確保 tree1.jpg 和 tree2.jpg 與此腳本在同一個資料夾中。
def load_local_image(image_name, fallback_url=None):
    if os.path.exists(image_name):
        return Image.open(image_name)
    elif fallback_url:
        # 如果找不到本地圖片，返回一個替代的 URL
        return fallback_url
    else:
        # 如果都沒有，返回一個空白圖片以避免報錯
        return Image.new('RGB', (100, 100), color='gray')

# ==========================================
# 4. 數據圖表 (20年軌跡)
# ==========================================
def draw_growth_chart():
    years = list(range(2004, 2025, 2))
    clients = [1, 15, 40, 120, 300, 550, 800, 1200, 1800, 2500, 3200]
    assets = [0.1, 2, 5, 15, 30, 60, 100, 180, 300, 550, 800]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=clients, mode='lines+markers', name='累積服務客戶 (人)',
                             line=dict(color='#1A4D2E', width=4, shape='spline'), marker=dict(size=10, color='#D4AF37')))
    fig.add_trace(go.Scatter(x=years, y=assets, mode='lines', name='管理資產規模 (億)',
                             line=dict(color='#D4AF37', width=3, dash='dot', shape='spline'), yaxis='y2'))

    fig.update_layout(
        title="<b>20年 穩健成長軌跡</b>",
        title_font_color="#1A4D2E",
        xaxis=dict(showgrid=False, tickfont=dict(size=14)),
        yaxis=dict(title="客戶數 (人)", showgrid=True, gridcolor='#F0F0F0', title_font=dict(size=14)),
        yaxis2=dict(title="資產規模 (億)", overlaying='y', side='right', showgrid=False, title_font=dict(size=14)),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified",
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(orientation="h", y=1.1, font=dict(size=12))
    )
    return fig

# ==========================================
# 5. 側邊選單
# ==========================================
with st.sidebar:
    # 使用更專業的圖標 (這裡用 emoji 暫代，可用圖片替換)
    st.markdown("<h1 style='text-align: center;'>👑</h1>", unsafe_allow_html=True)
    st.title("宥妤金牌業務")
    st.markdown("<div style='text-align: center; color: #666; margin-bottom: 20px;'>傳世資產・極致守護<br>Since 2004</div>", unsafe_allow_html=True)
    
    menu = st.radio(
        "",
        ["📖 宥妤品牌故事", "🏰 精選傳世豪宅", "🌲 頂級羅漢松鑑賞", "👩‍💼 專業團隊與人力", "📞 預約專屬諮詢"],
    )
    
    st.markdown("---")
    st.markdown("### 🏆 榮耀時刻")
    st.success("連續 5 年榮獲千萬經紀人殊榮")
    st.info("2024 年度客戶滿意度金獎")

# ==========================================
# 6. 主要內容區塊
# ==========================================

# --- 📖 宥妤品牌故事 ---
if "品牌故事" in menu:
    # Hero Image (首圖衝擊)
    st.image("https://images.unsplash.com/photo-1560518883-ce09059ee971?q=80&w=2073", use_container_width=True)
    
    st.markdown('<div class="hero-title animate-box">宥妤金牌業務 - 您的傳世資產守護者</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; font-size: 1.2rem; color: #555; margin-bottom: 40px;" class="animate-box">
    20 年前，憑藉著一份「把客戶當家人」的初心起步。<br>
    如今，宥妤帶領團隊，以最專業的視角，為您整合房產、園藝與生活服務，成就家的最高標準。
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">📈 成長見證</div>', unsafe_allow_html=True)
    st.plotly_chart(draw_growth_chart(), use_container_width=True)

    st.markdown('<div class="section-title">🛤️ 心路歷程</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large") # 增加欄位間距
    with col1:
        st.markdown("""
        <div class="animate-box">
        <h3>🌱 2004：誠信起家</h3>
        <p>沒有華麗的背景，只有比別人更勤奮的雙腳。宥妤深信，業務不只是買賣，更是承載客戶對「家」的夢想。每一個成交，都是一份信任的交付。</p>
        </div>
        """, unsafe_allow_html=True)
        # 讀取本地圖片 tree1.jpg (請確保檔案在同目錄下)
        img1 = load_local_image("tree1.jpg", "https://via.placeholder.com/800x600?text=Image+Not+Found:+tree1.jpg")
        st.image(img1, caption="早期的堅持：如同培育樹苗般的耐心", use_container_width=True)
    
    with col2:
        # 讀取本地圖片 tree2.jpg
        img2 = load_local_image("tree2.jpg", "https://via.placeholder.com/800x600?text=Image+Not+Found:+tree2.jpg")
        st.image(img2, caption="2024年的成就：開枝散葉的金牌團隊", use_container_width=True)
        
        st.markdown("""
        <div class="animate-box">
        <h3>👑 2024：全方位資產管家</h3>
        <p>二十年磨一劍。宥妤整合了頂級房地產、珍稀羅漢松與專業家務人力。我們提供的不再是單一產品，而是為層峰人士量身打造的<b>「極致生活解決方案」</b>。</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 增加團隊形象照片 (增加印象)
    st.markdown('<div class="section-title">👩‍💼 宥妤與專業團隊</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2070", caption="我們準備好為您服務 (團隊示意圖)", use_container_width=True)

    st.markdown("---")
    
    # 數字成就
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("深耕業界", "20 年", "始於 2004")
    m2.metric("圓滿成交", "3,200+ 戶", "信譽保證")
    m3.metric("管理資產規模", "800 億+", "持續增長")
    m4.metric("客戶回購/推薦率", "95%", "口碑見證")

# --- 🏰 精選傳世豪宅 ---
elif "精選傳世豪宅" in menu:
    st.markdown('<div class="hero-title">🏰 宥妤嚴選・尊榮居所</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; margin-bottom: 30px;'>每一間豪宅，都經過宥妤親自鑑賞，確保具備傳世價值。</p>", unsafe_allow_html=True)
    
    # 增加更多物件以豐富頁面
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1613490493576-7fde63acd811?q=80&w=2071", use_container_width=True)
        st.markdown("### 🌟 信義首席公館")
        st.markdown('<span class="tag">SRC鋼骨</span><span class="tag">環景露台</span><span class="tag">總裁級</span>', unsafe_allow_html=True)
        st.markdown("總價：**2.88 億**")
        st.button("預約賞屋 - 信義首席", use_container_width=True)

    with c2:
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2070", use_container_width=True)
        st.markdown("### 🌿 陽明山隱世莊園")
        st.markdown('<span class="tag">千坪基地</span><span class="tag">私人泳池</span><span class="tag">高度隱私</span>', unsafe_allow_html=True)
        st.markdown("總價：**4.5 億**")
        st.button("預約賞屋 - 陽明山莊園", use_container_width=True)

    c3, c4 = st.columns(2, gap="medium")
    with c3:
        st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=2069", use_container_width=True)
        st.markdown("### 💎 大直水岸帝寶")
        st.markdown('<span class="tag">河岸第一排</span><span class="tag">名師設計</span><span class="tag">頂級物管</span>', unsafe_allow_html=True)
        st.markdown("總價：**3.2 億**")
        st.button("預約賞屋 - 大直水岸", use_container_width=True)
    with c4:
        # 佔位符，讓版面平衡
        st.markdown("<div style='height: 100%; display: flex; align-items: center; justify-content: center; background: #f0f0f0; border-radius: 16px; color: #999;'>更多非公開物件<br>請洽宥妤專線</div>", unsafe_allow_html=True)


# --- 🌲 頂級羅漢松鑑賞 ---
elif "頂級羅漢松鑑賞" in menu:
    st.markdown('<div class="hero-title">🌲 傳世名樹・家宅守護神</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(to right, #f8f9fa, #ffffff); padding: 30px; border-radius: 16px; border-left: 6px solid #1A4D2E; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <h3 style="color: #1A4D2E; margin-top: 0;">📜 宥妤觀點：為什麼豪宅必備羅漢松？</h3>
        <p style="font-size: 1.1rem;">在服務眾多層峰客戶的過程中，宥妤發現，真正的豪宅，不僅要有奢華的硬體，更要有「氣」。羅漢松，正是凝聚宅氣、展現底蘊的最佳載體。</p>
        <ul>
            <li><b>🐢 長壽與傳承</b>：樹齡動輒百年，見證家族世代興旺。</li>
            <li><b>🛡️ 鎮宅與風水</b>：強大的氣場，為家宅帶來安寧與吉祥。</li>
            <li><b>💰 活的資產</b>：俗語云<b>「家有羅漢松，世世不受窮」</b>，其價值隨時間穩健增長。</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">💎 鎮園之寶鑑賞</div>', unsafe_allow_html=True)

    # 使用本地圖片 tree2.jpg 作為主角
    img_main = load_local_image("tree2.jpg", "https://via.placeholder.com/1200x800?text=Image+Not+Found:+tree2.jpg")
    st.image(img_main, caption="【極品】日本百年造型羅漢松 - 蒼勁古樸，氣宇非凡", use_container_width=True)

    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.markdown("""
        ### 🇯🇵 日本職人精神養護
        宥妤引進的每一棵名樹，皆來自日本知名園區，並由專業團隊進行長達 1,000 天以上的在地化養護，確保樹勢強健，適應台灣氣候。
        
        * **品種嚴選**：蘭嶼羅漢松、日本系魚川真柏、黑松
        * **樹齡保證**：50 年至 150 年以上老樹
        """)
        st.button("📞 預約園區專人導覽", type="primary", use_container_width=True)
    with c2:
        # 使用本地圖片 tree1.jpg 作為對照
        img_secondary = load_local_image("tree1.jpg", "https://via.placeholder.com/800x600?text=Image+Not+Found:+tree1.jpg")
        st.image(img_secondary, caption="園區實景：萬樹蔥蘢，生機盎然", use_container_width=True)

# --- 👩‍💼 專業團隊與人力 ---
elif "專業團隊與人力" in menu:
    st.markdown('<div class="hero-title">👩‍💼 宥妤金牌團隊・極致服務</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; margin-bottom: 40px;'>您專注事業與享受生活，家中的大小事，請放心交給宥妤團隊。</p>", unsafe_allow_html=True)
    
    # 加入專業形象圖 (增加信任感)
    st.image("https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=2074", caption="受過嚴格訓練的專業管家團隊 (示意圖)", use_container_width=True)

    st.markdown('<div class="section-title">✅ 業界最高標準篩選</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px; margin-bottom: 40px;">
        <div style="flex: 1; min-width: 200px; text-align: center; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2rem;">✈️</div>
            <h4>海外親選</h4>
            <p style="font-size: 0.9rem;">團隊親赴來源國<br>嚴格面試挑選</p>
        </div>
        <div style="flex: 1; min-width: 200px; text-align: center; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2rem;">🔍</div>
            <h4>背景詳查</h4>
            <p style="font-size: 0.9rem;">良民證審核<br>無不良嗜好紀錄</p>
        </div>
        <div style="flex: 1; min-width: 200px; text-align: center; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2rem;">🎓</div>
            <h4>專業培訓</h4>
            <p style="font-size: 0.9rem;">豪宅清潔禮儀<br>基礎照護知識</p>
        </div>
        <div style="flex: 1; min-width: 200px; text-align: center; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2rem;">🏥</div>
            <h4>健康把關</h4>
            <p style="font-size: 0.9rem;">入境前後<br>完整健康檢查</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">🛠️ 專屬服務項目</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.success("🏠 豪宅居家清潔")
        st.write("懂名貴建材與家具保養，飯店級整理收納。")
    with col2:
        st.warning("👵 貼身長者照護")
        st.write("耐心陪伴，具備護理常識，讓長輩安心。")
    with col3:
        st.error("🌳 庭園專業維護")
        st.write("懂羅漢松與植栽修剪，維護庭院景觀。")

# --- 📞 預約專屬諮詢 ---
elif "預約專屬諮詢" in menu:
    st.markdown('<div class="hero-title">🤝 與宥妤聯繫</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>準備好開啟您的傳世資產規劃了嗎？宥妤隨時準備為您服務。</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.markdown('<div class="section-title">📍 宥妤金牌服務處</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.08);">
            <p><b>地址</b>：台北市信義區頂級商辦大樓</p>
            <p><b>貴賓專線</b>：0912-345-678 (宥妤親自服務)</p>
            <p><b>LINE ID</b>：@yoyu_vip</p>
            <p><b>服務時間</b>：09:00 - 21:00 (採全預約制)</p>
        </div>
        """, unsafe_allow_html=True)
        # 這裡可以放一張地圖截圖或宥妤的名片圖
        st.image("https://via.placeholder.com/600x400?text=Map+Placeholder", use_container_width=True)
    
    with c2:
        st.markdown('<div class="section-title">💬 線上預約諮詢</div>', unsafe_allow_html=True)
        with st.form("contact", clear_on_submit=True):
            name = st.text_input("您的尊姓大名")
            phone = st.text_input("聯絡電話 (必填)")
            need = st.multiselect("感興趣的服務項目", ["委託買賣豪宅", "鑑賞頂級羅漢松", "申請專業外勞/管家", "資產配置諮詢"])
            msg = st.text_area("備註需求或方便聯繫時間")
            
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("送出預約單", use_container_width=True)
            if submit:
                if phone:
                    st.balloons()
                    st.success(f"感謝您，{name} 貴賓！宥妤已收到您的預約，將會在最短時間內親自與您聯繫。")
                else:
                    st.error("麻煩請填寫聯絡電話，以便宥妤與您聯繫，謝謝。")