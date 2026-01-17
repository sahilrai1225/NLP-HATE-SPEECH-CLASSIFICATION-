import os

class GCloudSync:

    def sync_folder_to_gcloud(self,gcp_bucket_url, filepath, filename):

        command=f"gsutil cp {filepath}/{filename}  gs://{gcp_bucket_url}"
# automaically push data in gcloud 
        os.system(command)

## now code to download data/file from gcloud
    
    def sync_folder_from_gcloud(self,gcp_bucket_url,filename,destination):
        command=f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"

        os.system(command)

## GCP COMPLETE Configuration and 

