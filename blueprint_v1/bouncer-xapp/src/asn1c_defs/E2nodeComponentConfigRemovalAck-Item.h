/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "E2AP-PDU-Contents"
 * 	found in "e2ap-v02.02.03.asn1"
 * 	`asn1c -fcompound-names -findirect-choice -fincludes-quoted -fno-include-deps -gen-PER -no-gen-example`
 */

#ifndef	_E2nodeComponentConfigRemovalAck_Item_H_
#define	_E2nodeComponentConfigRemovalAck_Item_H_


#include "asn_application.h"

/* Including external dependencies */
#include "E2nodeComponentInterfaceType.h"
#include "E2nodeComponentID.h"
#include "E2nodeComponentConfigurationAck.h"
#include "constr_SEQUENCE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* E2nodeComponentConfigRemovalAck-Item */
typedef struct E2nodeComponentConfigRemovalAck_Item {
	E2nodeComponentInterfaceType_t	 e2nodeComponentInterfaceType;
	E2nodeComponentID_t	 e2nodeComponentID;
	E2nodeComponentConfigurationAck_t	 e2nodeComponentConfigurationAck;
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} E2nodeComponentConfigRemovalAck_Item_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_E2nodeComponentConfigRemovalAck_Item;

#ifdef __cplusplus
}
#endif

#endif	/* _E2nodeComponentConfigRemovalAck_Item_H_ */
#include "asn_internal.h"
