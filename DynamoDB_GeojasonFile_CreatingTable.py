# boto3 install this package to connect dynamodb 
# uuid  install this package to had unique id 
# json to import json files 

import json
import uuid
import boto3


def replace_floats(obj):
    """
    Argd:
        obj parameter: Object with nested dict/list values to convert to strings.
    Returns:
        The same object will all strings
    """
    if isinstance(obj, list):
        for i, _ in enumerate(obj):
            obj[i] = replace_floats(obj[i])
        return obj
    if isinstance(obj, dict):
        for k in obj.keys():
            obj[k] = replace_floats(obj[k])
        return obj
    if isinstance(obj, float):
        return str(obj)
    return obj

def connect_to_dynamo():
    """
    Enter your aws access key 
    """
    print('Enter your aws_access_key: ')
    aws_acc_key = input()
    print('Enter your aws_secret_access_key:')
    aws_sec_key = input()
    
        
    dynamodb = boto3.resource(
        'dynamodb',
        region_name= "us-west-1",
        
        aws_access_key_id= str(aws_acc_key),
        
        aws_secret_access_key= str(aws_sec_key))
    return dynamodb

def create_dynamo_table(dynamodb_resource, table_name):
    
    table = dynamodb_resource.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 25,
            'WriteCapacityUnits': 25}
    )
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    return table

def upload_segments_to_dynamo(dynamodb_resource, table_name, segments):

    table = dynamodb_resource.Table(table_name)
    with table.batch_writer() as batch:
        for segment in segments['features']:
            
            for i in range(0,len(segment['geometry']['coordinates'][0][0])):
                batch.put_item(
                    Item={
                         'id' : str (uuid.uuid1()),
                        'latitude': str(segment['geometry']['coordinates'][0][0][i][0]),
                        'longitude': str(segment['geometry']['coordinates'][0][0][i][1]),
                    })
    return 1

def initialize_dynamodb(geojson_name, dynamodb_table_name):
    
    with open(f"{geojson_name}.geojson", 'r') as shapefile:
        segments = json.load(shapefile)

    # Turn all float values (coordinates mostly) into strings in the geojson
    segments = replace_floats(segments)

    # Upload the modified segments to a newly created dynamodb table
    print("Connecting to Dynamodb...")
    dynamodb_resource = connect_to_dynamo()
    print("Creating new table...")
    create_dynamo_table(dynamodb_resource, dynamodb_table_name)
    print("Uploading segments to table...")
    upload_segments_to_dynamo(
        dynamodb_resource,
        dynamodb_table_name,
        segments)
    # Return the number of features that are in the kcm data
    return len(segments['features'])

if __name__ == "__main__":
    # Main program starts here
    NUM_FEATURES_UPLOADED = initialize_dynamodb(
        geojson_name=r'C:\Users\mistr\OneDrive\Documents\GitHub\airbnb_Data225_project\project_data\geojson files\SantaClara_neighbourhoods',
        dynamodb_table_name='neighbourhood_SantaClara')
    print(f"{NUM_FEATURES_UPLOADED} features in data uploaded to dynamodb")
