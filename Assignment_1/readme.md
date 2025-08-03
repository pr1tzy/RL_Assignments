# RL Environment Explorer

This project allows you to interact with and analyze popular reinforcement learning environments using [Gymnasium](https://gymnasium.farama.org/). It will play through several classic RL environments, display them visually, and record observations and environment properties for study and analysis.

## Features

- Runs and displays the following environments:
  - `MountainCar-v0`
  - `Pendulum-v1`
  - `Acrobot-v1`
  - `LunarLander-v3`
  - `CarRacing-v3`
- Saves step-by-step observations to a text file.
- Documents each environment's observation space, action space, goal, episode length, and challenges.

## How to Use

1. **Install dependencies**  
   Make sure you have Python 3.8+ and install required packages:
   ```
   pip install gymnasium[box2d] numpy
   ```

2. **Run the script**
   ```
   python main.py
   ```

   Each environment will be displayed in a pop-up window as it plays with random actions. After all environments finish, a file called `observations.txt` will contain:
   - The analysis for each environment.
   - All observations recorded during play.

## Notes

- **Environment Versions:**  
  The code uses `LunarLander-v3` and `CarRacing-v3` (not `v2`), as these are the latest and recommended versions in Gymnasium. If you see instructions elsewhere using `v2`, just use `v3` for better compatibility and support.
- **Box2D & Rendering:**  
  For `LunarLander` and `CarRacing`, you need Box2D. Install with `pip install gymnasium[box2d]` as shown above.
- **Observation Data:**  
  The script will overwrite `observations.txt` each run. Modify the open mode to append or use timestamps if you want to keep multiple runs.

## Example Output

The relevant analysis and observations for each environment will be saved and easily reviewable in `observations.txt`.

---