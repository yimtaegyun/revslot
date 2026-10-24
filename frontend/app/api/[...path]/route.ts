import { NextRequest } from 'next/server';
export const dynamic='force-dynamic';
export const maxDuration=60;
async function proxy(request:NextRequest,{params}:{params:Promise<{path:string[]}>}){
 const {path}=await params;
 const target=new URL(`/api/${path.map(encodeURIComponent).join('/')}`,process.env.FASTAPI_URL||'http://127.0.0.1:8000');
 target.search=request.nextUrl.search;
 const headers=new Headers();
 for(const name of ['content-type','cookie','origin','x-forwarded-proto']){const value=request.headers.get(name);if(value)headers.set(name,value);}
 headers.set('x-forwarded-host',request.headers.get('host')||request.nextUrl.host);
 try{
  const upstream=await fetch(target,{method:request.method,headers,body:request.method==='GET'?undefined:await request.text(),cache:'no-store',signal:AbortSignal.timeout(30000)});
  const out=new Headers({'Cache-Control':'no-store'});
  for(const name of ['content-type','set-cookie','x-accel-buffering']){const value=upstream.headers.get(name);if(value)out.set(name,value);}
  return new Response(upstream.body,{status:upstream.status,headers:out});
 }catch{return Response.json({detail:'Recovery API is unavailable. Start FastAPI or configure FASTAPI_URL.'},{status:503});}
}
export {proxy as GET,proxy as POST};
