import streamlit as st

# --- 页面配置（必须放在第一行） ---
st.set_page_config(page_title="宫廷生存记", page_icon="👑")

# --- 自定义 CSS 样式（让图片居中） ---
st.markdown("""
    <style>
    .center-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 15px;
        border: 2px solid #ddd;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. 初始化游戏状态 ---
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# --- 2. 定义剧情函数 ---
def start_game():
    st.session_state.stage = 1

def choose_sleep():
    st.session_state.stage = 99

def choose_explore():
    st.session_state.stage = 2

def go_to_king():
    st.session_state.stage = 3

def pretend_ill():
    st.session_state.stage = 4

def restart_game():
    st.session_state.stage = 0

# --- 3. 游戏主逻辑 ---

# 阶段 0：游戏封面
if st.session_state.stage == 0:
    # 这里用了一个网络图片作为封面，你可以换成任何你喜欢的图片链接
    st.image("start.jpg", use_column_width=True)
    st.markdown("<h1 style='text-align: center; color: #4a1c4a;'>👑 宫廷生存记</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>你醒来时发现自己身处华丽的宫殿，命运掌握在你手中。</p>", unsafe_allow_html=True)
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.button("✨ 开始冒险", on_click=start_game, use_container_width=True)

# 阶段 1：醒来
elif st.session_state.stage == 1:
    st.image("bed.jpg", caption="清晨的寝宫", use_column_width=True)
    st.write("### 第一章：苏醒")
    st.write("你躺在柔软的丝绸被褥中，阳光透过窗棂洒进来。")
    st.write("你是选择继续**睡觉**，还是**出门打探消息**？")

    col1, col2 = st.columns(2)
    with col1:
        st.button("😴 再睡一会", on_click=choose_sleep, use_container_width=True)
    with col2:
        st.button("🚶 出门看看", on_click=choose_explore, use_container_width=True)

# 阶段 2：婢女与侍卫
elif st.session_state.stage == 2:
    st.image("shiwei.jpg", caption="宫廷走廊", use_column_width=True)
    st.write("### 第二章：惊人的秘密")
    st.write("婢女告诉你，你是这个国家尊贵的公主，三天后将成为女王。")
    st.write("突然，一名侍卫走过来，冷冰冰地说：“国王请您过去一趟。”")
    st.warning("你感觉到了一丝杀气...")
    st.write("你会怎么做？")

    col1, col2 = st.columns(2)
    with col1:
        st.button("🤒 装病推脱", on_click=pretend_ill, use_container_width=True)
    with col2:
        st.button("🚶 跟随侍卫", on_click=go_to_king, use_container_width=True)

# 阶段 3：坏结局
elif st.session_state.stage == 3:
    st.image("die.jpg", caption="黑暗的角落", use_column_width=True)
    st.error("### 结局：暗杀")
    st.write("你跟随侍卫走进了一条偏僻的走廊...")
    st.write("突然背后一阵剧痛。你被侍卫暗杀了。")
    st.write("原来这是你失散多年的弟弟（王子）为了夺位设下的圈套。")
    st.button("🔄 重新开始", on_click=restart_game)

# 阶段 4：好结局
elif st.session_state.stage == 4:
    st.image("win.jpg", caption="女王加冕", use_column_width=True)
    st.success("### 结局：女王万岁！")
    st.write("你称病不出，暗中观察。")
    st.write("三天后，你果然发现了弟弟（王子）准备暗杀你的阴谋。")
    st.write("你先发制人，揭露了他的罪行。")
    st.balloons()
    st.write("恭喜！你成功登上了王位，成为了这个国家最尊贵的人！")
    st.button("🔄 再玩一次", on_click=restart_game)

# 阶段 99：现实结局
elif st.session_state.stage == 99:
    st.image("wake.jpg", caption="办公桌", use_column_width=True)
    st.info("### 结局：大梦初醒")
    st.write("你在床上翻了个身，再次醒来时，发现自己躺在狭小的出租屋里。")
    st.write("原来这只是一场梦。")
    st.write("你叹了口气，看了一眼时间，该去上班了。")
    st.write("请继续你的牛马生活吧...")
    st.button("🔄 醒来", on_click=restart_game)