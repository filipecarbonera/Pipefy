# Pipefy
Integration class with Pipefy Rest API.

---

### **Common Use Cases**
- [Create card](https://github.com/filipecarbonera/Pipefy/blob/main/create_card.py)
- [Move cards](https://github.com/filipecarbonera/Pipefy/blob/main/move_cards.py)
- [Update cards](https://github.com/filipecarbonera/Pipefy/blob/main/update_cards.py)

---

## [Pipefy Class](https://github.com/filipecarbonera/Pipefy/blob/main/pipefy_classes.py)

### Basic Methods
- **__init__** : Constructor of the class.
- **request** : Method to make requests.
- **__prepare_json_dict** : Method to prepare a JSON dictionary.
- **__prepare_json_list** : Method to prepare a JSON list.

---

### Pipe Methods
- [**pipes**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L49) : Get pipes by their identifiers.
- [**pipe**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L61) : Get a pipe by its identifier.
- [**clonePipes**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L73) : Mutation to clone a pipe, in case of success a query is returned.
- [**createPipe**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L85) : Mutation to create a pipe, in case of success a query is returned.
- [**updatePipe**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L116) : Mutation to update a pipe, in case of success a query is returned.
- [**deletePipe**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L151) : Mutation to delete a pipe, in case of success success: true is returned.

---

### Phase Methods
- [**phase**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L163) : Get a phase by its identifier.
- [**createPhase**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L173) : Mutation to create a phase, in case of success a query is returned.
- [**updatePhase**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L202) : Mutation to update a phase, in case of success a query is returned.
- [**deletePhase**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L229) : Mutation to delete a phase of a pipe, in case of success success: true is returned.

---

### Field Methods
- [**createPhaseField**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L240) : Mutation to create a phase field, in case of success a query is returned.
- [**updatePhaseField**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L270) : Mutation to update a phase field, in case of success a query is returned.
- [**deletePhaseField**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L296) : Mutation to delete a phase field, in case of success success: true is returned.

---

### Label Methods
- [**createLabel**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L308) : Mutation to create a label, in case of success a query is returned.
- [**updateLabel**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L330) : Mutation to update a label, in case of success a query is returned.
- [**deleteLabel**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L351) : Mutation to delete a label, in case of success success: true is returned.

---

### Card Methods
- [**cards**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L363) : Get cards by pipe identifier.
- [**allCards**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L376) : Get cards by pipe identifier.
- [**card**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L388) : Get a card by its identifier.
- [**createCard**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L399) : Mutation to create a card, in case of success a query is returned.
- [**updateCard**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L420) : Mutation to update a card, in case of success a query is returned.
- [**deleteCard**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L445) : Mutation to delete a card, in case of success success: true is returned.
- [**moveCardToPhase**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L454) : Mutation to move a card to a phase, in case of success a query is returned.
- [**updateCardField**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L473) : Mutation to update a card field, in case of success a query is returned.

---

### Comment Methods
- [**createComment**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L496) : Mutation to create a comment, in case of success a query is returned.
- [**updateComment**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L515) : Mutation to update a comment, in case of success a query is returned.
- [**deleteComment**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L534) : Mutation to delete a comment, in case of success success: true is returned.

---

### Role Methods
- [**setRole**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L545) : Mutation to set a user's role, in case of success a query is returned.

---

### Pipe Relation Methods
- [**pipe_relations**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L566) : Get pipe relations by their identifiers.
- [**createPipeRelation**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L577) : Mutation to create a pipe relation between two pipes, in case of success a query is returned.
- [**updatePipeRelation**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L614) : Mutation to update a pipe relation, in case of success a query is returned.
- [**deletePipeRelation**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L649) : Mutation to delete a pipe relation, in case of success success: true is returned.

---

### Table Methods
- [**tables**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L660) : Get tables through table ids.
- [**table**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L669) : Get a table through table id.
- [**createTable**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L681) : Mutation to create a table, in case of success a query is returned.
- [**updateTable**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L706) : Mutation to update a table, in case of success a query is returned.
- [**deleteTable**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L742) : Mutation to delete a table, in case of success a query with the field success is returned.
- [**createTableField**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L751) : Mutation to create a table field, in case of success a query is returned.
- [**updateTableField**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L785) : Mutation to update a table field, in case of success a query is returned.
- [**setTableFieldOrder**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L819) : Mutation to set a table field order, in case of success a query with the field success is returned.
- [**deleteTableField**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L838) : Mutation to delete a table field, in case of success a query with the field success is returned.
- [**table_records**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L848) : Get table records with pagination through table id.
- [**table_record**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L859) : Get table record through table record id.
- [**createTableRecord**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L871) : Mutation to create a table record, in case of success a query is returned.
- [**updateTableRecord**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L894) : Mutation to update a table record, in case of success a query is returned.
- [**setTableRecordFieldValue**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L915) : Mutation to set a table record field value, in case of success a query with the field success is returned.
- [**deleteTableRecord**](https://github.com/filipecarbonera/Pipefy/blob/991055403d6f750a57ad86ee9a5c7f3a4e93e04d/pipefy_classes.py#L936) : Mutation to delete a table record, in case of success a query with the field success is returned.
