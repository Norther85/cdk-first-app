from aws_cdk import core as cdk
import aws_cdk.aws_s3 as _s3

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkFirstAppStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = _s3.Bucket(self, "MyBucket",
                            enforce_ssl=True,
                            bucket_name="tczekaj-mybucket",
                            versioned=True,
                            encryption=_s3.BucketEncryption.S3_MANAGED
                            )
