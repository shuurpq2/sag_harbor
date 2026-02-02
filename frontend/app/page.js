import Image from "next/image";
import cl from "./page.module.css";
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <div className={cl.Content}>
        <Link href='/shortener'>shortener</Link>
      </div>
    </div>
  );
}
