import { application } from "./application.js";

export const vendor = {
    type: "object",
    properties: {
        id: {
            type: "string",
        },
        tradeName: {
            type: "string",
        },
        statutoryName: {
            type: "string",
        },
        kvkNumber: {
            type: "string",
        },
        applications: {
            type: "array",
            items: application,
        }
    },
    required: [
        "id",
        "tradeName",
        "statutoryName",
        "kvkNumber",
        "applications",
    ]
}