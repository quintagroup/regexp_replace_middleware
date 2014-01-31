import re


class RegExpFilterHandler(object):
    """
    WSGI middleware for filter http response with regular expression
    """
    def __init__(self, application, pattern, relp):
        self.application = application
        self.pattern = pattern.decode("string-escape")
        self.relp = relp.decode("string-escape")
        self.active = False

    def __call__(self, environ, start_response):
        self.active = False

        def local_start_response(start_str, headers, exec_info=None):
            headers_dict = dict(headers)
            self.active = "text/html" in headers_dict.get("Content-Type", '')
            headers = [item for item in headers
                       if item[0].lower() != 'content-length' and self.active]
            return start_response(start_str, headers, exec_info)

        resp = self.application(environ, local_start_response)
        if self.active:
            resp = [re.sub(self.pattern, self.relp, item) for item in resp]
        return resp


def make_wsgi_middleware(app, global_conf, pattern, repl, **kw):
    """
    Config looks like this::

        [app:main]
        use = egg:Deliverance#proxy
        ## This is the site that is being wrapped:global_conf
        rule_filename = /projects/pt/buildouts/develpt/static/pt.xml
        filter-with = regexp_replace_middleware

        [filter:regexp_replace_middleware]
        use = egg:regexp_replace_middleware#regexp_replace_middleware
        pattern = (?P<pre_url><a.*href=[\'|"])(?P<url>noprefix://)(?P<post_url>\[[\w\s]+\][\'|"])
        repl = \g<pre_url>\g<post_url>
    """
    return RegExpFilterHandler(app, pattern, repl)
