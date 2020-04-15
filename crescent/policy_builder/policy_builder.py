"""
    General Json structure for action grouping:
    {
        "Allow": {
            "*": [ ],
            "<AWS_SERVICE_NAME>": {
                "* or <RESOURCE_ARN>": [ ]
            }
        },
        "Deny: {
            "*": [ ],
            "<AWS_SERVICE_NAME>": {
                "* or <RESOURCE_ARN>": [ ]
            }
        }
    }
"""


from .actions import Action
from itertools import chain


class PolicyBuilder:
    __KEY_VERSION = "Version"
    __KEY_ID = "Id"
    __KEY_STATEMENT = "Statement"
    __KEY_SID = "Sid"
    __KEY_ACTION = "Action"
    __KEY_RESOURCE = "Resource"
    __KEY_EFFECT = "Effect"
    __EFFECT_ALLOW = "Allow"
    __EFFECT_DENY = "Deny"

    def __init__(self, id, version="2012-10-17"):
        self.__policy = {
            self.__KEY_VERSION: version,
            self.__KEY_ID: id,
            self.__KEY_STATEMENT: []
        }
        self.__action_groups = {}

    def __delete_previous_duplicate_actions(self, action):
        deleted_effect_resources = []

        # Find duplicate actions and remove these actions
        for effect, effect_resources in self.__action_groups.items():
            for effect_svc, effect_svc_resources_or_actions in effect_resources.items():
                # All resources
                if effect_svc == "*":
                    if str(action) in effect_svc_resources_or_actions:
                        if len(effect_svc_resources_or_actions) > 1:
                            effect_svc_resources_or_actions.remove(str(action))
                        else:
                            deleted_effect_resources.append((effect, effect_svc))
                else:
                    # Service specific resources
                    deleted_effect_svc_resources = []

                    for effect_svc_resource, effect_svc_resource_actions in effect_svc_resources_or_actions.items():
                        if str(action) in effect_svc_resource_actions:
                            if len(effect_svc_resource_actions) > 1:
                                effect_svc_resource_actions.remove(str(action))
                            else:
                                deleted_effect_svc_resources.append(effect_svc_resource)

                    # Delete empty service specific resources and actions
                    for deleted_effect_svc_resource in deleted_effect_svc_resources:
                        effect_svc_resources_or_actions.pop(deleted_effect_svc_resource)

                    if not effect_svc_resources_or_actions:
                        deleted_effect_resources.append((effect, effect_svc))

        # Delete empty effect resources
        for deleted_effect_resource in deleted_effect_resources:
            self.__action_groups[deleted_effect_resource[0]].pop(deleted_effect_resource[1])

    def __action_grouping(self, effect, actions):
        if not self.__action_groups.get(effect, None):
            self.__action_groups[effect] = {}

        effect_group = self.__action_groups[effect]

        # Group actions according to effect and their defined resources
        for action in actions:
            # Validation for required resources
            action.__validate__()

            action_resource = action.__get_resources__()
            action_svc = action.__get_service__()

            self.__delete_previous_duplicate_actions(action)

            if action_resource == "*":
                if not effect_group.get(action_resource, None):
                    effect_group[action_resource] = []

                effect_group[action_resource].append(str(action))
            else:
                if not effect_group.get(action_svc, None):
                    effect_group[action_svc] = {}

                if not effect_group[action_svc].get(action_resource, None):
                    effect_group[action_svc][action_resource] = []

                effect_group[action_svc][action_resource].append(str(action))

    def __statement_creator(self, effect, actions):
        # Flattening actions
        actions = list(chain(*[[action] if not isinstance(action, list) else action for action in actions]))

        # Re-group actions before create statements
        self.__action_grouping(effect, actions)

        # Clear old statements
        self.__policy[self.__KEY_STATEMENT].clear()

        statement_no = 0

        # Generate statements according to groups
        for effect, effect_resources in self.__action_groups.items():
            for effect_svc, effect_svc_resources_or_actions in effect_resources.items():
                if effect_svc == "*":
                    self.__policy[self.__KEY_STATEMENT].append({
                        self.__KEY_SID: "CrescentStatement{}".format(statement_no),
                        self.__KEY_EFFECT: effect,
                        self.__KEY_ACTION: effect_svc_resources_or_actions,
                        self.__KEY_RESOURCE: effect_svc
                    })

                    statement_no += 1
                else:
                    for effect_svc_resource, effect_svc_resource_actions in effect_svc_resources_or_actions.items():
                        self.__policy[self.__KEY_STATEMENT].append({
                            self.__KEY_SID: "CrescentStatement{}".format(statement_no),
                            self.__KEY_EFFECT: effect,
                            self.__KEY_ACTION: effect_svc_resource_actions,
                            self.__KEY_RESOURCE: (
                                list(effect_svc_resource) if len(effect_svc_resource) > 1 else effect_svc_resource[0]
                            ) if isinstance(effect_svc_resource, list) else effect_svc_resource
                        })

                        statement_no += 1

        return self

    def AllowActions(self, *actions: Action):
        return self.__statement_creator(self.__EFFECT_ALLOW, list(actions))

    def DenyActions(self, *actions: Action):
        return self.__statement_creator(self.__EFFECT_DENY, list(actions))

    def Create(self):
        return self.__policy
