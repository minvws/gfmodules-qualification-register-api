import http from "k6/http";
import { fail, group } from "k6";
import { describe } from "https://jslib.k6.io/k6chaijs/4.3.4.1/index.js";

import { pageResponseSchema } from "../api_contracts/page_schema.js";
import { roleSchema } from "../api_contracts/role_schema.js";
import { notFoundResponseSchema, validationErrorResponseSchema } from "../api_contracts/default_response_schemas.js";
import { expectToMatchResponseSchema } from "../utils/expects.js";

export function rolesTests(baseUrl) {
    group("/v1/roles", () => {
        let roleId = undefined;

        describe('GET /v1/roles', () => {
            const response = http.get(`${baseUrl}/v1/roles`);
            const data = response.json();

            expectToMatchResponseSchema(response, 200, pageResponseSchema(roleSchema));

            if (data.items.length > 0) {
                roleId = data.items[0].id;
            }
        });

        describe('GET /v1/roles/:id', () => {
            if (!roleId) {
                fail('No role found to test GET /v1/roles/:id');
                return;
            }

            const response = http.get(`${baseUrl}/v1/roles/${roleId}`);

            expectToMatchResponseSchema(response, 200, roleSchema);
        });

        describe('GET 422 /v1/roles/:id', () => {
            const response = http.get(`${baseUrl}/v1/roles/incorrect-id`);

            expectToMatchResponseSchema(response, 422, validationErrorResponseSchema);
        });

        describe('GET 404 /v1/roles/:id', () => {
            const response = http.get(`${baseUrl}/v1/roles/ef0b6a18-b294-424e-979c-3dea57c33948`);

            expectToMatchResponseSchema(response, 404, notFoundResponseSchema);
        });
    });
}