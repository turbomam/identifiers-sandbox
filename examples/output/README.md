## NamedThingCollection-valid
### Input
```yaml
entries:
- description: foo bar
  id: example:Thing001
  name: foo bar
- description: foo bar
  id: example:Thing002
  name: foo bar

```
## NamedThingCollection-no-id
### Input
```yaml
entries:
- description: foo bar
  name: foo bar

```
## NamedThingCollection-undefined-slot
### Input
```yaml
entries:
- id: example:Thing001
  name: foo bar
  undefined: undefined

```
## NamedThingCollection-bad-id-pattern
### Input
```yaml
entries:
- id: example_Person001
  name: foo bar

```
