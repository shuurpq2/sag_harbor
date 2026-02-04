import Image from "next/image";
import cl from "./page.module.css";
import Link from "next/link";
import { getBackendUrl } from "./api";

export default function Home() {
  const API_URL = getBackendUrl()
  return (
    <div>
      <div className={cl.Content}>
        <Link href='/shortener' className={cl.AppLink}>
          <img src={`${API_URL}/static/app_imgs/shortener.png`}/>
          <div className={cl.AppLinkName}>
            SHORTENER
          </div>
        </Link>
        <Link href='/img_converter' className={cl.AppLink}>
          <img className={cl.AppLinkImg} src={`${API_URL}/static/app_imgs/img_converter.png`}/>
          <div className={cl.AppLinkName}>
            IMG CONVERTER
          </div>
        </Link>
        {[...Array(100)].map((_, i) => (
          <Link key={i} href='/' className={cl.AppLink}>
            <img src={`${API_URL}/static/app_imgs/default.png`}/>
            <div className={cl.AppLinkName}>
              SOON
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
