import type { Metadata } from 'next';
import './globals.css';
export const metadata:Metadata={title:'Revslot — Recover cancelled time',description:'Autonomous recovery for cancelled beauty and wellness appointments. Synthetic hackathon demonstration.',icons:{icon:'/favicon.svg'}};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>;}
