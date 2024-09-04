import { applicationBaseSchema } from "./application_base_schema.js";
import { generateVendorSchema } from "./vendor_base_schema.js";

export const vendorSchema = generateVendorSchema({
    applications: {
        type: "array",
        items: applicationBaseSchema,
    }
})
