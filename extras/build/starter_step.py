import os
from py_sas_studio_custom_steps import CustomStep 


step_folder = "/create-export/create/homes/Sundaresh.Sankaran@sas.com/casuser/csv-to-parquet"

extras_folder = "/create-export/create/homes/Sundaresh.Sankaran@sas.com/casuser/csv-to-parquet/extras"

custom_step = CustomStep(name="DuckDB - CSV to Parquet")

custom_step.add_about_page()

custom_step.create_custom_step(os.path.join(step_folder,f"{custom_step.name}.step"))

with open(os.path.join(extras_folder,f"{custom_step.name}.sas"),"w", encoding="utf-8") as f:
    f.write(custom_step.extract_sas_program())

with open(os.path.join(extras_folder,f"{custom_step.name}.json"),"w", encoding="utf-8") as f:
    f.write(custom_step.extract_ui())