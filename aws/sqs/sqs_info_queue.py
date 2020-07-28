#/bin/python3

import boto3


client = boto3.client('sqs')


def list_queues():
    queue = client.list_queues()
    list_queue = queue['QueueUrls']
    return list_queue


def info_queue(queue_url):
    response = client.get_queue_attributes(
     QueueUrl=queue_url, AttributeNames=['MessageRetentionPeriod'])
    sqs_info = response['Attributes']
    return sqs_info


def format_report(queue_url):
    sqs_info = info_queue(queue_url=queue_url)
    name_queue = queue_url
    time_retention = int(sqs_info['MessageRetentionPeriod']) / 86400
    report_queue = [name_queue, int(time_retention)]
    return report_queue


if __name__ == '__main__':
    list_queue = list_queues()
    for queue in list_queue:
        report_queue = format_report(queue_url=queue)
        print(report_queue)
