"""
CuraVision AI – Supabase Client
=================================
Author : Janhvi Chaurasia  <janvhi2308@gmail.com>
Role   : Backend & API Engineer
Module : Initialises the Supabase client from Streamlit secrets for
         authentication and report storage across the application.
"""
import streamlit as st
from supabase import create_client, Client


@st.cache_resource
def get_supabase() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"],
    )


supabase = get_supabase()