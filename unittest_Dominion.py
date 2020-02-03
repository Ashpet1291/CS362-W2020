from unittest import TestCase
import Dominion

from pettiboa.dominion.Dominion import Card


class TestAction_card(TestCase):
    def testActionCardInit(self):
        woodcutter = Dominion.Woodcutter()
        smithy = Dominion.Smithy()
        ac = Dominion.Action_card(self, "Woodcutter", 3, 0,  1, 2)
        ac.cards = [woodcutter, smithy]
        ac.coins = 2
        ac.actions = "Karate Chop"
        assert ac.actions == "Karate Chop"
        assert ac.coins == 2
        assert len(ac.cards) == 2


pass


class TestUseAction_card(TestCase):

    def test_use(self):
        self = Dominion.Woodcutter
        player = Dominion.Player("Annie")
        trash = []
        woodcutter = Dominion.Woodcutter()
        smithy = Dominion.Smithy()
        player.hand.append(woodcutter)
        ac = Dominion.Action_card(self, player.name, 3, 0, 1, 2)
        ac.cards = [woodcutter, smithy]
        ac.coins = 2
        ac.actions = "Karate Chop"
        assert ac.actions == "Karate Chop"
        assert ac.coins == 2
        assert len(ac.cards) == 2
        ac = player.hand[1]
        ac.use(self, trash)
        assert len(ac.cards) == 2
        # assert (len)player.Cards == 0
        # player.hand.append(self)
        # smithy = Dominion.Smithy()
        # woodcutter = Dominion.Woodcutter()
        # player.Cards = [smithy, woodcutter]
        # player.played.append(self)
        # player.hand.remove(self)
        # assert len(player.Cards) == 2



pass


    # class Action_card(Card):
    #     def __init__(self, name, cost, actions, cards, buys, coins):
    #         Card.__init__(self, name, "action", cost, 0, 0)
    #         self.actions = actions
    #         self.cards = cards
    #         self.buys = buys
    #         self.coins = coins
    #
    #     def use(self, player, trash):
    #         player.played.append(self)
    #         player.hand.remove(self)
    #
    #     def augment(self, player):
    #         player.actions += self.actions
    #         player.buys += self.buys
    #         player.purse += self.coins
    #         for i in range(self.cards):
    #             player.draw()
    #
    #     def play(self, player, players, supply, trash):
    #         pass

    #       def turn(self, players, supply, trash):
    #           self.show()
    #           self.actions = 1
    #           self.buys = 1
    #           self.purse = 0
    # action phase
    #           while self.actions > 0 and 'action' in catinlist(self.hand):
    #               playthis = input("Which card would you like to play?  You have " +
    #                                str(self.actions) + " action(s).  \n-Hit enter for no play. --> ")
    #               if playthis:
    #                   c = getcard(playthis, supply, self.hand, "your hand", ['action'])
    #                   if c:
    #                       self.actions = self.actions - 1
    #                       c.use(self, trash)
    #                       c.augment(self)
    #                       c.play(self, players, supply, trash)
    #                       self.show()
    #               else:
    #                   self.actions = 0

    # pass

