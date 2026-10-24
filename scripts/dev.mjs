import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const python=fs.existsSync(path.join(root,'.venv/bin/python'))?path.join(root,'.venv/bin/python'):'python3';
const api=spawn(python,['-m','uvicorn','main:app','--app-dir',path.join(root,'backend'),'--host','127.0.0.1','--port','8000'],{stdio:'inherit',env:process.env});
const args=process.argv.slice(2), port=args.includes('--port')?args[args.indexOf('--port')+1]:'3000';
const web=spawn(process.execPath,[path.join(root,'frontend/node_modules/next/dist/bin/next'),'dev','--hostname','0.0.0.0','--port',port],{cwd:path.join(root,'frontend'),stdio:'inherit',env:process.env});
function shutdown(){api.kill('SIGTERM');web.kill('SIGTERM');}
process.on('SIGTERM',shutdown);process.on('SIGINT',shutdown);
api.on('exit',c=>{if(c){shutdown();process.exitCode=c;}});
web.on('exit',c=>{shutdown();process.exitCode=c??0;});
