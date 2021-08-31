"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi import automation as auto
import pulumi_azure_native as azure

PROJECT_NAME = "azure-python"
ENV_ORG = "dev"
stack_id = "SID-2886"
stack_name = "dev"

workspace = auto.LocalWorkspace(project_settings=auto.ProjectSettings(name=PROJECT_NAME, runtime="python"))
full_stack_name = auto.fully_qualified_stack_name(ENV_ORG, PROJECT_NAME, stack_id)

try:
    def pulumi_program():
        return create_pulumi_program()

    stack = auto.create_stack(stack_name=full_stack_name,
                              project_name=PROJECT_NAME,
                              program=pulumi_program)

except auto.StackNotFoundError:
    print("Stack Not Found")
except auto.ConcurrentUpdateError:
    print("Concurrent Update Error")


def create_pulumi_program():
    amap_provider = azure.Provider(resource_name="amap_provider")