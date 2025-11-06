import streamlit as st
import math

st.title("液滴落下速度計算ツール（液滴中心高度指定版）")

st.markdown("""
直径 D [mm] の液滴が落下開始高さ H [m] から落ちるとき、  
**液滴中心が D/2 高さにある時の速度** を計算します（空気抵抗なし）。
""")

g = 9.80665  # 重力加速度 [m/s^2]

# 入力欄
H = st.number_input("落下開始高さ H [m]", min_value=0.001, max_value=10.0, value=0.15, step=0.01)
D = st.number_input("液滴直径 D [mm]", min_value=0.1, max_value=100.0, value=4.0, step=0.1)

# 液滴中心が D/2 の高さにあるときの速度
z_center = D / 1000 / 2  # mm → m に変換して半分
if H > z_center:
    v = math.sqrt(2 * g * (H - z_center))
    st.success(f"液滴中心が {z_center:.3f} m の高さにあるときの速度: **{v:.3f} m/s**")
else:
    st.warning("落下高さ H は液滴中心より高い値にしてください。")

st.caption("※空気抵抗は無視しています。")
