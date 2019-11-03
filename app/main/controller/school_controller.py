from flask_restplus import Resource
from ..service.school_service import SchoolServices
from ..util import school_swagger, schoolBaseResponse

schoolServices = SchoolServices()
school_NameSpace = school_swagger.namespace('school')


@school_NameSpace.route('')
class AllFields(Resource):
    """
    Retrieves all the school records without any filter applied
    """
    @school_NameSpace.doc(
        responses={404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description = "Retrieves all the school records without any filter applied")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self):
        return schoolServices.retrieve_all_school_details()


@school_NameSpace.route('/sortBy/<string:field>/forward')
class SortByField(Resource):
    """
    Retrieves school details sorted in forward order w.r.t the input field given
    """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description = "Retrieves school details sorted in forward order w.r.t the input field given")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, field):
        return schoolServices.retrieve_sorted_field(field,0)


@school_NameSpace.route('/sortBy/<string:field>/reverse')
class SortReverseByField(Resource):
    """
       Retrieves school details sorted in reverse order w.r.t the input field given
    """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description = "Retrieves school details sorted in reverse order w.r.t the input field given")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, field):
        return schoolServices.retrieve_sorted_field(field, 1)


@school_NameSpace.route('/searchby/schoolname/<string:value>')
class SearchBySchoolName(Resource):
    """
    Retrieves the school details w.r.t schoolname provided on mere search
    """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description = "Retrieves the school details w.r.t schoolname provided on mere search")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, value):
        return schoolServices.retrieve_by_field_value('schoolname',value)


@school_NameSpace.route('/searchby/address/<string:value>')
class SearchByAddress(Resource):
    """
        Retrieves the school details w.r.t address provided on mere search
    """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description="Retrieves the school details w.r.t address provided on mere search")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, value):
        return schoolServices.retrieve_by_field_value("address", value)


@school_NameSpace.route('/searchby/area/<string:value>')
class SearchByArea(Resource):
    """
        Retrieves the school details w.r.t area provided on mere search
        """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'})
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, value):
        return schoolServices.retrieve_by_field_value("area",value)


@school_NameSpace.route('/searchby/pincode/<int:value>')
class SearchByPincode(Resource):
    """
        Retrieves the school details w.r.t pincode provided on mere search
    """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description = " Retrieves the school details w.r.t pincode provided on mere search")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, value):
        return schoolServices.retrieve_by_field_value("pincode", value)


@school_NameSpace.route('/searchby/landmark/<string:value>')
class SearchByLandmark(Resource):
    """
            Retrieves the school details w.r.t landmark provided on mere search
        """
    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description = "Retrieves the school details w.r.t landmark provided on mere search")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, value):
        return schoolServices.retrieve_by_field_value("landmark", value)


@school_NameSpace.route('/searchby/field/<string:field>/value/<string:value>')
class SearchByLandmark(Resource):
    """
                Retrieves the school details w.r.t field and value provided on mere search
            """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description = "Retrieves the school details w.r.t field and value provided on mere search")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, field,value):
        return schoolServices.retrieve_by_field_value(field, value)


@school_NameSpace.route('/filterBy/<string:field>')
class FilterByLandmark(Resource):
    """
    Provides the unique values available w.r.t to the field  on all the school records fetched after each search operation
    """

    @school_NameSpace.doc(
        responses={412: 'INVALID INPUT', 404: 'NOT FOUND', 424: 'FAILED DEPENDENCY', 500: 'SERVER_ERROR'},
        description=" Provides the unique values available w.r.t to the field  on all the school records fetched "
                    "after each search operation")
    @school_NameSpace.response(200, 'OK', schoolBaseResponse)
    def get(self, field):
        return schoolServices.filter_by_field(field)