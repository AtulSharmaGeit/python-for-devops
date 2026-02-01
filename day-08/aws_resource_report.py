import boto3
import json

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId' : instance['InstanceId'],
                'State': instance['State']['Name']
            })
    return instances

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return buckets

def main():
    report = {
        'EC2Instances': list_ec2_instances(),
        'S3Buckets': list_s3_buckets()    
    }

    print(json.dumps(report, indent=4))

    with open('aws_report.json', 'w') as f:
        json.dump(report, f, indent=4)

if __name__ == "__main__":
    main()