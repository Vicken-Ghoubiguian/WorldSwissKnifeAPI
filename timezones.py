#
from flask_restx import Namespace, Resource, reqparse
from pytz import timezone, common_timezones, country_timezones

#
from commonFunctions import *

#
timezonesNamespace = Namespace('timezones', description='Namespace to manipulate and get some informations about timezones...')

#
parser_timezones_infos = reqparse.RequestParser()
parser_timezones_infos.add_argument('timezone', type=str, required=True, choices=getAllTimezones(), help='Select here the IANA (Internet Assigned Numbers Authority) timezone...')

#
@timezonesNamespace.route('/infos')
@timezonesNamespace.expect(parser_timezones_infos)
class TimezonesInfos(Resource):

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200

#
@timezonesNamespace.route('/byCountries')
class TimezonesByCountries(Resource):

    #
    def get(self):

        #
        args = parser_timezones_infos.parse_args()

        #
        return {
                    "timezone": args["timezone"],
                    "country": getCountry(args["timezone"]),
                    "TODO": "TODO"
                }, 200
