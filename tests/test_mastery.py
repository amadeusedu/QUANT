from quant_core.skills.mastery import update_mastery


def test_mastery_capped() -> None:
    new = update_mastery(50, True, 10, 1)
    assert 50 <= new <= 54
