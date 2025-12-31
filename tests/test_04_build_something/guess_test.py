import lab_04_build_something.guess as guess

def test_pick_target_number():
    number = guess.pick_target_number()
    assert guess.LOWEST_NUMBER <= number <= guess.HIGHEST_NUMBER
