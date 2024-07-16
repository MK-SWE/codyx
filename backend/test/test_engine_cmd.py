import unittest
from unittest import TestCase, mock
from io import StringIO
from engine.engine_cmd import terminal

class TestTerminal(TestCase):

    def setUp(self):
        self.terminal = terminal()
        self.output = StringIO()

    def tearDown(self):
        self.output.close()

    def test_do_exit(self):
        self.assertTrue(self.terminal.do_exit(''))

    def test_do_help(self):
        with mock.patch('sys.stdout', self.output):
            self.assertIsNone(self.terminal.do_help(''))

    def test_do_new(self):
        with mock.patch('sys.stdout', self.output):
            self.terminal.do_new('')
            self.assertIn('ContainerID is', self.output.getvalue())

    def test_do_ls_no_containers(self):
        with mock.patch('sys.stdout', self.output):
            self.terminal.do_ls('')
            self.assertIn('*** No container available ***', self.output.getvalue())

    def test_do_ls_with_containers(self):
        with mock.patch('sys.stdout', self.output):
            with mock.patch('engine_cmd.DOCKER.get_containers', return_value=['container1', 'container2']):
                self.terminal.do_ls('')
                self.assertIn('1) container1', self.output.getvalue())
                self.assertIn('2) container2', self.output.getvalue())

    def test_do_rm_missing_containerID(self):
        with mock.patch('sys.stdout', self.output):
            self.terminal.do_rm('')
            self.assertIn('*** Missing containerID ***', self.output.getvalue())

    def test_do_rm_success(self):
        with mock.patch('sys.stdout', self.output):
            with mock.patch('engine_cmd.DOCKER.remove_container', return_value=True):
                self.terminal.do_rm('containerID')
                self.assertIn('*** removed containerID ***', self.output.getvalue())

    def test_do_echo(self):
        with mock.patch('sys.stdout', self.output):
            with mock.patch('engine_cmd.DOCKER.get_one', return_value='container_name'):
                self.terminal.do_echo('containerID')
                self.assertIn('*** Container with id containerID is container_name***', self.output.getvalue())

    def test_do_rebase(self):
        with mock.patch('engine_cmd.DOCKER.rebase') as mock_rebase:
            self.terminal.do_rebase('')
            mock_rebase.assert_called_once()

    def test_do_refresh(self):
        with mock.patch('engine_cmd.DOCKER.refresh_containers') as mock_refresh:
            self.terminal.do_refresh('')
            mock_refresh.assert_called_once()
if __name__ == '__main__':
    unittest.main()
