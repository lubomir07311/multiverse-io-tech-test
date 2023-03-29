# Multiverse engineering take-home challenge
This is a solution to the Multiverse.io take-home challenge written in Python (v3.8.8). This version was chosen because I already had a development environment set-up.
## Requirements

### Development environment
The solution does not use any external libraries and dependencies so all you need is Python.
- Install [Python](https://www.python.org/downloads/) - to be safe, use Python 3.8.16+

Alternatively, you could use an online python compiler like [this one](https://www.onlinegdb.com/online_python_compiler) and paste the contents of `main.py`

### Unit tests
- Install [pip](https://pip.pypa.io/en/stable/installation/) - usually pip comes with Python if you've installed from Python.org but for any issues, follow the link.
- In the home directory of the project run `pip install -r requirements.txt` to get [pytest](https://docs.pytest.org/en/7.2.x/)

## Running the project

The project was tested on Windows OS. Generally, running the script shouldn't be much different on other environments.

- Open a new terminal window in the home directory of the project
- Run the command `python main.py` (or `python3 main.py` if you have older versions of python also installed)
- Enter grid size in format `x y` where x and y are numbers
- Enter position, orientation and commands in format `(n, n, D) C` where n is a number, D is one of `N E S W`, C is one of `L F R`, repeated as many times as desired
- Enter the second robot's position, orientation and commands.

The program should output 2 lines, each with the required solution.

Please note that the project uses [REGEX](https://regexr.com/) pattern matching for input validation and will keep on asking for a valid input until one is provided. To break the cycle and exit early, use `CTRL+C`.

## Running the unit tests

The project has a small amount of unit tests associated with it. They cover a robot's movement with possible happy and unhappy paths described in the comments in `test_move.py`

To run the unit tests:

- Open a new terminal window in the home directory of the project
- Run the command `pytest`

The output should look something like:
```
platform win32 -- Python 3.8.8, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\Users\Lubo\Documents\multiverse-io-tech-test
collected 9 items

test_move.py .........                                                   [100%]

============================== 9 passed in 0.02s ==============================

```

## Next steps

In order to improve on this repository, we could add a CI/CD integration to automatically run the unit tests and communicate the outcome back to GitHub. We could also extend the unit test coverage to test the input validation. In addition, integration tests could be setup to test the `main` function and check the actual output of the program.

Currently, the program runs 2 robots, but this could easily be changed. As there is a `ROBOTS_TO_RUN` constant in `main.py`. This could easily be an environment variable coming from a config file or injected during the CI/CD pipeline to allow more robots to be run. The specs specifically had 2 examples and both of them asked for 1 grid and 2 robots, hence the decision to stick to the original spec document.

Lastly, the latest version of Python is 3.11.2. The code should be tested and upgraded to this version to take advantage of the latest security and bugfixes of the language.