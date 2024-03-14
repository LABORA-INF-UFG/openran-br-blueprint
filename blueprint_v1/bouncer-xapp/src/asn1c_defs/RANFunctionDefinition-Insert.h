/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "E2SM-RC-IEs"
 * 	found in "e2sm-rc-v01.02.03.asn1"
 * 	`asn1c -fcompound-names -findirect-choice -fincludes-quoted -fno-include-deps -gen-PER -no-gen-example`
 */

#ifndef	_RANFunctionDefinition_Insert_H_
#define	_RANFunctionDefinition_Insert_H_


#include "asn_application.h"

/* Including external dependencies */
#include "asn_SEQUENCE_OF.h"
#include "constr_SEQUENCE_OF.h"
#include "constr_SEQUENCE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations */
struct RANFunctionDefinition_Insert_Item;

/* RANFunctionDefinition-Insert */
typedef struct RANFunctionDefinition_Insert {
	struct RANFunctionDefinition_Insert__ric_InsertStyle_List {
		A_SEQUENCE_OF(struct RANFunctionDefinition_Insert_Item) list;
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} ric_InsertStyle_List;
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} RANFunctionDefinition_Insert_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_RANFunctionDefinition_Insert;
extern asn_SEQUENCE_specifics_t asn_SPC_RANFunctionDefinition_Insert_specs_1;
extern asn_TYPE_member_t asn_MBR_RANFunctionDefinition_Insert_1[1];

#ifdef __cplusplus
}
#endif

#endif	/* _RANFunctionDefinition_Insert_H_ */
#include "asn_internal.h"
