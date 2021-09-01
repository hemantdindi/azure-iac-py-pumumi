import pulumi
import pulumi.automation as auto
from pulumi_azure_native import resources
from pulumi import Output
import sys, json


def pulumi_program():
    resource_group = resources.ResourceGroup("hemant-rg2")
    pulumi.export("stack_output", resource_group.name)

PROJECT_NAME    = "azure-python"
STACK_NAME      = "dev"

stack = auto.create_or_select_stack(stack_name      = STACK_NAME    ,
                                    project_name    = PROJECT_NAME  ,
                                    program         = pulumi_program
                                    )

stack.workspace.install_plugin("azure", "4.11.0")
stack.set_config("azure-native:location", auto.ConfigValue(value="southindia"))

destroy = False
args = sys.argv[1:]
if len(args) > 0:
    if args[0] == "destroy":
        destroy = True

if destroy:
    print("destroying stack...")
    stack.destroy(on_output=print)
    print("stack destroy complete")
    sys.exit()
try:
    up_res = stack.up(on_output=print)
    print("Created the Resource Group : " ,list(up_res.outputs.values())[0])

except Exception as e:
    print("Encounterd an exception : ", e)
