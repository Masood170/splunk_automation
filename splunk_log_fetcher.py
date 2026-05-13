import splunklib.client as client
import splunklib.results as results

HOST = "10.236.6.52"
PORT = 8089

USERNAME = "admin"
PASSWORD = "ch@ngeme!"

service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)

query = """
search index=_internal
| head 100
"""

job = service.jobs.create(query)

while not job.is_done():
    pass

result_stream = job.results(output_mode='json') 

reader = results.JSONResultsReader(result_stream)

with open("logs/remote_splunk.log", "w") as f:

    for item in reader:

        if isinstance(item, dict):

            raw_event = item.get("_raw", "")

            f.write(raw_event + "\n")

print("Logs fetched successfully")