from aws_cdk import (
    aws_lambda as lb,
    aws_events as events,
    aws_events_targets as targets,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    core,
)


class AlarmStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        topic = sns.Topic(self, "Topic",
            content_based_deduplication=True,
            display_name="Customer subscription topic",
            fifo=True,
            topic_name="customerTopic"
            )
        topic.add_subscription(subscriptions.UrlSubscription("https://foobar.com/"))

        