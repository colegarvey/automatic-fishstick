from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from env.portfolioEnv import PortfolioEnv
from data.load import get_data
import os

# Set data specific parameters
symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]
start_date = "2020-01-01"
end_date = "2023-01-01"

data = get_data(symbols, start_date, end_date)

env = PortfolioEnv(data)
env = DummyVecEnv([lambda: env])  # Wrap the environment for Stable Baselines3

model = PPO(
    "MlpPolicy",          # Multilayer perceptron policy
    env,                  # our custom environment
    verbose=1,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    ent_coef=0.005,
    gamma=0.99,
    tensorboard_log="./tensorboard_logs/"
)

# tensorboard --logdir=./tensorboard_logs/
# Run cmd in terminal to visualize tensorboard logs

# Train the model 
model.learn(total_timesteps=50_000)

# Save the model 
os.makedirs("models", exist_ok=True)
model.save("models/ppo_portfolio")
print("Model training complete and saved.")