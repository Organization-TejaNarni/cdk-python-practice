### SNS Topic ###

from aws_cdk import (
    aws_sns as sns,
    core,
)


#import aws_cdk.aws_sns as sns

# data_protection_policy: Any


class AlarmStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


topic = sns.Topic(self, "Topic",
    content_based_deduplication=True,
    display_name="Customer subscription topic",
    fifo=True,
    topic_name="customerTopic"
)

#my_topic.add_subscription(subscriptions.UrlSubscription("https://foobar.com/"))