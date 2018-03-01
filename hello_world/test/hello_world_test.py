from unittest import TestCase

from flask import json
from zsl.application.containers.web_container import WebContainer
from zsl.application.modules.context_module import DefaultContextModule
from zsl.application.modules.error_handler_module import ErrorHandlerModule
from zsl.application.modules.logger_module import LoggerModule
from zsl.application.modules.task_router import TaskRouterModule
from zsl.application.modules.web.configuration import MethodConfiguration
from zsl.application.modules.web.web_context_module import WebContextModule
from zsl.interface.web.performers.method import call_exposers_in_method_packages
from zsl.router.method import METHOD_CONFIG_NAME
from zsl.testing.http import HTTPTestCase
from zsl.testing.zsl import ZslTestCase, ZslTestConfiguration


class TestContainer(WebContainer):
    logger = LoggerModule
    context = DefaultContextModule
    task_router = TaskRouterModule
    error_handler = ErrorHandlerModule
    web_context = WebContextModule


class TestHelloWorld(ZslTestCase, TestCase, HTTPTestCase):
    ZSL_TEST_CONFIGURATION = ZslTestConfiguration(
        app_name="hello-world-zsl-test-app",
        profile='test',
        container=TestContainer,
        config_object={
            METHOD_CONFIG_NAME: MethodConfiguration(package='api', url_prefix='api')
        }
    )

    @classmethod
    def setUpClass(cls):
        super(TestHelloWorld, cls).setUpClass()
        call_exposers_in_method_packages()

    def test_hello_world(self):
        with self.getHTTPClient() as client:
            response = client.get("/api/hello/John")
            data = response.data.decode()
            data = json.loads(data)
            self.assertEqual(data, {"message": "Hello World for John!"}, "Response must be correct.")
