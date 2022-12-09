Feature: Unique_test

  Scenario: List of integer
    Given We have list of integers [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
     When We run Unique()
     Then We must have [1, 2]
  Scenario: List of generator of integers
    Given We have generator of integers [1, 2, 3, 1, 2, 1, 2, 3, 3]
     When We run Unique()
     Then We must have [1, 2, 3]
  Scenario: List of string
    Given We have list of string ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
     When We run Unique()
     Then We must have string ['a', 'A', 'b', 'B']
  Scenario: List of string ignore case
    Given We have list of string ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
     When We run Unique() with ignore_case
     Then We must have string ['a', 'b']
