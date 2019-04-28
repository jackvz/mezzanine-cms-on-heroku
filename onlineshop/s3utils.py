import os, sys
from storages.backends.s3boto3 import S3Boto3Storage, S3Boto3StorageFile 


class S3BotoStorageSafe(S3Boto3Storage): 
    def __init__(self, *args, **kwargs): 
        return super(S3BotoStorageSafe, self).__init__(*args, **kwargs) 

    def isfile(self, name): 
        try: 
            name = self._normalize_name(self._clean_name(name)) 
            f = S3Boto3StorageFile(name, 'rb', self) 
            if not f.buffer_size:
                return False 
            return True 
        except: 
            return False 

    def isdir(self, name): 
        return not self.isfile(name) 

    def save(self, name, content): 
        re = super(S3BotoStorageSafe, self).save(name, content) 
        return re 

StaticS3BotoStorage = lambda: S3BotoStorageSafe(location='static') 
StaticStagingS3BotoStorage = lambda: S3BotoStorageSafe(location='static_staging') 
MediaS3BotoStorage = lambda: S3BotoStorageSafe(location='media') 
