'use client'
import axios from 'axios';
import cl from './page.module.css'
import { getBackendUrl } from '../api';
import { useRef, useState } from 'react';


export default function ShortenerUrl() {
  const inputRef = useRef()
  const [shortenedUrl, setShortenedUrl] = useState('')


  const API_URL = getBackendUrl()
  const shortenUrl = async (longUrl) => {
    const response = await axios.post(`${API_URL}/api/shortener?long_url=${longUrl}`)
    setShortenedUrl(response.data)
  }
  return (
    <div className={cl.Content}>
      <form onSubmit={(e) => {e.preventDefault(); shortenUrl(inputRef.current.value)}}>
        <input className={[cl.Input, cl.LongUrlInput].join(' ')} placeholder='Input URL to shorten' ref={inputRef} minLength={3} maxLength={2000}/>
        <button>SHORTEN</button>
      </form>
      <a href={shortenedUrl && `${window.location}/${shortenedUrl}`}>{shortenedUrl && `${window.location}/${shortenedUrl}`}</a>
    </div>
  );
}
