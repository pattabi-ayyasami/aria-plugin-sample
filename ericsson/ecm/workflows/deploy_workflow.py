from aria import workflow
from aria.orchestrator.workflows.api import task
from aria.orchestrator.workflows.exceptions import TaskException


INTERFACE_NAME = 'Custom'
DEPLOY_OPERATION_NAME = 'deploy'

@workflow
def deploy(ctx, graph):
    """
    Custom workflow to call the operations on the Deploy interface.
    """
    print "Inside the deploy workflow"
    for node in ctx.model.node.iter():
        try:
            graph.add_tasks(task.OperationTask(node,
                            interface_name=INTERFACE_NAME,
                            operation_name=DEPLOY_OPERATION_NAME))
        except TaskException:
            pass
