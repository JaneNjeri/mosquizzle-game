# test_mos_control.py

import pytest  # noqa: F401
from unittest.mock import patch
from modules.mos_control import MalariaControlGame


def test_attack_mosquito():
    game = MalariaControlGame()
    assert isinstance(game.mosquito_population, int)

    # store state variables before running function under test
    mosquito_population_before = game.mosquito_population

    # call the method
    game.attack_mosquito()

    # compare state variables afterwards, check changes are as expected
    mosquito_population_after = game.mosquito_population

    # assert mosquito_population_after < mosquito_population_before
    assert mosquito_population_after == mosquito_population_before - 1


def test_use_bed_net():
    game = MalariaControlGame()
    assert isinstance(game.bed_net_available, bool)

    # get initial health
    initial_health = game.player_health

    # call the method
    game.use_bed_net()

    # assert that bed_net_available is set to False
    assert not game.bed_net_available
    # check if player health increased
    assert game.player_health > initial_health


def test_use_insecticide(monkeypatch, capsys):
    game = MalariaControlGame()
    # get the initial mosquito popn
    initial_population = game.mosquito_population

    # mocking the random number generator to return a fixed value for testing
    monkeypatch.setattr('random.randint', lambda a, b: 3)

    # call the method
    game.use_insecticide()

    # check if insecticide_available is set to False
    assert not game.insecticide_available
    # check if mosquito_population decreased by the expected value
    assert game.mosquito_population == initial_population - 3
    # check if the expected message is printed
    reduced = capsys.readouterr()
    assert 'You used insecticide to reduce the mosquito population.' in reduced.out


def test_explore(capsys):
    game = MalariaControlGame()

    # get initial values for the variables
    initial_days_survived = game.days_survived
    initial_mosquito_population = game.mosquito_population
    initial_player_health = game.player_health

    # print for debugging
    #print(f"Initial mosquito population: {initial_mosquito_population}")
    #print(f"Initial player health: {initial_player_health}")

    # patching random.randint
    with patch('random.randint') as mock_randint:
        # configure mock_randint to return fixed values
        mock_randint.side_effect = [2, 10]

        # call method
        game.explore()

    # check if days survived increased by 1
    assert game.days_survived == initial_days_survived + 1
    # check if mosquito popn increased by 2
    assert game.mosquito_population == initial_mosquito_population + 2
    # check if player's health decreased by 10
    assert game.player_health == initial_player_health - 10

    # check if the expected message is printed
    captured = capsys.readouterr()
    assert 'You explored the area. Mosquitoes are breeding, and your health decreased.' in captured.out


def test_rest(monkeypatch, capsys):
    game = MalariaControlGame()

    # get initial values of variables
    initial_days_survived = game.days_survived
    initial_player_health = game.player_health

    # mock the random.randint function with monkeypatch
    monkeypatch.setattr('random.randint', lambda a, b: 15)

    # call method
    game.rest()

    # check if days survived increased by 1
    assert game.days_survived == initial_days_survived + 1
    # check if player's health increased by fixed value 15
    assert game.player_health == initial_player_health + 15
    # check if the expected message is printed
    rested = capsys.readouterr()
    assert 'You rested and regained some health.' in rested.out
