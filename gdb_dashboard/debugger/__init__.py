import gdb_dashboard.util
import gdb


def config() -> None:
    with gdb_dashboard.util.package_file_path("config.gdb") as config_path:
        gdb.execute(f"source {str(config_path)}")
