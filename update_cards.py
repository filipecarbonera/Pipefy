from pipefy import Pipefy

def update_pipefy_cards(pipefy_token, card_ids, field_name, field_value, phase_id=None):
    errors = []
    pipefy = Pipefy(pipefy_token)

    for card_id in card_ids:
        print(f"Updating card: {card_id}")

        try:
            if phase_id:
                pipefy.moveCardToPhase(card_id, phase_id)

            pipefy.updateCardField(card_id, field_name, field_value)
            print(f"Card {card_id} updated")

        except Exception as e:
            print(f"Card {card_id} encountered an error: {e}")
            errors.append(card_id)

    if errors:
        print('Errors:')
        print(errors)
    else:
        print('No errors.')
