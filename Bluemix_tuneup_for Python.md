The [Bluemix default Buildpack for Python](https://console.ng.bluemix.net/docs/runtimes/python) is often [several releases out-of-date](https://github.com/cloudfoundry/python-buildpack/releases) from the [Cloud Foundry Buildpack for Python](https://github.com/cloudfoundry/python-buildpack).  This means that your project will probably not have access to the latest CPython or pip builds.  To fix this, I do the following tweeks to modernize my default Bluemix Python projects:

1. Edit [manifest.yml](https://github.com/cclauss/platform_info/blob/master/manifest.yml) to add a `buildpack` line at the end:
    *  `buildpack: https://github.com/cloudfoundry/python-buildpack.git`
2. For Python 3 apps, I add a [runtime.txt](https://github.com/cclauss/platform_info/blob/master/runtime.txt) file at the root of the project which contains:
    * `python-3.6.0`

These changes will give your project access to the current [Cloud Foundery Buildpack for Python](https://github.com/cloudfoundry/python-buildpack) and the most current Cloud Foundry supported implementation of CPython2 or CPython3.
