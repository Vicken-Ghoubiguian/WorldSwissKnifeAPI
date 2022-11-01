#
from flask_restx import Namespace, Resource, inputs
from pycountry import countries

#
from commonFunctions import *

#
currentCountriesNamespace = Namespace('countries', description='Namespace to manipulate and get informations about all countries in the world...')

#
@currentCountriesNamespace.route('')
class CountriesList(Resource):

    #
    def get(self):

        """
        Get the list of all existing countries in the world...
        """

        #
        return getJSONOfCountries(list(pycountry.countries)), 200

#
@currentCountriesNamespace.route('/historical')
class HistoricalCountriesList(Resource):

    #
    def get(self):

        """
        Get the list of all ancient countries in the world...
        """

        #
        return getJSONOfHistoricalCountries(list(pycountry.historic_countries)), 200

#
parser_sort = reqparse.RequestParser()

#
parser_sort.add_argument('pattern', type=str, required=True, help='Fill in the pattern you want...')
parser_sort.add_argument('order', type=str, required=True, choices=["desc", "asc"], help='')

#
@currentCountriesNamespace.route('/sort/name')
@currentCountriesNamespace.expect(parser_sort)
class CountriesSortName(Resource):

    #
    def get(self):

        """
        Get the list of all ancient countries selected according a to pattern and sort according to an order...
        """

        #
        args = parser_sort.parse_args()

        #
        return getJSONofCountriesFromSort(field = "name", order = args.order, pattern = args["pattern"]), 200

#
@currentCountriesNamespace.route('/sort/alpha_2')
@currentCountriesNamespace.expect(parser_sort)
class CountriesSortAlpha2(Resource):

    #
    def get(self):

        """
        """

        #
        args = parser_sort.parse_args()

        #
        return getJSONofCountriesFromSort(field = "alpha_2", order = args.order, pattern = args["pattern"]), 200

#
@currentCountriesNamespace.route('/sort/alpha_3')
class CountriesSortAlpha3(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200

#
@currentCountriesNamespace.route('/historical/sort/name')
class HistoricalCountriesSortName(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200

#
@currentCountriesNamespace.route('/historical/sort/alpha_2')
class HistoricalCountriesSortAlpha2(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200

#
@currentCountriesNamespace.route('/historical/sort/alpha_3')
class HistoricalCountriesSortAlpha3(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200