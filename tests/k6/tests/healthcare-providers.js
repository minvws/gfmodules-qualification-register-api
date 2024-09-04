import http from "k6/http";
import { fail, group } from "k6";
import { describe } from "https://jslib.k6.io/k6chaijs/4.3.4.1/index.js";

import { expectToMatchResponseSchema } from "../utils/expects.js";
import { healthcareProviderSchema } from "../api_contracts/healthcare_provider_schema.js";
import { notFoundResponseSchema, validationErrorResponseSchema } from "../api_contracts/default_response_schemas.js";

export function healthcareProvidersTests(baseUrl) {
    group("/v1/healthcare-providers", () => {
        describe('GET /v1/healthcare-providers/:id', () => {
            const healthcareProviderId = getHealthcareProviderIdFromQualifications(baseUrl);
            if(!healthcareProviderId) {
                fail("No healthcare provider id found");
            }

            const response = http.get(`${baseUrl}/v1/healthcare-providers/${healthcareProviderId}`);

            expectToMatchResponseSchema(response, 200, healthcareProviderSchema);
        });

        describe('GET 422 /v1/healthcare-providers/:id', () => {
            const response = http.get(`${baseUrl}/v1/healthcare-providers/incorrect-id`);

            expectToMatchResponseSchema(response, 422, validationErrorResponseSchema);
        });

        describe('GET 404 /v1/healthcare-providers/:id', () => {
            const response = http.get(`${baseUrl}/v1/healthcare-providers/ef0b6a18-b294-424e-979c-3dea57c33948`);

            expectToMatchResponseSchema(response, 404, notFoundResponseSchema);
        });
    });
}


function getHealthcareProviderIdFromQualifications(baseUrl) {
    const response = http.get(`${baseUrl}/v1/qualifications/healthcare-providers`);
    const data = response.json();

    if (response.status !== 200) {
        fail(`GET /v1/qualifications/healthcare-providers failed with status ${response.status}`);
    }

    return data?.items[0]?.healthcareProviderId;
}