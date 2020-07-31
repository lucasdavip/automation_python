#!/bin/python3
# Script python gera relatorio sns Informações relevantes para crir sns com terraform
# Obs Criar o arquivo sns_arn.txt
# Pupular o arquivo: aws sns list-topics | grep -v { | grep -v } | grep -v "Topics" | cut -d"\"" -f4 | grep -v ] > sns_arn.txt


import boto3
client = boto3.client('sns')


def topic_attribute(topico):
    response = client.get_topic_attributes(TopicArn=topico)
    return response


def topic_subscriptions(topico):
    response = client.list_subscriptions_by_topic(TopicArn=topico)
    return response


def report_attribute(topico):
    attributes_all = topic_attribute(topico=topico)
    attributes = attributes_all['Attributes']
    arn = attributes['TopicArn']
    delivery = attributes['EffectiveDeliveryPolicy']
    return arn, delivery


def report_subscriptions(topico):
    subscription_all = topic_subscriptions(topico=topico)
    subscription = subscription_all['Subscriptions']
    return subscription


if __name__ == '__main__':
    try:
        sns_arn = open("sns_arn.txt", "r", encoding="utf-8")
        for topico in sns_arn:
            topico = topico.rstrip()
            report_att = report_attribute(topico=topico)
            report_sub = report_subscriptions(topico=topico)
            print('\n')
            print('------Topic Info-------------')
            print(report_att)
            print('------Subscription Info------')
            print(report_sub)
            print('\n')
    finally:
        sns_arn.close()
