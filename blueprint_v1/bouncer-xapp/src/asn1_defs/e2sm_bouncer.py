# -*- coding: UTF-8 -*-
# Code automatically generated by pycrate_asn1c

from pycrate_asn1rt.utils            import *
from pycrate_asn1rt.err              import *
from pycrate_asn1rt.glob             import make_GLOBAL, GLOBAL
from pycrate_asn1rt.dictobj          import ASN1Dict
from pycrate_asn1rt.refobj           import *
from pycrate_asn1rt.setobj           import *
from pycrate_asn1rt.asnobj_basic     import *
from pycrate_asn1rt.asnobj_str       import *
from pycrate_asn1rt.asnobj_construct import *
from pycrate_asn1rt.asnobj_class     import *
from pycrate_asn1rt.asnobj_ext       import *
from pycrate_asn1rt.init             import init_modules

class E2SM_Bouncer_IEs:

    _name_  = 'E2SM-Bouncer-IEs'
    _oid_   = []
    
    _obj_ = [
        'maxofRANParameters',
        'E2SM-Bouncer-EventTriggerDefinition',
        'E2SM-Bouncer-EventTriggerDefinition-Format1',
        'E2SM-Bouncer-ActionDefinition',
        'E2SM-Bouncer-ActionDefinition-Format1',
        'E2SM-Bouncer-IndicationHeader',
        'E2SM-Bouncer-IndicationHeader-Format1',
        'E2SM-Bouncer-IndicationMessage',
        'E2SM-Bouncer-IndicationMessage-Format1',
        'E2SM-Bouncer-ControlHeader',
        'E2SM-Bouncer-ControlHeader-Format1',
        'E2SM-Bouncer-ControlMessage',
        'E2SM-Bouncer-ControlMessage-Format1',
        'B-Header',
        'B-Message',
        'B-TriggerNature',
        'RANparameter-Item',
        'RANparameter-ID',
        'RANparameter-Name',
        'RANparameter-Test',
        'RANparameter-Value',
        ]
    _type_ = [
        'E2SM-Bouncer-EventTriggerDefinition',
        'E2SM-Bouncer-EventTriggerDefinition-Format1',
        'E2SM-Bouncer-ActionDefinition',
        'E2SM-Bouncer-ActionDefinition-Format1',
        'E2SM-Bouncer-IndicationHeader',
        'E2SM-Bouncer-IndicationHeader-Format1',
        'E2SM-Bouncer-IndicationMessage',
        'E2SM-Bouncer-IndicationMessage-Format1',
        'E2SM-Bouncer-ControlHeader',
        'E2SM-Bouncer-ControlHeader-Format1',
        'E2SM-Bouncer-ControlMessage',
        'E2SM-Bouncer-ControlMessage-Format1',
        'B-Header',
        'B-Message',
        'B-TriggerNature',
        'RANparameter-Item',
        'RANparameter-ID',
        'RANparameter-Name',
        'RANparameter-Test',
        'RANparameter-Value',
        ]
    _set_ = [
        ]
    _val_ = [
        'maxofRANParameters',
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< maxofRANParameters >-----#
    maxofRANParameters = INT(name='maxofRANParameters', mode=MODE_VALUE)
    maxofRANParameters._val = 255
    
    #-----< E2SM-Bouncer-EventTriggerDefinition >-----#
    E2SM_Bouncer_EventTriggerDefinition = CHOICE(name='E2SM-Bouncer-EventTriggerDefinition', mode=MODE_TYPE)
    _E2SM_Bouncer_EventTriggerDefinition_eventDefinition_Format1 = SEQ(name='eventDefinition-Format1', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'E2SM-Bouncer-EventTriggerDefinition-Format1')))
    E2SM_Bouncer_EventTriggerDefinition._cont = ASN1Dict([
        ('eventDefinition-Format1', _E2SM_Bouncer_EventTriggerDefinition_eventDefinition_Format1),
        ])
    E2SM_Bouncer_EventTriggerDefinition._ext = []
    
    #-----< E2SM-Bouncer-EventTriggerDefinition-Format1 >-----#
    E2SM_Bouncer_EventTriggerDefinition_Format1 = SEQ(name='E2SM-Bouncer-EventTriggerDefinition-Format1', mode=MODE_TYPE)
    _E2SM_Bouncer_EventTriggerDefinition_Format1_triggerNature = ENUM(name='triggerNature', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'B-TriggerNature')))
    E2SM_Bouncer_EventTriggerDefinition_Format1._cont = ASN1Dict([
        ('triggerNature', _E2SM_Bouncer_EventTriggerDefinition_Format1_triggerNature),
        ])
    E2SM_Bouncer_EventTriggerDefinition_Format1._ext = []
    
    #-----< E2SM-Bouncer-ActionDefinition >-----#
    E2SM_Bouncer_ActionDefinition = CHOICE(name='E2SM-Bouncer-ActionDefinition', mode=MODE_TYPE)
    _E2SM_Bouncer_ActionDefinition_actionDefinition_Format1 = SEQ(name='actionDefinition-Format1', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'E2SM-Bouncer-ActionDefinition-Format1')))
    E2SM_Bouncer_ActionDefinition._cont = ASN1Dict([
        ('actionDefinition-Format1', _E2SM_Bouncer_ActionDefinition_actionDefinition_Format1),
        ])
    E2SM_Bouncer_ActionDefinition._ext = []
    
    #-----< E2SM-Bouncer-ActionDefinition-Format1 >-----#
    E2SM_Bouncer_ActionDefinition_Format1 = SEQ(name='E2SM-Bouncer-ActionDefinition-Format1', mode=MODE_TYPE)
    _E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List = SEQ_OF(name='ranParameter-List', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), opt=True)
    __E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List__item_ = SEQ(name='_item_', mode=MODE_TYPE, typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'RANparameter-Item')))
    _E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List._cont = __E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List__item_
    _E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=1, ub=255)], ev=None, er=[])
    E2SM_Bouncer_ActionDefinition_Format1._cont = ASN1Dict([
        ('ranParameter-List', _E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List),
        ])
    E2SM_Bouncer_ActionDefinition_Format1._ext = []
    
    #-----< E2SM-Bouncer-IndicationHeader >-----#
    E2SM_Bouncer_IndicationHeader = CHOICE(name='E2SM-Bouncer-IndicationHeader', mode=MODE_TYPE)
    _E2SM_Bouncer_IndicationHeader_indicationHeader_Format1 = SEQ(name='indicationHeader-Format1', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'E2SM-Bouncer-IndicationHeader-Format1')))
    E2SM_Bouncer_IndicationHeader._cont = ASN1Dict([
        ('indicationHeader-Format1', _E2SM_Bouncer_IndicationHeader_indicationHeader_Format1),
        ])
    E2SM_Bouncer_IndicationHeader._ext = []
    
    #-----< E2SM-Bouncer-IndicationHeader-Format1 >-----#
    E2SM_Bouncer_IndicationHeader_Format1 = SEQ(name='E2SM-Bouncer-IndicationHeader-Format1', mode=MODE_TYPE)
    _E2SM_Bouncer_IndicationHeader_Format1_indicationHeaderParam = INT(name='indicationHeaderParam', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'B-Header')))
    E2SM_Bouncer_IndicationHeader_Format1._cont = ASN1Dict([
        ('indicationHeaderParam', _E2SM_Bouncer_IndicationHeader_Format1_indicationHeaderParam),
        ])
    E2SM_Bouncer_IndicationHeader_Format1._ext = []
    
    #-----< E2SM-Bouncer-IndicationMessage >-----#
    E2SM_Bouncer_IndicationMessage = CHOICE(name='E2SM-Bouncer-IndicationMessage', mode=MODE_TYPE)
    _E2SM_Bouncer_IndicationMessage_indicationMessage_Format1 = SEQ(name='indicationMessage-Format1', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'E2SM-Bouncer-IndicationMessage-Format1')))
    E2SM_Bouncer_IndicationMessage._cont = ASN1Dict([
        ('indicationMessage-Format1', _E2SM_Bouncer_IndicationMessage_indicationMessage_Format1),
        ])
    E2SM_Bouncer_IndicationMessage._ext = []
    
    #-----< E2SM-Bouncer-IndicationMessage-Format1 >-----#
    E2SM_Bouncer_IndicationMessage_Format1 = SEQ(name='E2SM-Bouncer-IndicationMessage-Format1', mode=MODE_TYPE)
    _E2SM_Bouncer_IndicationMessage_Format1_indicationMsgParam = OCT_STR(name='indicationMsgParam', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'B-Message')))
    E2SM_Bouncer_IndicationMessage_Format1._cont = ASN1Dict([
        ('indicationMsgParam', _E2SM_Bouncer_IndicationMessage_Format1_indicationMsgParam),
        ])
    E2SM_Bouncer_IndicationMessage_Format1._ext = []
    
    #-----< E2SM-Bouncer-ControlHeader >-----#
    E2SM_Bouncer_ControlHeader = CHOICE(name='E2SM-Bouncer-ControlHeader', mode=MODE_TYPE)
    _E2SM_Bouncer_ControlHeader_controlHeader_Format1 = SEQ(name='controlHeader-Format1', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'E2SM-Bouncer-ControlHeader-Format1')))
    E2SM_Bouncer_ControlHeader._cont = ASN1Dict([
        ('controlHeader-Format1', _E2SM_Bouncer_ControlHeader_controlHeader_Format1),
        ])
    E2SM_Bouncer_ControlHeader._ext = []
    
    #-----< E2SM-Bouncer-ControlHeader-Format1 >-----#
    E2SM_Bouncer_ControlHeader_Format1 = SEQ(name='E2SM-Bouncer-ControlHeader-Format1', mode=MODE_TYPE)
    _E2SM_Bouncer_ControlHeader_Format1_controlHeaderParam = INT(name='controlHeaderParam', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'B-Header')))
    E2SM_Bouncer_ControlHeader_Format1._cont = ASN1Dict([
        ('controlHeaderParam', _E2SM_Bouncer_ControlHeader_Format1_controlHeaderParam),
        ])
    E2SM_Bouncer_ControlHeader_Format1._ext = []
    
    #-----< E2SM-Bouncer-ControlMessage >-----#
    E2SM_Bouncer_ControlMessage = CHOICE(name='E2SM-Bouncer-ControlMessage', mode=MODE_TYPE)
    _E2SM_Bouncer_ControlMessage_controlMessage_Format1 = SEQ(name='controlMessage-Format1', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'E2SM-Bouncer-ControlMessage-Format1')))
    E2SM_Bouncer_ControlMessage._cont = ASN1Dict([
        ('controlMessage-Format1', _E2SM_Bouncer_ControlMessage_controlMessage_Format1),
        ])
    E2SM_Bouncer_ControlMessage._ext = []
    
    #-----< E2SM-Bouncer-ControlMessage-Format1 >-----#
    E2SM_Bouncer_ControlMessage_Format1 = SEQ(name='E2SM-Bouncer-ControlMessage-Format1', mode=MODE_TYPE)
    _E2SM_Bouncer_ControlMessage_Format1_controlMsgParam = OCT_STR(name='controlMsgParam', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'B-Message')))
    E2SM_Bouncer_ControlMessage_Format1._cont = ASN1Dict([
        ('controlMsgParam', _E2SM_Bouncer_ControlMessage_Format1_controlMsgParam),
        ])
    E2SM_Bouncer_ControlMessage_Format1._ext = []
    
    #-----< B-Header >-----#
    B_Header = INT(name='B-Header', mode=MODE_TYPE)
    
    #-----< B-Message >-----#
    B_Message = OCT_STR(name='B-Message', mode=MODE_TYPE)
    
    #-----< B-TriggerNature >-----#
    B_TriggerNature = ENUM(name='B-TriggerNature', mode=MODE_TYPE)
    B_TriggerNature._cont = ASN1Dict([('now', 0), ('onchange', 1)])
    B_TriggerNature._ext = []
    
    #-----< RANparameter-Item >-----#
    RANparameter_Item = SEQ(name='RANparameter-Item', mode=MODE_TYPE)
    _RANparameter_Item_ranParameter_ID = INT(name='ranParameter-ID', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'RANparameter-ID')))
    _RANparameter_Item_ranParameter_Name = OCT_STR(name='ranParameter-Name', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'RANparameter-Name')))
    _RANparameter_Item_ranParameter_Test = ENUM(name='ranParameter-Test', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'RANparameter-Test')))
    _RANparameter_Item_ranParameter_Value = OCT_STR(name='ranParameter-Value', mode=MODE_TYPE, tag=(3, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('E2SM-Bouncer-IEs', 'RANparameter-Value')))
    RANparameter_Item._cont = ASN1Dict([
        ('ranParameter-ID', _RANparameter_Item_ranParameter_ID),
        ('ranParameter-Name', _RANparameter_Item_ranParameter_Name),
        ('ranParameter-Test', _RANparameter_Item_ranParameter_Test),
        ('ranParameter-Value', _RANparameter_Item_ranParameter_Value),
        ])
    RANparameter_Item._ext = []
    
    #-----< RANparameter-ID >-----#
    RANparameter_ID = INT(name='RANparameter-ID', mode=MODE_TYPE)
    RANparameter_ID._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=255)], ev=None, er=[])
    
    #-----< RANparameter-Name >-----#
    RANparameter_Name = OCT_STR(name='RANparameter-Name', mode=MODE_TYPE)
    
    #-----< RANparameter-Test >-----#
    RANparameter_Test = ENUM(name='RANparameter-Test', mode=MODE_TYPE)
    RANparameter_Test._cont = ASN1Dict([('equal', 0), ('greaterthan', 1), ('lessthan', 2), ('contains', 3), ('present', 4)])
    RANparameter_Test._ext = []
    
    #-----< RANparameter-Value >-----#
    RANparameter_Value = OCT_STR(name='RANparameter-Value', mode=MODE_TYPE)
    
    _all_ = [
        maxofRANParameters,
        _E2SM_Bouncer_EventTriggerDefinition_eventDefinition_Format1,
        E2SM_Bouncer_EventTriggerDefinition,
        _E2SM_Bouncer_EventTriggerDefinition_Format1_triggerNature,
        E2SM_Bouncer_EventTriggerDefinition_Format1,
        _E2SM_Bouncer_ActionDefinition_actionDefinition_Format1,
        E2SM_Bouncer_ActionDefinition,
        __E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List__item_,
        _E2SM_Bouncer_ActionDefinition_Format1_ranParameter_List,
        E2SM_Bouncer_ActionDefinition_Format1,
        _E2SM_Bouncer_IndicationHeader_indicationHeader_Format1,
        E2SM_Bouncer_IndicationHeader,
        _E2SM_Bouncer_IndicationHeader_Format1_indicationHeaderParam,
        E2SM_Bouncer_IndicationHeader_Format1,
        _E2SM_Bouncer_IndicationMessage_indicationMessage_Format1,
        E2SM_Bouncer_IndicationMessage,
        _E2SM_Bouncer_IndicationMessage_Format1_indicationMsgParam,
        E2SM_Bouncer_IndicationMessage_Format1,
        _E2SM_Bouncer_ControlHeader_controlHeader_Format1,
        E2SM_Bouncer_ControlHeader,
        _E2SM_Bouncer_ControlHeader_Format1_controlHeaderParam,
        E2SM_Bouncer_ControlHeader_Format1,
        _E2SM_Bouncer_ControlMessage_controlMessage_Format1,
        E2SM_Bouncer_ControlMessage,
        _E2SM_Bouncer_ControlMessage_Format1_controlMsgParam,
        E2SM_Bouncer_ControlMessage_Format1,
        B_Header,
        B_Message,
        B_TriggerNature,
        _RANparameter_Item_ranParameter_ID,
        _RANparameter_Item_ranParameter_Name,
        _RANparameter_Item_ranParameter_Test,
        _RANparameter_Item_ranParameter_Value,
        RANparameter_Item,
        RANparameter_ID,
        RANparameter_Name,
        RANparameter_Test,
        RANparameter_Value,
    ]

init_modules(E2SM_Bouncer_IEs)