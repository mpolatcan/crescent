class Engine:
    AURORA = "aurora"
    AURORA_MYSQL = "aurora-mysql"
    AURORA_POSTGRESQL = "aurora-postgresql"


class EngineMode:
    PROVISIONED = "provisioned"
    SERVERLESS = "serverless"
    PARALLEL_QUERY = "parallelquery"
    GLOBAL = "global"
    MULTI_MASTER = "multimaster"


class RestoreType:
    FULL_COPY = "full-copy"
    COPY_ON_WRITE = "copy-on-write"


class Capacity:
    class __CapacityAuroraMysql:
        CAP_1 = 1
        CAP_2 = 2
        CAP_4 = 4
        CAP_8 = 8
        CAP_16 = 16
        CAP_32 = 32
        CAP_64 = 64
        CAP_128 = 128
        CAP_256 = 256

    class __CapacityAuroraPostgresql:
        CAP_2 = 2
        CAP_4 = 4
        CAP_8 = 8
        CAP_16 = 16
        CAP_32 = 32
        CAP_64 = 64
        CAP_192 = 192
        CAP_384 = 384

    aurora = __CapacityAuroraMysql
    aurora_mysql = __CapacityAuroraMysql
    aurora_postgresql = __CapacityAuroraPostgresql


class Property:
    ASSOCIATED_ROLES = "AssociatedRoles"
    ENGINE = "Engine"
    ENGINE_MODE = "EngineMode"
    SCALING_CONFIGURATION = "ScalingConfiguration"
    SCALING_CONFIGURATION_MAX_CAPACITY = "MaxCapacity"
    SCALING_CONFIGURATION_MIN_CAPACITY = "MinCapacity"
    DB_CLUSTER_IDENTIFIER = "DBClusterIdentifier"
    SNAPSHOT_IDENTIFIER = "SnapshotIdentifier"
    SOURCE_DB_INSTANCE_IDENTIFIER = "SourceDBInstanceIdentifier"


class Constants:
    KEY_PARAMETERS = "parameters"
    KEY_CONDITION_FUNCTION = "condition_function"
    ENGINE_CAPACITIES = {
        Engine.AURORA: [
            Capacity.aurora_mysql.CAP_1, Capacity.aurora_mysql.CAP_2, Capacity.aurora_mysql.CAP_4,
            Capacity.aurora_mysql.CAP_8, Capacity.aurora_mysql.CAP_16, Capacity.aurora_mysql.CAP_32,
            Capacity.aurora_mysql.CAP_64, Capacity.aurora_mysql.CAP_128, Capacity.aurora_mysql.CAP_256
        ],
        Engine.AURORA_MYSQL: [
            Capacity.aurora_mysql.CAP_1, Capacity.aurora_mysql.CAP_2, Capacity.aurora_mysql.CAP_4,
            Capacity.aurora_mysql.CAP_8, Capacity.aurora_mysql.CAP_16, Capacity.aurora_mysql.CAP_32,
            Capacity.aurora_mysql.CAP_64, Capacity.aurora_mysql.CAP_128, Capacity.aurora_mysql.CAP_256
        ],
        Engine.AURORA_POSTGRESQL: [
            Capacity.aurora_postgresql.CAP_2, Capacity.aurora_postgresql.CAP_4,
            Capacity.aurora_postgresql.CAP_8, Capacity.aurora_postgresql.CAP_16,
            Capacity.aurora_postgresql.CAP_32, Capacity.aurora_postgresql.CAP_64,
            Capacity.aurora_postgresql.CAP_192, Capacity.aurora_postgresql.CAP_384
        ]
    }


class Conditions:
    SCALING_CONFIGURATION = [
        (
            [Property.ENGINE_MODE],
            lambda engine_mode:
                True if engine_mode == EngineMode.SERVERLESS else Exception("Property \"EngineMode\"'s value must be \"serverless\"")
        ),
        (
            [Property.ENGINE, Property.SCALING_CONFIGURATION],
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
            [Property.ENGINE, Property.SCALING_CONFIGURATION],
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