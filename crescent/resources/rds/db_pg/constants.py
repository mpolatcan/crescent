from crescent.resources.rds.constants import EngineFamily
from crescent.core.constants import get_values
from itertools import chain


class AllowedValues:
    FAMILY = list(chain.from_iterable(
        [
            get_values(EngineFamily.Aurora),
            get_values(EngineFamily.AuroraMysql),
            get_values(EngineFamily.AuroraPostgresql),
            get_values(EngineFamily.MariaDb),
            get_values(EngineFamily.Mysql),
            get_values(EngineFamily.OracleEe),
            get_values(EngineFamily.OracleSe),
            get_values(EngineFamily.OracleSe1),
            get_values(EngineFamily.OracleSe2),
            get_values(EngineFamily.Postgresql),
            get_values(EngineFamily.SqlServerEe),
            get_values(EngineFamily.SqlServerEx),
            get_values(EngineFamily.SqlServerSe),
            get_values(EngineFamily.SqlServerWeb)
        ]
    ))
