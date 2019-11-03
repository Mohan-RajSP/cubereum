import logging
from ..schema import Schools
from ..util import dictionary_response, custom_response, overall_response, Constants, custom_log
from operator import itemgetter

logger = custom_log(__name__)

constants = Constants()


class SchoolServices:

    def __init__(self):

        schools = Schools()
        self.unique_dict = dict()
        self.school_details = list()
        json_url = "C:\\Users\\mohan.r.paramasivam\\OneDrive - Accenture\\WorkSpace-OneDrive\\Cubereum\\cubereum_school_service\\schools.json"
        jsonfile = open(json_url, 'r')
        for line in jsonfile:
            loaded_data = schools.loads(line, unknown="EXCLUDE")
            if loaded_data['schoolid'] !="" and loaded_data['schoolid'] != 'schoolid':
                self.school_details.append(loaded_data)
        self.school_details_copy = self.school_details
        jsonfile.close()


    @staticmethod
    def unique_field_values(school_list, field):
        try:

            logger.info(" unique_field_values || Entered Services")
            unique_fields = []
            for school in school_list:
                if school[field] not in unique_fields:
                    unique_fields.append(school[field])
            return unique_fields

        except Exception as err:
            logger.exception("unique_field_values || Exception occured || {}".format(err))
            return overall_response(424, constants.FAILURE_MSG )

    def unique_values(self):
        self.unique_dict = {"category": self.unique_field_values(self.school_details, "category"),
                            "gender": self.unique_field_values(self.school_details, "gender"),
                            "medium_of_inst": self.unique_field_values(self.school_details, "medium_of_inst")}

    def filter_by_field(self, field):
        try:

            logger.info(" filter_by_field || Entered Services")
            if self.unique_dict :
                out = dictionary_response(200, "RETRIEVED")
                out[field] = self.unique_dict[field]
                return custom_response(out)
            else:
                self.unique_dict = {"category": self.unique_field_values(self.school_details, "category"),
                                    "gender": self.unique_field_values(self.school_details, "gender"),
                                    "medium_of_inst": self.unique_field_values(self.school_details, "medium_of_inst")}

                out = dictionary_response(200, "RETRIEVED")
                out[field] = self.unique_dict[field]
                return custom_response(out)

        except KeyError as kerr:
            logger.exception(" filter_by_field || Exception Occured || {}".format(kerr))
            return overall_response(412, constants.KEY_ERROR_MSG)

        except Exception as err:
            logger.exception(" filter_by_field || Exception Occured || {}".format(err))
            return overall_response(424, constants.FAILURE_MSG)

    def retrieve_all_school_details(self):
        try:

            logger.info(" retrieve_by_field_value || Entered Services")
            out = dictionary_response(200, "RETRIEVED")
            if len(self.school_details_copy) ==0:
                return overall_response(404, "Record Not found")
            out["schoolDetails"] = self.school_details_copy
            self.unique_values()
            return custom_response(out)

        except Exception as err:
            logger.exception(" retrieve_by_field_value || Exception Occured || {}".format(err))
            return overall_response(424, constants.FAILURE_MSG)

    def retrieve_sorted_field(self, field, rev):
        try:

            logger.info(" retrieve_by_field_value || Entered Services")
            if rev == 0:
                self.school_details = sorted(self.school_details_copy, key=itemgetter(field))
            elif rev == 1:
                self.school_details = sorted(self.school_details_copy, key=itemgetter(field), reverse=True)
            self.unique_values()
            if len(self.school_details) ==0:
                return overall_response(404, "Record Not found")
            out = dictionary_response(200, "RETRIEVED")
            out["schoolDetails"] = self.school_details
            return custom_response(out)

        except Exception as err:
            logger.exception(" retrieve_by_field_value || Exception Occured || {}".format(err))
            return overall_response(424, constants.FAILURE_MSG)

    def retrieve_by_field_value(self, field, value):
        try:

            logger.info(" retrieve_by_field_value || Entered Services")
            if type(value) is str:
                self.school_details = eval("[school for school in self.school_details_copy if school['{0}'] and "
                                       "'{1}' in school['{0}']]".format(field.strip(), value.strip()))
            elif type(value) is int:
                self.school_details = eval("[school for school in self.school_details_copy if school['{0}'] and "
                                           "school['{0}']== str({1})]".format(field.strip(), value))
            self.unique_values()
            if len(self.school_details) == 0:
                return overall_response(404, "Record Not found")
            out = dictionary_response(200, "RETRIEVED")
            out["schoolDetails"] = self.school_details
            return custom_response(out)

        except Exception as err:
            logger.exception(" retrieve_by_field_value || Exception Occured || {}".format(err))
            return overall_response(424, constants.FAILURE_MSG)




