import json
import boto3

sns = boto3.client("sns")
SNS_TOPIC_ARN = "arn:aws:sns:eu-west-3:822710269935:Misconfiguration_S3_Visibility"

def lambda_handler(event, context):
    alarm = event.get("alarmData", {})
    alarm_name = alarm.get("alarmName")
    state = alarm.get("state", {})
    metric = None

    # aller chercher le nom de la métrique
    metrics = alarm.get("configuration", {}).get("metrics", [])
    if metrics:
        metric = metrics[0].get("metricStat", {}).get("metric", {}).get("name")

    # construire un message résumé
    message = {
        "AlarmName": alarm_name,
        "NewState": state.get("value"),
        "Reason": state.get("reason"),
        "Metric": metric,
        "Region": event.get("region"),
        "AccountId": event.get("accountId"),
        "Time": event.get("time")
    }

    # publier
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"[ALARM] {alarm_name}",
        Message=json.dumps(message, indent=2)
    )
