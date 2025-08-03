#!/usr/bin/env python3
"""
Entry point for demonstrating the modular Multi-Armed Bandit (MAB) framework.
"""

from utils.config import MABConfig
from experiments.experiment_runner import MABExperimentRunner
from algorithms.exploration_only import ExplorationOnly
from algorithms.exploitation_only import ExploitationOnly
from algorithms.epsilon_greedy import EpsilonGreedy
from algorithms.ucb import UCB

def check_algorithm(algorithm, label):
    """
    Checks if the given algorithm implementation is valid.
    """
    try:
        arm = algorithm.select_arm()
        if arm is None:
            return False, f"{label}: Not implemented (returned None)"
        if not isinstance(arm, int):
            return False, f"{label}: Not implemented (returned {type(arm)})"
        if not (0 <= arm < algorithm.n_arms):
            return False, f"{label}: Invalid arm index ({arm})"
        return True, f"{label}: Implemented"
    except Exception as exc:
        return False, f"{label}: Not implemented (error: {exc})"

def main():
    # Initialize configuration
    config = MABConfig()
    config.get_bernoulli_config(n_arms=5, n_trials=1000)
    config.set_algorithm_params('epsilon_greedy', {'epsilon': 0.1})
    config.set_algorithm_params('ucb', {'c': 2.0})

    # Instantiate experiment runner
    runner = MABExperimentRunner(config)

    # Prepare algorithm instances
    algos = {
        'Exploration Only': ExplorationOnly(config.n_arms),
        'Exploitation Only': ExploitationOnly(config.n_arms),
        'Epsilon-Greedy': EpsilonGreedy(config.n_arms, epsilon=0.1),
        'UCB': UCB(config.n_arms, c=2.0)
    }

    print("=== MAB Algorithm Implementation Check ===")
    implemented = {}
    not_implemented = []

    for label, algo in algos.items():
        ok, msg = check_algorithm(algo, label)
        print(msg)
        if ok:
            implemented[label] = algo
        else:
            not_implemented.append(label)

    print(f"\nAlgorithms ready: {len(implemented)}")
    if not_implemented:
        print(f"Pending: {', '.join(not_implemented)}")

    if implemented:
        print(f"\n=== Running Experiments ({len(implemented)} algorithms) ===")
        results = runner.compare_algorithms(implemented)
        runner.print_summary(results)
        runner.plot_results(results, save_path='mab_comparison.png')
        print("Plot saved as 'mab_comparison.png'.")
    else:
        print("\nNo algorithms implemented.")
        print("Please implement at least one algorithm to see the results.")

    if not_implemented:
        print("\nStudent To-Do:")
        print("Implement these algorithms to complete your assignment:")
        for label in not_implemented:
            print(f"  - {label}")
        print("\nRelevant files:")
        print("  - src/algorithms/exploration_only.py")
        print("  - src/algorithms/exploitation_only.py")
        print("  - src/algorithms/ucb.py")
        print("\nNote: Epsilon-Greedy is already implemented for reference.")

if __name__ == "__main__":
    main()