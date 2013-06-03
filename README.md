GAE.py
======

GAE.py is a set of side-menu commands in Sublime Text 2 for interacting with the
Google App Engine SDK. Currently, there is support for starting the GAE app dev
server with all command-line options configured in a `.gaedevserver-settings`
file stored in the app's root directory.

Coming Soon
-----------

There will be a command for interaction with the appcfg.py file to push/get app
resources from the GAE environment.

Use
---

* Create .gaedevserver-settings files with ease
  * Right-click your app folder in the side bar.

The .gaedevserver-settings file
============================
```json
{
	"sdk_path":						"/path/to/gae/python/sdk",
	"options": {
		"--host":					null,
		"--port":					null,
		"--admin_host":				null,
		"--admin_port":				null,
		"--auto_id_policy":			null,
		"--clear_datastore":		null,
		"--datastore_path":			null,
		"--storage_path":			null,
		"--logs_path":				null,
		"--log_level":				null,
		"--require_indexes":		null,
		"--enable_sendmail":		false,
		"--smtp_host":				null,
		"--smtp_post":				null,
		"--smtp_user":				null,
		"--smtp_password":			null,
		"--php_executable_path":	null,
		"--php_remote_debugging":	null
	}
}
```