import axios from 'axios';
import cl from './page.module.css'
import { getBackendUrl } from '@/app/api';
import { redirect } from 'next/navigation';


export default async function OpenShortenedURL({ params }) {
  const {slug} = await params
  const API_URL = getBackendUrl()
  let longURL = ''
  try {
    const response = await axios.get(`${API_URL}/api/shortener/${slug}`)
    longURL = response.data
  } catch {
    null
  } finally {
    if (longURL) {
      redirect(longURL)
    }
  }
  return (
    <div className={cl.Content}>
      Not found
    </div>
  );
}