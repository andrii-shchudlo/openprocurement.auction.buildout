# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

import sys
sys.path[0:0] = [
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Paste-2.0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/PasteScript-2.0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/PasteDeploy-1.5.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/openprocurement.auction',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/openprocurement.auction.worker',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/openprocurement.auction.dutch',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/openprocurement.auth',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/CouchDB-1.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/circus-0.13.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/circus_web-1.0.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/gunicorn-19.3.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/ExtendedJournalHandler',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/request_id_middleware-0.1.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/penstock',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/nose-1.3.7-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/jarn.mkrelease-4.0.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pytest-3.1.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pytest_mock-1.6.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pytest_cov-2.5.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/openprocurement.auction.js',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/openprocurement.auction.dutch-js',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/mock-2.0.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/WebTest-2.0.27-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/chromedriver',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/robotframework_selenium2screenshots-0.7.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/robotframework_debuglibrary-0.8.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/robotframework_selenium2library-1.8.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/robotframework-2.9.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/walkabout-0.10-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/zope.interface-4.4.2-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/retrying-1.3.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/python_consul-0.7.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/openprocurement_client',
  '/usr/lib/python2.7/site-packages',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/ndg_httpsclient-0.4.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pyOpenSSL-0.15.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/barbecue',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/PyMemoize-1.0.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/restkit',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/PyYAML-3.11-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Flask_OAuthlib-0.8.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/sse-1.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/gevent-1.0.2-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/WSGIProxy2-0.4.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Flask_Redis-0.0.6-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Flask-0.10.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/python_dateutil-2.4.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/iso8601-0.1.10-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/APScheduler-3.0.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/requests-2.7.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/setuptools-11.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/WTForms_JSON-0.2.10-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/WTForms-2.0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/coverage-4.4.1-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/py-1.4.34-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/keyring-10.4.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/wheel-0.29.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/lazy-1.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/setuptools_git-1.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/setuptools_hg-0.4-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/setuptools_subversion-3.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/oslo.middleware-2.8.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/tomako-0.1.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/TornadIO2-0.0.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/tornado-4.2.1-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pyzmq-14.7.0-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/six-1.9.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/anyjson-0.3.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/MarkupSafe-0.23-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Mako-1.0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/psutil-3.2.1-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/iowait-0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Werkzeug-0.10.4-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Flask_SQLAlchemy-2.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pbr-1.7.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/funcsigs-1.0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/beautifulsoup4-4.6.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/waitress-1.0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/WebOb-1.4.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/selenium-3.4.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/python_magic-0.4.13-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/simplejson-3.8.0-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/munch-2.1.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/cryptography-1.9-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/src/rfc6266',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/socketpool-0.5.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/http_parser-0.8.3-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/oauthlib-1.0.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/greenlet-0.4.9-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/redis-2.10.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/itsdangerous-0.24-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Jinja2-2.9.6-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/futures-3.0.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/tzlocal-1.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pytz-2015.4-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/SecretStorage-2.3.1-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/stevedore-1.8.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/oslo.i18n-2.6.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/oslo.context-0.6.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/oslo.config-2.4.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/Babel-2.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/certifi-2015.9.6.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/backports.ssl_match_hostname-3.4.0.2-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/SQLAlchemy-1.0.8-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/cffi-1.7.0-py2.7-linux-x86_64.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/asn1crypto-0.22.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/LEPL-5.1.3-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/argparse-1.4.0-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/netaddr-0.7.18-py2.7.egg',
  '/data/andriis/Dutch/openprocurement.auction.buildout/eggs/pycparser-2.13-py2.7.egg',
  ]



import json
import contextlib
import os
import tempfile
import datetime
from dateutil.tz import tzlocal
from gevent.subprocess import check_output, sleep

PWD = os.path.dirname(os.path.realpath(__file__))
CWD = os.getcwd()

@contextlib.contextmanager
def update_auction_period():
    path = os.path.join("./src/openprocurement.auction/openprocurement/auction/tests/functional/data/tender_simple.json")
    with open(path) as file:
        data = json.loads(file.read())
    new_start_time = (datetime.datetime.now(tzlocal()) + datetime.timedelta(seconds=120)).isoformat()

    data['data']['auctionPeriod']['startDate'] = new_start_time

    with tempfile.NamedTemporaryFile(delete=False) as auction_file:
        json.dump(data, auction_file)
        auction_file.seek(0)
    yield auction_file.name
    auction_file.close()

def main():
  check_output('{0}/bin/circusd --daemon'.format(CWD).split())
  print "Circus is run..."
  print "Please wait..."
  with update_auction_period() as auction_file:
    check_output('{0}/bin/auction_worker planning {1}'
                 ' {0}/etc/auction_worker_dutch.yaml --planning_procerude partial_db --auction_info {2}'.format(CWD, "11111111111111111111111111111111", auction_file).split())
  sleep(10)
  print '='*100
  print u"To start the auction, enter the command"+"\n" \
        u" bin/auction_worker run 11111111111111111111111111111111 ./etc/auction_worker_defaults.yaml --planning_procerude partial_db --auction_info ./src/openprocurement.auction/openprocurement/auction/tests/functional/data/tender_simple.json"
  print '=' * 100


if __name__ == "__main__":
    main()
