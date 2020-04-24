# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analyze.proto

import template_pb2 as template__pb2
import common_pb2 as common__pb2
from google.protobuf import descriptor_pb2
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
from google.protobuf import descriptor as _descriptor
import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor.FileDescriptor(
    name='analyze.proto',
    package='types',
    syntax='proto3',
    serialized_pb=_b('\n\ranalyze.proto\x12\x05types\x1a\x0c\x63ommon.proto\x1a\x0etemplate.proto\"m\n\x11\x41nalyzeApiRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x19\n\x11\x61nalyzeTemplateId\x18\x02 \x01(\t\x12/\n\x0f\x61nalyzeTemplate\x18\x03 \x01(\x0b\x32\x16.types.AnalyzeTemplate\">\n\nRecognizer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x65ntities\x18\x02 \x03(\t\x12\x10\n\x08language\x18\x03 \x01(\t\"O\n\x0e\x41nalyzeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12/\n\x0f\x61nalyzeTemplate\x18\x02 \x01(\x0b\x32\x16.types.AnalyzeTemplate\"R\n\x0f\x41nalyzeResponse\x12,\n\x0e\x61nalyzeResults\x18\x01 \x03(\x0b\x32\x14.types.AnalyzeResult\x12\x11\n\trequestId\x18\x02 \x01(\t\")\n\x15RecognizersAllRequest\x12\x10\n\x08language\x18\x03 \x01(\t\"F\n\x16RecognizersAllResponse\x12,\n\x11recognizerResults\x18\x01 \x03(\x0b\x32\x11.types.Recognizer2\x9e\x01\n\x0e\x41nalyzeService\x12\x38\n\x05\x41pply\x12\x15.types.AnalyzeRequest\x1a\x16.types.AnalyzeResponse\"\x00\x12R\n\x11GetAllRecognizers\x12\x1c.types.RecognizersAllRequest\x1a\x1d.types.RecognizersAllResponse\"\x00\x62\x06proto3'),
    dependencies=[common__pb2.DESCRIPTOR, template__pb2.DESCRIPTOR, ])



_ANALYZEAPIREQUEST = _descriptor.Descriptor(
    name='AnalyzeApiRequest',
    full_name='types.AnalyzeApiRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='text', full_name='types.AnalyzeApiRequest.text', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='analyzeTemplateId', full_name='types.AnalyzeApiRequest.analyzeTemplateId', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='analyzeTemplate', full_name='types.AnalyzeApiRequest.analyzeTemplate', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=54,
    serialized_end=163,
)


_RECOGNIZER = _descriptor.Descriptor(
    name='Recognizer',
    full_name='types.Recognizer',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='types.Recognizer.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='entities', full_name='types.Recognizer.entities', index=1,
            number=2, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='language', full_name='types.Recognizer.language', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=165,
    serialized_end=227,
)


_ANALYZEREQUEST = _descriptor.Descriptor(
    name='AnalyzeRequest',
    full_name='types.AnalyzeRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='text', full_name='types.AnalyzeRequest.text', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='analyzeTemplate', full_name='types.AnalyzeRequest.analyzeTemplate', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=229,
    serialized_end=308,
)


_ANALYZERESPONSE = _descriptor.Descriptor(
    name='AnalyzeResponse',
    full_name='types.AnalyzeResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='analyzeResults', full_name='types.AnalyzeResponse.analyzeResults', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='requestId', full_name='types.AnalyzeResponse.requestId', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=310,
    serialized_end=392,
)


_RECOGNIZERSALLREQUEST = _descriptor.Descriptor(
    name='RecognizersAllRequest',
    full_name='types.RecognizersAllRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='language', full_name='types.RecognizersAllRequest.language', index=0,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=394,
    serialized_end=435,
)


_RECOGNIZERSALLRESPONSE = _descriptor.Descriptor(
    name='RecognizersAllResponse',
    full_name='types.RecognizersAllResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='recognizerResults', full_name='types.RecognizersAllResponse.recognizerResults', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=437,
    serialized_end=507,
)

_ANALYZEAPIREQUEST.fields_by_name['analyzeTemplate'].message_type = template__pb2._ANALYZETEMPLATE
_ANALYZEREQUEST.fields_by_name['analyzeTemplate'].message_type = template__pb2._ANALYZETEMPLATE
_ANALYZERESPONSE.fields_by_name['analyzeResults'].message_type = common__pb2._ANALYZERESULT
_RECOGNIZERSALLRESPONSE.fields_by_name['recognizerResults'].message_type = _RECOGNIZER
DESCRIPTOR.message_types_by_name['AnalyzeApiRequest'] = _ANALYZEAPIREQUEST
DESCRIPTOR.message_types_by_name['Recognizer'] = _RECOGNIZER
DESCRIPTOR.message_types_by_name['AnalyzeRequest'] = _ANALYZEREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeResponse'] = _ANALYZERESPONSE
DESCRIPTOR.message_types_by_name['RecognizersAllRequest'] = _RECOGNIZERSALLREQUEST
DESCRIPTOR.message_types_by_name['RecognizersAllResponse'] = _RECOGNIZERSALLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalyzeApiRequest = _reflection.GeneratedProtocolMessageType('AnalyzeApiRequest', (_message.Message,), dict(
    DESCRIPTOR=_ANALYZEAPIREQUEST,
    __module__='analyze_pb2'
    # @@protoc_insertion_point(class_scope:types.AnalyzeApiRequest)
))
_sym_db.RegisterMessage(AnalyzeApiRequest)

Recognizer = _reflection.GeneratedProtocolMessageType('Recognizer', (_message.Message,), dict(
    DESCRIPTOR=_RECOGNIZER,
    __module__='analyze_pb2'
    # @@protoc_insertion_point(class_scope:types.Recognizer)
))
_sym_db.RegisterMessage(Recognizer)

AnalyzeRequest = _reflection.GeneratedProtocolMessageType('AnalyzeRequest', (_message.Message,), dict(
    DESCRIPTOR=_ANALYZEREQUEST,
    __module__='analyze_pb2'
    # @@protoc_insertion_point(class_scope:types.AnalyzeRequest)
))
_sym_db.RegisterMessage(AnalyzeRequest)

AnalyzeResponse = _reflection.GeneratedProtocolMessageType('AnalyzeResponse', (_message.Message,), dict(
    DESCRIPTOR=_ANALYZERESPONSE,
    __module__='analyze_pb2'
    # @@protoc_insertion_point(class_scope:types.AnalyzeResponse)
))
_sym_db.RegisterMessage(AnalyzeResponse)

RecognizersAllRequest = _reflection.GeneratedProtocolMessageType('RecognizersAllRequest', (_message.Message,), dict(
    DESCRIPTOR=_RECOGNIZERSALLREQUEST,
    __module__='analyze_pb2'
    # @@protoc_insertion_point(class_scope:types.RecognizersAllRequest)
))
_sym_db.RegisterMessage(RecognizersAllRequest)

RecognizersAllResponse = _reflection.GeneratedProtocolMessageType('RecognizersAllResponse', (_message.Message,), dict(
    DESCRIPTOR=_RECOGNIZERSALLRESPONSE,
    __module__='analyze_pb2'
    # @@protoc_insertion_point(class_scope:types.RecognizersAllResponse)
))
_sym_db.RegisterMessage(RecognizersAllResponse)


_ANALYZESERVICE = _descriptor.ServiceDescriptor(
    name='AnalyzeService',
    full_name='types.AnalyzeService',
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=510,
    serialized_end=668,
    methods=[
        _descriptor.MethodDescriptor(
            name='Apply',
            full_name='types.AnalyzeService.Apply',
            index=0,
            containing_service=None,
            input_type=_ANALYZEREQUEST,
            output_type=_ANALYZERESPONSE,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='GetAllRecognizers',
            full_name='types.AnalyzeService.GetAllRecognizers',
            index=1,
            containing_service=None,
            input_type=_RECOGNIZERSALLREQUEST,
            output_type=_RECOGNIZERSALLRESPONSE,
            options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_ANALYZESERVICE)

DESCRIPTOR.services_by_name['AnalyzeService'] = _ANALYZESERVICE

# @@protoc_insertion_point(module_scope)
