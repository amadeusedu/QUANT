from quant_core.db.db import DB_PATH, init_db
from quant_core.db.repositories import Repo


def test_db_roundtrip() -> None:
    init_db(reset=True)
    repo = Repo(DB_PATH)
    repo.add_application('Acme', 'Quant Intern', 'applied', 'wait', 'note')
    apps = repo.list_applications()
    assert not apps.empty
