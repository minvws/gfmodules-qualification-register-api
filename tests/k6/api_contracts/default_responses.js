export const validationItemSchema = {
    type: "object",
    properties: {
        loc: {
            type: "array",
        },
        msg: {
            type: "string",
        },
        type: {
            type: "string",
        },
    },
    required: [
        "loc",
        "msg",
        "type"
    ]
}

export const validationErrorResponse = {
    type: "object",
    properties: {
        detail: {
            type: "array",
            items: validationItemSchema
        }
    },
    required: [
        "detail"
    ]
}

export const notFoundResponse = {
    type: "object",
    properties: {
        detail: {
            type: "string",
        },
    },
    required: [
        "detail"
    ]
}