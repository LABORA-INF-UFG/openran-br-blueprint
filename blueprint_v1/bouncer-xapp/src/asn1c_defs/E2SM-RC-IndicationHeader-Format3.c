/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "E2SM-RC-IEs"
 * 	found in "e2sm-rc-v01.02.03.asn1"
 * 	`asn1c -fcompound-names -findirect-choice -fincludes-quoted -fno-include-deps -gen-PER -no-gen-example`
 */

#include "E2SM-RC-IndicationHeader-Format3.h"

#include "UEID.h"
asn_TYPE_member_t asn_MBR_E2SM_RC_IndicationHeader_Format3_1[] = {
	{ ATF_POINTER, 2, offsetof(struct E2SM_RC_IndicationHeader_Format3, ric_eventTriggerCondition_ID),
		(ASN_TAG_CLASS_CONTEXT | (0 << 2)),
		-1,	/* IMPLICIT tag at current level */
		&asn_DEF_RIC_EventTriggerCondition_ID,
		0,
		{ 0, 0, 0 },
		0, 0, /* No default value */
		"ric-eventTriggerCondition-ID"
		},
	{ ATF_POINTER, 1, offsetof(struct E2SM_RC_IndicationHeader_Format3, ueID),
		(ASN_TAG_CLASS_CONTEXT | (1 << 2)),
		+1,	/* EXPLICIT tag at current level */
		&asn_DEF_UEID,
		0,
		{ 0, 0, 0 },
		0, 0, /* No default value */
		"ueID"
		},
};
static const int asn_MAP_E2SM_RC_IndicationHeader_Format3_oms_1[] = { 0, 1 };
static const ber_tlv_tag_t asn_DEF_E2SM_RC_IndicationHeader_Format3_tags_1[] = {
	(ASN_TAG_CLASS_UNIVERSAL | (16 << 2))
};
static const asn_TYPE_tag2member_t asn_MAP_E2SM_RC_IndicationHeader_Format3_tag2el_1[] = {
    { (ASN_TAG_CLASS_CONTEXT | (0 << 2)), 0, 0, 0 }, /* ric-eventTriggerCondition-ID */
    { (ASN_TAG_CLASS_CONTEXT | (1 << 2)), 1, 0, 0 } /* ueID */
};
asn_SEQUENCE_specifics_t asn_SPC_E2SM_RC_IndicationHeader_Format3_specs_1 = {
	sizeof(struct E2SM_RC_IndicationHeader_Format3),
	offsetof(struct E2SM_RC_IndicationHeader_Format3, _asn_ctx),
	asn_MAP_E2SM_RC_IndicationHeader_Format3_tag2el_1,
	2,	/* Count of tags in the map */
	asn_MAP_E2SM_RC_IndicationHeader_Format3_oms_1,	/* Optional members */
	2, 0,	/* Root/Additions */
	2,	/* First extension addition */
};
asn_TYPE_descriptor_t asn_DEF_E2SM_RC_IndicationHeader_Format3 = {
	"E2SM-RC-IndicationHeader-Format3",
	"E2SM-RC-IndicationHeader-Format3",
	&asn_OP_SEQUENCE,
	asn_DEF_E2SM_RC_IndicationHeader_Format3_tags_1,
	sizeof(asn_DEF_E2SM_RC_IndicationHeader_Format3_tags_1)
		/sizeof(asn_DEF_E2SM_RC_IndicationHeader_Format3_tags_1[0]), /* 1 */
	asn_DEF_E2SM_RC_IndicationHeader_Format3_tags_1,	/* Same as above */
	sizeof(asn_DEF_E2SM_RC_IndicationHeader_Format3_tags_1)
		/sizeof(asn_DEF_E2SM_RC_IndicationHeader_Format3_tags_1[0]), /* 1 */
	{ 0, 0, SEQUENCE_constraint },
	asn_MBR_E2SM_RC_IndicationHeader_Format3_1,
	2,	/* Elements count */
	&asn_SPC_E2SM_RC_IndicationHeader_Format3_specs_1	/* Additional specs */
};

