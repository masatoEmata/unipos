import json,os
from google.cloud import bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"..\\credential\\my-api-project-167306-121b461f2074.json"
client = bigquery.Client()

class UploadCSVtoBigquery:
    def __init__(self,table_name,file):
        config_file = open("config.json","r")
        config = json.load(config_file)

        dataset_id = config["bigquery"]["dataset_id"]
        dataset_ref = client.dataset(dataset_id)
        file_path = config["file_path"]

        table_ref = dataset_ref.table(table_name)
        job_config = bigquery.LoadJobConfig()
        job_config.schema = [
            bigquery.SchemaField("timestamp","TIMESTAMP"),
            bigquery.SchemaField("post_time","TIMESTAMP"),
            bigquery.SchemaField("sender","STRING"),
            bigquery.SchemaField("receiver","STRING"),
            bigquery.SchemaField("point","INTEGER"),
            bigquery.SchemaField("message","STRING")
        ]
        job_config.source_format = bigquery.SourceFormat.CSV
        job_config.skip_leading_rows = 1
        job_config.autodetect = True
        
        try:
            with open(file, "rb") as f:
                job = client.load_table_from_file(f, table_ref, job_config=job_config)
            job.result()  # Waits for table load to complete.
            print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_name))
        except FileNotFoundError:
            print("no such csv")

if __name__=="__main__":
    UploadCSVtoBigquery()
