import boto3

session = boto3.Session(profile_name='pythonAutomation')

ec2_client = session.resource('ec2')
s3 = session.resource('s3')

'''
for bucket in s3.buckets.all():
    print(bucket)
'''