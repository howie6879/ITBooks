import random
import os


class HeadersMiddleware():
    """
    Add headers before request
    """

    def process_request(self, request, spider):
        user_agent = self.get_random_user_agent()
        request.headers['User-Agent'] = user_agent
        spider.logger.info(u'User-Agent is : {} {}'.format(
            request.headers.get('User-Agent'), request))

    def get_random_user_agent(self):
        """
        Generate a random user_agent
        :return: user_agent
        """
        # Default user agent
        USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
        # Load the list of valid user agents from the data dir.
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        try:
            with open(os.path.join(path, 'user_agents.txt')) as fp:
                user_agents_list = [_.strip() for _ in fp.readlines()]
        except Exception:
            user_agents_list = [USER_AGENT]
        return random.choice(user_agents_list)
