import json

from google.cloud import bigquery

def query_stackoverflow():
    client = bigquery.Client()
    query_job = client.query(
        """
        SELECT
          CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
          view_count
        FROM `bigquery-public-data.stackoverflow.posts_questions` -- public dataset offered by google!
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 10"""
    )

    results = query_job.result()  # Waits for job to complete.

    # {'_started': False, '_Iterator__active_iterator': None, 'client': <google.cloud.bigquery.client.Client object at 0x101087fd0>, 'item_to_value': <function _item_to_row at 0x104837880>, 'max_results': None, 'page_number': 0, 'next_page_token': None, 'num_results': 0, 'api_request': functools.partial(<bound method Client._call_api of <google.cloud.bigquery.client.Client object at 0x101087fd0>>, <google.api_core.retry.Retry object at 0x1047700d0>, timeout=None), 'path': '/projects/gcp-poc-411110/queries/78eb2f97-ea57-43b1-aef9-e5fb056a99f1', '_items_key': 'rows', 'extra_params': {'fields': 'jobReference,totalRows,pageToken,rows', 'location': 'US', 'formatOptions.useInt64Timestamp': True}, '_page_size': None, '_page_start': <function _rows_page_start at 0x10483eb00>, '_next_token': 'pageToken', '_field_to_index': {'url': 0, 'view_count': 1}, '_preserve_order': <re.Match object; span=(302, 310), match='ORDER BY'>, '_schema': [SchemaField('url', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('view_count', 'INTEGER', 'NULLABLE', None, None, (), None)], '_selected_fields': None, '_table': TableReference(DatasetReference('gcp-poc-411110', '_53f0a535e2b5554eeda7561f49582d3237190a97'), 'anon41e5448b33fc11ec0640971cd2884fb4a6576a5c66c743314ceb6ce33981da1b'), '_total_rows': 10, '_first_page_response': None, '_location': 'US', '_job_id': '78eb2f97-ea57-43b1-aef9-e5fb056a99f1', '_query_id': None, '_project': 'gcp-poc-411110', '_num_dml_affected_rows': None}
    print(results.__dict__)
    print(results.project) # property

    for row in results:
        print("{} : {} views".format(row.url, row.view_count))

if __name__ == "__main__":
    query_stackoverflow()