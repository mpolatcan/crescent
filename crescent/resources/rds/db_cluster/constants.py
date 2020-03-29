from crescent.core.constants import get_values
from crescent.resources.rds.constants import EngineVersion


class DBClusterEngine:
    AURORA = "aurora"
    AURORA_MYSQL = "aurora-mysql"
    AURORA_POSTGRESQL = "aurora-postgresql"

# -----------------------------------------------------------


class DBClusterEngineVersion:
    Aurora = EngineVersion.Aurora
    AuroraMysql = EngineVersion.AuroraMysql
    AuroraPostgresql = EngineVersion.AuroraPostgresql

# -----------------------------------------------------------


class EngineMode:
    PROVISIONED = "provisioned"
    SERVERLESS = "serverless"
    PARALLEL_QUERY = "parallelquery"
    GLOBAL = "global"
    MULTI_MASTER = "multimaster"

# -----------------------------------------------------------


class RestoreType:
    FULL_COPY = "full-copy"
    COPY_ON_WRITE = "copy-on-write"

# -----------------------------------------------------------


class Capacity:
    class Aurora:
        CAP_1 = 1
        CAP_2 = 2
        CAP_4 = 4
        CAP_8 = 8
        CAP_16 = 16
        CAP_32 = 32
        CAP_64 = 64
        CAP_128 = 128
        CAP_256 = 256

    class AuroraMysql:
        CAP_1 = 1
        CAP_2 = 2
        CAP_4 = 4
        CAP_8 = 8
        CAP_16 = 16
        CAP_32 = 32
        CAP_64 = 64
        CAP_128 = 128
        CAP_256 = 256

    class AuroraPostgresql:
        CAP_2 = 2
        CAP_4 = 4
        CAP_8 = 8
        CAP_16 = 16
        CAP_32 = 32
        CAP_64 = 64
        CAP_192 = 192
        CAP_384 = 384

# -----------------------------------------------------------


class _Property:
    class DBCluster:
        ENGINE = "Engine"
        ENGINE_MODE = "EngineMode"
        ENGINE_VERSION = "EngineVersion"
        SCALING_CONFIGURATION = "ScalingConfiguration"
        DB_CLUSTER_IDENTIFIER = "DBClusterIdentifier"
        SNAPSHOT_IDENTIFIER = "SnapshotIdentifier"
        SOURCE_DB_INSTANCE_IDENTIFIER = "SourceDBInstanceIdentifier"

    class ScalingConfiguration:
        MAX_CAPACITY = "MaxCapacity"
        MIN_CAPACITY = "MinCapacity"

# -----------------------------------------------------------


class AllowedValues:
    RESTORE_TYPE = get_values(RestoreType)
    ENGINE = get_values(DBClusterEngine)
    ENGINE_MODE = get_values(EngineMode)

# -----------------------------------------------------------


class NotSpecifyIfSpecified:
    DB_CLUSTER_STORAGE_ENCRYPTED = [
        _Property.DBCluster.DB_CLUSTER_IDENTIFIER,
        _Property.DBCluster.SNAPSHOT_IDENTIFIER,
        _Property.DBCluster.SOURCE_DB_INSTANCE_IDENTIFIER
    ]
    DB_CLUSTER_MASTER_USERNAME = [_Property.DBCluster.SNAPSHOT_IDENTIFIER]
    DB_CLUSTER_MASTER_USER_PASSWORD = [_Property.DBCluster.SOURCE_DB_INSTANCE_IDENTIFIER, _Property.DBCluster.SNAPSHOT_IDENTIFIER]

# -----------------------------------------------------------


class _RequiredProperties:
    class DBClusterRole:
        ROLE_ARN = "RoleArn"

# -----------------------------------------------------------


class ModelRequiredProperties:
    DB_CLUSTER_ROLE = get_values(_RequiredProperties.DBClusterRole)

# -----------------------------------------------------------


class Constants:
    ENGINE_CAPACITIES = {
        DBClusterEngine.AURORA: get_values(Capacity.Aurora),
        DBClusterEngine.AURORA_MYSQL: get_values(Capacity.AuroraMysql),
        DBClusterEngine.AURORA_POSTGRESQL: get_values(Capacity.AuroraPostgresql)
    }
    ENGINE_VERSIONS = {
        DBClusterEngine.AURORA: get_values(DBClusterEngineVersion.Aurora),
        DBClusterEngine.AURORA_MYSQL: get_values(DBClusterEngineVersion.AuroraMysql),
        DBClusterEngine.AURORA_POSTGRESQL: get_values(DBClusterEngineVersion.AuroraPostgresql)
    }
# -----------------------------------------------------------


class Conditions:
    SCALING_CONFIGURATION = [
        (
            [_Property.DBCluster.ENGINE_MODE],
            lambda engine_mode:
                True if engine_mode == EngineMode.SERVERLESS else Exception("_Property \"EngineMode\"'s value must be \"serverless\"")
        ),
        (
            [_Property.DBCluster.ENGINE, _Property.DBCluster.SCALING_CONFIGURATION],
            lambda engine, scaling_conf:
                True if scaling_conf.get(_Property.ScalingConfiguration.MAX_CAPACITY, None) is None or
                        scaling_conf[_Property.ScalingConfiguration.MAX_CAPACITY] in Constants.ENGINE_CAPACITIES[engine]
                else Exception(
                    "Property \"MaxCapacity\" must be equal to one of these values for engine \"{engine}\"! ({capacities})".format(
                        engine=engine, capacities=str(Constants.ENGINE_CAPACITIES[engine]).replace('[', '').replace(']', '')
                    )
                )
        ),
        (
            [_Property.DBCluster.ENGINE, _Property.DBCluster.SCALING_CONFIGURATION],
            lambda engine, scaling_conf:
                True if scaling_conf.get(_Property.ScalingConfiguration.MIN_CAPACITY, None) is None or
                        scaling_conf[_Property.ScalingConfiguration.MIN_CAPACITY] in Constants.ENGINE_CAPACITIES[engine]
                else Exception(
                    "Property \"MinCapacity\" must be equal to one of these values for engine \"{engine}\"! ({capacities})".format(
                        engine=engine, capacities=str(Constants.ENGINE_CAPACITIES[engine]).replace('[', '').replace(']', '')
                    )
                )
        )
    ]
    ENGINE_VERSION = [
        (
            [_Property.DBCluster.ENGINE, _Property.DBCluster.ENGINE_VERSION],
            lambda engine, engine_version:
                True if engine_version in Constants.ENGINE_VERSIONS[engine]
                else Exception("Invalid engine version {engine_version} for engine {engine}!".format(
                    engine_version=engine_version, engine=engine
                ))
        )
    ]