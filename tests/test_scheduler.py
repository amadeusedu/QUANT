from quant_core.drills.scheduler import schedule_next


def test_schedule_next_progresses() -> None:
    s = schedule_next(5, 2.5, 6, 2)
    assert s.interval >= 6
    assert s.repetitions == 3
