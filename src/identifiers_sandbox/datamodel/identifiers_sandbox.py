# Auto generated from identifiers_sandbox.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-05-05T10:23:28
# Schema: identifiers-sandbox
#
# id: https://w3id.org/turbomam/identifiers-sandbox
# description: A LinkML schema and project for exploring the functionality of LinkML slots with `identifier: true`
# license: BSD-3

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
IDENTIFIERS_SANDBOX = CurieNamespace('identifiers_sandbox', 'https://w3id.org/turbomam/identifiers-sandbox/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = IDENTIFIERS_SANDBOX


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = IDENTIFIERS_SANDBOX.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class NamedThingCollection(YAMLRoot):
    """
    A holder for Thing objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTIFIERS_SANDBOX.NamedThingCollection
    class_class_curie: ClassVar[str] = "identifiers_sandbox:NamedThingCollection"
    class_name: ClassVar[str] = "NamedThingCollection"
    class_model_uri: ClassVar[URIRef] = IDENTIFIERS_SANDBOX.NamedThingCollection

    entries: Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=NamedThing, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=IDENTIFIERS_SANDBOX.id, domain=None, range=URIRef,
                   pattern=re.compile(r'[a-zA-Z0-9_]+:[a-zA-Z0-9_]+'))

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=IDENTIFIERS_SANDBOX.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=IDENTIFIERS_SANDBOX.description, domain=None, range=Optional[str])

slots.namedThingCollection__entries = Slot(uri=IDENTIFIERS_SANDBOX.entries, name="namedThingCollection__entries", curie=IDENTIFIERS_SANDBOX.curie('entries'),
                   model_uri=IDENTIFIERS_SANDBOX.namedThingCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]])