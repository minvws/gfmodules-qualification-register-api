export const application     = {
    type: "object",
    properties: {
        id: {
            type: "string",
        },
        name: {
            type: "string",
        },
        createdAt: {
            type: "string",
        },
        modifiedAt: {
            type: "string",
        },
    },
    required: [
        "id",
        "name",
        "createdAt",
        "modifiedAt",
    ]
}