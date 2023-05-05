from linkml.generators.pythongen import PythonGenerator
from linkml.validators import JsonSchemaDataValidator
from linkml_runtime.dumpers import yaml_dumper

# create a schema from a string for self-sufficiency
schema_string = """
id: https://w3id.org/turbomam/identifiers-sandbox
name: identifiers-sandbox
title: identifiers-sandbox
description: |-
  A LinkML schema and project for exploring the functionality of LinkML slots with `identifier: true`
license: BSD-3
see_also:
  - https://turbomam.github.io/identifiers-sandbox

prefixes:
  identifiers_sandbox: https://w3id.org/turbomam/identifiers-sandbox/
  linkml: https://w3id.org/linkml/
  schema: http://schema.org/
  example: https://example.org/
  
default_prefix: identifiers_sandbox
default_range: string

imports:
  - linkml:types

classes:

  NamedThing:
    description: >-
      A generic grouping for any identifiable entity
    slots:
      - id
      - name
      - description
    class_uri: schema:Thing

  NamedThingCollection:
    tree_root: true
    description: >-
      A holder for Thing objects
    attributes:
      entries:
        range: NamedThing
        multivalued: true
        inlined: true
        inlined_as_list: true

slots:
  id:
    description: A unique identifier for a thing
    identifier: true
    pattern: "[a-zA-Z0-9_]+:[a-zA-Z0-9_]+"
    range: uriorcurie
    required: true
    slot_uri: schema:identifier
  name:
    slot_uri: schema:name
    description: A human-readable name for a thing
  description:
    slot_uri: schema:description
    description: A human-readable description for a thing

"""

# could also generate the module from a file
# sv = SchemaView(schema_string)
# schema_obj = sv.schema
# gen = PythonGenerator(schema_obj)

gen = PythonGenerator(schema_string)

identifiers_sandbox_module = gen.compile_module()

thing_as_dict = {
    "id": "example:1",
    "name": "example name"
}

thing_as_instance = identifiers_sandbox_module.NamedThing(**thing_as_dict)

print(yaml_dumper.dumps(thing_as_instance))

validator = JsonSchemaDataValidator(schema_string)

try:
    validator.validate_object(thing_as_instance)
    print("Valid!")
except Exception as e:
    print(e)
