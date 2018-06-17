# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request.proto',
  package='request',
  serialized_pb='\n\rrequest.proto\x12\x07request\"\xb7\x01\n\x07Request\x12%\n\x05inner\x18\x01 \x02(\x0b\x32\x16.request.Request.Inner\x12\x0b\n\x03\x64ig\x18\x02 \x02(\x0c\x12\x0b\n\x03sig\x18\x03 \x02(\x0c\x12\r\n\x05outer\x18\x04 \x01(\x0c\x1a\\\n\x05Inner\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0b\n\x03seq\x18\x02 \x02(\x05\x12\x0c\n\x04view\x18\x03 \x02(\x05\x12\x0c\n\x04type\x18\x04 \x02(\t\x12\x0b\n\x03msg\x18\x05 \x02(\x0c\x12\x11\n\ttimestamp\x18\x06 \x01(\x05\"(\n\x07History\x12\x1d\n\x03req\x18\x01 \x03(\x0b\x32\x10.request.Request')




_REQUEST_INNER = _descriptor.Descriptor(
  name='Inner',
  full_name='request.Request.Inner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='request.Request.Inner.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq', full_name='request.Request.Inner.seq', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view', full_name='request.Request.Inner.view', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='request.Request.Inner.type', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='request.Request.Inner.msg', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='request.Request.Inner.timestamp', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=118,
  serialized_end=210,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='request.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inner', full_name='request.Request.inner', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dig', full_name='request.Request.dig', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sig', full_name='request.Request.sig', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outer', full_name='request.Request.outer', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_INNER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=27,
  serialized_end=210,
)


_HISTORY = _descriptor.Descriptor(
  name='History',
  full_name='request.History',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='request.History.req', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=212,
  serialized_end=252,
)

_REQUEST_INNER.containing_type = _REQUEST;
_REQUEST.fields_by_name['inner'].message_type = _REQUEST_INNER
_HISTORY.fields_by_name['req'].message_type = _REQUEST
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['History'] = _HISTORY

class Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Inner(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _REQUEST_INNER

    # @@protoc_insertion_point(class_scope:request.Request.Inner)
  DESCRIPTOR = _REQUEST

  # @@protoc_insertion_point(class_scope:request.Request)

class History(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HISTORY

  # @@protoc_insertion_point(class_scope:request.History)


# @@protoc_insertion_point(module_scope)
