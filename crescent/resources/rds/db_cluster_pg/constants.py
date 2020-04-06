from crescent.core.constants import get_values
from crescent.resources.rds.constants import EngineFamily
from itertools import chain


class DBClusterParameterGroupEngineFamily:
    Aurora = EngineFamily.Aurora
    AuroraMysql = EngineFamily.AuroraMysql
    AuroraPostgresql = EngineFamily.AuroraPostgresql


# -----------------------------------------


class AllowedValues:
    FAMILY = list(chain.from_iterable(
        [
            get_values(DBClusterParameterGroupEngineFamily.Aurora),
            get_values(DBClusterParameterGroupEngineFamily.AuroraMysql),
            get_values(DBClusterParameterGroupEngineFamily.AuroraPostgresql)
        ]
    ))

# -------------------------------------------


class _RequiredProperties:
    class DBClusterParameterGroup:
        DESCRIPTION = "Description"
        FAMILY = "Family"
        PARAMETERS = "Parameters"


# -------------------------------------------


class ResourceRequiredProperties:
    DB_CLUSTER_PARAMETER_GROUP = get_values(_RequiredProperties.DBClusterParameterGroup)
