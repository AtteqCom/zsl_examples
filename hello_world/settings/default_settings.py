from zsl.application.modules.web.configuration import MethodConfiguration
from zsl.router.task import TaskConfiguration

RESOURCE_PACKAGE = ()
DATABASE_URI = 'postgresql://postgres:postgres@db/postgres'
DATABASE_ENGINE_PROPS = {}
SERVICE_INJECTION = ()
RELOAD = True
TASK_CONFIGURATION = TaskConfiguration()

METHOD = MethodConfiguration(package='api', url_prefix='api')
