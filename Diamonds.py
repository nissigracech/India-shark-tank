import streamlit as st
import random

class Banker:
    def create_diamond_suit(self):
        suit = "\u2666"
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        diamond_cards = [(suit, value) for value in values]
        return diamond_cards

class Players:
    def __init__(self, suit):
        self.suit = suit

    def creating_suit(self):
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] # Standard card values
        cards = [(self.suit, value) for value in values]
        return cards

def shuffle_cards(cards):
    random.shuffle(cards)
    return cards

def pop_card(cards):
    return cards.pop()

def points_evaluation(card):
    value = card[1]
    if isinstance(value, int) and 2 <= value <= 10:
        return 3
    elif value in ['J', 'Q', 'K']:
        return 10
    elif value == 'A':
        return 20
    else:
        return 0

def final_winner(p1, p2, p3, player_1, player_2, player_3):
    scores = {player_1: p1, player_2: p2, player_3: p3}
    max_score = max(p1, p2, p3)
    winners = [player for player, score in scores.items() if score == max_score]

    if len(winners) == 1:
        st.write(f"\n~~ WINNER IS ~~ {winners[0]}")
    elif len(winners) > 1:
        st.write(f"\n~ THE GAME IS TIE BETWEEN {', '.join(winners)}")
    else:
        st.write("\n~~ NO WINNER ~~")

def player_scores():
    if "p1_score" not in st.session_state:
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.p3_score = 0
        st.session_state.round = 1
        st.session_state.diamonds_list = Banker().create_diamond_suit()
        st.session_state.player1_list1 = Players("\u2660").creating_suit()
        st.session_state.player2_list2 = Players("\u2665").creating_suit()
        st.session_state.player3_list3 = Players("\u2663").creating_suit()
        st.session_state.diamond_card = None
        st.session_state.player1_card = None
        st.session_state.player2_card = None
        st.session_state.player3_card = None
        st.session_state.winners = []


    st.title("Diamonds Card Game")

    st.write(f"Round: {st.session_state.round}")

    if st.session_state.diamond_card is None:
        st.session_state.diamonds_list = shuffle_cards(st.session_state.diamonds_list)
        st.session_state.diamond_card = pop_card(st.session_state.diamonds_list)
    st.write(f"|DISPLAYED DIAMOND CARD|: {st.session_state.diamond_card}")

    if st.session_state.player1_card is None:
        st.session_state.player1_list1 = shuffle_cards(st.session_state.player1_list1)
        if st.button(f"{st.session_state.player_1}'s Card"):
            st.session_state.player1_card = pop_card(st.session_state.player1_list1)
            st.write(f"{st.session_state.player_1}'s card: {st.session_state.player1_card}")
    else:
        st.write(f"{st.session_state.player_1}'s card: {st.session_state.player1_card}")


    if st.session_state.player2_card is None:
        st.session_state.player2_list2 = shuffle_cards(st.session_state.player2_list2)
        if st.button(f"{st.session_state.player_2}'s Card"):
            st.session_state.player2_card = pop_card(st.session_state.player2_list2)
            st.write(f"{st.session_state.player_2}'s card: {st.session_state.player2_card}")
    else:
        st.write(f"{st.session_state.player_2}'s card: {st.session_state.player2_card}")

    if st.session_state.player3_card is None:
        st.session_state.player3_list3 = shuffle_cards(st.session_state.player3_list3)
        if st.button(f"{st.session_state.player_3}'s Card"):
            st.session_state.player3_card = pop_card(st.session_state.player3_list3)
            st.write(f"{st.session_state.player_3}'s card: {st.session_state.player3_card}")
    else:
         st.write(f"{st.session_state.player_3}'s card: {st.session_state.player3_card}")

    if st.session_state.player1_card and st.session_state.player2_card and st.session_state.player3_card:
        if st.button("Evaluate Round"):
            winner_card = max(st.session_state.player1_card, st.session_state.player2_card, st.session_state.player3_card, key=lambda x: x[1] if isinstance(x[1],int) else 0)
            st.session_state.winners = []
            if st.session_state.player1_card[1] == winner_card[1]: st.session_state.winners.append(st.session_state.player_1)
            if st.session_state.player2_card[1] == winner_card[1]: st.session_state.winners.append(st.session_state.player_2)
            if st.session_state.player3_card[1] == winner_card[1]: st.session_state.winners.append(st.session_state.player_3)

            num_winners = len(st.session_state.winners)
            shared_points = points_evaluation(st.session_state.diamond_card) // num_winners if num_winners > 0 else 0

            for winner in st.session_state.winners:
                if winner == st.session_state.player_1: st.session_state.p1_score += shared_points
                elif winner == st.session_state.player_2: st.session_state.p2_score += shared_points
                elif winner == st.session_state.player_3: st.session_state.p3_score += shared_points

            st.write(f"~~ DIAMOND CARD WON BY ~~ {', '.join(st.session_state.winners)}, {winner_card}")
            st.write(f"{', '.join(st.session_state.winners)} Wins and get points {shared_points}")

            st.write(f"\n\nAFTER ROUND {st.session_state.round} THE PLAYERS SCORES:")
            st.write(f"{st.session_state.player_1}: {st.session_state.p1_score}")
            st.write(f"{st.session_state.player_2}: {st.session_state.p2_score}")
            st.write(f"{st.session_state.player_3}: {st.session_state.p3_score}")

            st.session_state.round += 1
            st.session_state.diamond_card = None
            st.session_state.player1_card = None
            st.session_state.player2_card = None
            st.session_state.player3_card = None
            st.session_state.winners = []

            if st.session_state.round > 13:
                final_winner(st.session_state.p1_