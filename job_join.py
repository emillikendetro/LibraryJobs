import json

master_job_list = []

with open('ala_job_list.json', 'r') as ala_data:

    ala_jobs = json.load(ala_data)

    for ala_job in ala_jobs:

        master_job_list.append(ala_job)

with open('asist_job_list.json', 'r') as asist_data:

    asist_jobs = json.load(asist_data)

    for asist_job in asist_jobs:

        master_job_list.append(asist_job)

json.dump(master_job_list, open('master_job_list.json','w'), indent=2)
