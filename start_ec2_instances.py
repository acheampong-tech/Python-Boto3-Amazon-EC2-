import boto3

def start_ec2_instances(instance_ids):
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2')

    try:
        # Start the instances
        response = ec2.start_instances(
            InstanceIds=instance_ids,
            DryRun=False                      # Set to True for a dry run to check permissions
        )
        # Print the response for debugging
        print(response)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    # List of instance IDs you want to start
    instance_ids = ['i-01b476xxxx927d0ae']
    start_ec2_instances(instance_ids)
