from aws_cdk import (
    aws_lambda as lb,
    aws_events as events,
    aws_events_targets as targets,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_cloudwatch as cloudwatch,
    core,
)


class AlarmStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
########################  TOPIC Creation ################
        topic = sns.Topic(self, "Topic",
            content_based_deduplication=True,
            display_name="Customer subscription topic",
            fifo=True,
            topic_name="customerTopic"
            )

########################  Subcription to htt[] ################
        topic.add_subscription(subscriptions.UrlSubscription("https://foobar.com/"))


######### cloudwatch Alarm ##############33

#####  Using an existing metric #####
        #metric = "ApproximateNumberOfMessagesVisible"


########Creating your own metric#######
        metric = cloudwatch.Metric(
            namespace="MyNamespace",
            metric_name="MyMetric",
            dimensions=dict(MyDimension="MyDimensionValue")
        )

###### Creating the alarm ####
        alarm = cloudwatch.Alarm(self, "Alarm",
            metric=metric,
            threshold=100,
            evaluation_periods=3,
            datapoints_to_alarm=2
        )

 