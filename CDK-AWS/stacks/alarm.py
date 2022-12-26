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
    display_name="Customer subscription topic"
)

my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(subscriptions.UrlSubscription("https://foobar.com/"))