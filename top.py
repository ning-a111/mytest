import streamlit as st
import pandas as pd

st.set_page_config(
    
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("选项卡简单示例")
tab1, tab2, tab3 ,tab4, tab5 ,tab6  = st.tabs(["数字档案", "南宁美食数据仪表盘", "相册","音乐播放器","视频网站","个人简历生成器"])

with tab1:
    st.header("这是第一个选项卡")
    st.markdown("#### 第一个选项卡的内容")
    # 页面配置：马卡龙风格
   
# 自定义CSS：马卡龙色系（粉/蓝/黄/绿柔和色调）
    st.markdown("""
    <style>
    .stApp {
        background-color: #f9f7f8;  /* 马卡龙浅底 */
        color: #4a4a4a;  /* 柔和文字色 */
    }
    .stMetric {
        background-color: #f0f8fb;  /* 浅蓝底 */
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #88c9e8;  /* 马卡龙蓝 */
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .stDataFrame {
        background-color: #fff9f2;  /* 浅黄底 */
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .stCode {
        background-color: #fef0f5 !important;  /* 浅粉底 */
        border-radius: 12px;
        border: 1px solid #f8d7e3;  /* 马卡龙粉 */
    }
    .css-1d391kg {
        background-color: #f5f9f7;  /* 浅绿底 */
    }
    .stProgress > div > div {
        background-color: #a8e6cf;  /* 马卡龙绿 */
    }
    h1, h2, h3 {
        color: #6b8e9e;  /* 马卡龙主色 */
    }
    </style>
""", unsafe_allow_html=True)

# 标题区域（动物主题）
    st.title("🐾 动物 小橘 数字档案")

# 基础信息模块
    st.header("📋 基础信息")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("动物ID: ZOO-2025-008")
    with col2:
        st.text("入园时间: 2025-01-15")
        st.markdown("健康状态: <span style='color: #66bb6a'>良好</span>", unsafe_allow_html=True)
    with col3:
        st.text("品种: 橘猫 | 年龄: 2岁")
        st.text("饲养员: 李星")

# 能力矩阵模块（适配动物行为能力）
    st.header("🐱 行为能力矩阵")
    skill_cols = st.columns(3)
    with skill_cols[0]:
        st.metric(label="攀爬能力", value="92%", delta="+5%")
    with skill_cols[1]:
        st.metric(label="捕猎反应", value="85%", delta="+2%")
    with skill_cols[2]:
        st.metric(label="社交互动", value="70%", delta="-3%")

# 训练进度
    st.subheader("社会化训练进度")
    st.progress(85)  # 对应85%的进度

# 日常记录模块（替换为动物日常）
    st.header("📅 日常行为记录")
    task_data = pd.DataFrame({
    "日期": ["2025-01-20", "2025-01-25", "2025-01-30"],
    "行为事件": ["使用猫抓板", "与其他猫咪互动", "完成进食训练"],
    "状态": ["✅ 已完成", "⚠️ 部分完成", "✅ 已完成"],
    "难度/评分": ["★★☆☆☆", "★★★☆☆", "★☆☆☆☆"]
})
    st.dataframe(task_data, use_container_width=True)

# 行为分析代码（适配动物主题）
    st.header("🐾 行为分析代码片段")
    code_content = """
def analyze_cat_behavior(behavior_data):
    \"\"\"分析猫咪日常行为数据\"\"\"
    try:
        # 统计活跃时长
        active_hours = sum(behavior_data["active_minutes"]) / 60
        if active_hours > 4:
            return "🐱 活跃度高 | 状态良好"
        elif active_hours < 2:
            return "😿 活跃度低 | 需关注健康"
        else:
            return "😺 活跃度正常"
    except Exception as e:
        print(f"分析失败: {e}")
        return "❌ 行为分析异常"
"""
    st.code(code_content, language="python")

# 饲养提示（Markdown格式）
    st.markdown("---")
    st.markdown("""
- **饲养提示**: 下周解锁新训练任务
- **任务**: 环境适应度提升训练
- **记录时间**: 2025-01-31 10:15:30
- **园区状态**: 温度25℃ | 湿度55% | 环境安全
""")

# 互动提议
    st.markdown("---")
    st.write("要不要我帮你添加一个**月度行为趋势图**来更直观地展示小橘的状态变化？")


with tab2:
    st.header("这是第二个选项卡")
    st.markdown("#### 第二个选项卡的内容")

    import streamlit as st
    import pandas as pd
    import numpy as np

# 页面基础配置（宽屏+标题+图标）
    st.set_page_config(
        page_title="南宁美食数据仪表盘",
        page_icon="🍜",
        layout="wide"
)

# --------------------------
# 自定义样式：马卡龙蓝色主调 + 美化组件
# --------------------------
    st.markdown("""
    <style>
    /* 全局主色调：马卡龙蓝 */
    :root {
        --primary-color: #8ECAE6;
        --secondary-color: #219EBC;
        --light-blue: #A7C957; /* 辅助色 */
        --pale-blue: #F8F9FA;
    }
    
    /* 标题样式 */
    h1, h2, h3, h4 {
        color: var(--secondary-color) !important;
    }
    
    /* 按钮样式 */
    .stButton>button {
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: var(--secondary-color);
    }
    
    /* 进度条样式 */
    .stProgress > div > div {
        background-color: var(--primary-color) !important;
    }
    
    /* 选择框/输入框样式 */
    .stSelectbox, .stTextInput {
        border: 1px solid var(--primary-color);
        border-radius: 8px;
    }
    
    /* 卡片背景 */
    .main {
        background-color: var(--pale-blue);
    }
    
    /* 缩小地图标记点 */
    .leaflet-marker-icon {
        width: 15px !important;
        height: 15px !important;
        margin-left: -7.5px !important;
        margin-top: -7.5px !important;
    }
    .leaflet-marker-shadow {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# 1. 核心数据准备（替换为指定5家店铺+精准定位）
# --------------------------
# 基础店铺信息（西乡塘罗文大道15号周边精准坐标）
    restaurants_data = {
    "餐厅": ["重庆小面", "兰州拉面", "塔斯汀", "KFC", "三品王"],
    "类型": ["中餐", "中餐", "快餐", "快餐", "快餐"],
    "评分": [4.3, 4.5, 4.2, 4.4, 4.1],
    "人均消费(元)": [12, 15, 18, 30, 16],
    "latitude": [22.806812, 22.805987, 22.807543, 22.808211, 22.806155],  # 罗文大道15号周边精准纬度
    "longitude": [108.203546, 108.204128, 108.202987, 108.205012, 108.203879],  # 罗文大道15号周边精准经度
    "推荐菜品": [
        ["招牌小面", "豌杂面", "酸辣粉"],
        ["牛肉拉面", "清汤拉面", "炒拉面"],
        ["香辣鸡腿堡", "薯条", "可乐"],
        ["原味鸡", "汉堡", "蛋挞"],
        ["牛肉粉", "杂酱粉", "猪脚粉"]
    ],
    "拥挤程度(%)": [78, 85, 70, 88, 68]
}
    df = pd.DataFrame(restaurants_data)

# 模拟用餐时段数据（贴合南宁本地习惯）
    time_data = pd.DataFrame({
    "时段": ["09:00", "11:00", "13:00", "17:00", "19:00", "21:00"],
    "用餐人数(峰值)": [40, 250, 100, 90, 300, 180]
}).set_index("时段")

# 新增：5家餐厅12个月价格走势数据（模拟真实波动，调整数值分层）
    months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
# 优化数值：让每条折线分层显示，避免堆叠（按价格区间梯度设计）
    price_trend = pd.DataFrame({
    "月份": months,
    "重庆小面": [12, 12, 12, 13, 13, 13, 14, 14, 13, 13, 12, 12],          # 12-14元区间
    "兰州拉面": [15, 15, 16, 16, 16, 17, 17, 17, 16, 16, 15, 15],          # 15-17元区间
    "三品王": [16, 16, 16, 17, 17, 17, 18, 18, 17, 17, 16, 16],            # 16-18元区间
    "塔斯汀": [18, 18, 18, 19, 19, 20, 20, 20, 19, 19, 18, 18],            # 18-20元区间
    "KFC": [30, 30, 31, 32, 32, 33, 33, 33, 32, 32, 31, 30]               # 30-33元区间
}).set_index("月份")

# --------------------------
# 2. 主标题+核心可视化模块
# --------------------------
    st.title("🍜 南宁西乡塘罗文大道美食数据仪表盘")

# 第一行：地图（精准定位） + 评分柱状图
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 餐厅位置分布（罗文大道15号）")
    # 地图聚焦罗文大道，zoom=15更精准
        st.map(df[["latitude", "longitude"]], zoom=15, use_container_width=True)

    with col2:
        st.subheader("⭐ 餐厅评分排行")
        score_df = df.sort_values("评分", ascending=False).set_index("餐厅")["评分"]
        st.bar_chart(score_df, color="#8ECAE6", use_container_width=True)  # 马卡龙蓝

# 第二行：人均消费折线图 + 用餐高峰面积图
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("💰 不同类型餐厅人均消费")
        consume_df = df.groupby("类型")["人均消费(元)"].mean()
        st.line_chart(consume_df, color="#219EBC", use_container_width=True)  # 深一点的马卡龙蓝

    with col4:
        st.subheader("📈 用餐高峰时段（南宁本地）")
        st.area_chart(time_data, color="#A7C957", use_container_width=True)  # 辅助色（浅绿）

# 新增：第三行 - 5家餐厅12个月价格走势折线图
    st.subheader("📊 5家餐厅12个月价格走势")
# 自定义马卡龙色系，每条折线颜色区分明显
    line_colors = ["#8ECAE6", "#219EBC", "#6A994E", "#F2E8CF", "#BC4749"]
    st.line_chart(
        price_trend,
        color=line_colors,  # 马卡龙色系
        use_container_width=True,
        height=400  # 增加高度，让分层折线更清晰
)

# --------------------------
# 3. 餐厅详情 + 可交互午餐推荐（兰州拉面配图）
# --------------------------
    st.subheader("📋 餐厅详情与午餐推荐")
    col5, col6 = st.columns([1, 1])

    with col5:
    # 餐厅下拉选择框
        selected_rest = st.selectbox(
        "选择餐厅查看详情",
            options=df["餐厅"],
            index=1  # 默认选中兰州拉面
    )
    # 获取选中餐厅信息
        rest_info = df[df["餐厅"] == selected_rest].iloc[0]
    
    # 展示餐厅详情（马卡龙蓝配色）
        st.markdown(f"### {rest_info['餐厅']}")
        st.markdown(f"**评分**：{rest_info['评分']}/5.0")
        st.markdown(f"**人均消费**：{rest_info['人均消费(元)']}元")
        st.markdown(f"**地址**：南宁西乡塘区罗文大道15号")
    
    # 推荐菜品
        st.markdown("**推荐菜品：**")
        for dish in rest_info["推荐菜品"]:
            st.markdown(f"- {dish}")
    
    # 拥挤程度进度条
        st.markdown("### 当前拥挤程度")
        st.progress(rest_info["拥挤程度(%)"] / 100, text=f"{rest_info['拥挤程度(%)']}% 拥挤")

    with col6:
    # 可交互午餐推荐按钮
        st.markdown("### 今日午餐推荐")
        lunch_click = st.button("帮我选午餐", use_container_width=True)
    
    # 按钮点击后显示推荐结果（马卡龙蓝提示）
        if lunch_click:
            st.success("✅ 为你推荐：兰州拉面（牛肉拉面）")
            st.markdown(f"""
        <div style="background-color: #8ECAE6; padding: 10px; border-radius: 8px; color: white; margin: 10px 0;">
            <strong>推荐理由</strong>：评分4.5分（最高），人均15元，拥挤度85%（适中），适合午餐！
        </div>
        """, unsafe_allow_html=True)
    
    # 兰州拉面配图（网络图，可替换为本地图）
        st.image(
        "https://img.zcool.cn/community/016f9058ac8598a801219c7df8e9833.jpg@1280w_1l_2o_100sh.jpg",
            caption="兰州拉面（南宁西乡塘罗文大道店）",
            use_container_width=True
    )
        st.caption("📍 地址：南宁西乡塘区罗文大道15号")



with tab3:
    st.header("这是第三个选项卡")
    st.markdown("#### 第三个选项卡的内容")
        # 设置页面配置（标题、图标）
    st.set_page_config(
        page_title="莫兰迪相册",
        page_icon="🖼️",
        layout="centered"
)

# 自定义莫兰迪马卡龙蓝灰色背景样式
    st.markdown(
    """
    <style>
    .stApp {
        background-color: #E0E5EC;  /* 莫兰迪蓝灰色 */
    }
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .caption {
        font-size: 18px;
        color: #5A6A85;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 初始化图片索引（session_state存储）
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

# 图片列表（至少3张，包含url和图注）
    images = [
    {
        'url': "https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        'text': "乖乖小狗"
    },
    {
        'url': "https://images.unsplash.com/photo-1507146426996-ef05306b995a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        'text': "小鸡毛"
    },
    {
        'url': "https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        'text': "大鸡毛"
    },
    {
        'url': "https://imgs.699pic.com/images/501/028/820.jpg!list1x.v2",
        'text': "贱兮兮柴犬"
    }
]

# 标题
    st.title("莫兰迪马卡龙相册")

# 显示当前图片和图注
    current_img = images[st.session_state['ind']]
    st.image(current_img['url'], use_column_width=True, caption=current_img['text'])

# 切换图片函数
    def next_img():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

    def prev_img():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

# 前后切换按钮
    col1, col2 = st.columns(2)
    with col1:
        st.button("上一张", on_click=prev_img)
    with col2:
        st.button("下一张", on_click=next_img)
with tab4:
    st.header("这是第四个选项卡")
    st.markdown("#### 第四个选项卡的内容")
    import streamlit as st
    import random

# 1. 设置页面标题和图标
    st.set_page_config(
            page_title="汪苏泷音乐播放器",
            page_icon="🎵",
            layout="centered"
)

# 2. 自定义CSS（莫兰迪灰粉色背景、样式优化）
    st.markdown("""
    <style>
    /* 页面整体背景 */
    .stApp {
        background-color: #f0e8e6;  /* 莫兰迪灰粉色 */
    }
    
    /* 标题样式 */
    h1 {
        color: #8b7369;  /* 莫兰迪深棕色 */
        text-align: center;
    }
    
    /* 子标题样式 */
    h2 {
        color: #9d887e;
    }
    
    /* 文本样式 */
    p, div, span {
        color: #7a6b61;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background-color: #e0d2cd;
        color: #6d5c53;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    /* 按钮hover效果 */
    .stButton > button:hover {
        background-color: #d1c4be;
        color: #5c4b43;
    }
    
    /* 滑块样式 */
    .stSlider > div > div > div {
        background-color: #d1c4be;
    }
    
    /* 滑块进度条 */
    .stSlider > div > div > div > div {
        background-color: #b9a79e;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 页面标题与描述
    st.title("🎵 汪苏泷 专属音乐播放器")
    st.caption("使用Streamlit制作的简单音乐播放器 | 莫兰迪灰粉色主题 | 支持切歌和基本播放控制")

# 4. 定义汪苏泷的歌曲列表（包含封面、歌曲名、歌手、时长、播放链接）
    music_list = [
    {
        "cover_url": "https://puui.qpic.cn/media_img/0/1087111581842036/0",
        "title": "年轮",
        "artist": "汪苏泷",
        "duration": "4:18",
        "audio_url": "https://music.163.com/song/media/outer/url?id=36966611.mp3"  # 示例链接
    },
    {
        "cover_url": "https://pic1.zhimg.com/50/v2-cc08e82965b5478be4dbb354733ddd84_hd.jpg?source=1940ef5c",
        "title": "不分手的恋爱",
        "artist": "汪苏泷",
        "duration": "3:50",
        "audio_url": "https://music.163.com/song/media/outer/url?id=506471182.mp3"  # 示例链接
    },
    {
        "cover_url": "https://www.360baike.com/uploads/202304/1681529925M6LOPzh4.jpg",
        "title": "大娱乐家",
        "artist": "汪苏泷",
        "duration": "3:25",
        "audio_url": "https://music.163.com/song/media/outer/url?id=1877241709.mp3"  # 示例链接
    }
]

# 5. 初始化session_state
    if "current_music_idx" not in st.session_state:
        st.session_state.current_music_idx = 0  # 默认第一首
    if "is_playing" not in st.session_state:
        st.session_state.is_playing = False  # 播放状态
    if "progress" not in st.session_state:
        st.session_state.progress = 0  # 播放进度

# 6. 获取当前播放的音乐信息
    current_music = music_list[st.session_state.current_music_idx]

# 7. 布局：左侧封面，右侧信息
    col_cover, col_info = st.columns([1, 2])

    with col_cover:
    # 显示专辑封面（圆角样式）
        st.markdown(f"""
        <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <img src="{current_music['cover_url']}" width="100%" style="display: block;">
        </div>
        <p style="text-align: center; margin-top: 8px; color: #8b7369;">专辑封面</p>
    """, unsafe_allow_html=True)

    with col_info:
    # 显示歌曲信息
        st.subheader(f"{current_music['title']}")
        st.write(f"🎤 歌手: {current_music['artist']}")
        st.write(f"⏱️ 时长: {current_music['duration']}")

    # 8. 切歌按钮
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            def prev_song():
            # 上一首逻辑：循环切换
                st.session_state.current_music_idx = (st.session_state.current_music_idx - 1) % len(music_list)
                st.session_state.progress = 0  # 切换歌曲重置进度
        
            st.button("◀◀ 上一首", on_click=prev_song, use_container_width=True)
    
        with btn_col2:
            def next_song():
            # 下一首逻辑：循环切换
                st.session_state.current_music_idx = (st.session_state.current_music_idx + 1) % len(music_list)
                st.session_state.progress = 0  # 切换歌曲重置进度
        
            st.button("▶▶ 下一首", on_click=next_song, use_container_width=True)

# 9. 播放控制区域
    st.markdown("---")  # 分隔线
    col_play, col_progress, col_volume = st.columns([1, 5, 1])

    with col_play:
    # 播放/暂停按钮逻辑
        def toggle_play():
            st.session_state.is_playing = not st.session_state.is_playing
    
        play_btn_label = "⏸️ 暂停" if st.session_state.is_playing else "▶️ 播放"
        st.button(play_btn_label, on_click=toggle_play, use_container_width=True)

    with col_progress:
    # 播放进度条
        st.session_state.progress = st.slider(
        "",
            0, 100,
            st.session_state.progress,
            label_visibility="collapsed"
    )
    
    # 计算当前播放时间（模拟）
        total_seconds = int(current_music['duration'].split(':')[0]) * 60 + int(current_music['duration'].split(':')[1])
        current_seconds = int(total_seconds * st.session_state.progress / 100)
        current_time = f"{current_seconds//60}:{current_seconds%60:02d}"
    
    # 显示播放时间
        st.caption(f"{current_time} / {current_music['duration']}")

    with col_volume:
    # 音量按钮
        st.button("🔊 音量", use_container_width=True)

# 10. 音频播放组件（实际播放音频）
    st.markdown("---")
    st.subheader("🎧 音频播放")
    st.audio(current_music["audio_url"], format="audio/mp3")

# 11. 随机播放按钮（额外功能）
    def random_play():
        st.session_state.current_music_idx = random.randint(0, len(music_list)-1)
        st.session_state.progress = 0

    st.button("🔀 随机播放", on_click=random_play, use_container_width=True)

# 12. 显示歌曲列表
    st.markdown("---")
    st.subheader("📜 歌曲列表")
    for idx, music in enumerate(music_list):
        active_tag = " 🟢 正在播放" if idx == st.session_state.current_music_idx else ""
        st.write(f"{idx+1}. {music['title']} - {music['artist']} {active_tag}")



with tab5:
    st.header("这是第五个选项卡")
    st.markdown("#### 第二个选项卡的内容")
    import streamlit as st

# 页面配置：卡通蓝主题+猫和老鼠图标
    st.set_page_config(
        page_title="猫和老鼠 - 经典剧集",
        page_icon="🐭",  # 杰瑞图标
        layout="centered"
)

# 自定义CSS：添加全局图片背景+样式优化
    st.markdown("""
<style>
/* 全局页面背景：设置猫和老鼠主题图片背景 */
body {
    background-image: url("https://pic1.zhimg.com/v2-d512738bfdea04b3c37541b3da7bb9da_r.jpg?source=1940ef5c");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center center;
}

/* 内容容器：半透明背景增强可读性 */
.block-container {
    background-color: rgba(255, 255, 255, 0.9);  /* 提高白色透明度，避免遮挡背景 */
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(74, 144, 226, 0.4);
    margin: 20px auto;
    max-width: 800px;  /* 限制内容宽度，适配背景 */
}

/* 标题样式 */
h1 {
    color: #2A76C8;
    text-align: center;
    font-family: "微软雅黑", sans-serif;
    font-weight: bold;
    text-shadow: 2px 2px 3px rgba(0, 0, 0, 0.15);
    margin-bottom: 20px;
}

/* 剧集按钮样式 */
.stButton>button {
    background-color: #4A90E2;
    color: white;
    width: 100%;
    border-radius: 8px;
    margin: 5px 0;
    font-size: 16px;
    border: none;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
.stButton>button:hover {
    background-color: #357ABD;
    transform: scale(1.02);
}

/* 视频容器样式：增强边框与背景融合 */
div[data-testid="stVideo"] {
    border: 3px solid #FFD700;  /* 用金色边框匹配猫和老鼠卡通风格 */
    border-radius: 10px;
    padding: 5px;
    background-color: white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* 剧情介绍卡片样式 */
.plot-card {
    background-color: #F0F8FF;
    border-left: 4px solid #4A90E2;
    padding: 10px 15px;
    margin-top: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

h3, h4 {
    color: #2A76C8;
    font-family: "微软雅黑", sans-serif;
}

/* 移除默认空白背景 */
.main {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

# 猫和老鼠视频+剧情介绍列表（国内可访问MP4链接）
    video_list = [
    {
        "url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4",
        "title": "第1集：奶酪大作战",
        "episode": 1,
        "plot": "杰瑞偷偷潜入汤姆的厨房偷奶酪，汤姆布下重重陷阱想要抓住杰瑞，却屡次被聪明的杰瑞反套路，不仅没抓到杰瑞，还把厨房搞得一团糟，最后被主人训斥，杰瑞则抱着奶酪在洞里得意洋洋～"
    },
    {
        "url": "https://www.w3schools.com/html/movie.mp4",
        "title": "第2集：汤姆的陷阱",
        "episode": 2,
        "plot": "汤姆为了抓住总偷吃东西的杰瑞，精心设计了一个复杂的奶酪陷阱，本以为万无一失，结果陷阱却频频失灵，反而把自己困在里面，杰瑞还趁机捉弄汤姆，最后汤姆只能眼睁睁看着杰瑞带着奶酪溜走。"
    },
    {
        "url": "https://media.w3.org/2010/05/sintel/trailer.mp4",
        "title": "第3集：杰瑞的反击",
        "episode": 3,
        "plot": "汤姆被主人要求看好新买的鱼缸，却总想着抓杰瑞，不小心把鱼缸打翻，为了掩盖错误汤姆试图糊弄主人，杰瑞看穿后故意捣乱，让汤姆一次次出糗，最后杰瑞还帮主人找回了小鱼，汤姆则被罚打扫卫生。"
    },
    {
        "url": "https://v-cdn.zjol.com.cn/280446.mp4",
        "title": "第4集：猫狗联盟",
        "episode": 4,
        "plot": "家里来了一只凶巴巴的流浪狗，汤姆和杰瑞都被欺负得团团转，为了赶走这只狗，原本针锋相对的汤姆和杰瑞首次联手，想出各种妙招捉弄流浪狗，最后成功把它赶出门，不过刚消停，俩活宝又开始互相打闹～"
    },
    {
        "url": "https://v-cdn.zjol.com.cn/280447.mp4",
        "title": "第5集：太空大冒险",
        "episode": 5,
        "plot": "汤姆意外被送上了去往太空的火箭，杰瑞也不小心跟着溜上了船，在失重的太空舱里，汤姆依旧想抓杰瑞，结果闹出各种爆笑笑话，还不小心触发了火箭的各种按钮，最后俩家伙靠着误打误撞成功返回地球。"
    }
]

# 初始化会话状态
    if "current_episode" not in st.session_state:
        st.session_state.current_episode = 0

# 切换剧集函数
    def switch_episode(index):
        st.session_state.current_episode = index

# 页面标题
    st.title("🐱🐭 猫和老鼠 - 经典剧集 🐭🐱")

# 播放当前选中的视频
    current_video = video_list[st.session_state.current_episode]
    st.info(f"正在播放：{current_video['title']}")
    st.video(
        data=current_video["url"],
        format="video/mp4",
        start_time=0,
        autoplay=False
)

# 显示当前剧集的剧情介绍
    st.markdown(f"""
<div class='plot-card'>
    <h4>📖 剧情介绍</h4>
    <p>{current_video['plot']}</p>
</div>
""", unsafe_allow_html=True)

# 剧集选择区域
    st.write("### 选择剧集")
    for idx, video in enumerate(video_list):
        st.button(
            label=video["title"],
            on_click=switch_episode,
            args=(idx,)
    )

with tab6:
    st.header("这是第六个选项卡")
    st.markdown("#### 第二个选项卡的内容")
    import streamlit as st
    import datetime
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    import io
    from PIL import Image as PILImage

# 全局页面配置（仅保留一个，放在最顶部）
    st.set_page_config(
    page_title="选项卡版简历生成器",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 选项卡主标题
    st.title("选项卡功能示例")
# 创建三个选项卡
    tab1, tab2, tab3 = st.tabs(["个人简历生成器", "选项卡2", "选项卡3"])

# ---------------------- 第一个选项卡：完整简历生成器功能 ----------------------
    with tab1:
    # 自定义浅色系样式（莫兰迪色系，柔和清新）
        st.markdown("""
        <style>
        /* 整体页面样式 */
        .stApp { 
            background-color: #F9F7F8; 
            color: #4A4A4A; 
            font-family: "Microsoft YaHei", sans-serif;
        }
        /* 输入框/下拉框样式 */
        .stTextInput > div > div > input, 
        .stSelectbox > div > div > select, 
        .stTextArea > div > div > textarea,
        .stDateInput > div > div > input { 
            background-color: #FFFFFF; 
            color: #4A4A4A; 
            border: 1px solid #E8D5DE; 
            border-radius: 8px;
            padding: 8px 12px;
        }
        /* 滑块样式 */
        .stSlider > div > div > div { color: #9D6588; }
        .stSlider [data-baseweb="slider"] { color: #D88FB9; }
        /* 按钮样式（柔和粉色） */
        .stButton > button { 
            background-color: #E899AF; 
            color: white; 
            border: none;
            border-radius: 8px;
            padding: 8px 20px;
            font-weight: 500;
        }
        .stButton > button:hover { background-color: #D88FB9; }
        /* 单选框/多选框样式 */
        .stRadio > div > label, .stMultiSelect > div > label { color: #6B5B6B; }
        /* 预览卡片（米白底色+浅粉边框） */
        .preview-card { 
            background-color: #FFFFFF; 
            padding: 30px; 
            border-radius: 12px;
            border: 1px solid #F0E0E6;
            box-shadow: 0 2px 10px rgba(222, 200, 210, 0.1);
        }
        /* 标题样式 */
        h1, h2, h3 { color: #8B6B89; }
        .stCaption { color: #9A8B98; }
        /* 分割线样式 */
        hr { border-top: 1px solid #F0E0E6; }
        /* 经历卡片样式 */
        .experience-card {
            background-color: #F9F7F8;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 8px;
            border-left: 3px solid #D88FB9;
        }
        </style>
    """, unsafe_allow_html=True)

    # 生成PDF简历的函数
        def generate_resume_pdf(name, nickname, birth_date, gender, education, work_exp, 
                           salary_min, salary_max, grad_info, job_intention, job_city, 
                           arrival_time, phone, email, address, id_card, skills, experience, intro, avatar):
        # 创建内存缓冲区
            buffer = io.BytesIO()
        
        # 创建PDF文档
            doc = SimpleDocTemplate(buffer, pagesize=A4,
                               rightMargin=inch/2, leftMargin=inch/2,
                               topMargin=inch/2, bottomMargin=inch/2)
            elements = []
            styles = getSampleStyleSheet()
        
        # 自定义样式
            title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=10,
            textColor=colors.Color(139/255, 107/255, 137/255)  # #8B6B89
        )
        
            sub_title_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=8,
            textColor=colors.Color(139/255, 107/255, 137/255)
        )
        
            normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=5,
            textColor=colors.Color(74/255, 74/255, 74/255)  # #4A4A4A
        )
        
        # 1. 姓名和基本信息
            name_text = name if name else "你的姓名"
            elements.append(Paragraph(name_text, title_style))
        
        # 基本信息行
            basic_info = f"昵称：{nickname if nickname else '暂无'} | {birth_date.strftime('%Y年%m月')}出生 | 性别：{gender} | 学历：{education}"
            elements.append(Paragraph(basic_info, normal_style))
            elements.append(Spacer(1, 10))
        
        # 2. 求职意向
            elements.append(Paragraph("求职意向", sub_title_style))
            intention_info = f"""
        意向岗位：{job_intention if job_intention else '暂无'}<br/>
        意向城市：{', '.join(job_city) if job_city else '暂无'}<br/>
        到岗时间：{arrival_time}<br/>
        期望薪资：{salary_min}-{salary_max}元/月 | 工作经验：{work_exp}年
        """
            elements.append(Paragraph(intention_info, normal_style))
            elements.append(Spacer(1, 10))
        
        # 3. 联系方式
            elements.append(Paragraph("联系方式", sub_title_style))
            contact_info = f"""
        电话：{phone if phone else '暂无'}<br/>
        邮箱：{email if email else '暂无'}<br/>
        地址：{address if address else '暂无'}<br/>
        身份证号：{id_card if id_card else '未填写'}
        """
            elements.append(Paragraph(contact_info, normal_style))
            elements.append(Spacer(1, 10))
        
        # 4. 毕业信息
            elements.append(Paragraph("毕业信息", sub_title_style))
            elements.append(Paragraph(f"毕业院校及时间：{grad_info}", normal_style))
            elements.append(Spacer(1, 10))
        
        # 5. 专业技能
            elements.append(Paragraph("专业技能", sub_title_style))
            if skills:
                skill_text = "、".join(skills)
            else:
                skill_text = "暂未填写"
            elements.append(Paragraph(skill_text, normal_style))
            elements.append(Spacer(1, 10))
        
        # 6. 个人经历
            elements.append(Paragraph("个人经历", sub_title_style))
            if experience.strip():
                exp_lines = [line.strip() for line in experience.strip().split('\n') if line.strip()]
                for line in exp_lines:
                    elements.append(Paragraph(line, normal_style))
            else:
                elements.append(Paragraph("暂未填写", normal_style))
            elements.append(Spacer(1, 10))
        
        # 7. 个人简介
            elements.append(Paragraph("个人简介", sub_title_style))
            intro_text = intro if intro else "✨ 这个人很温柔，还没有留下介绍哦～"
            elements.append(Paragraph(intro_text, normal_style))
        
        # 生成PDF
            doc.build(elements)
        
        # 重置缓冲区指针
            buffer.seek(0)
            return buffer

    # 页面标题
        st.title("👩‍🎓 个人简历生成器（女生版）")
        st.caption("基于Streamlit的清新系简历制作工具")

    # 分栏：左侧表单（更紧凑），右侧预览（更精致）
        col1, col2 = st.columns([1, 1.3])

        with col1:
            st.subheader("📝 个人信息填写")
        
        # 基础信息（增加emoji装饰）
            name = st.text_input("姓名", placeholder="请输入你的姓名")
            nickname = st.text_input("昵称/艺名", placeholder="可选，如：小桃、Lily")
            phone = st.text_input("📱 联系电话", placeholder="请输入常用手机号")
            email = st.text_input("✉️ 电子邮箱", placeholder="请输入常用邮箱")
            address = st.text_input("📍 居住地址", placeholder="如：XX市XX区XX路")
            id_card = st.text_input("🆔 身份证号", placeholder="可选，谨慎填写")
        
        # 出生日期（默认2000年，样式更柔和）
            birth_date = st.date_input(
            "🎂 出生日期", 
            datetime.date(2000, 1, 1),
            format="YYYY-MM-DD"
        )
        
        # 性别、学历（选项更友好）
            gender = st.radio("👧 性别", ["女", "男", "其他"], horizontal=True)
            education = st.selectbox(
            "🎓 最高学历", 
            ["本科", "专科", "硕士", "博士", "高中及以下"],
            index=0
        )
        
        # 技能选择（增加女性求职高频技能）
            skills = st.multiselect(
            "💻 掌握技能", 
            [
                "HTML/CSS", "JavaScript", "Python", "Java", 
                "数据分析", "UI/UX设计", "新媒体运营", "文案策划",
                "人力资源管理", "财务会计", "行政办公", "客户服务",
                "电商运营", "视频剪辑", "插画设计", "英语口译"
            ],
            default=["UI/UX设计", "新媒体运营"]
        )
        
        # 工作经验（滑块范围调整，更贴合应届生/职场新人）
            work_exp = st.slider("💼 工作经验（年）", 0, 10, 0)
        
        # 薪资期望（范围滑块，默认更贴合女性求职区间）
            salary_min, salary_max = st.slider(
            "💰 期望薪资范围（元/月）",
            min_value=3000,
            max_value=50000,
            value=(8000, 12000)
        )
        
        # 毕业信息（样式优化）
            grad_info = st.selectbox(
            "🎓 毕业院校及时间", 
            ["2024届 某某大学 某某专业", "2023届 某某大学 某某专业", "2022届 某某大学 某某专业", "自定义"],
            index=0
        )
            if grad_info == "自定义":
                grad_info = st.text_input("请输入毕业院校及时间", placeholder="如：2024届 北京师范大学 汉语言文学")
        
        # 新增：求职意向模块
            st.subheader("🎯 求职意向")
            job_intention = st.selectbox(
            "意向岗位",
            [
                "新媒体运营", "UI/UX设计师", "行政专员", "人力资源专员",
                "电商运营", "文案策划", "财务会计", "客户服务",
                "视频剪辑师", "插画设计师", "英语翻译", "数据分析专员",
                "自定义"
            ],
            index=0
        )
        # 自定义意向岗位
            if job_intention == "自定义":
                job_intention = st.text_input("请输入自定义意向岗位", placeholder="如：小红书内容运营、品牌策划")
        
        # 意向工作城市
            job_city = st.multiselect(
            "意向工作城市",
            ["北京", "上海", "广州", "深圳", "杭州", "成都", "南京", "武汉", "重庆", "西安", "其他"],
            default=["北京", "上海"]
        )
        # 自定义工作城市
            custom_city = ""
            if "其他" in job_city:
                custom_city = st.text_input("请输入其他意向城市", placeholder="如：苏州、厦门")
                job_city = [city for city in job_city if city != "其他"] + ([custom_city] if custom_city else [])
        
        # 到岗时间
            arrival_time = st.selectbox(
            "期望到岗时间",
            ["随时到岗", "1周内", "2周内", "1个月内", "待定"],
            index=0
        )
        
        # 个人经历填写
            st.markdown("---")
            st.subheader("📜 个人经历")
            experience = st.text_area(
            "工作/实习/项目经历",
            placeholder="请按以下格式填写（每行一条经历）：\n2023.07-2024.02 XX公司 新媒体运营 主要负责小红书内容创作，月均涨粉500+，策划爆款笔记10篇\n2022.09-2023.06 XX大学 学生会宣传部部长 组织校园文创活动，参与人数超500人...",
            height=150
        )
        
        # 个人简介（提示语更温柔）
            intro = st.text_area(
            "💬 个人简介", 
                placeholder="请简要介绍你的专业背景、职业目标和个人特点～\n比如：擅长新媒体内容创作，有2年小红书运营经验，审美在线，执行力强...",
            height=120
        )
        
        # 头像上传（提示更友好）
            avatar = st.file_uploader(
            "🖼️ 上传个人照片（可选）", 
            type=["jpg", "jpeg", "png"],
            help="建议上传清晰的正面照/生活照，尺寸1:1最佳"
        )

        with col2:
            st.subheader("✨ 简历实时预览")
        # 预览卡片（浅色系样式）
            with st.container(border=True):
                st.markdown('<div class="preview-card">', unsafe_allow_html=True)
            
            # 预览头部（更精致）
                st.markdown(
                f"<h3 style='color:#8B6B89; margin-bottom: 8px;'>{name if name else '你的姓名'}</h3>", 
                unsafe_allow_html=True
            )
                st.caption(f"昵称：{nickname if nickname else '暂无'} | {birth_date.strftime('%Y年%m月')}出生")
            
            # 头像+核心信息栏（布局更美观）
                info_col1, info_col2 = st.columns([0.3, 0.7])
                with info_col1:
                # 头像占位（女生风格头像）
                    if avatar:
                        st.image(avatar, width=120, caption="个人照片")
                    else:
                        st.image(
                        "https://api.dicebear.com/7.x/avataaars-neutral/svg?seed=girl&accessories=round&hair=longStraight&clothes=blazerShirt",
                        width=120,
                        caption="头像占位"
                    )
                with info_col2:
                    st.markdown(f"<p>👧 性别：{gender}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>🎓 学历：{education}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>💼 工作经验：{work_exp}年</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>💰 期望薪资：{salary_min}-{salary_max}元/月</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>🎓 毕业信息：{grad_info}</p>", unsafe_allow_html=True)
            
            # 新增：求职意向预览
                st.markdown("---")
                st.subheader("🎯 求职意向", anchor=False)
                intention_col1, intention_col2, intention_col3 = st.columns(3)
                with intention_col1:
                    st.markdown(f"<p><strong>意向岗位：</strong>{job_intention if job_intention else '暂无'}</p>", unsafe_allow_html=True)
                with intention_col2:
                    st.markdown(f"<p><strong>意向城市：</strong>{', '.join(job_city) if job_city else '暂无'}</p>", unsafe_allow_html=True)
                with intention_col3:
                    st.markdown(f"<p><strong>到岗时间：</strong>{arrival_time}</p>", unsafe_allow_html=True)
            
            # 联系方式（排版更整洁）
                st.markdown("---")
                st.subheader("📞 联系方式", anchor=False)
                contact_col1, contact_col2 = st.columns(2)
                with contact_col1:
                    st.write(f"电话：{phone if phone else '暂无'}")
                    st.write(f"邮箱：{email if email else '暂无'}")
                with contact_col2:
                    st.write(f"地址：{address if address else '暂无'}")
                    st.write(f"身份证号：{id_card if id_card else '未填写'}")
            
            # 技能展示（标签化样式）
                st.markdown("---")
                st.subheader("💻 专业技能", anchor=False)
                if skills:
                # 技能标签化展示（更美观）
                    skill_tags = " ".join([f"<span style='background-color:#F0E0E6; color:#8B6B89; padding:4px 10px; border-radius:20px; margin:0 5px 5px 0; display:inline-block;'>{skill}</span>" for skill in skills])
                    st.markdown(skill_tags, unsafe_allow_html=True)
                else:
                    st.write("暂未填写技能信息，快去左侧选择吧～")
            
            # 个人经历预览
                st.markdown("---")
                st.subheader("📜 个人经历", anchor=False)
                if experience.strip():
                # 按行拆分经历并格式化展示
                    exp_lines = [line.strip() for line in experience.strip().split('\n') if line.strip()]
                    for line in exp_lines:
                        st.markdown(f"<div class='experience-card'>{line}</div>", unsafe_allow_html=True)
                else:
                    st.write("暂未填写个人经历，快去左侧补充吧～")
            
            # 个人简介（样式优化）
                st.markdown("---")
                st.subheader("💬 个人简介", anchor=False)
                st.write(intro if intro else "✨ 这个人很温柔，还没有留下介绍哦～")
            
                st.markdown('</div>', unsafe_allow_html=True)

    # 底部操作按钮（下载/重置）
        st.markdown("---")
        btn_col1, btn_col2 = st.columns([0.1, 0.9])
        with btn_col1:
        # 生成PDF并提供下载
            if st.button("📥 导出简历", use_container_width=True):
            # 生成PDF文件
                pdf_buffer = generate_resume_pdf(
                name, nickname, birth_date, gender, education, work_exp,
                salary_min, salary_max, grad_info, job_intention, job_city,
                arrival_time, phone, email, address, id_card, skills,
                experience, intro, avatar
            )
            
            # 设置下载文件名
                file_name = f"{name if name else '个人简历'}_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
            
            # 提供下载按钮
                st.download_button(
                label="下载PDF简历",
                data=pdf_buffer,
                file_name=file_name,
                mime="application/pdf",
                use_container_width=True
            )
                st.success("✅ 简历已生成，点击按钮即可下载！")

        with btn_col2:
        # 重置表单功能
            if st.button("🔄 重置表单", use_container_width=True):
            # 重置所有输入项（通过刷新页面实现）
                st.rerun()

