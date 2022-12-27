from aws_cdk import (
    # aws_lambda as lb,
    # aws_events as events,
    # aws_events_targets as targets,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_cloudwatch as cloudwatch,
    aws_cloudwatch_actions as cw_actions,
    aws_ecs as ecs,
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
        # metric = ecs.metric("FargatePageError")


########Creating your own metric#######
        # metric = cloudwatch.Metric(
        #     namespace="MyNamespace",
        #     metric_name="MyMetric",
        #     dimensions=dict(MyDimension="MyDimensionValue")
        # )


#         metric = cloudwatch.Metric(
#     namespace="AWS/Route53",
#     metric_name="DNSQueries",
#     dimensions_map={
#         "HostedZoneId": hosted_zone.hosted_zone_id
#     }
# )
#https://pypi.org/project/aws-cdk.aws-cloudwatch/

###### Creating the alarm ####
        # alarm = cloudwatch.Alarm(self, "Alarm",
        #     metric=metric,
        #     threshold=100,
        #     evaluation_periods=3,
        #     datapoints_to_alarm=2
        # )
######  alarm action ####

        # alarm.add_alarm_action(cw_actions.SnsAction(topic))
 