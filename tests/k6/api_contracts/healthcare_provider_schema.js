export const healthcareProviderSchema = {
    type: "object",
    properties: {
        id: {
            type: "string",
        },
        uraCode: {
            type: "string",
        },
        agbCode: {
            type: "string",
        },
        tradeName: {
            type: "string",
        },
        statutoryName: {
            type: "string",
        },
        applicationVersions: {
            type: "array",
        },
    },
    required: [
        "id",
        "uraCode",
        "agbCode",
        "tradeName",
        "statutoryName",
        "applicationVersions",
    ]
}