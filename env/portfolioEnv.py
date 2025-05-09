import numpy as np
import pandas as pd
import gym
from gym import spaces

class PortfolioEnv(gym.Env):
    """
    Custom Environment for Portfolio Management.
    This environment simulates a portfolio management scenario where an agent can buy, sell, or hold stocks.
    """
    def __init__(self, data: pd.DataFrame, initial_cash=10000):
        super(PortfolioEnv, self).__init__()
        self.data = data
        self.initial_cash = initial_cash
        self.portfolio_value_history = []
        self.symbols = sorted(list(data.index.get_level_values(0).unique()))
        self.num_assets = len(self.symbols)
        self.timestamps = sorted(list(data.index.get_level_values(1).unique()))
        self.max_steps = len(self.timestamps) - 1

        # Action space: portfolio weights for each asset (sum to 1)
        self.action_space = spaces.Box(low=0, high=1, shape=(self.num_assets,), dtype=np.float32)

        # Observation: previous day's normalized prices + portfolio weights
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(2 * self.num_assets,), dtype=np.float32
        )

        self.reset()


    def reset(self):
        self.current_step = 0
        self.cash = self.initial_cash
        self.portfolio_value_history = [self.initial_cash]
        self.portfolio_weights = np.ones(self.num_assets) / self.num_assets  # equally weighted
        self.last_prices = self._get_prices(self.current_step)
        self.last_value = self.cash
        return self._get_observation()


    def step(self, action):
        # Normalize the action into valid weights
        weights = np.clip(action, 0, 1)
        weights = weights / (np.sum(weights) + 1e-8)  # sum to 1

        # Get today's and tomorrow's prices
        current_prices = self._get_prices(self.current_step)
        next_prices = self._get_prices(self.current_step + 1)

        # Calculate portfolio return based on price change
        price_ratio = next_prices / current_prices
        portfolio_return = np.dot(weights, price_ratio)

        # Update portfolio value
        new_value = self.last_value * portfolio_return
        self.portfolio_value_history.append(new_value)

        # Reward: log return (safer numerics than raw return)
        reward = np.log(portfolio_return + 1e-8)

        self.current_step += 1
        self.last_value = new_value
        self.portfolio_weights = weights
        self.last_prices = next_prices

        done = self.current_step >= self.max_steps

        return self._get_observation(), reward, done, {}


    def _get_prices(self, step):
        date = self.timestamps[step]
        prices = []
        for sym in self.symbols:
            try:
                prices.append(self.data.loc[(sym, date)]['close'])
            except:
                prices.append(np.nan)
        prices = np.array(prices)
        return np.nan_to_num(prices, nan=np.nanmean(prices))


    def _get_observation(self):
        # Normalize prices and concatenate with current weights
        normalized_prices = self.last_prices / np.max(self.last_prices)
        obs = np.concatenate([normalized_prices, self.portfolio_weights])
        return obs.astype(np.float32)