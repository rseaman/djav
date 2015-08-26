import urllib2
import json

# Known bad: 69.43.161.174
# Known good: 8.8.8.8
# Find more examples at https://www.alienvault.com/open-threat-exchange/dashboard


class IPDetails(object):
    def __init__(self, *args, **kwargs):
        ip                  = args[0]
        self.address        = ip
        self.is_valid       = False
        self.reputation_val = 0
        self._id            = {}
        self._id['$id']     = ''
        self.first_activity = None
        self.last_activity  = None
        self.activities     = []
        self.activity_types = []

        # Pull raw details
        raw = Reputation.get_details(ip)

        # JSONify details
        if raw is '':
            # Blank item, return partial object
            return
        else:
            raw_dict = json.loads(raw)
            self.is_valid = True

        # Assign values to object
        for k, v in raw_dict.items():
            setattr(self, k, v)

        # Set for enumeration of activity types
        self.activity_types = set()


        # Aggregate activity_types from activities and dates where appropriate
        if 'activities' in raw_dict:
            # Get earliest and latest values from activities where available
            earliest_list = []
            latest_list   = []
            for data in raw_dict['activities']:
                data['activity_type'] = data['name']
                self.activity_types.add(data['name'])
                del data['name']
                if 'first_date' in data:
                    earliest_list.append(data['first_date']['sec'])
                    latest_list.append(data['last_date']['sec'])
                    data['first_date'] = data['first_date']['sec']
                    data['last_date']  = data['last_date']['sec']
            self.first_activity = min(earliest_list)
            self.last_activity  = min(latest_list)


        return


class Reputation(object):
    @staticmethod
    def get_details(ip):
        if ip:
            try:
                # Fetch raw results from source
                url = "http://reputation.alienvault.com/panel/ip_json.php?ip=%s" % (ip)
                return urllib2.urlopen(url).read()
            except:
                return "fetch_error"
        else:
            return None
