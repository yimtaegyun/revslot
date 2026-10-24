import {defineConfig,devices} from '@playwright/test';
export default defineConfig({
 testDir:'./e2e',timeout:60000,retries:0,workers:1,
 reporter:[['list'],['html',{open:'never'}]],
 use:{baseURL:'http://127.0.0.1:3000',trace:'retain-on-failure',screenshot:'only-on-failure',video:'on'},
 projects:[{name:'chromium',use:{...devices['Desktop Chrome'],viewport:{width:1440,height:1000}}}],
 webServer:{command:'node ../scripts/dev.mjs --production',url:'http://127.0.0.1:3000/api/health',reuseExistingServer:!process.env.CI,timeout:60000},
});
