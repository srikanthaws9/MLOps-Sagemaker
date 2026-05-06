import boto3
import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import os
Train a tiny ML model
iris = load_iris()
X, y = iris.data, iris.target

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "iris-model.pkl")

print("Model saved as iris-model.pkl")
Upload model to S3
import boto3

s3 = boto3.client("s3")
bucket = "my-sagemaker-demo-bucket"

s3.upload_file("iris-model.pkl", bucket, "model-artifacts/iris-model.pkl")

print("Uploaded to S3:", f"s3://{bucket}/model-artifacts/iris-model.pkl")
Verify upload from CLI
aws s3 ls s3://my-sagemaker-demo-bucket/model-artifacts/
