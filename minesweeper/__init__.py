from gym.envs.registration import register

register(
        id='Minesweeper-v0',
        entry_point='minesweeper.envs:MinesweeperEnv',
        )


register(
        id='MinesweeperDiscreet-v0',
        entry_point='minesweeper.envs:MinesweeperDiscreetEnv',
)


