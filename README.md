# Exact Learning DOTAs

> This project is a refactored version of [OTALearning](https://github.com/Leslieaj/OTALearning) and [OTALearningNormal](https://github.com/Leslieaj/OTALearningNormal).

## Overview

This tool is dedicated to learning deterministic one-clock timed automata (DOTAs) which is a subclass of timed automata with only one clock. In 1987, Dana Angluin introduced the L* Algorithm for learning regular sets from queries and counterexamples. The tool implement an Angluin-style active learning algorithm on DOTAs. This branch is the smart teacher situation and normal teacher situation with an accelerating trick. 

## Installation

The project was developed using Python3, and you only need to download the project, but there are a few prerequisites before running：

- Python3.7.* (or high)
- graphviz (used for drawing)

## Usage

```
$python3 main.py benchmarks/3_2_10/3_2_10-1.json smart_teacher
$python3 main.py benchmarks/3_2_10/3_2_10-1.json normal_teacher
```

- `learnota.py` is the main file of the program.
- `smart_teacher` or `normal_teacher` is teacher situation.
- The target DOTA is stored in a JSON file, in this example, `3_2_10-1.json` . The details are as follows.

#### DOTA.json

```json
{
    "states": ["1", "2"],
    "inputs": ["a", "b", "c"],
    "trans": {
        "0": ["1", "a", "[3,9)", "r", "2"],
        "1": ["1", "b", "[1,5]", "r", "2"],
        "2": ["1", "c", "[0,3)", "n", "1"],
        "3": ["2", "a", "(5,+)", "n", "1"],
        "4": ["2", "b", "(7,8]", "n", "1"],
        "5": ["2", "c", "(4,+)", "r", "1"]
    },
    "initState": "1",
    "acceptStates": ["2"]
}
```

*Explanation:*

- "states": the set of the name of locations;
- "inputs": the input alphabet;
- "trans": the set of transitions in the form `id : [name of the source location, input action, guards, reset, name of the target location];`
  - "+" in a guard means INFTY;
  - "r" means resetting the clock, "n" otherwise
- "initState": the name of initial location;
- "acceptStates": the set of the name of accepting locations.

⚠️⚠️⚠️ During use, you must ensure that the naming is correct and the content follows the prescribed format.

## Output

If we learn the target DOTA successfully, the final COTA will be drawn and displayed as a PDF file. Additionally, we will count the total learning time, total number of tables explored, the number of equivalence query, and the number of membership query, etc. All results will be stored in a folder named `results` and a file named `result.json`.

## License

See [MIT LICENSE](./LICENSE) file.

## Contact

Please let me know if you have any questions 👉 [EnvisionShen@gmail.com](mailto:EnvisionShen@gmail.com)

