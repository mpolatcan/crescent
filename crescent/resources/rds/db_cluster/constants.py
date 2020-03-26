class DBClusterEngines:
    AURORA = "aurora"
    AURORA_MYSQL = "aurora-mysql"
    AURORA_POSTGRESQL = "aurora-postgresql"

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


class Property:
    DB_CLUSTER_ASSOCIATED_ROLES = "AssociatedRoles"
    DB_CLUSTER_ENGINE = "Engine"
    DB_CLUSTER_ENGINE_MODE = "EngineMode"
    DB_CLUSTER_SCALING_CONFIGURATION = "ScalingConfiguration"
    DB_CLUSTER_IDENTIFIER = "DBClusterIdentifier"
    DB_CLUSTER_SNAPSHOT_IDENTIFIER = "SnapshotIdentifier"
    DB_CLUSTER_SOURCE_DB_INSTANCE_IDENTIFIER = "SourceDBInstanceIdentifier"
    SCALING_CONFIGURATION_MAX_CAPACITY = "MaxCapacity"
    SCALING_CONFIGURATION_MIN_CAPACITY = "MinCapacity"
    DB_CLUSTER_ROLE_ROLE_ARN = "RoleARN"

# -----------------------------------------------------------


class AllowedValues:
    RESTORE_TYPE = [
        RestoreType.FULL_COPY,
        RestoreType.COPY_ON_WRITE
    ]
    ENGINE = [
        DBClusterEngines.AURORA,
        DBClusterEngines.AURORA_MYSQL,
        DBClusterEngines.AURORA_POSTGRESQL
    ]
    ENGINE_MODE = [
        EngineMode.PROVISIONED,
        EngineMode.SERVERLESS,
        EngineMode.PARALLEL_QUERY,
        EngineMode.GLOBAL,
        EngineMode.MULTI_MASTER
    ]

# -----------------------------------------------------------


class NotSpecifyIfSpecified:
    DB_CLUSTER_STORAGE_ENCRYPTED = [
        Property.DB_CLUSTER_IDENTIFIER,
        Property.DB_CLUSTER_SNAPSHOT_IDENTIFIER,
        Property.DB_CLUSTER_SOURCE_DB_INSTANCE_IDENTIFIER
    ]
    DB_CLUSTER_MASTER_USERNAME = [
        Property.DB_CLUSTER_SNAPSHOT_IDENTIFIER
    ]
    DB_CLUSTER_MASTER_USER_PASSWORD = [
        Property.DB_CLUSTER_SOURCE_DB_INSTANCE_IDENTIFIER,
        Property.DB_CLUSTER_SNAPSHOT_IDENTIFIER
    ]

# -----------------------------------------------------------


class RequiredProperties:
    DB_CLUSTER_ROLE = [
        Property.DB_CLUSTER_ROLE_ROLE_ARN
    ]

# -----------------------------------------------------------


class Constants:
    ENGINE_CAPACITIES = {
        DBClusterEngines.AURORA: [
            Capacity.Aurora.CAP_1, Capacity.Aurora.CAP_2, Capacity.Aurora.CAP_4,
            Capacity.Aurora.CAP_8, Capacity.Aurora.CAP_16, Capacity.Aurora.CAP_32,
            Capacity.Aurora.CAP_64, Capacity.Aurora.CAP_128, Capacity.Aurora.CAP_256
        ],
        DBClusterEngines.AURORA_MYSQL: [
            Capacity.AuroraMysql.CAP_1, Capacity.AuroraMysql.CAP_2, Capacity.AuroraMysql.CAP_4,
            Capacity.AuroraMysql.CAP_8, Capacity.AuroraMysql.CAP_16, Capacity.AuroraMysql.CAP_32,
            Capacity.AuroraMysql.CAP_64, Capacity.AuroraMysql.CAP_128, Capacity.AuroraMysql.CAP_256
        ],
        DBClusterEngines.AURORA_POSTGRESQL: [
            Capacity.AuroraPostgresql.CAP_2, Capacity.AuroraPostgresql.CAP_4,
            Capacity.AuroraPostgresql.CAP_8, Capacity.AuroraPostgresql.CAP_16,
            Capacity.AuroraPostgresql.CAP_32, Capacity.AuroraPostgresql.CAP_64,
            Capacity.AuroraPostgresql.CAP_192, Capacity.AuroraPostgresql.CAP_384
        ]
    }

# -----------------------------------------------------------


class Conditions:
    DB_CLUSTER_SCALING_CONFIGURATION = [
        (
            [Property.DB_CLUSTER_ENGINE_MODE],
            lambda engine_mode:
                True if engine_mode == EngineMode.SERVERLESS else Exception("Property \"EngineMode\"'s value must be \"serverless\"")
        ),
        (
            [Property.DB_CLUSTER_ENGINE_MODE, Property.DB_CLUSTER_SCALING_CONFIGURATION],
            lambda engine, scaling_conf:
                True if scaling_conf.get(Property.SCALING_CONFIGURATION_MAX_CAPACITY, None) is None or
                        scaling_conf[Property.SCALING_CONFIGURATION_MAX_CAPACITY] in Constants.ENGINE_CAPACITIES[engine]
                else Exception(
                    "Property \"MaxCapacity\" must be equal to one of these values for engine \"{engine}\"! ({capacities})".format(
                        engine=engine, capacities=str(Constants.ENGINE_CAPACITIES[engine]).replace('[', '').replace(']', '')
                    )
                )
        ),
        (
            [Property.DB_CLUSTER_ENGINE, Property.DB_CLUSTER_SCALING_CONFIGURATION],
            lambda engine, scaling_conf:
                True if scaling_conf.get(Property.SCALING_CONFIGURATION_MIN_CAPACITY, None) is None or
                        scaling_conf[Property.SCALING_CONFIGURATION_MIN_CAPACITY] in Constants.ENGINE_CAPACITIES[engine]
                else Exception(
                    "Property \"MinCapacity\" must be equal to one of these values for engine \"{engine}\"! ({capacities})".format(
                        engine=engine, capacities=str(Constants.ENGINE_CAPACITIES[engine]).replace('[', '').replace(']', '')
                    )
                )
        )
    ]