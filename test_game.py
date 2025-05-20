def test_enemy_defeated_at_zero_health(self):
        initial_enemy_health = 1
        initial_player_health = 10
        new_enemy_health, enemy_defeated, new_player_health = handle_combat([0, 0], [0, 0], initial_enemy_health, initial_player_health)
        self.assertEqual(new_enemy_health, 0)
        self.assertEqual(new_player_health, initial_player_health)
        self.assertTrue(enemy_defeated)

def test_no_combat_when_positions_differ(self): # This is the problematic line (around line 27 in the traceback)
        initial_enemy_health = 10
        initial_player_health = 10
        new_enemy_health, enemy_defeated, new_player_health = handle_combat([0, 0], [1, 1], initial_enemy_health, initial_player_health)
        self.assertEqual(new_enemy_health, initial_enemy_health)
        self.assertFalse(enemy_defeated)
        self.assertEqual(new_player_health, initial_player_health) # This is line 27


    def test_no_combat_when_enemy_defeated(self): # This is line 31 in the traceback
        initial_enemy_health = 0
        initial_player_health = 10
        new_enemy_health, enemy_defeated, new_player_health = handle_combat([0, 0], [0, 0], initial_enemy_health, initial_player_health)
        self.assertEqual(new_enemy_health, 0)
        self.assertEqual(new_player_health, initial_player_health)
        self.assertTrue(enemy_defeated)
