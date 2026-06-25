# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:14:48 2026

@author: jaken
"""
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import gspread
import os
import pandas as pd

class DataHandler:
    def __init__(self, json_filename, spreadsheet_id):
        base_path = r'C:\proyecto_ganadero'
        full_path = os.path.join(base_path, json_filename)
        
        self.gc = gspread.service_account(filename=full_path)
        self.sh = self.gc.open_by_key(spreadsheet_id)
    
    def get_as_dataframe(self, worksheet_name):
        worksheet = self.sh.worksheet(worksheet_name)
        data = worksheet.get_all_records()
        return pd.DataFrame(data)

    def add_record(self, worksheet_name, list_of_data):
        worksheet = self.sh.worksheet(worksheet_name)
        worksheet.append_row(list_of_data)