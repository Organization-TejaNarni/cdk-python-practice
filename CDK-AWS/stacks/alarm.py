from aws_cdk import (
    aws_lambda as lb,
    aws_events as events,
    aws_events_targets as targets,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core,
)


class AlarmStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cfn_topic = sns.CfnTopic(self, "MyCfnTopic",
            content_based_deduplication=False,
            data_protection_policy=data_protection_policy,
            display_name="displayName",
            fifo_topic=False,
            kms_master_key_id="kmsMasterKeyId",
            signature_version="signatureVersion",
            subscription=[sns.CfnTopic.SubscriptionProperty(
            endpoint="endpoint",
            protocol="protocol"
        )],
        tags=[CfnTag(
            key="key",
            value="value"
        )],
        topic_name="topicName"
        )

        