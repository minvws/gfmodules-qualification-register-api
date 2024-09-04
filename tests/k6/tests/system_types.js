import http from "k6/http";
import { fail, group } from "k6";
import { describe } from "https://jslib.k6.io/k6chaijs/4.3.4.1/index.js";

import { pageResponseSchema } from "../api_contracts/page_schema.js";
import { systemTypeSchema } from "../api_contracts/system_type_schema.js";
import { notFoundResponseSchema, validationErrorResponseSchema } from "../api_contracts/default_response_schemas.js";
import { expectToMatchResponseSchema } from "../utils/expects.js";

export function systemTypesTests(baseUrl) {
    group("/v1/system-types", () => {
        let systemTypeId = undefined;

        describe("GET /v1/system-types", () => {
            const response = http.get(`${baseUrl}/v1/system-types`);
            const data = response.json();

            expectToMatchResponseSchema(response, 200, pageResponseSchema(systemTypeSchema));

            if (data.items.length > 0) {
                systemTypeId = data.items[0].id;
            }
        });

        describe('GET /v1/system-types/:id', () => {
            if (!systemTypeId) {
                fail('No system type found to test GET /v1/system-types/:id');
                return;
            }

            const response = http.get(`${baseUrl}/v1/system-types/${systemTypeId}`);

            expectToMatchResponseSchema(response, 200, systemTypeSchema);
        });

        describe('GET 422 /v1/system-types/:id', () => {
            const response = http.get(`${baseUrl}/v1/system-types/incorrect-id`);

            expectToMatchResponseSchema(response, 422, validationErrorResponseSchema);
        });

        describe('GET 404 /v1/system-types/:id', () => {
            const response = http.get(`${baseUrl}/v1/system-types/ef0b6a18-b294-424e-979c-3dea57c33948`);

            expectToMatchResponseSchema(response, 404, notFoundResponseSchema);
        });
    });
}