from catmoro.engine.runner import run_tiny_simulation


def test_engine_smoke() -> None:
    results = run_tiny_simulation()
    assert len(results) == 3
    assert all(r.year >= 1 for r in results)
