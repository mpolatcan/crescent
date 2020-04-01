from crescent.policy_builder import PolicyBuilder, Actions
from crescent import ecr

PolicyBuilder("test").AllowActions(
    Actions.Ecr.ReadAll().Repository(ecr.RepositoryArn("test")),
    Actions.Ecr.WriteAll().Repository(ecr.RepositoryArn("test"))
).JSON("test")
