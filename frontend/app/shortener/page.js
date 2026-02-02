'use client'
import axios from 'axios';
import cl from './page.module.css'
import { getBackendUrl } from '../api';
import { useRef, useState } from 'react';


export default function ShortenerURL() {
  const inputRef = useRef()
  const [shortenedURL, setShortenedURL] = useState('')


  const API_URL = getBackendUrl()
  const shortenURL = async (longURL) => {
    const response = await axios.post(`${API_URL}/api/shortener?long_url=${longURL}`)
    setShortenedURL(response.data)
  }
  return (
    <div className={cl.Content}>
      <form onSubmit={(e) => {e.preventDefault(); shortenURL(inputRef.current.value)}}>
        <input className={[cl.Input, cl.LongUrlInput].join(' ')} placeholder='Input URL to shorten' ref={inputRef} minLength={3} maxLength={2000}/>
        <button>SHORTEN</button>
      </form>
      <a href={shortenedURL && `${window.location}/${shortenedURL}`}>{shortenedURL && `${window.location}/${shortenedURL}`}</a>
    </div>
  );
}
