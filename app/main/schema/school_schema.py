from marshmallow import Schema, fields

class Schools(Schema):
    district= fields.Str()
    block= fields.Str(allow_none=True, required=False)
    cluster= fields.Str(allow_none=True, required=False)
    schoolid= fields.Str(allow_none=True, required=False)
    schoolname = fields.Str(allow_none=True, required=False)
    category= fields.Str(allow_none=True, required=False)
    gender = fields.Str(allow_none=True, required=False)
    medium_of_inst= fields.Str(allow_none=True, required=False)
    address = fields.Str(allow_none=True, required=False)
    area = fields.Str(allow_none=True, required=False)
    pincode= fields.Str(allow_none=True, required=False)
    landmark = fields.Str(allow_none=True, required=False)
    identification1 = fields.Str(allow_none=True, required=False)
    busroutes= fields.Str(allow_none=True, required=False)
    identification2 = fields.Str(allow_none=True, required=False)
    latlong= fields.Str(allow_none=True, required=False)