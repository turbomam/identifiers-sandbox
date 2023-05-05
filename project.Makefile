## Add your own custom Makefile targets here

RUN = poetry run

.PHONY: check-jsonschema-example run-linkml-validation


JSON_SCHEMA_FILE := project/jsonschema/identifiers_sandbox.schema.json
INVALID_EXAMPLES_DIR := src/data/examples/invalid
INVALID_EXAMPLE_FILES := $(wildcard src/data/examples/invalid/*.yaml)
VALID_EXAMPLES_DIR := src/data/examples/valid
VALID_EXAMPLE_FILES := $(wildcard src/data/examples/valid/*.yaml)

check-valid-and-invalid: check-all-invalid-examples check-all-valid-examples

check-all-invalid-examples: $(patsubst $(INVALID_EXAMPLES_DIR)/%.yaml,jsonschema-vs-invalid--%,$(INVALID_EXAMPLE_FILES))

jsonschema-vs-invalid--%: $(JSON_SCHEMA_FILE) $(INVALID_EXAMPLES_DIR)/%.yaml
	! $(RUN) check-jsonschema --schemafile $^

check-all-valid-examples: $(patsubst $(VALID_EXAMPLES_DIR)/%.yaml,jsonschema-vs-valid-%,$(VALID_EXAMPLE_FILES))

jsonschema-vs-valid-%: $(JSON_SCHEMA_FILE) $(VALID_EXAMPLES_DIR)/%.yaml
	$(RUN) check-jsonschema --schemafile $^



#check-jsonschema-examples: $(JSON_SCHEMA_FILE) $(EXAMPLE_FILES)
#	$(RUN) check-jsonschema --schemafile $< $(INVALID_EXAMPLE_FILES)

#check-examples:
#	- @for f in $(INVALID_EXAMPLES_DIR)/*.yaml; do \
#  		echo "Checking $$f"; \
#		$(RUN) check-jsonschema --schemafile $(JSON_SCHEMA_FILE) $$f; \
#	done

#check-jsonschema-example: project/jsonschema/identifiers_sandbox.schema.json \
#	  src/data/examples/invalid/NamedThingCollection-undefined-slot.yaml
#	# showing ignore failures here
#	# this should be templated
#	- $(RUN) check-jsonschema \
#	  --schemafile $^

# # #

run-linkml-validation: src/identifiers_sandbox/schema/identifiers_sandbox.yaml \
src/data/examples/invalid/NamedThingCollection-undefined-slot.yaml
	# PersonCollection is assumed as the target-class because it has been defined as the tree_root in the schema
	- $(RUN) linkml-validate \
	  --schema $^


src/data/dh_vs_linkml_json/ThingCollection_linkml_raw.yaml: src/data/dh_vs_linkml_json/Thing_dh.json
	$(RUN) dh-json2linkml \
		--input-file $< \
		--output-file $@ \
		--output-format yaml \
		--key entries


src/data/dh_vs_linkml_json/ThingCollection_linkml_normalized.yaml: src/data/dh_vs_linkml_json/ThingCollection_linkml_raw.yaml
	$(RUN) linkml-normalize \
		--schema src/identifiers_sandbox/schema/identifiers_sandbox.yaml \
		--output $@ \
		--no-expand-all $<

src/data/dh_vs_linkml_json/entries.json: src/data/dh_vs_linkml_json/ThingCollection_linkml_normalized.yaml
	$(RUN) linkml-json2dh \
		--input-file $< \
		--input-format yaml \
		--output-dir $(dir $@)

project/reports/slot_usage_esp_validation.tsv:
	linkml2sheets \
		--schema src/identifiers_sandbox/schema/identifiers_sandbox.yaml \
		--output $@ \
		src/local_schemasheets/templates/slot_usage_esp_validation.tsv
