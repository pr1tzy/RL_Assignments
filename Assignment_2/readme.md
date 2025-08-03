# Multi-Armed Bandit Algorithms (Assignment 2)

This project implements and compares three classic Multi-Armed Bandit (MAB) algorithms, as described in Lecture 2 of your RL course.

## Algorithms Implemented

- **Exploration Only:** Random arm selection each step.
- **Exploitation Only:** Always select the arm with the highest estimated reward so far (greedy).
- **UCB (Upper Confidence Bound):** Balances exploration and exploitation using a statistical confidence bound.

You can find the implementations in:
- `src/algorithms/exploration_only.py`
- `src/algorithms/exploitation_only.py`
- `src/algorithms/ucb.py`

## How to Run

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the main script**
   ```bash
   cd src
   python main.py
   ```
   This will execute all three algorithms and display their performance. Results and plots will help you compare the approaches.

## Notes

- **Environment:**  
  This project uses standard Python packages for numerical computation and plotting.  
- **Algorithm Strategy:**  
  - Exploration Only: Random arm selection  
  - Exploitation Only: Always pick currently best arm  
  - UCB: Pick arm with highest upper confidence bound (see comments in `ucb.py` for formula)
- **Expected Results:**  
  - UCB should perform best.  
  - Exploration Only performs worst.  
  - Exploitation Only can get stuck.

---

## Version Notes

- Some environments or instructions may reference different file or folder names. This project uses the latest structure, with all algorithms in `src/algorithms/`.

---

Happy experimenting with Bandit algorithms!