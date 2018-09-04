1. $ python --version

Python 3.6.5 :: Anaconda, Inc.

2. $ virtualenv analytics

-bash: virtualenv: command not found

3. $ pip install virtualenv

Collecting virtualenv
  Downloading https://files.pythonhosted.org/packages/b6/30/96a02b2287098b23b875bc8c2f58071c35d2efe84f747b64d523721dc2b5/virtualenv-16.0.0-py2.py3-none-any.whl (1.9MB)
    100% |████████████████████████████████| 1.9MB 1.1MB/s
distributed 1.21.8 requires msgpack, which is not installed.
Installing collected packages: virtualenv
Successfully installed virtualenv-16.0.0

4. $ virtualenv analytics

Using base prefix '/anaconda3'
New python executable in /Users/weshop.dev/analytics/bin/python
Installing setuptools, pip, wheel...done.


5. $ cd analytics/
6. $ source bin/activate

(analytics) weshopdev:analytics weshop.dev$ pip install flask peewee
Collecting flask
  Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
    100% |████████████████████████████████| 92kB 716kB/s
Collecting peewee


7. $ pip install gevent

Collecting gevent
  Downloading https://files.pythonhosted.org/packages/2b/a9/7c38605b9672a6ede6ccf822a645fdeec0c80fb467c87c5ce4976e4056dd/gevent-1.3.6-cp36-cp36m-macosx_10_6_intel.whl (3.1MB)
    100% |████████████████████████████████| 3.1MB 979kB/s

8. $ vi analytics.py

9. $ DEBUG=1 python analytics.py
 * Serving Flask app "analytics" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 258-079-966


10. $ pip install peewee


11. Code Intergrate :  <script src="http://127.0.0.1:5000/a.js" type="text/javascript"></script>


12. ImportError: No module named flask
    pip install flask

13. File "analytics.py", line 5, in <module>
    from urllib.parse   import parse_qsl, urlparse
    ImportError: No module named pars
    ------change code ----------
    from urllib.parse   import parse_qsl, urlparse
    --->
    from urlparse   import parse_qsl, urlparse