# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:14:48 2026

@author: jaken
"""
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import streamlit as st
import gspread
import json

class DataHandler:
    def __init__(self, json_filename, spreadsheet_id):
        # Intenta cargar desde los Secrets de Streamlit en la nube
        try:
            if "GSPREAD" in st.secrets:
                creds = json.loads(st.secrets["GSPREAD"]["json"])
                self.gc = gspread.service_account_from_dict(creds)
            else:
                # Si estamos en tu PC local, busca el archivo json
                self.gc = gspread.service_account(filename=json_filename)
            self.sh = self.gc.open_by_key(spreadsheet_id)
        except Exception as e:
            st.error(f"Error al conectar con Google Sheets: {e}")

    def add_record(self, sheet_name, data):
        worksheet = self.sh.worksheet(sheet_name)
        worksheet.append_row(data)
