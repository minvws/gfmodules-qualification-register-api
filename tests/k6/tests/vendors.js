import http from "k6/http";
import { fail, group } from "k6";
import { describe } from "https://jslib.k6.io/k6chaijs/4.3.4.1/index.js";

import { pageResponseSchema } from "../api_contracts/page_schema.js";
import { vendorSchema } from "../api_contracts/vendor_schema.js";
import { notFoundResponseSchema, validationErrorResponseSchema } from "../api_contracts/default_response_schemas.js";
import { expectToMatchResponseSchema } from "../utils/expects.js";

export function vendorsTests(baseUrl) {
    group("/v1/vendors", () => {
        let vendorId = undefined;

        describe('GET /v1/vendors', () => {
            const response = http.get(`${baseUrl}/v1/vendors`);
            const data = response.json();

            expectToMatchResponseSchema(response, 200, pageResponseSchema(vendorSchema));

            if (data.items.length > 0) {
                vendorId = data.items[0].id;
            }
        });

        describe('GET /v1/vendors/:id', () => {
            if (!vendorId) {
                fail('No vendor found to test GET /v1/vendors/:id');
                return;
            }

            const response = http.get(`${baseUrl}/v1/vendors/${vendorId}`);

            expectToMatchResponseSchema(response, 200, vendorSchema);
        });

        describe('GET 422 /v1/vendors/:id', () => {
            const response = http.get(`${baseUrl}/v1/vendors/incorrect-id`);

            expectToMatchResponseSchema(response, 422, validationErrorResponseSchema);
        });

        describe('GET 404 /v1/vendors/:id', () => {
            const response = http.get(`${baseUrl}/v1/vendors/ef0b6a18-b294-424e-979c-3dea57c33948`);

            expectToMatchResponseSchema(response, 404, notFoundResponseSchema);
        });
    });
}