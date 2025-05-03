from pipefy import Pipefy

def move_cards_to_phase(pipefy_token, destination_phase_id, card_ids):
    errors = []

    pipefy = Pipefy(pipefy_token)

    for card_id in card_ids:
        print(f"Updating card: {card_id}")
        try:
            pipefy.moveCardToPhase(card_id, destination_phase_id)
            print(f"Card {card_id} moved successfully.")
        except Exception as e:
            print(f"Error moving card {card_id}: {e}")
            erros.append(card_id)

    if errors:
        print('Errors list:')
        print(errors)
    else:
        print('All cards was moved successfully.')
