from uuid import UUID

from fixit.cli import main


def test_uuid_command_prints_requested_number_of_uuid4_values(capsys):
    main(["uuid", "--count", "3"])

    values = capsys.readouterr().out.splitlines()
    assert len(values) == 3, f"expected 3 UUIDs, got {len(values)}"
    assert all(UUID(value).version == 4 for value in values)
