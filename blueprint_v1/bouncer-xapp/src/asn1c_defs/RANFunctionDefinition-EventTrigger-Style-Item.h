/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "E2SM-RC-IEs"
 * 	found in "e2sm-rc-v01.02.03.asn1"
 * 	`asn1c -fcompound-names -findirect-choice -fincludes-quoted -fno-include-deps -gen-PER -no-gen-example`
 */

#ifndef	_RANFunctionDefinition_EventTrigger_Style_Item_H_
#define	_RANFunctionDefinition_EventTrigger_Style_Item_H_


#include "asn_application.h"

/* Including external dependencies */
#include "RIC-Style-Type.h"
#include "RIC-Style-Name.h"
#include "RIC-Format-Type.h"
#include "constr_SEQUENCE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* RANFunctionDefinition-EventTrigger-Style-Item */
typedef struct RANFunctionDefinition_EventTrigger_Style_Item {
	RIC_Style_Type_t	 ric_EventTriggerStyle_Type;
	RIC_Style_Name_t	 ric_EventTriggerStyle_Name;
	RIC_Format_Type_t	 ric_EventTriggerFormat_Type;
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} RANFunctionDefinition_EventTrigger_Style_Item_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_RANFunctionDefinition_EventTrigger_Style_Item;
extern asn_SEQUENCE_specifics_t asn_SPC_RANFunctionDefinition_EventTrigger_Style_Item_specs_1;
extern asn_TYPE_member_t asn_MBR_RANFunctionDefinition_EventTrigger_Style_Item_1[3];

#ifdef __cplusplus
}
#endif

#endif	/* _RANFunctionDefinition_EventTrigger_Style_Item_H_ */
#include "asn_internal.h"
