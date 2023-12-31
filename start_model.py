import boto3

def start_model(project_arn, model_arn, version_name, min_inference_units):

    client=boto3.client('rekognition', region_name='ap-northeast-1')

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        #Get the running status
        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage']) 
    except Exception as e:
        print(e)
        
    print('Done...')
    
def main():
    project_arn='arn:aws:rekognition:ap-northeast-1:591284369655:project/SimpleImagerecognation/1668778312729'
    model_arn='arn:aws:rekognition:ap-northeast-1:591284369655:project/SimpleImagerecognation/version/SimpleImagerecognation.2022-11-25T21.47.19/1669394838883'
    min_inference_units=1 
    version_name='SimpleImagerecognation.2022-11-25T21.47.19'
    start_model(project_arn, model_arn, version_name, min_inference_units)

if __name__ == "__main__":
    main()