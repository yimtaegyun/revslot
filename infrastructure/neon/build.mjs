import { build } from "esbuild";

await build({
  entryPoints: ["recoveryclock.mjs"],
  outfile: "dist/index.mjs",
  bundle: true,
  platform: "node",
  target: "node24",
  format: "esm",
  banner: { js: "import{createRequire as ___cr}from'module';const require=___cr(import.meta.url);" },
});
