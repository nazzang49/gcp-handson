from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1

project_id = "winged-poetry-410913"
subscription_id = "my-sub"

# in seconds
timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()

# projects/{project_id}/subscriptions/{subscription_id}
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    # todo response format is not json, but instance!
    # Received Message {
    #   data: b'Message number 9'
    #   ordering_key: ''
    #   attributes: {}
    # }.

    # todo data is attribution
    print(f"Received {message.data.decode('utf-8')}.")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

with subscriber:
    try:
        # timeout recommended
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  # shutdown
        streaming_pull_future.result()  # block until shutdown