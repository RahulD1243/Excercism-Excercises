"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    face_cards = ["J", "Q", "K"]
    ace_card = ["A"]
    numeric_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

    if card in face_cards:
        return 10
    if card in ace_card:
        return 1
    if card in numeric_cards:
        return int(card)
    return None

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)

    if value_1 < value_2:
        return card_two
    if value_1 > value_2:
        return card_one
    if value_1 == value_2:
        return (card_one, card_two)
    return None


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    card_1 = value_of_card(card_one)
    card_2 = value_of_card(card_two)

    if card_1 == 1 or card_2 == 1:
        return 1

    before = card_1 + card_2

    if before + 11 > 21:
        return 1
    
    return 11



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    
    #J, A
    #Q, A
    #K, A
    #10, A
    #Only combintations for blackjack
    
    if [card_one, card_two] in [["J","A"],["Q","A"], ["K","A"], ["10","A"], ["A", "J"],["A", "Q"],["A", "K"],["A", "10"]]:
        return True
    
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_one == card_two:
        return True
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    cd_1 = value_of_card(card_one)
    cd_2 = value_of_card(card_two)

    if cd_1 + cd_2 in {9,10,11}:
        return True

    return False