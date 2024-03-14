/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "E2AP-PDU-Contents"
 * 	found in "e2ap-v02.02.03.asn1"
 * 	`asn1c -fcompound-names -findirect-choice -fincludes-quoted -fno-include-deps -gen-PER -no-gen-example`
 */

#ifndef	_E2connectionUpdate_H_
#define	_E2connectionUpdate_H_


#include "asn_application.h"

/* Including external dependencies */
#include "ProtocolIE-Container.h"
#include "constr_SEQUENCE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* E2connectionUpdate */
typedef struct E2connectionUpdate {
	ProtocolIE_Container_2007P15_t	 protocolIEs;
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} E2connectionUpdate_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_E2connectionUpdate;
extern asn_SEQUENCE_specifics_t asn_SPC_E2connectionUpdate_specs_1;
extern asn_TYPE_member_t asn_MBR_E2connectionUpdate_1[1];

#ifdef __cplusplus
}
#endif

#endif	/* _E2connectionUpdate_H_ */
#include "asn_internal.h"
