import boto3


def provision_ec2_instance(instance_name):
    ec2 = boto3.client("ec2")

    key_pair_name = f"{instance_name}_keypair"
    key_pair = ec2.create_key_pair(KeyName=key_pair_name)
    private_key = key_pair["KeyMaterial"]

    with open(f"{key_pair_name}.pem", "w") as file:
        file.write(private_key)

    print(f"Key pair created: {key_pair_name}.pem")

    sg_name = f"{instance_name}_sg"
    security_group = ec2.create_security_group(
        GroupName=sg_name, Description="Security group for Minecraft server"
    )
    sg_id = security_group["GroupId"]

    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            },
            {
                "IpProtocol": "tcp",
                "FromPort": 80,
                "ToPort": 80,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            },
            {
                "IpProtocol": "tcp",
                "FromPort": 25565,
                "ToPort": 25565,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            },
        ],
    )
    print(f"Security group created and configured: {sg_name} (ID: {sg_id})")

    instance = ec2.run_instances(
        ImageId="ami-055943271915205db",
        InstanceType="t2.micro",
        KeyName=key_pair_name,
        SecurityGroupIds=[sg_id],
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [{"Key": "Name", "Value": instance_name}],
            }
        ],
    )

    instance_id = instance["Instances"][0]["InstanceId"]
    print(f"Instance launched: {instance_id}")

    ec2_resource = boto3.resource("ec2")
    instance = ec2_resource.Instance(instance_id)
    print("Waiting for instance to enter running state...")
    instance.wait_until_running()

    instance.load()

    public_dns = instance.public_dns_name
    print(f"Instance is running. Public DNS: {public_dns}")

    return {
        "key_pair_name": key_pair_name,
        "private_key_file": f"{key_pair_name}.pem",
        "security_group_id": sg_id,
        "instance_id": instance_id,
        "public_dns": public_dns,
    }


if __name__ == "__main__":
    instance_details = provision_ec2_instance("minecraft-server")

    print("\nProvisioning complete. Details:")
    print(f"Key Pair Name: {instance_details['key_pair_name']}")
    print(f"Private Key File: {instance_details['private_key_file']}")
    print(f"Security Group ID: {instance_details['security_group_id']}")
    print(f"Instance ID: {instance_details['instance_id']}")
    print(f"Public DNS: {instance_details['public_dns']}")
