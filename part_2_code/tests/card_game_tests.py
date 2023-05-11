import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame()
        self.card_D1 = Card("Diamonds", 1)
        self.card_S2 = Card("Spades", 2)
        self.card_H3 = Card("Hearts", 3)
        

    def test_check_for_ace__true(self):
        result = self.game.check_for_ace(self.card_D1)
        self.assertTrue(result)

    def test_check_for_ace__False(self):
        result = self.game.check_for_ace(self.card_S2)
        self.assertFalse(result)

    def test_highest_card__card1(self):
        expected = self.card_H3
        actual = self.game.highest_card(self.card_H3, self.card_S2)
        self.assertEqual(expected, actual)

    def test_highest_card__card2(self):
        expected = self.card_H3
        actual = self.game.highest_card(self.card_S2, self.card_H3)
        self.assertEqual(expected, actual)

    def test_highest_card__equal(self):
        expected = "Cards are equal"
        actual = self.game.highest_card(self.card_S2, self.card_S2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        cards = [self.card_D1, self.card_S2, self.card_H3]
        expected = "You have a total of 6"
        actual = self.game.cards_total(cards)
        self.assertEqual(expected, actual)
