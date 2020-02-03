from unittest import TestCase
import Dominion


class TestPlayer(TestCase):
    def test_action_balance(self):
        player = Dominion.Player("Annie")
        self.assertEqual(10, len(player.stack()))
        acbal = player.action_balance()

        print(acbal)
        assert acbal == 0.0
        player.deck = [Dominion.Woodcutter()] * 2
        acbal2 = player.action_balance()
        # //expected action balance after adding woodcutters to the deck is -20.0

        print(acbal2)
        assert acbal2 == -20.0
        pass

        # balance = 0
        # for c in self.stack():
        #     if c.category == "action":
        #         balance = balance - 1 + c.actions
        # return 70 * balance / len(self.stack())
    # 0 self.fail()


class TestPlayer(TestCase):
    def test_calcpoints(self):
        player = Dominion.Player("Annie")
        self.assertEqual(10, len(player.stack()))
        vpbal = player.calcpoints()

        print(vpbal)
        assert vpbal == 3
        player.deck = [Dominion.Woodcutter()]
        vpbal2 = player.calcpoints()
        # //expected action balance after adding woodcutters to the deck is -20.0
        print(vpbal2)
        assert vpbal2 == 1

        pass


class TestPlayer(TestCase):
    def test_draw(self):
        player = Dominion.Player("Annie")
        self.assertEqual(10, len(player.stack()))
        print(len(player.hand()))
       # player.draw()
        print(len(player.hand()))
        pass


class TestPlayer(TestCase):
    def test_cardsummary(self):
        player = Dominion.Player("Annie")
        self.assertEqual(10, len(player.stack()))
        print(player.cardsummary())

        pass

