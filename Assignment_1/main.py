import gymnasium as gym
import numpy as np
import time

env_analysis = {
    "MountainCar-v0": {
        "Observation space": "2D (position, velocity): Box(-1.2, 0.6) x (-0.07, 0.07)",
        "Action space": "Discrete(3): push left, no push, push right",
        "Goal/objective": "Drive car to the top of the right hill",
        "Episode length": "Up to 200 steps",
        "Challenge": "Engine not strong enough; must build momentum by rocking"
    },
    "Pendulum-v1": {
        "Observation space": "3D (cos(theta), sin(theta), theta_dot): Box(-1,1)x2 + (-8,8)",
        "Action space": "Continuous: torque between -2 and +2",
        "Goal/objective": "Keep pendulum upright and still",
        "Episode length": "200 steps (default)",
        "Challenge": "Continuous control, must balance with precise torques"
    },
    "Acrobot-v1": {
        "Observation space": "6D (cos/sin of 2 angles, 2 angular velocities): Box(-1,1)x4 + (-12.57,12.57)x2",
        "Action space": "Discrete(3): torque -1, 0, +1 applied to joint",
        "Goal/objective": "Swing the lower link up to a height",
        "Episode length": "Up to 500 steps",
        "Challenge": "Only one joint is actuated; system is underactuated"
    },
    "LunarLander-v3": {
        "Observation space": "8D: position, velocity, angle, angular velocity, leg contacts",
        "Action space": "Discrete(4): do nothing, fire left, main, or right engine",
        "Goal/objective": "Land the module safely between flags",
        "Episode length": "Up to 1000 steps",
        "Challenge": "Requires careful thrust and orientation control, sparse rewards"
    },
    "CarRacing-v3": {
        "Observation space": "RGB image (96x96x3)",
        "Action space": "Continuous(3): steering [-1,1], gas [0,1], brake [0,1]",
        "Goal/objective": "Drive around randomly generated track as fast as possible",
        "Episode length": "~1000 steps (varies)",
        "Challenge": "End-to-end vision, continuous control, diverse tracks"
    }
}

def play_env(env_id, steps=300, delay=0.02):
    print(f"\n--- Playing {env_id} ---")
    observations = []
    try:
        env = gym.make(env_id, render_mode="human")
    except TypeError:
        env = gym.make(env_id)
    except gym.error.Error as e:
        print(f"Could not make {env_id}: {e}")
        return observations

    obs, info = env.reset(seed=42)
    terminated, truncated = False, False

    for step in range(steps):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        observations.append(np.array2string(obs, precision=4, separator=","))
        time.sleep(delay)
        if terminated or truncated:
            print(f"Episode ended at step {step+1}")
            obs, info = env.reset()

    env.close()
    return observations

if __name__ == "__main__":
    envs = [
        "MountainCar-v0",
        "Pendulum-v1",
        "Acrobot-v1",
        "LunarLander-v3",
        "CarRacing-v3"
    ]
    steps_dict = {
        "MountainCar-v0": 200,
        "Pendulum-v1": 200,
        "Acrobot-v1": 200,
        "LunarLander-v3": 300,
        "CarRacing-v3": 500
    }

    all_observations = {}

    for env_id in envs:
        observations = play_env(env_id, steps=steps_dict.get(env_id, 200), delay=0.02 if env_id != "CarRacing-v3" else 0.005)
        all_observations[env_id] = observations
        print(f"Finished playing {env_id}")
        time.sleep(1)

    # Print and save to a txt file, including environment analysis
    with open("observations.txt", "w") as f:
        for env_id in envs:
            # Write analysis
            analysis = env_analysis.get(env_id, {})
            f.write(f"=== {env_id} ===\n")
            for key, value in analysis.items():
                f.write(f"{key}: {value}\n")
            f.write("\nObservations:\n")
            # Write observations
            for obs in all_observations.get(env_id, []):
                f.write(obs + "\n")
            f.write("\n\n")