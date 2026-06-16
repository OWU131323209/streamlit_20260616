import streamlit as st

st.title("パッキングリスト")

# --- 1. 入力・条件の取得 ---
# 【新機能①】お出かけ先の入力欄（文字を入力欄の中に薄く表示するplaceholder付き）
destination = st.text_input("お出かけ先・イベント名", placeholder="例：テーマパーク、ショッピング、ロケ地など")

# 条件の入力（スライダーとチェックボックス）
rain_prob = st.slider("今日の降水確率は？（仮の入力）", 0, 100, 50)
is_photo_day = st.checkbox("今日はiPhoneで写真をたくさん撮る！")

# 【新機能②】自由に追加できる持ち物の入力欄
custom_item = st.text_input("追加で持っていきたいもの")


# --- 2. 持ち物リストの生成 ---
items = ["スマホ", "お財布", "家の鍵" # いつでも絶対に持っていく基本セット
]
# 【マイルール】靴擦れ対策はデフォルトで追加！
items.append("絆創膏")

# 天候による気遣い
if rain_prob > 30:
    items.extend(["折りたたみ傘", "タオル", "濡れたものを入れるビニール袋"])

# 目的による気遣い
if is_photo_day:
    items.extend(["大容量モバイルバッテリー", "画面拭きクロス"])

# 【新機能②のロジック】もし入力欄に文字が打ち込まれたら、リストの末尾に追加する
if custom_item:
    items.append(custom_item)


# --- 3. 画面への表示 ---
# 【新機能①のロジック】行き先が入力されていたら見出しをダイナミックに変える
if destination:
    st.write(f"### 🎒 {destination} の持ち物リスト")
else:
    st.write("### 🎒 今日の持ち物リスト")

# チェックボックスとして一覧表示
for item in items:
    st.checkbox(item)
