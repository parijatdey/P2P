import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    for filelist in s3.Bucket(bucket.name).objects.page_size(20):
        print(filelist.key)
 
