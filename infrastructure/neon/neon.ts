import { defineConfig } from "@neon/config/v1";

export default defineConfig({
  functions: {
    recoveryclock: {
      name: "Revslot recovery clock",
      source: "./recoveryclock.mjs",
      env: { CRON_SECRET: process.env.CRON_SECRET! },
    },
  },
  triggers: {
    "recovery-clock-every-minute": {
      type: "schedule",
      function: "recoveryclock",
      cron: "*/15 * * * *",
      functionPath: "/cron",
    },
  },
});
