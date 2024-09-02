export const systemType = {
    type: "object",
    properties: {
        id: {
            type: "string",
        },
        name: {
            type: "string",
        },
        description: {
            type: ["string", "null"]
        },
    },
    required: [
        "id",
        "name",
    ]
}