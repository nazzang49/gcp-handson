#!/bin/zsh

# publish
gcloud pubsub topics create my-topic

# subscribe
gcloud pubsub subscriptions create my-sub --topic my-topic