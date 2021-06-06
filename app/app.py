import tensorflow as tf
import json


def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'predict': tf.__version__,
            }
        ),
    }
