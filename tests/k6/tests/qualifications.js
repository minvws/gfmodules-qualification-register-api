import http from "k6/http";
import { fail, group } from "k6";
import { describe } from "https://jslib.k6.io/k6chaijs/4.3.4.1/index.js";

import { pageResponseSchema } from "../api_contracts/page_schema.js";
import { expectToMatchResponseSchema } from "../utils/expects.js";
import { vendorQualificationSchema } from "../api_contracts/vendor_qualification_schema.js";
import { healthcareProviderQualificationSchema } from "../api_contracts/healthcare_provider_qualification_schema.js";

export function qualificationsTests(baseUrl) {
    group("/v1/qualifications", () => {
        describe('GET /v1/qualifications/vendors', () => {
            const response = http.get(`${baseUrl}/v1/qualifications/vendors`);

            expectToMatchResponseSchema(response, 200, pageResponseSchema(vendorQualificationSchema));
        });

        describe('GET /v1/qualifications/healthcare-providers', () => {
            const response = http.get(`${baseUrl}/v1/qualifications/healthcare-providers`);

            expectToMatchResponseSchema(response, 200, pageResponseSchema(healthcareProviderQualificationSchema));
        });
    });
}
