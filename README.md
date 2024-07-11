# Report for Assignment 1 resit

## Project chosen

Name: Thefuck

URL: https://github.com/nvbn/thefuck

Number of lines of code and the tool used to count it: 13077, counted with lizard.

Programming language: Pyt

## Coverage measurement with existing tool

For the initial coverage measurment I used coverage.py, a tool for coverage reports in Python. Since the suite for the project is pytest, in order to measure the code coverage I used the following commands:

```coverage run -m pytest```

And after that, in order to represent the code in a cleaner manner:

```coverage html```

Which generates a nice report for us to be able to read the information in a more visual way. This resulted in the following:
![Coverage before test addition](img/screenshot_full_coverage_prev.png)


## Coverage improvement

### Individual tests

#### Failed function

![Link to github](https://github.com/juno-soyr/thefuck/commit/22cda687627a21b9280f5e2ce6ae2e0d082f9a32)

![Previous coverage](img/test_failed_coverage_prev.png)
![Final coverage](img/test_failed_coverage_final.png)

There is an improvement of a hundred percent, since the function was not covered previously. With the print statements tested and the value passed to the function being the only two possible results, I made 2 test functions for the 2 possible outcomes.

#### Warn function

![Link to github](https://github.com/juno-soyr/thefuck/commit/2b8f4890c94ac348c51054913ba2e4417316fc5a)

![Previous coverage](img/test_warn_coverage_prev.png)
![Final coverage](img/test_warn_coverage_final.png)

As the previous function, the improvement is a hundred percent, since the function was not covered previously. The inner workings of the two functions are similar, so It was the same logic, but with a different result.


### Overall

![Coverage before test addition](img/screenshot_full_coverage_prev.png)

![Coverage after test addition](img/full_coverage_final.png)
