/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "E2SM-RC-IEs"
 * 	found in "e2sm-rc-v01.02.03.asn1"
 * 	`asn1c -fcompound-names -findirect-choice -fincludes-quoted -fno-include-deps -gen-PER -no-gen-example`
 */

#ifndef	_NeighborRelation_Info_H_
#define	_NeighborRelation_Info_H_


#include "asn_application.h"

/* Including external dependencies */
#include "ServingCell-PCI.h"
#include "ServingCell-ARFCN.h"
#include "NeighborCell-List.h"
#include "constr_SEQUENCE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* NeighborRelation-Info */
typedef struct NeighborRelation_Info {
	ServingCell_PCI_t	 servingCellPCI;
	ServingCell_ARFCN_t	 servingCellARFCN;
	NeighborCell_List_t	 neighborCell_List;
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} NeighborRelation_Info_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_NeighborRelation_Info;
extern asn_SEQUENCE_specifics_t asn_SPC_NeighborRelation_Info_specs_1;
extern asn_TYPE_member_t asn_MBR_NeighborRelation_Info_1[3];

#ifdef __cplusplus
}
#endif

#endif	/* _NeighborRelation_Info_H_ */
#include "asn_internal.h"
