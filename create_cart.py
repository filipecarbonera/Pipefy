from pipefy import Pipefy

def create_pipefy_cards(pipefy_token, pipe_id, card_data_list):
    errors = []

    pipefy = Pipefy(pipefy_token)

    for card_data in card_data_list:
        cliente_id = card_data.get("client_id")
        fields = card_data.get("fields", [])

        fields.append({"field_id": "client", "field_value": cliente_id})

        try:
            response = pipefy.createCard(pipe_id, fields)
            print(f"Card created for cliente_id: {cliente_id}")
            print(response)
        
        except Exception as e:
            print(f"Error creating card for cliente_id {cliente_id}: {e}")
            erros.append(client_id)

    if errors:
        print('Errors list:')
        print(errors)
    else:
        print('No errors.')
