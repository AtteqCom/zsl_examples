from zsl.router import method
from zsl.task.task_decorator import json_output


@method.route('/hello/<x>')
@json_output
def hello(x):
    return {"message": f"Hello World for {x}!"}
