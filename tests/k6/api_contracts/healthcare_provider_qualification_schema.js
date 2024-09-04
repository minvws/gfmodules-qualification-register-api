export const healthcareProviderQualificationSchema = {
    type: "object",
    properties: {
        qualificationId: {
            type: "string",
        },
        healthcareProviderId: {
            type: "string",
        },
        protocolId: {
            type: "string",
        },
        protocolVersionId: {
            type: "string",
        },
        healthcareProvider: {
            type: "string",
        },
        protocol: {
            type: "string",
        },
        protocolType: {
            type: "string",
        },
        protocolVersion: {
            type: "string",
        },
    },
    required: [
        "qualificationId",
        "healthcareProviderId",
        "protocolId",
        "protocolVersionId",
        "healthcareProvider",
        "protocol",
        "protocolType",
        "protocolVersion",
    ]
}