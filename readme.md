Overview: These instructions provide you with a skeleton python definition for each problem type. After cloning this repo, you will modify only those functions that you have signed up for (at most 3 for a three person group)
* You will clone a repo that has skeleton code for each possible program.
* You will modify the body of your selected code for your implementation. Do not change the arguments.
* Your output can be simply printed to screen for visual inspection. but while we grade this assignment, we will use have our custom test case files and see if we are able to see results as expected.
* Instructions are also included on running your code when you want to test it.
* When you modified code is called the arguments to the function on each call provide a test case (you do not need to read test cases rom any files with this procedure).
* The "input" folder holds the test cases that the above mechanism will use when you run your tests.
* The test cases to be used for grading are separate, and are not visible to you.
* If you need to access other python packages in your code, the UV package discussed below can give your functions access to them.
* Send all questions about this infrastructure to Laxminarayana Vadnala lvadnala@nd.edu

<!-- ## instructions to generate a PAT (a Personal Access Token): -->


<!-- * Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
* Click "Generate new token" → "Generate new token (classic)"
* Set expiration (90 days recommended)
* Select scopes: repo (full control of private repositories)
* Generate token and copy it -->


## Student Instructions to clone the repository and how to run and finally submit the assignment:
------------------
* From your browser, go to [GITHUB URL](https://github.com/pkogge/Project1-TOC) and click the fork button as shown in the picture below


![fork_button](documentation/assets/fork_button.png "fork button")


* You will now enter the fork screen, from here make sure to select your own github account which is highlighted in screen below (for instance, I have selected my own personal account), after that click on the `create fork` button highlighted in orange arrow and box.

![fork_screen](documentation/assets/fork_screen.png "fork screen")

* You will now see the screen which looks like below, the first red box on left should reflect your own github account and should say forked from `forked from pkogge/Project1-TOC.` Then you can follow general instructions of cloning the github repository. Here is the [Docs Link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) that can help you to clone the github repository on your computer.

![cloned_repo](documentation/assets/cloned_repo.png "cloned_repo")

* Once you clone the repository, open the project in the IDE of your choice.

### Getting started with the python support package manager "UV" installation.
----------------

* Start  by installing `UV` in your machine. Here is the [instructions page](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) that helps you to install the `UV`.

* Immediately after installing it run command `uv sync` which installs the pytests and other required packages.

* NOTE: If you are struggling with installing `UV` please feel to reach me out via slack, I can help you navigate. lvadnala@nd.edu

* This project template is equipped with all the packages required for your project. No additional python packages are required to be installed, but if you want to install additional python packages make sure use the command `uv add <python-package-name>` (mostly it is not useful).

### How can we run the code using UV when other packages are needed
----------------
* For this project I am using UV to demonstrate to run the code. Basically you need to use the command `uv run main.py <filename> <input_string>` from the root of the project folder in the terminal to see your code executes. eg., `uv run main.py ./input/aplus.csv "aaaa"`
* Immediately after cloning the repository, and you didnt do any code changes, if you run the command `uv run main.py ./input/aplus.csv "aaaa"` you would see the results below.

```
(base) lax@Mac Project1-TOC % uv run main.py ./input/aplus.csv "aaaa"
Tracing NTM: a plus on input 'aaaa'
```

* the `Tracing NTM: a plus on input 'aaaa'` message states that you are good to make changes to the code.

### Making changes to the code and running the test cases of your own
----------------

* Here is the folder structure that every student should make changes to. This is personalized for SAT, but the others are similar. The src directory hold the code you want to modify.

```
.
|── src/
│   |── entrypoint.py
|   |── ktape_dtm.py
|   |-- ntm_tracer.py
|   |── input/
|   |   |-- aplus.csv
|   |   |-- ktape.csv
|   |   |-- ntm_n1n.csv
|-- main.py
```

* The `src/entrypoint.py` file contains the function called as `main.` Make sure to add all your auxikiary files into the `src` folder and make sure to use the `entrypoint.py` file's main function as your main function Dont change this structure as if you do the automation wont be able to perform the grading.
* The `input` folder is where you will find sample inputs for to get started for project.
* The `module_tests` is the folder where you can add your own custom test cases. If you are familiar with pytests you can do so, but it is not compulsory to add test cases to the project, its totally the students choice to add, since the pytests have a little learning curve.
* `main.py` please dont edit this file, this is the main file and it should stay like this.

### Commit the code and make sure to raise a PR (Pull Request)
---------------

* Push the changes to the repositiory. Here is the [Docs Link](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) that helps you with basic git commands to push the code.
* Now the last step is to raise the PR to the Forked repo, here is the [Docs link](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
* Please update the PR link to the [Teams Spread Sheet](https://docs.google.com/spreadsheets/d/1FYyJMDnft__n0SohcIcSL7lUO60RMtJk9nuVJ5l30SY/edit?usp=sharing) shared by Dr. Kogge. This is most important since we grade only the links that are part of the teams spreadsheet.

# Project 1 Readme – Team Problem Solverz

**Version:** 1  
**Date:** 9/11/24  

---

## 1. Team Name
Problem Solverz

---

## 2. Team Members (Name and NetID)
- AJ Jones (ajones42)

---

## 3. Overall Project Attempted
**Program 1:** Tracing NTM Behavior  
A Nondeterministic Turing Machine (NTM) tracer implemented using **Breadth-First Search (BFS)** to fairly explore all computation paths.

---

## 4. Overall Success of the Project
The project was **successful**. The NTM tracer correctly:
- Performs breadth-first exploration of all computation paths
- Identifies accepting and rejecting configurations
- Traces and prints the accepting computation path
- Computes the degree of nondeterminism as specified

---

## 5. Approximate Total Time to Complete
8–10 hours

---

## 6. GitHub Repository
https://github.com/ajones2005/Project1-TOC.git

---

## 7. List of Included Files

### Code Files
| File | Description |
|----|----|
| `src/ntm_tracer.py` | Main NTM tracing logic using breadth-first search |
| `src/entrypoint.py` | Command-line interface and program entry point |
| `src/helpers/turing_machine.py` | Turing Machine simulator class and transition parsing |

### Test Files
| File | Description |
|----|----|
| `input/aplus.csv` | Test NTM for the language a⁺ |
| `input/composite.csv` | Composite NTM used to test nondeterminism |
| `input/a_star.csv` | Deterministic NTM for the language a* |

---

## 8. Programming Languages and Libraries Used
- **Python**
- Libraries: `os`, `sys`, `csv`, `time`

---

## 9. Key Data Structures
- **Config class:** Stores (left tape, current state, right tape), parent reference, transition used, and depth
- **Tree structure:** List of lists, where each list represents configurations at a given depth
- **Configuration representation:** Tuple `(left_of_head, current_state, right_of_head)`
- **Transition dictionary:** Stores `read`, `next`, `write`, and `move`
- **Path list:** Used to reconstruct the accepting path via backtracking

---

## 10. General Operation of the Code
The NTM tracer simulates nondeterministic Turing machines using breadth-first search:

1. Reads the Turing Machine description from a CSV file
2. Creates the initial configuration with an empty left tape, start state, and input string
3. Maintains a BFS tree where level *k* contains all configurations reachable in *k* transitions
4. Applies all valid transitions for each configuration
5. Accepts immediately when an accept state is reached
6. Continues until all paths reject or a maximum depth is exceeded

---

## 11. Test Cases Used
I followed the approach described in **Section 4.1** of the project specification to ensure fair exploration of all computation paths.  
The test machines verified:
- Correct halting behavior
- Proper BFS traversal
- Accurate path reconstruction
- Immediate acceptance upon reaching an accept state

---

## 12. Code Development Strategy
I began by carefully studying the project specification, especially Section 4.1.  
The project was broken into the following components:
- Configuration representation
- Transition application and tape movement
- BFS tree construction
- Halting detection
- Accepting path reconstruction

---

## 13. Discussion of Results
The tracer was tested on the **a⁺ machine**.  
For input `"aaa"`:
- The machine accepted after 4 steps
- Total transitions simulated ranged between 4–15
- The accepting path demonstrated correct tape manipulation and state transitions

These results confirm that the BFS approach explores all paths fairly and correctly identifies accepting configurations.

---

## 14. Team Organization
This was a solo project.

---

## 15. What I Would Do Differently
I would implement **duplicate configuration detection** to prevent re-exploration of identical configurations, improving efficiency for machines with loops.

---

## 16. Additional Material
N/A

