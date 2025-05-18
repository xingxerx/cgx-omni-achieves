import unittest
from chronicle_fates.main import handle_combat

class TestCombat(unittest.TestCase):

    def test_combat_reduces_enemy_health(self):
        initial_enemy_health = 10
        new_enemy_health, enemy_defeated = handle_combat([0, 0], [0, 0], initial_enemy_health)
        self.assertEqual(new_enemy_health, initial_enemy_health - 1)
        self.assertFalse(enemy_defeated)

    def test_enemy_defeated_at_zero_health(self):
        initial_enemy_health = 1
        new_enemy_health, enemy_defeated = handle_combat([0, 0], [0, 0], initial_enemy_health)
        self.assertEqual(new_enemy_health, 0)
        self.assertTrue(enemy_defeated)

    def test_no_combat_when_positions_differ(self):
        initial_enemy_health = 10
        new_enemy_health, enemy_defeated = handle_combat([0, 0], [1, 1], initial_enemy_health)
        self.assertEqual(new_enemy_health, initial_enemy_health)
        self.assertFalse(enemy_defeated)

    def test_no_combat_when_enemy_defeated(self):
        initial_enemy_health = 0
        new_enemy_health, enemy_defeated = handle_combat([0, 0], [0, 0], initial_enemy_health)
        self.assertEqual(new_enemy_health, 0)
        self.assertTrue(enemy_defeated)

if __name__ == '__main__':
    unittest.main()