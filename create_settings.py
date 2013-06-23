import sublime, sublime_plugin

import os

skeleton = '''{
	"sdk_path":				"/path/to/gae/python/sdk",
	"options": {
		"--host":			null,
		"--port":			null,
		"--admin_host":			null,
		"--admin_port":			null,
		"--auto_id_policy":		null,
		"--clear_datastore":		null,
		"--datastore_path":		null,
		"--storage_path":		null,
		"--logs_path":			null,
		"--log_level":			null,
		"--require_indexes":		null,
		"--enable_sendmail":		false,
		"--smtp_host":			null,
		"--smtp_post":			null,
		"--smtp_user":			null,
		"--smtp_password":		null,
		"--php_executable_path":	null,
		"--php_remote_debugging":	null
	}
}'''

class CreatePythonGaeDevSettingsCommand(sublime_plugin.WindowCommand):

	def run(self, paths=[]):
		if len(paths) > 0:
			if os.path.isdir(paths[0]):
				filename = os.path.join(paths[0], '.gaedevserver-settings')

				if not os.path.exists(filename):
					with open(filename, 'w+') as f:
						f.write(skeleton)

				view = self.window.open_file(filename)
				view.set_syntax_file('Packages/Javascript/JSON.tmLanguage')
		else:
			view = self.window.new_file()
			view.settings().set('default_dir', self.window.folders()[0])
			view.set_syntax_file('Packages/Javascript/JSON.tmLanguage')
			view.set_name('.gaedevserver-settings')

			skeleton.replace('/path/to/gae/python/sdk',
				'${1:/path/to/gae/python/sdk}')
			view.run_command('insert_snippet', {'contents': skeleton})
