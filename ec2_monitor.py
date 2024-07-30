import sys
import boto3

def monitor_instance(instance_id, region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.monitor_instances(InstanceIds=[instance_id])
    return response

def unmonitor_instance(instance_id, region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.unmonitor_instances(InstanceIds=[instance_id])
    return response

def main():
    if len(sys.argv) != 4:
        print("Usage: python ec2_monitor.py <ON|OFF> <instance_id> <region>")
        sys.exit(1)

    action = sys.argv[1]
    instance_id = sys.argv[2]
    region = sys.argv[3]

    if action == 'ON':
        response = monitor_instance(instance_id, region)
        print(f"Monitoring enabled for instance {instance_id}.")
    elif action == 'OFF':
        response = unmonitor_instance(instance_id, region)
        print(f"Monitoring disabled for instance {instance_id}.")
    else:
        print("Invalid action. Use 'ON' to enable monitoring or 'OFF' to disable monitoring.")
        sys.exit(1)

    print(response)

if __name__ == '__main__':
    main()
