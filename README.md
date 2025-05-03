# Pipefy
Integration class with Pipefy Rest API.

---

### **Common Use Cases**


---

## [PIPEFY CLASS](https://github.com/filipecarbonera/Pipefy/blob/main/pipefy_classes.py)

### BASIC METHODS
- **__init__** : Constructor of the class.
- **request** : Method to make requests.
- **__prepare_json_dict** : Method to prepare a JSON dictionary.
- **__prepare_json_list** : Method to prepare a JSON list.

---

### PIPE METHODS
- **pipes** : Get pipes by their identifiers.
- **pipe** : Get a pipe by its identifier.
- **clonePipes** : Mutation to clone a pipe, in case of success a query is returned.
- **createPipe** : Mutation to create a pipe, in case of success a query is returned.
- **updatePipe** : Mutation to update a pipe, in case of success a query is returned.
- **deletePipe** : Mutation to delete a pipe, in case of success success: true is returned.

---

### PHASE METHODS
- **phase** : Get a phase by its identifier.
- **createPhase** : Mutation to create a phase, in case of success a query is returned.
- **updatePhase** : Mutation to update a phase, in case of success a query is returned.
- **deletePhase** : Mutation to delete a phase of a pipe, in case of success success: true is returned.

---

### FIELD METHODS
- **createPhaseField** : Mutation to create a phase field, in case of success a query is returned.
- **updatePhaseField** : Mutation to update a phase field, in case of success a query is returned.
- **deletePhaseField** : Mutation to delete a phase field, in case of success success: true is returned.

---

### LABEL METHODS
- **createLabel** : Mutation to create a label, in case of success a query is returned.
- **updateLabel** : Mutation to update a label, in case of success a query is returned.
- **deleteLabel** : Mutation to delete a label, in case of success success: true is returned.

---

### CARD METHODS
- **cards** : Get cards by pipe identifier.
- **allCards** : Get cards by pipe identifier.
- **card** : Get a card by its identifier.
- **createCard** : Mutation to create a card, in case of success a query is returned.
- **updateCard** : Mutation to update a card, in case of success a query is returned.
- **deleteCard** : Mutation to delete a card, in case of success success: true is returned.
- **moveCardToPhase** : Mutation to move a card to a phase, in case of success a query is returned.
- **updateCardField** : Mutation to update a card field, in case of success a query is returned.

---

### COMMENT METHODS
- **createComment** : Mutation to create a comment, in case of success a query is returned.
- **updateComment** : Mutation to update a comment, in case of success a query is returned.
- **deleteComment** : Mutation to delete a comment, in case of success success: true is returned.

---

### ROLE METHODS
- **setRole** : Mutation to set a user's role, in case of success a query is returned.

---

### PIPE RELATION METHODS
- **pipe_relations** : Get pipe relations by their identifiers.
- **createPipeRelation** : Mutation to create a pipe relation between two pipes, in case of success a query is returned.
- **updatePipeRelation** : Mutation to update a pipe relation, in case of success a query is returned.
- **deletePipeRelation** : Mutation to delete a pipe relation, in case of success success: true is returned.

---

### TABLE METHODS
- **tables** : Get tables through table ids.
- **table** : Get a table through table id.
- **createTable** : Mutation to create a table, in case of success a query is returned.
- **updateTable** : Mutation to update a table, in case of success a query is returned.
- **deleteTable** : Mutation to delete a table, in case of success a query with the field success is returned.
- **createTableField** : Mutation to create a table field, in case of success a query is returned.
- **updateTableField** : Mutation to update a table field, in case of success a query is returned.
- **setTableFieldOrder** : Mutation to set a table field order, in case of success a query with the field success is returned.
- **deleteTableField** : Mutation to delete a table field, in case of success a query with the field success is returned.
- **table_records** : Get table records with pagination through table id.
- **table_record** : Get table record through table record id.
- **createTableRecord** : Mutation to create a table record, in case of success a query is returned.
- **updateTableRecord** : Mutation to update a table record, in case of success a query is returned.
- **setTableRecordFieldValue** : Mutation to set a table record field value, in case of success a query with the field success is returned.
- **deleteTableRecord** : Mutation to delete a table record, in case of success a query with the field success is returned.
