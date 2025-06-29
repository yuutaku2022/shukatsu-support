import streamlit as st
import pandas as pd
import datetime
import os
from dashBord import show_dashboard
from organization_create import show_org_create
from organization_detail import show_org_detail

#初期ページ設定
if "page" not in st.session_state:
	st.session_state.page = "dashboard"

#表示画面の切り替え
if st.session_state.page == "org_create":
	show_org_create()
elif st.session_state.page == "org_detail":
    show_org_detail()
elif st.session_state.page == "event_make":
	show_event_create()
else:
	show_dashboard()