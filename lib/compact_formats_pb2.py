# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compact_formats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ompact_formats.proto\x12\x15pirate.wallet.sdk.rpc\"\xa1\x01\n\x0c\x43ompactBlock\x12\x14\n\x0cprotoVersion\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0c\n\x04hash\x18\x03 \x01(\x0c\x12\x10\n\x08prevHash\x18\x04 \x01(\x0c\x12\x0c\n\x04time\x18\x05 \x01(\r\x12\x0e\n\x06header\x18\x06 \x01(\x0c\x12-\n\x03vtx\x18\x07 \x03(\x0b\x32 .pirate.wallet.sdk.rpc.CompactTx\"\xed\x01\n\tCompactTx\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x0b\n\x03\x66\x65\x65\x18\x03 \x01(\r\x12:\n\x06spends\x18\x04 \x03(\x0b\x32*.pirate.wallet.sdk.rpc.CompactSaplingSpend\x12<\n\x07outputs\x18\x05 \x03(\x0b\x32+.pirate.wallet.sdk.rpc.CompactSaplingOutput\x12<\n\x07\x61\x63tions\x18\x06 \x03(\x0b\x32+.pirate.wallet.sdk.rpc.CompactOrchardAction\"!\n\x13\x43ompactSaplingSpend\x12\n\n\x02nf\x18\x01 \x01(\x0c\"D\n\x14\x43ompactSaplingOutput\x12\x0b\n\x03\x63mu\x18\x01 \x01(\x0c\x12\x0b\n\x03\x65pk\x18\x02 \x01(\x0c\x12\x12\n\nciphertext\x18\x03 \x01(\x0c\"`\n\x14\x43ompactOrchardAction\x12\x11\n\tnullifier\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63mx\x18\x02 \x01(\x0c\x12\x14\n\x0c\x65phemeralKey\x18\x03 \x01(\x0c\x12\x12\n\nciphertext\x18\x04 \x01(\x0c\x42\x1bZ\x16lightwalletd/walletrpc\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'compact_formats_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\026lightwalletd/walletrpc\272\002\000'
  _globals['_COMPACTBLOCK']._serialized_start=49
  _globals['_COMPACTBLOCK']._serialized_end=210
  _globals['_COMPACTTX']._serialized_start=213
  _globals['_COMPACTTX']._serialized_end=450
  _globals['_COMPACTSAPLINGSPEND']._serialized_start=452
  _globals['_COMPACTSAPLINGSPEND']._serialized_end=485
  _globals['_COMPACTSAPLINGOUTPUT']._serialized_start=487
  _globals['_COMPACTSAPLINGOUTPUT']._serialized_end=555
  _globals['_COMPACTORCHARDACTION']._serialized_start=557
  _globals['_COMPACTORCHARDACTION']._serialized_end=653
# @@protoc_insertion_point(module_scope)
