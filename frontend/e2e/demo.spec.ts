import {test,expect} from '@playwright/test';
import fs from 'node:fs';
const shots='e2e-captures';
test('cancellation, autonomous reprice, sandbox booking and merchant revenue',async({page})=>{
 fs.mkdirSync(shots,{recursive:true});
 await page.goto('/');
 await expect(page.getByRole('heading',{name:'Recovery overview'})).toBeVisible();
 await expect(page.getByRole('button',{name:'Run cancellation scenario'})).toBeEnabled();
 await page.screenshot({path:`${shots}/01-merchant-ready.png`,fullPage:true});
 await page.getByRole('button',{name:'Run cancellation scenario'}).click();
 await expect(page.getByText('Recovery offer published',{exact:true})).toBeVisible();
 await expect(page.getByText('$64',{exact:true}).first()).toBeVisible();
 await page.screenshot({path:`${shots}/02-agent-first-offer.png`,fullPage:true});
 await page.getByRole('button',{name:'+20 min'}).click();
 await expect(page.getByText('Strategy updated',{exact:true})).toBeVisible();
 await expect(page.getByText('$56',{exact:true}).first()).toBeVisible();
 await page.screenshot({path:`${shots}/03-reprice.png`,fullPage:true});
 await page.getByRole('button',{name:'Marketplace',exact:true}).click();
 await expect(page.getByRole('button',{name:'Reserve this time'})).toBeVisible();
 await page.screenshot({path:`${shots}/04-marketplace.png`,fullPage:true});
 await page.getByRole('button',{name:'Reserve this time'}).click();
 await page.getByRole('button',{name:'Confirm sandbox reservation · $56'}).click();
 await expect(page.getByRole('dialog')).not.toBeVisible();
 await page.getByRole('button',{name:'Overview',exact:true}).click();
 await expect(page.getByRole('heading',{name:'$56 recovered.'})).toBeVisible();
 await page.screenshot({path:`${shots}/05-recovered.png`,fullPage:true});
 await page.getByRole('button',{name:'Analytics',exact:true}).click();
 await expect(page.getByText('The complete trade-off')).toBeVisible();
 await page.screenshot({path:`${shots}/06-analytics.png`,fullPage:true});
 await page.getByRole('button',{name:'Guardrails',exact:true}).click();
 await expect(page.getByRole('button',{name:'Save & revalidate offers'})).toBeVisible();
 await page.screenshot({path:`${shots}/07-guardrails.png`,fullPage:true});
});

test('human approval gate and no below-floor override',async({page})=>{
 await page.goto('/');
 await page.getByRole('switch',{name:'Toggle autopilot'}).click();
 await expect(page.getByRole('switch',{name:'Toggle autopilot'})).toHaveAttribute('aria-checked','false');
 await page.getByRole('button',{name:'Run cancellation scenario'}).click();
 await expect(page.getByText('Approval required',{exact:true})).toBeVisible();
 await page.getByRole('button',{name:'Approve $64 offer'}).click();
 await expect(page.getByText('Offer visible in marketplace')).toBeVisible();
});

test('mobile viewport supports the marketplace and navigation',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 await page.goto('/marketplace');
 await expect(page.getByRole('heading',{name:'A little room in your day.'})).toBeVisible();
 await page.getByLabel('Navigate workspace').selectOption('overview');
 await page.getByRole('button',{name:'Run cancellation scenario'}).click();
 await expect(page.getByText('Recovery offer published',{exact:true})).toBeVisible();
 await page.getByLabel('Navigate workspace').selectOption('marketplace');
 await expect(page.getByRole('button',{name:'Reserve this time'})).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBeTruthy();
 await page.screenshot({path:`${shots}/08-mobile.png`,fullPage:true});
});
