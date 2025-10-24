import numpy as np
import pandas as pd

# Q-Learning simple (como antes)
Q = np.zeros((5,2))
alpha, gamma, epsilon = 0.1, 0.9, 0.1
logs = []  # Para DataFrame

for episode in range(100):
    state = 0
    ep_reward = 0
    steps = 0
    while state != 4:
        action = np.random.choice(2) if np.random.rand() < epsilon else np.argmax(Q[state])
        next_state = max(0, min(4, state + (1 if action == 1 else -1)))
        reward = 1 if next_state == 4 else 0
        ep_reward += reward
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state
        steps += 1
    logs.append({'episode': episode, 'reward': ep_reward, 'steps': steps})

# Crear DataFrame de logs
df_logs = pd.DataFrame(logs)

# Explorar
print(df_logs.head())
print(df_logs.describe())

# Ejemplo: Promedio de recompensas
print('Recompensa promedio:', df_logs['reward'].mean())