import pytest
from mailchimp3 import MailChimp
from utilities.BaseClass import BaseClass


class TestApi(BaseClass):
    @pytest.mark.run(order=4)
    def testPullData(self):
        log = self.getLogger()
        client = MailChimp(mc_api='2d5ea34bcef6b8948883d38d82727366-us17', mc_user='huqxsbrcekec@emergentvillage.org')

        expected_mail = 'hshs@sarkarripon.com'
        actual_list = client.lists.members.all('80e1a0fab7', count=100, offset=0, fields="members.email_address")

        membersArray = actual_list['members'][-1]['email_address']
        assert membersArray == expected_mail
        log.info("Hurray! API test passed. Obtained email is: "+membersArray)





