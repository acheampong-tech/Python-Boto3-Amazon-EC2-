import boto3

def create_ec2_instance():
    # Initialize a session using Amazon EC2
    ec2 = boto3.resource('ec2', region_name='your-region')  # e.g., 'us-west-2'

    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',  # Replace with the desired AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',  # Replace with the desired instance type
        KeyName='your-key-pair',  # Replace with the name of your key pair
        SecurityGroupIds=[
            'sg-xxxxxxxx',  # Replace with your security group ID
        ],
        SubnetId='subnet-xxxxxxxx'  # Replace with your subnet ID
    )

    instance = instances[0]

    # Add a name tag to the instance
    instance.create_tags(Tags=[{'Key': 'Name', 'Value': 'MyEC2Instance'}])  # Replace 'MyEC2Instance' with your desired name

    print(f'Created instance with ID: {instance.id}')

if __name__ == '__main__':
    create_ec2_instance()
