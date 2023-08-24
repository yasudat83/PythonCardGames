from collections import Counter

hand_names = [
    "High Card",
    "One Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush",
    "Royal Flush"
]

hand_to_index = {hand: index for index, hand in enumerate(hand_names)}

def evaluate_hand(hand):
    ranks = [rank for rank, _ in hand]
    suits = [suit for _, suit in hand]
    
    rank_counts = Counter(ranks)
    num_unique_ranks = len(rank_counts)
    
    is_flush = len(set(suits)) == 1

    if num_unique_ranks == 5:
        is_straight, highest_card = check_for_straight(ranks)
        if is_straight and is_flush:
            if highest_card == 12:
                return "Royal Flush"
            else:
                return "Straight Flush"
        elif is_flush:
            return "Flush"
        elif is_straight:
            return "Straight"

    if num_unique_ranks == 4:
        return "One Pair"

    if num_unique_ranks == 3:
        if 3 in rank_counts.values():
            return "Three of a Kind"
        else:
            return "Two Pair"

    if num_unique_ranks == 2:
        if 4 in rank_counts.values():
            return "Four of a Kind"
        else:
            return "Full House"

    return "High Card"

def check_for_straight(ranks):
    rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    ranks_set = set(ranks)
    # Special case for A, 2, 3, 4, 5 straight
    if len(ranks_set) == 5 and set(["A", "2", "3", "4", "5"]).issubset(ranks_set):
        return True, rank_order.index("5")
    # General case
    for i in range(len(rank_order) - 4):
        if set(rank_order[i:i+5]).issubset(ranks_set):
            return True, rank_order.index(rank_order[i+4])
    return False, None

test_cases = [
    [("A", "Hearts"), ("K", "Hearts"), ("Q", "Hearts"), ("J", "Hearts"), ("10", "Hearts")],  # Royal Flush
    [("7", "Diamonds"), ("8", "Diamonds"), ("9", "Diamonds"), ("10", "Diamonds"), ("J", "Diamonds")],  # Straight Flush
    [("5", "Clubs"), ("5", "Diamonds"), ("5", "Hearts"), ("5", "Spades"), ("10", "Hearts")],  # Four of a Kind
    [("J", "Hearts"), ("J", "Diamonds"), ("K", "Hearts"), ("K", "Diamonds"), ("K", "Spades")],  # Full House
    [("2", "Hearts"), ("4", "Hearts"), ("6", "Hearts"), ("8", "Hearts"), ("10", "Hearts")],  # Flush
    [("8", "Hearts"), ("9", "Spades"), ("10", "Diamonds"), ("J", "Hearts"), ("Q", "Clubs")],  # Straight
    [("3", "Spades"), ("3", "Hearts"), ("3", "Diamonds"), ("6", "Clubs"), ("7", "Hearts")],  # Three of a Kind
    [("9", "Spades"), ("9", "Hearts"), ("J", "Diamonds"), ("J", "Clubs"), ("A", "Hearts")],  # Two Pair
    [("4", "Spades"), ("4", "Hearts"), ("4", "Diamonds"), ("10", "Clubs"), ("J", "Hearts")],  # Three of a Kind
    [("A", "Hearts"), ("2", "Diamonds"), ("7", "Clubs"), ("10", "Hearts"), ("K", "Spades")]  # High Card
]

for test_case in test_cases:
    result = evaluate_hand(test_case)
    print(f"Hand: {test_case}, Result: {result}")


def compare_hands(hand1, hand2):
    result1 = evaluate_hand(hand1)
    result2 = evaluate_hand(hand2)
    rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    rank1 = hand_to_index[result1]
    rank2 = hand_to_index[result2]

    if rank1 > rank2:
        return "Hand 1"
    elif rank1 < rank2:
        return "Hand 2"
    else:
        # If the hand rankings are the same, compare individual card ranks
        sorted_hand1 = sorted(hand1, key=lambda card: rank_order.index(card[0]), reverse=True)
        sorted_hand2 = sorted(hand2, key=lambda card: rank_order.index(card[0]), reverse=True)
        
        for card1, card2 in zip(sorted_hand1, sorted_hand2):
            if card1[0] > card2[0]:
                return "Hand 1"
            elif card1[0] < card2[0]:
                return "Hand 2"
        
        return "Tie"
# Test comparing hands
test_cases = [
    ( # Royal Flush vs. Straight Flush
        [("A", "Hearts"), ("K", "Hearts"), ("Q", "Hearts"), ("J", "Hearts"), ("10", "Hearts")],  # Royal Flush
        [("7", "Diamonds"), ("8", "Diamonds"), ("9", "Diamonds"), ("10", "Diamonds"), ("J", "Diamonds")]  # Straight Flush
    ),
    ( # Four of a Kind vs. Full House
        [("5", "Clubs"), ("5", "Diamonds"), ("5", "Hearts"), ("5", "Spades"), ("10", "Hearts")],  # Four of a Kind
        [("J", "Hearts"), ("J", "Diamonds"), ("K", "Hearts"), ("K", "Diamonds"), ("K", "Spades")]  # Full House
    ),
    ( # Flush vs. Straight
        [("2", "Hearts"), ("4", "Hearts"), ("6", "Hearts"), ("8", "Hearts"), ("10", "Hearts")],  # Flush
        [("8", "Hearts"), ("9", "Spades"), ("10", "Diamonds"), ("J", "Hearts"), ("Q", "Clubs")]  # Straight
    ),
    ( # Three of a Kind vs. Two Pair
        [("3", "Spades"), ("3", "Hearts"), ("3", "Diamonds"), ("6", "Clubs"), ("7", "Hearts")],  # Three of a Kind
        [("9", "Spades"), ("9", "Hearts"), ("J", "Diamonds"), ("J", "Clubs"), ("A", "Hearts")]  # Two Pair
    ),
    ( # High Card vs. High Card
        [("4", "Spades"), ("4", "Hearts"), ("4", "Diamonds"), ("10", "Clubs"), ("J", "Hearts")],  # High Card
        [("A", "Hearts"), ("2", "Diamonds"), ("7", "Clubs"), ("10", "Hearts"), ("K", "Spades")]  # High Card
    )
]
print()
for idx, (hand1, hand2) in enumerate(test_cases, start=1):
    winner = compare_hands(hand1, hand2)
    print(f"Test case {idx}:")
    print(f"Hand 1: {hand1}")
    print(f"Hand 2: {hand2}")
    print(f"The winner is: {winner}")
    print()
