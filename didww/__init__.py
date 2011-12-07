import hashlib
from suds.client import Client


class Didww(object):

    def get_mapping(self, type, proto, detail, pref_server, itsp_id):
        return {
            'map_type' : type,
            'map_proto': proto,
            'map_detail': detail,
            'map_pref_server': pref_server,
            'map_itsp_id': itsp_id
        }


    def __init__(self, username, api_key, sandbox):
        """ initialise the DIDWW API
        @param username : didww username
        @param api_key  : didww api_key
        @param sandbox  : boolean
        """
        self.username = username

        if sandbox:
            self.url = 'https://sandbox2.didww.com/api2/?wsdl'
            self.auth_string = hashlib.sha1(username + api_key).hexdigest()

        else:
            self.auth_string = hashlib.sha1(username + api_key + 'sandbox').hexdigest()
            self.url = 'http://api.didww.com/api/?wsdl'

        self.client = Client(self.url)

    def get_regions(self, country_iso=None, city_prefix=None, last_request_gmt=None):
        """
        This method will return list of regions from DIDWW coverage list
        """
        return self.client.didww_getdidwwregions(auth_string=self.auth_string,
                           country_iso = country_iso,
                           city_prefix = city_prefix,
                           last_request_gmt = last_request_gmt)


    def get_pstn_rates(self, country_iso=None, pstn_prefix=None, last_request_gmt=None):
        """
        This method will return list of supported PSTN prefixes from DIDWW.
        """
        return self.client.didww_getdidwwpstnrates(auth_string = self.auth_string,
                                                   country_iso = country_iso,
                                                   pstn_prefix = pstn_prefix,
                                                   last_request_gmt = last_request_gmt)


    def check_pstn_number(self, pstn_number):
        """
        This method will validate a PSTN Number.
        """
        return self.client.didww_checkpstnnumber(auth_string = self.auth_string,
                                                 pstn_number = pstn_number)


    def order_create(self, customer_id, country_iso, city_prefix, period, map_data, prepaid_funds, uniq_hash, city_id):
        """
        This method will purchase new service
        """
        return self.client.didww_ordercreate(auth_string = self.auth_string,
                                             customer_id = customer_id,
                                             country_iso = country_iso,
                                             city_prefix = city_prefix,
                                             period = period,
                                             map_data = map_data,
                                             prepaid_funds = prepaid_funds,
                                             uniq_hash = uniq_hash,
                                             city_id = city_id)
