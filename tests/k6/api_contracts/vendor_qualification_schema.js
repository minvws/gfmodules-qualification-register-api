export const vendorQualificationSchema = {
    type: "object",
    properties: {
        qualificationId: {
            type: "string",
        },
        applicationVersionId: {
            type: "string",
        },
        applicationId: {
            type: "string",
        },
        vendorId: {
            type: "string",
        },
        protocolId: {
            type: "string",
        },
        systemTypeId: {
            type: "string",
        },
        roleId: {
            type: "string",
        },
        applicationVersion: {
            type: "string",
        },
        application: {
            type: "string",
        },
        protocol: {
            type: "string",
        },
        protocolVersion: {
            type: "string",
        },
        systemType: {
            type: "string",
        },
        role: {
            type: "string",
        },
        kvkNumber: {
            type: "string",
        },
        tradeName: {
            type: "string",
        },
        statutoryName: {
            type: "string",
        },
        qualificationDate: {
            type: "string",
            format: "date",
        },
    },
    required: [
        "qualificationId",
        "applicationVersionId",
        "applicationId",
        "vendorId",
        "protocolId",
        "systemTypeId",
        "roleId",
        "applicationVersion",
        "application",
        "protocol",
        "protocolVersion",
        "systemType",
        "role",
        "kvkNumber",
        "tradeName",
        "statutoryName",
        "qualificationDate",
    ]
}