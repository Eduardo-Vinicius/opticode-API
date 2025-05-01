import boto3
import uuid
from boto3.dynamodb.conditions import Key

class DynamoDBClient:
    def __init__(self, region_name='us-east-1'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)

    def _get_table(self, table_name):
        return self.dynamodb.Table(table_name)

    def create_item(self, table_name, data, use_uuid=True):
        table = self._get_table(table_name)
        item = data.copy()
        if use_uuid:
            item["id"] = str(uuid.uuid4())
        table.put_item(Item=item)
        return {"message": "Item criado com sucesso", "item": item}

    def get_all_items(self, table_name):
        table = self._get_table(table_name)
        response = table.scan()
        return response.get('Items', [])

    def get_item(self, table_name, item_id):
        table = self._get_table(table_name)
        response = table.get_item(Key={"id": item_id})
        return response.get('Item', None)

    def update_item(self, table_name, item_id, data):
        table = self._get_table(table_name)
        expression = []
        values = {}

        for key, value in data.items():
            expression.append(f"{key} = :{key}")
            values[f":{key}"] = value

        update_expression = "SET " + ", ".join(expression)

        table.update_item(
            Key={"id": item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=values,
            ReturnValues="UPDATED_NEW"
        )
        return {"message": "Item atualizado com sucesso"}

    def delete_item(self, table_name, item_id):
        table = self._get_table(table_name)
        table.delete_item(Key={"id": item_id})
        return {"message": "Item deletado com sucesso"}
