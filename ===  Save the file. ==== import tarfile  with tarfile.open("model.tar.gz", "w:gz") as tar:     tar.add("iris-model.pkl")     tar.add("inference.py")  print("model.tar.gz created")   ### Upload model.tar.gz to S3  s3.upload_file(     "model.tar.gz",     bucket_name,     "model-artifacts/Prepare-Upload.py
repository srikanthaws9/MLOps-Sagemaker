===

Save the file.
====
import tarfile

with tarfile.open("model.tar.gz", "w:gz") as tar:
    tar.add("iris-model.pkl")
    tar.add("inference.py")

print("model.tar.gz created")


### Upload model.tar.gz to S3

s3.upload_file(
    "model.tar.gz",
    bucket_name,
    "model-artifacts/model.tar.gz"
)

print("Packaged model uploaded to S3")
