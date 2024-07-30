import boto3

def stop_ec2_instance(instance_id):
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2', region_name='us-east-1')  # e.g., 'us-west-2'

    # Stop the instance
    response = ec2.stop_instances(InstanceIds=[instance_id])

    # Print the response
    print(f'Stopped instance with ID: {instance_id}')
    print(response)

if __name__ == '__main__':
    instance_id = 'i-06b2xxxxxe3e3e056a4'  # Replace with your instance ID
    stop_ec2_instance(instance_id)
