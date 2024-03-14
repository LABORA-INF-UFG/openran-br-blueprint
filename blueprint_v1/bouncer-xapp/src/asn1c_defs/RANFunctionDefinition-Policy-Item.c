/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "E2SM-RC-IEs"
 * 	found in "e2sm-rc-v01.02.03.asn1"
 * 	`asn1c -fcompound-names -findirect-choice -fincludes-quoted -fno-include-deps -gen-PER -no-gen-example`
 */

#include "RANFunctionDefinition-Policy-Item.h"

#include "RANFunctionDefinition-Policy-Action-Item.h"
static int
memb_ric_PolicyAction_List_constraint_1(const asn_TYPE_descriptor_t *td, const void *sptr,
			asn_app_constraint_failed_f *ctfailcb, void *app_key) {
	size_t size;
	
	if(!sptr) {
		ASN__CTFAIL(app_key, td, sptr,
			"%s: value not given (%s:%d)",
			td->name, __FILE__, __LINE__);
		return -1;
	}
	
	/* Determine the number of elements */
	size = _A_CSEQUENCE_FROM_VOID(sptr)->count;
	
	if((size >= 1 && size <= 65535)) {
		/* Perform validation of the inner elements */
		return td->encoding_constraints.general_constraints(td, sptr, ctfailcb, app_key);
	} else {
		ASN__CTFAIL(app_key, td, sptr,
			"%s: constraint failed (%s:%d)",
			td->name, __FILE__, __LINE__);
		return -1;
	}
}

static asn_oer_constraints_t asn_OER_type_ric_PolicyAction_List_constr_5 CC_NOTUSED = {
	{ 0, 0 },
	-1	/* (SIZE(1..65535)) */};
static asn_per_constraints_t asn_PER_type_ric_PolicyAction_List_constr_5 CC_NOTUSED = {
	{ APC_UNCONSTRAINED,	-1, -1,  0,  0 },
	{ APC_CONSTRAINED,	 16,  16,  1,  65535 }	/* (SIZE(1..65535)) */,
	0, 0	/* No PER value map */
};
static asn_oer_constraints_t asn_OER_memb_ric_PolicyAction_List_constr_5 CC_NOTUSED = {
	{ 0, 0 },
	-1	/* (SIZE(1..65535)) */};
static asn_per_constraints_t asn_PER_memb_ric_PolicyAction_List_constr_5 CC_NOTUSED = {
	{ APC_UNCONSTRAINED,	-1, -1,  0,  0 },
	{ APC_CONSTRAINED,	 16,  16,  1,  65535 }	/* (SIZE(1..65535)) */,
	0, 0	/* No PER value map */
};
static asn_TYPE_member_t asn_MBR_ric_PolicyAction_List_5[] = {
	{ ATF_POINTER, 0, 0,
		(ASN_TAG_CLASS_UNIVERSAL | (16 << 2)),
		0,
		&asn_DEF_RANFunctionDefinition_Policy_Action_Item,
		0,
		{ 0, 0, 0 },
		0, 0, /* No default value */
		""
		},
};
static const ber_tlv_tag_t asn_DEF_ric_PolicyAction_List_tags_5[] = {
	(ASN_TAG_CLASS_CONTEXT | (3 << 2)),
	(ASN_TAG_CLASS_UNIVERSAL | (16 << 2))
};
static asn_SET_OF_specifics_t asn_SPC_ric_PolicyAction_List_specs_5 = {
	sizeof(struct RANFunctionDefinition_Policy_Item__ric_PolicyAction_List),
	offsetof(struct RANFunctionDefinition_Policy_Item__ric_PolicyAction_List, _asn_ctx),
	0,	/* XER encoding is XMLDelimitedItemList */
};
static /* Use -fall-defs-global to expose */
asn_TYPE_descriptor_t asn_DEF_ric_PolicyAction_List_5 = {
	"ric-PolicyAction-List",
	"ric-PolicyAction-List",
	&asn_OP_SEQUENCE_OF,
	asn_DEF_ric_PolicyAction_List_tags_5,
	sizeof(asn_DEF_ric_PolicyAction_List_tags_5)
		/sizeof(asn_DEF_ric_PolicyAction_List_tags_5[0]) - 1, /* 1 */
	asn_DEF_ric_PolicyAction_List_tags_5,	/* Same as above */
	sizeof(asn_DEF_ric_PolicyAction_List_tags_5)
		/sizeof(asn_DEF_ric_PolicyAction_List_tags_5[0]), /* 2 */
	{ &asn_OER_type_ric_PolicyAction_List_constr_5, &asn_PER_type_ric_PolicyAction_List_constr_5, SEQUENCE_OF_constraint },
	asn_MBR_ric_PolicyAction_List_5,
	1,	/* Single element */
	&asn_SPC_ric_PolicyAction_List_specs_5	/* Additional specs */
};

asn_TYPE_member_t asn_MBR_RANFunctionDefinition_Policy_Item_1[] = {
	{ ATF_NOFLAGS, 0, offsetof(struct RANFunctionDefinition_Policy_Item, ric_PolicyStyle_Type),
		(ASN_TAG_CLASS_CONTEXT | (0 << 2)),
		-1,	/* IMPLICIT tag at current level */
		&asn_DEF_RIC_Style_Type,
		0,
		{ 0, 0, 0 },
		0, 0, /* No default value */
		"ric-PolicyStyle-Type"
		},
	{ ATF_NOFLAGS, 0, offsetof(struct RANFunctionDefinition_Policy_Item, ric_PolicyStyle_Name),
		(ASN_TAG_CLASS_CONTEXT | (1 << 2)),
		-1,	/* IMPLICIT tag at current level */
		&asn_DEF_RIC_Style_Name,
		0,
		{ 0, 0, 0 },
		0, 0, /* No default value */
		"ric-PolicyStyle-Name"
		},
	{ ATF_NOFLAGS, 0, offsetof(struct RANFunctionDefinition_Policy_Item, ric_SupportedEventTriggerStyle_Type),
		(ASN_TAG_CLASS_CONTEXT | (2 << 2)),
		-1,	/* IMPLICIT tag at current level */
		&asn_DEF_RIC_Style_Type,
		0,
		{ 0, 0, 0 },
		0, 0, /* No default value */
		"ric-SupportedEventTriggerStyle-Type"
		},
	{ ATF_POINTER, 1, offsetof(struct RANFunctionDefinition_Policy_Item, ric_PolicyAction_List),
		(ASN_TAG_CLASS_CONTEXT | (3 << 2)),
		0,
		&asn_DEF_ric_PolicyAction_List_5,
		0,
		{ &asn_OER_memb_ric_PolicyAction_List_constr_5, &asn_PER_memb_ric_PolicyAction_List_constr_5,  memb_ric_PolicyAction_List_constraint_1 },
		0, 0, /* No default value */
		"ric-PolicyAction-List"
		},
};
static const int asn_MAP_RANFunctionDefinition_Policy_Item_oms_1[] = { 3 };
static const ber_tlv_tag_t asn_DEF_RANFunctionDefinition_Policy_Item_tags_1[] = {
	(ASN_TAG_CLASS_UNIVERSAL | (16 << 2))
};
static const asn_TYPE_tag2member_t asn_MAP_RANFunctionDefinition_Policy_Item_tag2el_1[] = {
    { (ASN_TAG_CLASS_CONTEXT | (0 << 2)), 0, 0, 0 }, /* ric-PolicyStyle-Type */
    { (ASN_TAG_CLASS_CONTEXT | (1 << 2)), 1, 0, 0 }, /* ric-PolicyStyle-Name */
    { (ASN_TAG_CLASS_CONTEXT | (2 << 2)), 2, 0, 0 }, /* ric-SupportedEventTriggerStyle-Type */
    { (ASN_TAG_CLASS_CONTEXT | (3 << 2)), 3, 0, 0 } /* ric-PolicyAction-List */
};
asn_SEQUENCE_specifics_t asn_SPC_RANFunctionDefinition_Policy_Item_specs_1 = {
	sizeof(struct RANFunctionDefinition_Policy_Item),
	offsetof(struct RANFunctionDefinition_Policy_Item, _asn_ctx),
	asn_MAP_RANFunctionDefinition_Policy_Item_tag2el_1,
	4,	/* Count of tags in the map */
	asn_MAP_RANFunctionDefinition_Policy_Item_oms_1,	/* Optional members */
	1, 0,	/* Root/Additions */
	4,	/* First extension addition */
};
asn_TYPE_descriptor_t asn_DEF_RANFunctionDefinition_Policy_Item = {
	"RANFunctionDefinition-Policy-Item",
	"RANFunctionDefinition-Policy-Item",
	&asn_OP_SEQUENCE,
	asn_DEF_RANFunctionDefinition_Policy_Item_tags_1,
	sizeof(asn_DEF_RANFunctionDefinition_Policy_Item_tags_1)
		/sizeof(asn_DEF_RANFunctionDefinition_Policy_Item_tags_1[0]), /* 1 */
	asn_DEF_RANFunctionDefinition_Policy_Item_tags_1,	/* Same as above */
	sizeof(asn_DEF_RANFunctionDefinition_Policy_Item_tags_1)
		/sizeof(asn_DEF_RANFunctionDefinition_Policy_Item_tags_1[0]), /* 1 */
	{ 0, 0, SEQUENCE_constraint },
	asn_MBR_RANFunctionDefinition_Policy_Item_1,
	4,	/* Elements count */
	&asn_SPC_RANFunctionDefinition_Policy_Item_specs_1	/* Additional specs */
};

