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


class Property:
    DB_INSTANCE_ROLE_FEATURE_NAME = "FeatureName"
    DB_INSTANCE_ROLE_ROLE_ARN = "RoleArn"

# -----------------------------------------------------------


class RequiredProperties:
    DB_INSTANCE_ROLE = [
        Property.DB_INSTANCE_ROLE_FEATURE_NAME,
        Property.DB_INSTANCE_ROLE_ROLE_ARN
    ]
