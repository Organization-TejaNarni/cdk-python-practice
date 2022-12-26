### SNS Topic ###

from aws_cdk import (
    aws_sns as sns,
    core,
)


#import aws_cdk.aws_sns as sns

# data_protection_policy: Any

topic = sns.Topic(self, "Topic",
    display_name="Customer subscription topic"
)

my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(subscriptions.UrlSubscription("https://foobar.com/"))