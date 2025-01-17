from django.db import models
from typing import List, Tuple, Any

def field_type(type_name):
    return getattr(models, type_name)


def fields_contructor(schema, model) -> None:
    validate_schema(schema)
    for field in schema:
        field_name = field.get("field")
        type_name = field.get("type")
        data = field.copy()
        data.pop("field")
        data.pop("type")

        model.add_to_class(
            field_name, 
            field_type(type_name)(**data)
        )   

def fields_contructor_migration(schema) -> List[Tuple[Any]]:
    field_output = []
    
    for field in schema:
        field_name = field.pop('field') 
        field_types = field.pop('type') 
        field_model = field_type(field_types)
        
        field_output.append(
            (field_name, field_model(**field))
        )
    
    return field_output

def get_field_schema(schema) -> List[Any]:
    return [field['field'] for field in schema]
    

def validate_schema(schema):
    required_keys = {"field", "type"}
    for field in schema:
        missing_keys = required_keys - field.keys()
        if missing_keys:
            raise ValueError(f"Missing keys {missing_keys} in field definition: {field}")
