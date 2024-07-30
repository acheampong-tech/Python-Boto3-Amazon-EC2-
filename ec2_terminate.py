import boto3

ec2 = boto3.resource('ec2')
ids = ['i-02b482583108f1217'] #insert instance ids separated by commas

response = ec2.instances.filter(InstanceIds = ids).terminate()
print(response)
