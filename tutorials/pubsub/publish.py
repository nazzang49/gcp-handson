from google.cloud import pubsub_v1

project_id = "winged-poetry-410913"
topic_id = "my-topic"

publisher = pubsub_v1.PublisherClient()

# projects/{project_id}/topics/{topic_id}
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 10):
    data_str = f"Message number {n}"

    # todo must encode!
    data = data_str.encode("utf-8")

    future = publisher.publish(topic_path, data)
    print(future.result())

print(f"Published messages to {topic_path}.")