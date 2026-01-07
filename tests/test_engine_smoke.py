from catmoro.config.schema import (
    CatProcessConfig,
    MappingConfig,
    MortalityConfig,
    ReinsuranceConfig,
    SeverityConfig,
    SimulationConfig,
    SimulationSettings,
)
from catmoro.engine.runner import run_simulation, run_tiny_simulation
from catmoro.insurance.contracts import XoLContract
from catmoro.insurance.program import Program


def test_engine_smoke() -> None:
    results = run_tiny_simulation()
    assert len(results) == 3
    assert all(r.year >= 1 for r in results)


def test_deterministic_seed() -> None:
    cfg = SimulationConfig(
        simulation=SimulationSettings(n_years=5, seed=42),
        cat_process=CatProcessConfig(
            annual_rate=1.0,
            event_type_mix={"test": 1.0},
        ),
        severity=SeverityConfig(mu=1.0, sigma=0.1),
        mortality=MortalityConfig(base_lambda=0.0, jump_prob=0.0, jump_lambda=0.0),
        loss_mapping=MappingConfig(cost_per_excess_death=1.0),
        reinsurance=ReinsuranceConfig(program=[]),
    )
    first = run_simulation(cfg)
    second = run_simulation(cfg)
    assert [item.net_loss for item in first] == [item.net_loss for item in second]


def test_xol_attach_monotonic() -> None:
    loss = 100.0
    low_attach = Program(contracts=[XoLContract(attachment=20.0, limit=50.0)])
    high_attach = Program(contracts=[XoLContract(attachment=40.0, limit=50.0)])
    _, ceded_low = low_attach.apply_total(loss)
    _, ceded_high = high_attach.apply_total(loss)
    assert ceded_high <= ceded_low
