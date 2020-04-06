from crescent.core.constants import get_values
from crescent.resources.rds.constants import EngineVersion


class DBInstanceEngine:
    AURORA = "aurora"
    AURORA_MYSQL = "aurora-mysql"
    AURORA_POSTGRESQL = "aurora-postgresql"
    MARIADB = "mariadb"
    MYSQL = "mysql"
    ORACLE_EE = "oracle-ee"
    ORACLE_SE2 = "oracle-se2"
    ORACLE_SE1 = "oracle-se1"
    ORACLE_SE = "oracle-se"
    POSTGRESQL = "postgres"
    SQLSERVER_EE = "sqlserver-ee"
    SQLSERVER_SE = "sqlserver-se"
    SQLSERVER_EX = "sqlserver-ex"
    SQLSERVER_WEB = "sqlserver-web"


# ------------------------------------------------


class StorageType:
    STANDARD = "standard"
    GP2 = "gp2"
    IO1 = "io1"

# ------------------------------------------------


class MonitoringInterval:
    SECS_0 = 0
    SECS_1 = 1
    SECS_5 = 5
    SECS_10 = 10
    SECS_15 = 15
    SECS_30 = 30
    SECS_60 = 60

# ------------------------------------------------


class DBInstanceClass:
    M5_24XL_96_VCPU_384GIB_MEM = "db.m5.24xlarge"
    M5_16XL_64_VCPU_256GIB_MEM = "db.m5.16xlarge"
    M5_12XL_48_VCPU_192GIB_MEM = "db.m5.12xlarge"
    M5_8XL_32_VCPU_128GIB_MEM = "db.m5.8xlarge"
    M5_4XL_16_VCPU_64GIB_MEM = "db.m5.4xlarge"
    M5_2XL_8_VCPU_32GIB_MEM = "db.m5.2xlarge"
    M5_XL_4_VCPU_16GIB_MEM = "db.m5.xlarge"
    M5_L_2_VCPU_8GIB_MEM = "db.m5.large"
    # ------------------------------------------
    M4_16XL_64_VCPU_25GIB_MEM = "db.m4.16xlarge"
    M4_10XL_40_VCPU_160GIB_MEM = "db.m4.10xlarge"
    M4_4XL_16_VCPU_64GIB_MEM = "db.m4.4xlarge"
    M4_2XL_8_VCPU_32GIB_MEM = "db.m4.2xlarge"
    M4_XL_4_VCPU_16GIB_MEM = "db.m4.xlarge"
    M4_L_2_VCPU_8GIB_MEM = "db.m4.large"
    # ------------------------------------------
    M3_2XL_8_VCPU_30GIB_MEM = "db.m3.2xlarge"
    M3_XL_4_VCPU_15GIB_MEM = "db.m3.xlarge"
    M3_L_2_VCPU_7_5GIB_MEM = "db.m3.large"
    M3_M_1_VCPU_3_75GIB_MEM = "db.m3.medium"
    # ------------------------------------------
    M2_4XL_8_VCPU_68_4GIB_MEM = "db.m2.4xlarge"
    M2_2XL_4_VCPU_34_2GIB_MEM = "db.m2.2xlarge"
    M2_XL_2_VCPU_17_1GIB_MEM = "db.m2.xlarge"
    # ------------------------------------------
    M1_XL_4_VCPU_15GIB_MEM = "db.m1.xlarge"
    M1_L_2_VCPU_7_5GIB_MEM = "db.m1.large"
    M1_M_1_VCPU_3_75GIB_MEM = "db.m1.medium"
    M1_S_1_VCPU_1_7GIB_MEM = "db.m1.small"
    # ------------------------------------------
    X1E_32XL_128_VCPU_3904GIB_MEM = "db.x1e.32xlarge"
    X1E_16XL_64_VCPU_1952GIB_MEM = "db.x1e.16xlarge"
    X1E_8XL_32_VCPU_976GIB_MEM = "db.x1e.8xlarge"
    X1E_4XL_16_VCPU_488GIB_MEM = "db.x1e.4xlarge"
    X1E_2XL_8_VCPU_244GIB_MEM = "db.x1e.2xlarge"
    X1E_XL_4_VCPU_122GIB_MEM = "db.x1e.xlarge"
    # ------------------------------------------
    X1_32XL_128_VCPU_1952GIB_MEM = "db.x1.32xlarge"
    X1_16XL_64_VCPU_976GIB_MEM = "db.x1.16xlarge"
    # ------------------------------------------
    R5_24XL_96_VCPU_768GIB_MEM = "db.r5.24xlarge"
    R5_16XL_64_VCPU_512GIB_MEM = "db.r5.16xlarge"
    R5_12XL_48_VCPU_384GIB_MEM = "db.r5.12xlarge"
    R5_8XL_32_VCPU_256GIB_MEM = "db.r5.8xlarge"
    R5_4XL_16_VCPU_128GIB_MEM = "db.r5.4xlarge"
    R5_2XL_8_VCPU_64GIB_MEM = "db.r5.2xlarge"
    R5_XL_4_VCPU_32GIB_MEM = "db.r5.xlarge"
    R5_L_2_VCPU_16GIB_MEM = "db.r5.large"
    # ------------------------------------------
    R4_16XL_64_VCPU_488GIB_MEM = "db.r4.16xlarge"
    R4_8XL_32_VCPU_244GIB_MEM = "db.r4.8xlarge"
    R4_4XL_16_VCPU_122GIB_MEM = "db.r4.4xlarge"
    R4_2XL_8_VCPU_61GIB_MEM = "db.r4.2xlarge"
    R4_XL_4_VCPU_30_5GIB_MEM = "db.r4.xlarge"
    R4_L_2_VCPU_15_25GIB_MEM = "db.r4.large"
    # ------------------------------------------
    R3_8XL_32_VCPU_244GIB_MEM = "db.r3.8xlarge"
    R3_4XL_16_VCPU_122GIB_MEM = "db.r3.4xlarge"
    R3_2XL_8_VCPU_61GIB_MEM = "db.r3.2xlarge"
    R3_XL_4_VCPU_30_5GIB_MEM = "db.r3.xlarge"
    R3_L_2_VCPU_15_25GIB_MEM = "db.r3.large"
    # ------------------------------------------
    T3_2XL_8_VCPU_32GIB_MEM = "db.t3.2xlarge"
    T3_XL_4_VCPU_16GIB_MEM = "db.t3.xlarge"
    T3_L_2_VCPU_8GIB_MEM = "db.t3.large"
    T3_M_2_VCPU_4GIB_MEM = "db.t3.medium"
    T3_S_2_VCPU_2GIB_MEM = "db.t3.small"
    T3_MICRO_2_VCPU_1GIB_MEM = "db.t3.micro"
    # ------------------------------------------
    T2_2XL_8_VCPU_32GIB_MEM = "db.t2.2xlarge"
    T2_XL_4_VCPU_16GIB_MEM = "db.t2.xlarge"
    T2_L_2_VCPU_8GIB_MEM = "db.t2.large"
    T2_M_2_VCPU_4GIB_MEM = "db.t2.medium"
    T2_S_1_VCPU_2GIB_MEM = "db.t2.small"
    T2_MICRO_1_VCPU_1GIB_MEM = "db.t2.micro"

# -----------------------------------------------------------


class _Property:
    class DBInstance:
        ENGINE = "Engine"
        ENGINE_VERSION = "EngineVersion"
        DB_NAME = "DBName"
        MASTER_USER_PASSWORD = "MasterUserPassword"


# -----------------------------------------------------------


class _RequiredProperties:
    class DBInstanceRole:
        FEATURE_NAME = "FeatureName"
        ROLE_ARN = "RoleArn"

    class DBInstance:
        DB_INSTANCE_CLASS = "DBInstanceClass"


# -----------------------------------------------------------

class ModelRequiredProperties:
    DB_INSTANCE_ROLE = get_values(_RequiredProperties.DBInstanceRole)

# -----------------------------------------------------------


class ResourceRequiredProperties:
    DB_INSTANCE = get_values(_RequiredProperties.DBInstance)


# -----------------------------------------------------------


class AllowedValues:
    ENGINE = get_values(DBInstanceEngine)
    DB_INSTANCE_CLASS = get_values(DBInstanceClass)
    MONITORING_INTERVAL = get_values(MonitoringInterval)
    STORAGE_TYPE = get_values(StorageType)

# ------------------------------------------------


class Constants:
    MASTER_USER_PASSWORD_LENGTHS = {
        DBInstanceEngine.MARIADB: (8, 41),
        DBInstanceEngine.SQLSERVER_SE: (8, 128),
        DBInstanceEngine.SQLSERVER_WEB: (8, 128),
        DBInstanceEngine.SQLSERVER_EE: (8, 128),
        DBInstanceEngine.SQLSERVER_EX: (8, 128),
        DBInstanceEngine.MYSQL: (8, 41),
        DBInstanceEngine.ORACLE_EE: (8, 30),
        DBInstanceEngine.ORACLE_SE: (8, 30),
        DBInstanceEngine.ORACLE_SE1: (8, 30),
        DBInstanceEngine.ORACLE_SE2: (8, 30),
        DBInstanceEngine.POSTGRESQL: (8, 128)
    }
    DB_NAME_LENGTHS = {
        DBInstanceEngine.MYSQL: (1, 64),
        DBInstanceEngine.MARIADB: (1, 64),
        DBInstanceEngine.POSTGRESQL: (1, 63),
        DBInstanceEngine.AURORA: (1, 64),
        DBInstanceEngine.AURORA_MYSQL: (1, 64),
        DBInstanceEngine.AURORA_POSTGRESQL: (1, 64),
        DBInstanceEngine.ORACLE_SE2: (1, 8),
        DBInstanceEngine.ORACLE_SE1: (1, 8),
        DBInstanceEngine.ORACLE_SE: (1, 8),
        DBInstanceEngine.ORACLE_EE: (1, 8)
    }
    ENGINE_VERSIONS = {
        DBInstanceEngine.AURORA: get_values(EngineVersion.Aurora),
        DBInstanceEngine.AURORA_MYSQL: get_values(EngineVersion.AuroraMysql),
        DBInstanceEngine.AURORA_POSTGRESQL: get_values(EngineVersion.AuroraPostgresql),
        DBInstanceEngine.MARIADB: get_values(EngineVersion.MariaDb),
        DBInstanceEngine.MYSQL: get_values(EngineVersion.Mysql),
        DBInstanceEngine.ORACLE_EE: get_values(EngineVersion.OracleEe),
        DBInstanceEngine.ORACLE_SE2: get_values(EngineVersion.OracleSe2),
        DBInstanceEngine.ORACLE_SE1: get_values(EngineVersion.OracleSe1),
        DBInstanceEngine.ORACLE_SE: get_values(EngineVersion.OracleSe),
        DBInstanceEngine.POSTGRESQL: get_values(EngineVersion.Postgresql),
        DBInstanceEngine.SQLSERVER_EE: get_values(EngineVersion.SqlServerEe),
        DBInstanceEngine.SQLSERVER_SE: get_values(EngineVersion.SqlServerSe),
        DBInstanceEngine.SQLSERVER_EX: get_values(EngineVersion.SqlServerEx),
        DBInstanceEngine.SQLSERVER_WEB: get_values(EngineVersion.SqlServerWeb)
    }
# ------------------------------------------------


class Conditions:
    BACKUP_RETENTION_PERIOD = [
        (
            [_Property.DBInstance.ENGINE],
            lambda engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property BackupRetentionPeriod is not applicable. The retention period "
                           "for automated backups is managed by the DBCluster for engine {}").format(engine)
                )
                if engine in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                else dict(is_valid=True)
        )
    ]
    CHARACTER_SET_NAME = [
        (
            [_Property.DBInstance.ENGINE],
            lambda engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property CharacterSetName is not applicable.The character set is managed "
                           "by the DB Cluster for engine {}").format(engine)
                )
                if engine in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                else dict(is_valid=True)
        )
    ]
    COPY_TAGS_TO_SNAPSHOT = [
        (
            [_Property.DBInstance.ENGINE],
            lambda engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property CopyTagsToSnapshot is not applicable. Copying tags to snapshots is "
                           "managed by the DB cluster for engine {}").format(engine)
                )
                if engine in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                else dict(is_valid=True)
        )
    ]
    DELETION_PROTECTION = [
        (
            [_Property.DBInstance.ENGINE],
            lambda engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property DeletionProtection is not applicable. You can enable or disable "
                           "deletion protection for the DB cluster for engine {}").format(engine)
                )
                if engine in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                else dict(is_valid=True)
        )
    ]
    ENABLE_IAM_DATABASE_AUTHENTICATION = [
        (
            [_Property.DBInstance.ENGINE],
            lambda engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property EnableIAMDatabaseAuthentication is not applicable. Mapping "
                           "AWS IAM accounts to database accounts is managed by the DB cluster "
                           "for engine {}").format(engine)
                )
                if engine in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                else dict(is_valid=True)
        )
    ]
    STORAGE_ENCRYPTED = [
        (
            [_Property.DBInstance.ENGINE],
            lambda engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property StorageEncrypted is not applicable. The encryption for DB "
                           "instances is managed by the DB cluster for engine {}").format(engine)
                )
                if engine in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                else dict(is_valid=True)
        )
    ]
    MASTER_USER_PASSWORD = [
        (
            [_Property.DBInstance.ENGINE],
            lambda engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property MasterUserPassword is not applicable. The password for the "
                           "master user is managed by the DB cluster for engine {}").format(engine)
                )
                if engine in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                else dict(is_valid=True)
        ),
        (
            [_Property.DBInstance.MASTER_USER_PASSWORD, _Property.DBInstance.ENGINE],
            lambda master_user_password, engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property MasterUserPassword must contain from {min} to {max} "
                           "characters for engine {engine}. Given length: {length}").format(
                                min=Constants.MASTER_USER_PASSWORD_LENGTHS[engine][0],
                                max=Constants.MASTER_USER_PASSWORD_LENGTHS[engine][1],
                                engine=engine,
                                length=len(master_user_password)
                    )
                )
                if engine
                and engine not in [DBInstanceEngine.AURORA, DBInstanceEngine.AURORA_MYSQL, DBInstanceEngine.AURORA_POSTGRESQL]
                and (
                    len(master_user_password) < Constants.MASTER_USER_PASSWORD_LENGTHS[engine][0] or
                    len(master_user_password) > Constants.MASTER_USER_PASSWORD_LENGTHS[engine][1]
                ) else dict(is_valid=True)
        )
    ]
    DB_NAME = [
        (
            [_Property.DBInstance.DB_NAME, _Property.DBInstance.ENGINE],
            lambda db_name, engine:
                dict(
                    is_valid=False,
                    error=("DBInstance's property DBName must contain from {min} to {max} characters "
                           "for engine {engine}. Given length: {length}").format(
                                min=Constants.DB_NAME_LENGTHS[engine][0],
                                max=Constants.DB_NAME_LENGTHS[engine][1],
                                engine=engine,
                                length=len(db_name)
                    )
                )
                if db_name is not None and engine and (
                    len(db_name) < Constants.DB_NAME_LENGTHS[engine][0] or
                    len(db_name) > Constants.DB_NAME_LENGTHS[engine][1]
                ) else dict(is_valid=True)
        )
    ]
    ENGINE_VERSION = [
        (
            [_Property.DBInstance.ENGINE, _Property.DBInstance.ENGINE_VERSION],
            lambda engine, engine_version:
                dict(is_valid=True) if not engine
                    or engine_version in Constants.ENGINE_VERSIONS[engine]
                else dict(
                    is_valid=False,
                    error=("DBInstance's property EngineVersion value {engine_version} is invalid "
                           "for engine {engine}!").format(engine_version=engine_version, engine=engine)
                )
        )
    ]
