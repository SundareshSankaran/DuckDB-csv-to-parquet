import os
from py_sas_studio_custom_steps import CustomStep 


step_folder = "/create-export/create/homes/Sundaresh.Sankaran@sas.com/casuser/csv-to-parquet"
extras_folder = "/create-export/create/homes/Sundaresh.Sankaran@sas.com/casuser/csv-to-parquet/extras"
custom_step = CustomStep(name="DuckDB - CSV to Parquet")
custom_step.attach_ui(os.path.join(extras_folder,f"{custom_step.name}.json"))
custom_step.attach_sas_program(os.path.join(extras_folder,f"{custom_step.name}.sas"))


custom_step.create_custom_step(os.path.join(step_folder,f"{custom_step.name}.step"))

prompt = """
Generate a README for the given custom step. Follow same standards as the example README template
you are aware of.  Ensure that dates are in alignment with what's given on the step.

"""

custom_step.generate_readme(prompt, readme_file=f"{step_folder}/README.md")



with open(os.path.join(extras_folder,f"{custom_step.name}.sas"),"w", encoding="utf-8") as f:
    f.write(custom_step.extract_sas_program())

with open(os.path.join(extras_folder,f"{custom_step.name}.json"),"w", encoding="utf-8") as f:
    f.write(custom_step.extract_ui())