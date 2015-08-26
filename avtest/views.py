import random

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from serializers import *
from datetime import datetime, timedelta
from models import User, Visit
from threat import *


class APIRoot(APIView):
    def get(self, request):
        return Response({
            'IP Details': reverse('threat_details', request=request),
        })


class IPDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        ip = kwargs['ip']

        # User's source address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            user_addr = x_forwarded_for.split(',')[0]
        else:
            user_addr = request.META.get('REMOTE_ADDR')

        # Generate IPDetails object for serialization
        details_request = IPDetails(ip, *args, **kwargs)

        # Serialize object
        result = DetailsSerializer(details_request)

        response = Response(result.data, status=status.HTTP_200_OK)

        # Set UTC time
        current_datetime = datetime.utcnow()
        epoch            = int((current_datetime - datetime(1970, 1, 1)).total_seconds())
        expires          = addYear(current_datetime, 1)

        # Handle Cookies
        if 'alienvaultid' in request.COOKIES:
            avid = request.COOKIES['alienvaultid']

            response.set_cookie('last_visit', epoch, expires=expires)

        else:
            # Didn't find cookie, set one.
            avid = ''.join(["%s" % random.randint(0, 9)
                           for num in range(0, 11)])
            response.set_cookie('alienvaultid', avid, expires=expires)
            response.set_cookie('last_visit', epoch, expires=expires)

        user = User(alienvaultid=avid)
        user.save()

        visit = Visit(user=user,
                      address=user_addr,
                      timestamp=epoch,
                      endpoint=kwargs['endpoint'] + ip)
        visit.save()

        return response


class Traffic(APIView):
    def get(self, request, *args, **kwargs):
        users    = User.objects.all()
        data     = []
        idx    = None

        for user in users:
            idx = None
            # Find index of user in data
            for i, j in enumerate(data):
                if user.alienvaultid in j['alienvaultid']:
                    idx = i

            # Found a user in list
            if idx is not None:
                # Add visits to existing user's visits list
                for v in user.visit_set.all():
                    data[idx]['visits'].append(json.loads(str(v)))
            # New user in list
            else:
                tmp_dict = {'alienvaultid': user.alienvaultid}
                tmp_dict['visits'] = []
                for v in user.visit_set.all():
                    tmp_dict['visits'].append(json.loads(str(v)))
                data.append(tmp_dict)

        data = sorted(data, key=lambda k: k['alienvaultid'])

        response = Response(data)

        return response


##############################################################################
def addYear(date, year):
    """
    Takes a datetime object and adds years to it.
    """

    result = date + timedelta(366 * year)

    if year > 0:
        while result.year - date.year > year or date.month < result.month or date.day < result.day:
            result += timedelta(-1)
    elif year < 0:
        while result.year - date.year < year or date.month > result.month or date.day > result.day:
            result += timedelta(1)

    return result