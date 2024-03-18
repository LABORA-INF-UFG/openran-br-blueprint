import ASN1_DEFS as asn1_defs
from binascii import hexlify, unhexlify

encoded = b'00050069000008001d000500007b0032000500020001000f000101001b00020070001c000140001900111020000001003734378001010104000000001a0025242000010001014400000001024400000001034400000001042a0009003734370000000ff0001400050470000000'

print("Encoded:", encoded)
print("Hexlify:", hexlify(encoded))
print("Unhexlify:", unhexlify(hexlify(encoded)))

# E2SM_Bouncer_IEs

print("E2SM_Bouncer_IEs")

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.B_Header
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.B_Message
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.B_TriggerNature
print(asn1_obj.from_aper(encoded), type(asn1_obj))

try:
    asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_ActionDefinition
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_ActionDefinition_Format1
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_ControlHeader
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_ControlHeader_Format1
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_ControlMessage
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_ControlMessage_Format1
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_EventTriggerDefinition
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_EventTriggerDefinition_Format1
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_IndicationHeader
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_IndicationHeader_Format1
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_IndicationMessage
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.E2SM_Bouncer_IndicationMessage_Format1
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.RANparameter_Item
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.RANparameter_Name
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.RANparameter_Value
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.RANparameter_Test
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_Bouncer_IEs.RANparameter_ID
print(asn1_obj.from_aper(encoded), type(asn1_obj))


print("E2SM_RC_IEs")

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationHeader
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationHeader_Format1
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationHeader_Format2
print(asn1_obj.from_aper(encoded), type(asn1_obj))

asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationHeader_Format3
print(asn1_obj.from_aper(encoded), type(asn1_obj))

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationMessage
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationMessage_Format1
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationMessage_Format2
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationMessage_Format3
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationMessage_Format4
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationMessage_Format5
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_IndicationMessage_Format6
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_RANFunctionDefinition
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_EventTrigger
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_EventTrigger_Format1
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_EventTrigger_Format2
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_EventTrigger_Format3
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_EventTrigger_Format4
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_EventTrigger_Format5
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ActionDefinition
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ActionDefinition_Format1
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ActionDefinition_Format2
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ActionDefinition_Format3
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ActionDefinition_Format4
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_CallProcessID
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_CallProcessID_Format1
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ControlOutcome
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ControlOutcome_Format1
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

try:
    asn1_obj = asn1_defs.E2SM_RC_IEs.E2SM_RC_ControlOutcome_Format2
    print(asn1_obj.from_aper(encoded), type(asn1_obj))
except Exception as e:
    print("Error:", e)

