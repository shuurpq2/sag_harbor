import axios from 'axios';
import cl from './page.module.css'
import { getBackendUrl } from '@/app/api';
import { redirect } from 'next/navigation';


export default async function OpenShortenedUrl({ params }) {
  const {slug} = await params
  const API_URL = getBackendUrl()
  let longUrl = ''
  try {
    const response = await axios.get(`${API_URL}/api/shortener/${slug}`)
    longUrl = response.data
  } catch {
    null
  } finally {
    if (longUrl) {
      redirect(longUrl)
    }
  }
  return (
    <div className={cl.Content}>
      Not found
    </div>
  );
}