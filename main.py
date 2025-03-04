import random

class BlackjackGame:
    def __init__(self):
        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.user_cards = []
        self.dealer_cards = []
        self.balance = 1000

    def deal_card(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def calculate_score(self, cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0  # Blackjack

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def display_cards(self, show_dealer=False):
        print(f"Your cards: {self.user_cards}, current score: {self.calculate_score(self.user_cards)}")
        if show_dealer:
            print(f"Dealer's cards: {self.dealer_cards}, score: {self.calculate_score(self.dealer_cards)}")
        else:
            print(f"Dealer's first card: {self.dealer_cards[0]}")

    def compare(self, user_score, dealer_score):
        if user_score > 21:
            return "You busted! You lose."
        elif dealer_score > 21:
            return "Dealer busted! You win."
        elif user_score == dealer_score:
            return "It's a draw."
        elif user_score == 0:
            return "Blackjack! You win."
        elif dealer_score == 0:
            return "Dealer has Blackjack! You lose."
        elif user_score > dealer_score:
            return "You win!"
        else:
            return "You lose."

    def play_round(self):
        print("\n" + "=" * 30)
        print(f"Balance: ${self.balance}")
        bet = int(input("Place your bet: $"))

        if bet > self.balance:
            print("Insufficient balance.")
            return

        self.user_cards = [self.deal_card(), self.deal_card()]
        self.dealer_cards = [self.deal_card(), self.deal_card()]

        game_over = False

        while not game_over:
            self.display_cards()
            user_score = self.calculate_score(self.user_cards)
            dealer_score = self.calculate_score(self.dealer_cards)

            if user_score == 0 or dealer_score == 0 or user_score > 21:
                game_over = True
            else:
                hit_or_stand = input("Type 'y' to hit or 'n' to stand: ").lower()
                if hit_or_stand == 'y':
                    self.user_cards.append(self.deal_card())
                else:
                    game_over = True

        while self.calculate_score(self.dealer_cards) < 17:
            self.dealer_cards.append(self.deal_card())

        self.display_cards(show_dealer=True)
        result = self.compare(self.calculate_score(self.user_cards), self.calculate_score(self.dealer_cards))
        print(result)

        if "win" in result:
            self.balance += bet
        elif "lose" in result:
            self.balance -= bet

    def play_game(self):
        print('''
        +--------+
        | 10     |
        |        |
        |   ♠    |
        |        |
        |     10 |
        +--------+
        ''')
        print("Welcome to Advanced Blackjack!")
        while self.balance > 0:
            play_again = input("Do you want to play a round? (y/n): ").lower()
            if play_again == 'y':
                self.play_round()
            else:
                print("Thanks for playing!")
                break

        if self.balance <= 0:
            print("You're out of money! Game over.")

if __name__ == "__main__":
    game = BlackjackGame()
    game.play_game()
