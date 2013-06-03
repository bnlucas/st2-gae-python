import sublime, sublime_plugin

import os

from threading import Thread

json = None
try:
	import simplejson as json
except ImportError:
	import json

def load_settings(path):
	try:
		with open(os.sep.join([path, '.gaedevserver-settings']), 'r') as f:
			content = f.read()
		return json.loads(content)
	except:
		sublime.error_message('No .gaedevserver-settings found.')
		return False

class StartGaeDevServerCommand(sublime_plugin.WindowCommand):

	def run(self, paths=[]):
		if len(paths) > 0:
			path = paths[0]

			settings = load_settings(path)
			if settings:
				server = os.sep.join([settings['sdk_path'], 'dev_appserver.py'])

				args = []
				for key, value in settings['options'].items():
					if value:
						if isinstance(value, bool):
							args.append(key)
						else:
							args.append('{k}={v}'.format(k=key, v=value))
				args.append(path)
				args = ' '.join(args)

				cmd = 'python {s} {a}'.format(s=server, a=args)

				Thread(target=os.system, args=[cmd]).start()

				print 'Started: {c}'.format(c=cmd)