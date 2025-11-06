import streamlit as st
import math

st.title("液滴落下速度計算ツール（中心高さ固定版）")

st.markdown("""
液滴中心が **4 mm の高さ** にあるときの速度を計算します。  
""")

g = 9.80665  # 重力加速度 [m/s^2]

# 入力欄
H = st.number_input("落下開始高さ H [m]", min_value=0.005, max_value=10.0, value=0.15, step=0.01)

# 固定中心高さ
z_center = 0.004  # 4 mm = 0.004 m

if H > z_center:
    v = math.sqrt(2 * g * (H - z_center))
    st.success(f"液滴中心が 4 mm の高さにあるときの速度: **{v:.3f} m/s**")
else:
    st.warning("落下開始高さ H は 4 mm より大きい値にしてください。")

st.caption("※空気抵抗は無視しています。")



